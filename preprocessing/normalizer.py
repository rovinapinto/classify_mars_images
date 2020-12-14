# import the necessary packages
import cv2

class Normalizer:

  def preprocess(self, image):
    return image.astype("float32")/255.0

