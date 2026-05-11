from flask import Blueprint, render_template

from app.models import (
    PokemonSpecies, AbilityList, Pokemon_Ability, MoveList, Pokemon_Move,
    Trainer, HeldItem, Trainer_HeldItem, PokemonInstance, Team
)

main = Blueprint("main", __name__)


@main.route("/")
def index():
    trainers = Trainer.query.order_by(Trainer.id.desc()).all()
    return render_template("index.html", trainers=trainers)
