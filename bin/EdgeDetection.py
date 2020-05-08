import cv2
import imutils as im
from imutils import contours


class picture:
    def __init__(self):
        self._pic = None
        self.focal_length = None
        self.distance_from_ref = None

    def get_picture(self):
        return self._pic

    def load(self, image_path):
        # load the image, convert it to grayscale, and blur it slightly
        image = cv2.imread(image_path)
        self._pic = image
        return self

    def get_box(self):
        if self._pic is None:
            print('Picture not loaded yet. Please load the picture')
        gs_image = cv2.cvtColor(self._pic, cv2.COLOR_BGR2GRAY)
        smooth_image = cv2.GaussianBlur(gs_image, (7, 7), 0)
        # perform edge detection, then perform a dilation + erosion to
        # close gaps in between object edges
        edged_obj = cv2.Canny(smooth_image, 50, 100)
        edged_obj = cv2.dilate(edged_obj, None, iterations=1)
        edged_obj = cv2.erode(edged_obj, None, iterations=1)
        # find contours in the edge map
        contoured_object = cv2.findContours(edged_obj.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contoured_object = im.grab_contours(contoured_object)
        # sort the contours from left-to-right and initialize the
        # 'pixels per metric' calibration variable
        (contoured_object, _) = contours.sort_contours(contoured_object)
        return contoured_object


def load_pic(image_path):
    return picture().load(image_path)