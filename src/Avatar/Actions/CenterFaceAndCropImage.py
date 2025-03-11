from math import floor

import cv2, cv2.data
from numpy import ceil


class CenterFaceAndCropImage:
    def __init__(self, avatar_filename):
        self.avatar_filename = avatar_filename


    def ensure_grayscale(self, image):
        if len(image.shape) == 3:
            return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            return image


    def find_face(self, image):
        classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        return classifier.detectMultiScale(image, scaleFactor=1.3, minNeighbors=5, minSize=(200, 200))


    def calculate_face_crop_position(self, face):
        for (x, y, w, h) in face:
            new_height = h if h > w else w
            new_width = w if w > h else h
            padding = floor(new_height / 5)

            return (
                x - padding,
                y - padding,
                new_width + floor(padding*2.5),
                new_height + floor(padding*2.5)
            )


    def handle(self):
        original_image = cv2.imread(self.avatar_filename)
        grayscale_image = self.ensure_grayscale(original_image)

        faces = self.find_face(grayscale_image)

        if len(faces) > 0:
            crop_position = self.calculate_face_crop_position(faces)
            return original_image[crop_position[1]:crop_position[1] + crop_position[3], crop_position[0]:crop_position[0] + crop_position[2]]

        return None
