from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.ext.login import login_required, login_user, logout_user
from forms import LoginForm
from utils import route_exists

import config
import flask
import librarian

app_bp = Blueprint('librarian', __name__)

@app_bp.route("/")
def index():
    return render_template("main.jinja")

@librarian_bp.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        from models import User
        user = User.query.filter_by(username=form.app_username.data,
          is_user_active=True).first()

        if user and user.password == form.app_password.data:
            login_user(user)
            next_url = flask.request.args.get("next")

            if next_url and not route_exists(next_url):
                return flask.abort(400)

            return redirect(next_url or url_for("librarian.dash"), code=302)
        else:
            flash("Wrong user credentials")

    return render_template("login.jinja", form=form)

@librarian_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("app.index"))
