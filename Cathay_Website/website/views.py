from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", row_1_image_2="https://lifestyle-api.asiamiles.com/medias/80025863.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3w1OTAzfGltYWdlL2pwZWd8YUdJd0wyZzVZeTh4TWpNMU1EVTVNek16TlRNeU5pODRNREF5TlRnMk15NXFjR2RmUVUxTUxVTnZiblpsY25RdE1qazBWM2d4T1RWSXw5OWEzNjRmODZiNTc2MmExNGNlYjk4MDBlZjhhYjMxNDI2Y2U2MjI4NmJkNWJmMjc0NzA3NWZiMjU4NjRhYjk0")

