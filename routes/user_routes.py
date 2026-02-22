from flask import Blueprint, render_template, request, redirect
from models.user import User
from models.role import Role
from models import db

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            name=request.form["name"],
            email=request.form["email"],
            phone=request.form["phone"],
            password=request.form["password"],
            role_id=1
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")

@user_bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
