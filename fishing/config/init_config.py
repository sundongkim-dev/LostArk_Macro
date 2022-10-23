import configparser, os
from pathlib import Path

configFilePath = str(Path(os.path.realpath(__file__)).parent.parent) + '\\' + 'config' + '\\' + 'config.txt'
config = configparser.ConfigParser()
config.read(configFilePath)

FISHING_WIDTH = int(config['fishing_info']['width'])
FISHING_HEIGHT = int(config['fishing_info']['height'])
FISHING_WAIT_SECONDS = int(config['fishing_info']['wait_seconds'])
FISHING_EXCLAMATION_MARK_IMG_NAME = config['fishing_info']['target_image_name']
FISHING_EXCLAMATION_MARK_DETECT_SECONDS = int(config['fishing_info']['detect_seconds'])