from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.ext.login import login_required, login_user, logout_user
from forms import LoginForm
from utils import route_exists

import config
import flask
import app

app_bp = Blueprint('app', __name__)

@app_bp.route("/")
def index():
    return render_template("main.jinja")

@app_bp.route("/login/", methods=["GET", "POST"])
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

            return redirect(next_url or url_for("app.dash"), code=302)
        else:
            flash("Wrong user credentials")

    return render_template("login.jinja", form=form)

@app_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("app.index"))
