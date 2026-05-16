from datetime import date

from flask import Blueprint, redirect, render_template, request
from app.extensions import db
from app.models import (
    PokemonSpecies, AbilityList, Pokemon_Ability, MoveList, Pokemon_Move,
    Trainer, HeldItem, Trainer_HeldItem, PokemonInstance, Team
)

main = Blueprint("main", __name__)


@main.route("/")
def index():
    trainers = Trainer.query.order_by(Trainer.id.desc()).all()

    trainerCount = Trainer.query.count()
    pokemonCount = PokemonSpecies.query.count()
    return render_template("index.html", trainers=trainers, trainerCount=trainerCount, pokemonCount=pokemonCount)

@main.route("/user/<string:trainer_id>")
def user(trainer_id):
    trainer = Trainer.query.get(trainer_id)

    if not trainer:
        return render_template("404.html"), 404

    return render_template("profile.html", trainer=trainer)

@main.route("/user/<string:trainer_id>/editTeam/<string:team_slot>")
def edit_team(trainer_id, team_slot):
    trainer = Trainer.query.get(trainer_id)

    team = Team.query.filter_by(trainer_id=trainer_id, team_slot=team_slot).order_by(Team.party_slot.desc()).all()

    if not trainer:
        return render_template("404.html"), 404

    return render_template("editTeam.html", trainer=trainer, team_slot=team_slot, team=team)


@main.route("/user/<string:trainer_id>/editTeam/<string:team_slot>/addPokemon", methods=["POST"])
def addPokemon(trainer_id, team_slot):
    pokemon_slot = request.form.get("pokemon_slot")
    selected_pokemon_id = request.form.get("selected_pokemon")
    selected_item_id = request.form.get("selected_item")

    if not selected_pokemon_id or not pokemon_slot:
        return redirect(f"/user/{trainer_id}/editTeam/{team_slot}")
    
    if not selected_item_id:
        selected_item_id = None

    current_team_member = Team.query.filter_by(trainer_id=trainer_id, team_slot=team_slot, party_slot=pokemon_slot).first()
    if current_team_member:
        current_team_member.pokemon_id = selected_pokemon_id
        current_team_member.item_id = selected_item_id
        current_team_member.last_updated = date.today()
    else:
        new_team_member = Team(
            id=f"{trainer_id}_{team_slot}_{pokemon_slot}",
            trainer_id=trainer_id,
            team_slot=team_slot,
            party_slot=pokemon_slot,
            pokemon_id=selected_pokemon_id,
            item_id=selected_item_id
        )
        db.session.add(new_team_member)
    
    db.session.commit()

    return redirect(f"/user/{trainer_id}/editTeam/{team_slot}")

@main.route("/user/<string:trainer_id>/itemList")
def addItem(trainer_id):
    owned_item_ids = [item.id for item in Trainer.query.get(trainer_id).held_items]
    
    unowned_items = HeldItem.query.filter(~HeldItem.id.in_(owned_item_ids)).all()
    return render_template("itemList.html", trainer_id=trainer_id, items=unowned_items)

@main.route("/user/<string:trainer_id>/itemList/addItem", methods=["POST"])
def addItemPost(trainer_id):
    item_id = request.form.get("item_id")
    item = HeldItem.query.get(item_id)

    if not item:
        return render_template("404.html"), 404
    
    trainer = Trainer.query.get(trainer_id)

    if item not in trainer.held_items:
        trainer.held_items.append(item)
        db.session.commit()

    return redirect(f"/user/{trainer_id}/itemList")

@main.route("/user/<string:trainer_id>/itemList/deleteItem", methods=["POST"])
def deleteItemPost(trainer_id):
    item_id = request.form.get("item_id")
    item = HeldItem.query.get(item_id)

    if not item:
        return render_template("404.html"), 404
    
    trainer = Trainer.query.get(trainer_id)

    #Remove the item from the trainer's held items if it exists
    if item in trainer.held_items:
        trainer.held_items.remove(item)
        db.session.commit()

    #Remove the item from all pokemon in the trainer's team if it is currently assigned
    teams_with_item = Team.query.filter_by(trainer_id=trainer_id, item_id=item_id).all()
    for team in teams_with_item:
        team.item_id = None
        team.last_updated = date.today()

    db.session.commit()

    return redirect(f"/user/{trainer_id}")