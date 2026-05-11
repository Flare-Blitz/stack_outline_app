from flask import Blueprint, render_template

from .models import Trainer

main = Blueprint("main", __name__)


@main.route("/")
def index():
    records = Trainer.query.order_by(Trainer.id.desc()).all()
    return render_template("index.html", records=records)
