import control
import image_processing
import time

PATH= "Pictures/temp/bild.jpg"

for i in range(10):
    control.take_picture(PATH)
    time.sleep(3)
    pic = image_processing.open_picture(PATH)
    control.save_pictures(pic, "Pictures")
