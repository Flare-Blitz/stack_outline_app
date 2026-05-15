from flask import Blueprint, render_template
from app.extensions import db
from app.models import (
    PokemonSpecies, AbilityList, Pokemon_Ability, MoveList, Pokemon_Move,
    Trainer, HeldItem, Trainer_HeldItem, PokemonInstance, Team
)

main = Blueprint("main", __name__)


@main.route("/")
def index():
    trainers = Trainer.query.order_by(Trainer.id.desc()).all()
    return render_template("index.html", trainers=trainers)

@main.route("/user/<string:trainer_id>")
def user(trainer_id):
    trainer = Trainer.query.get(trainer_id)

    if not trainer:
        return render_template("404.html"), 404

    return render_template("profile.html", trainer=trainer)
