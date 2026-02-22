from flask import Blueprint, render_template, request
from models.claim import Claim
from models import db
import datetime

claim_bp = Blueprint("claim_bp", __name__)

@claim_bp.route("/claim", methods=["GET", "POST"])
def claim_item():
    if request.method == "POST":
        claim = Claim(
            claim_date=datetime.date.today(),
            proof_description=request.form["proof"],
            claim_status="Pending",
            user_id=1,
            item_id=1
        )
        db.session.add(claim)
        db.session.commit()
    return render_template("claim_item.html")