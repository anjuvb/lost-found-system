from flask import Blueprint, render_template
from models.claim import Claim

admin_bp = Blueprint("admin_bp", __name__)

@admin_bp.route("/admin")
def admin_panel():
    claims = Claim.query.all()
    return render_template("admin_panel.html", claims=claims)