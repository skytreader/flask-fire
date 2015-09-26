import json
import pytz

from datetime import datetime

from app import app, db
from flask import Blueprint, request
from flask.ext.login import login_required
from models import get_or_create
from sqlalchemy.exc import IntegrityError

import re
import traceback

app_api = Blueprint("app_api", __name__)


@app_api.route("/api/util/servertime")
def servertime():
    return {"now": str(datetime.now(tz=pytz.utc).isoformat())}
