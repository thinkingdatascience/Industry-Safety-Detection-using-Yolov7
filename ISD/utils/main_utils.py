import yaml
import sys
import base64

from isd.exception import isdException
from isd.logger import logging


def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfull")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise isdException(e, sys)


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + filename, "wb") as image:
        image.write(imgdata)
        image.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as image:
        return base64.b64encode(image.read())
