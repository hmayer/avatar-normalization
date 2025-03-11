import cv2
from main import app, tempdir
from flask import request
from werkzeug.utils import secure_filename
from src.Avatar.Actions.CenterFaceAndCropImage import CenterFaceAndCropImage


@app.route("/", methods=["POST"])
def create():
    cropped_image = process_image(request.files['avatar'].filename)

    if cropped_image is None:
        return "No face found", 400

    return cv2.imencode(".jpg", cropped_image)[1].tobytes(), 200, {"Content-Type": "image/jpg"}


def process_image(image_path):
    temporary_file = secure_filename(image_path)
    input_image = "{}/{}".format(tempdir, temporary_file)
    request.files['avatar'].save(input_image)
    return CenterFaceAndCropImage(input_image).handle()
