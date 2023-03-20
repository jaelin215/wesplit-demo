from healthcheck import HealthCheck
import requests
from functools import wraps
import os
import logging
import json
import io
from flask import (Flask, flash, jsonify, make_response,
                   redirect, render_template, request, session, url_for)

from run import enhanced_ocr
import pytesseract
# import code2flow

# Configure logging
logging.basicConfig(format='%(message)s', level=logging.INFO)
logging.info('All libraries are imported to flask correctly.')

# Initialize Flask app
app = Flask(__name__)


# Initialize server connection health check
health = HealthCheck(app, "/hcheck")


def howami():
    return True, "Server connection OK, Thanks for checking :)"


health.add_check(howami)


# ----- utilities ------
def save_raw_img_txt(file):
    # Input - Raw
    filename = file.filename
    raw_path = os.path.join('static/raw', filename)
    file.save(raw_path)

    # Save txt - Raw
    txt = 'static/raw/raw.txt'
    with open(txt, 'w') as f:
        f.write(txt)
        f.close()

    return filename, raw_path


def raw_ocr(raw_path):
    # Run OCR - Raw
    options_all = f"--psm 1 --oem 1"
    raw_txt = pytesseract.image_to_string(raw_path, config=options_all)
    return raw_txt


def save_enhanced_txt(enhanced_txt_path):
    with open(enhanced_txt_path, 'r') as f:
        enhanced_content = f.read()
        f.close()
    return enhanced_content
# ----------------------


@app.route("/")
def home():
    demo_path = 'static/image/Screenshot 2023-03-18 at 6.48.51 PM.png'
    return redirect(url_for("upload_receipt"))


@app.route("/upload_receipt", methods=["GET", "POST"])
def upload_receipt():
    if request.method == "POST":
        # Raw
        file = request.files["file"]
        filename, raw_path = save_raw_img_txt(file)
        raw_txt = raw_ocr(raw_path)

        # Enhanced
        try:
            enhanced_path, enhanced_txt_path, enhanced_txt = enhanced_ocr(
                raw_path)
            enhanced_content = save_enhanced_txt(enhanced_txt_path)
        except:
            enhanced_path = ''
            enhanced_content = ''
            logging.info(
                'Input enhancement failed. Replaced enhanced path/content with blank. OK')

        return render_template("results.html", filename=filename, raw_path=raw_path, raw_txt=raw_txt, enhanced_path=enhanced_path, enhanced_txt=enhanced_content)
    return render_template("upload_receipt.html")


# code2flow.code2flow(['app.py', 'run.py', 'functions.py'],
#                     'flask_flowchart/out.png')

if __name__ == "__main__":
    app.run(debug=False, use_reloader=True, host="127.0.0.1",
            port=int(os.environ.get("PORT", 8080)))
