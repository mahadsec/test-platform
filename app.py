# app.py - MahadSec Internal Tools Demo
# Author: MahadSec Dev Team

import os
from flask import Flask, request, jsonify, render_template
import logging
import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# -- Configuration Section --
DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///mahadsec.db")
SECRET_KEY = os.getenv("SECRET_KEY", "dev-key-change-in-prod")
FLAG_PLACEHOLDER = os.getenv("FLAG", "flag_not_set")

# -- Utils Section --
def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_event(event):
    logging.info(f"{get_timestamp()} - {event}")

# -- Routes Section --

@app.route("/")
def home():
    log_event("Home page accessed.")
    return render_template("index.html")

@app.route("/api/data", methods=["GET"])
def get_data():
    log_event("API data endpoint called.")
    sample_data = {
        "status": "success",
        "timestamp": get_timestamp(),
        "data": [1, 2, 3, 4, 5]
    }
    return jsonify(sample_data)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        message = request.form.get("message", "")
        log_event(f"Contact form submitted by {name}")
        return render_template("contact.html", sent=True, name=name)
    return render_template("contact.html", sent=False)

# -- Admin Section --
@app.route("/admin")
def admin_panel():
    # TODO: Implement authentication!
    log_event("Admin panel accessed!")
    return "Admin panel (access restricted in production!)"

# --------------- DEV SECTION ---------------
# WARNING: REMOVE THIS BEFORE PUSHING TO PROD!
#
# Used for internal testing ONLY. Contains test secrets and CTF flag.
def dev_only():
    admin_secret = "s3cr3t_admin"
    # MAHADSEC_CTF_FLAG
    flag = "MS{git_h1st0ry_c4n_r3v34l_s3cr3ts}"
    test_password = "p@ssword123"
    print("Admin secret (dev only):", admin_secret)
    print("Flag (dev only):", flag)
    print("Test password (dev only):", test_password)
    # TODO: Remove before production!

if __name__ == "__main__":
    log_event("App started.")
    app.run(host="0.0.0.0", port=8000, debug=True)

# End of app.py
