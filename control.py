import os
import datetime
import PIL


def take_picture(path: str, time: int=2000, contrast: int=0, width: int=2592, height: int=1944):
    """
    takes the picture
    :param path: temporary picture storage
    :param time: time to take picture
    :param contrast: contrast of picture
    :param width: picture width
    :param height: picture height
    """
    os.system(f"raspistill -t {time} -c {contrast} -n -w {width} -h {height} -o {path}")


def delete_picture(path: str):
    """
    removes pictures
    :param path:
    """
    if path[:7] in ['jpg']:
        os.remove(path)
    else:
        pass


def save_pictures(picture, new_folder: str):
    """
    saves the picture with a date
    :param picture:
    :param new_folder:
    :return:
    """
    date = datetime.datetime.now().strftime()
    picture.save(f"{new_folder}/{date}.jpg")
