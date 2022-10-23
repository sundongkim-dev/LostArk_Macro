import os, time, sys, pyautogui, configparser
from pathlib import Path

def make_TargetBox(c, w, h):
    """ 이것은 target box를 생성하는 함수입니다.
    
    Args:
        c: 스크린 정중앙 좌표
        w: 스크린 너비 
        h: 스크린 높이
    
    Returns:
        target box를 튜플로 반환합니다.
    """
    x = c[0]
    y = c[1]

    pos = (x - w, y - h)
    targetBox = (pos[0], pos[1], 2*w, 2*h)
    return targetBox

def get_Center(): 
    """ 이것은 스크린의 정중앙 좌표를 생성하는 함수입니다.
    
    Args:
        None
    
    Returns:
        정중앙 좌표를 튜플로 반환합니다.
    """
    pos = pyautogui.size()
    pos = (int(pos[0]/2), int(pos[1]/2))
    return pos

def is_Image_In_Box(targetImage, targetBox, confidence=.7):
    """ 이것은 targetBox에서 찾고자하는 이미지가 있는 지 확인하는 함수입니다.
    
    Args:
        targetImage: 찾고자하는 이미지 파일
        targetBox: Box 좌표 튜플
        confidence: 일치하는 정도 / 기본값: 0.7 (70.0%)

    Returns:
        TargetBox에서 이미지 찾으면 True 반환하고 못 찾으면 None
    """
    targetImageFilePath = str(Path(os.path.realpath(__file__)).parent.parent) + '\\' + 'img' + '\\' + targetImage
    result = pyautogui.locateOnScreen(targetImageFilePath, confidence=confidence, region=targetBox)

    sys.stdout.write('. '); sys.stdout.flush()
    if result != None:
        print('Find Image ' +  str(result))
    return result


def find_Image_For_N_Seconds(targetImage, targetBox, seconds = 60, confidence=.7, wait=0.1):
    """ 이것은 N 초 동안 찾고자하는 이미지가 있는 지 확인하는 함수입니다.
    
    Args:
        targetImage: 찾고자하는 이미지 파일
        targetBox: Box 좌표 튜플
        seconds: 찾고자하는 시간(초)
        confidence: 일치하는 정도 / 기본값: 0.7 (70.0%)
        wait: 다시 기다리는 정도 / 기본값: 0.1초

    Returns:
        TargetBox에서 이미지 찾으면 True 반환하고 못 찾으면 None
    """
    for i in range(seconds):
        is_find = is_Image_In_Box(targetImage, targetBox, confidence)
        if is_find != None:
            break
        else:
            time.sleep(wait)
    if is_find == None:
        return None
    else:
        return is_find


if __name__ == "__main__":
    # /config/config.txt의 width와 height 값을 가져온다.
    configFilePath = str(Path(os.path.realpath(__file__)).parent.parent) + '\\' + 'config' + '\\' + 'config.txt'
    config = configparser.ConfigParser()
    config.read(configFilePath)
    w = int(config['fishing_info']['width'])
    h = int(config['fishing_info']['heght'])

    # TargetBox 생성한다.
    targetBox = make_TargetBox(get_Center(), w, h)
    
    # 100초간 targetBox에서 이미지 찾는다.
    find_Image_For_N_Seconds("LA_exclamation_mark.png", targetBox, 100, 0.7, 5)