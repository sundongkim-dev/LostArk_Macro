from pathlib import Path
from config import init_config as cf
from utils import coordinate, find
import pyautogui, random, time

def find_Image_Then_Press_Key(targetImage, targetBox, seconds, confidence, wait, key):
    """ 찾고자 하는 이미지가 존재할 경우 key를 입력하는 함수이다.
    
    Args:
        targetImage: 찾고자 하는 이미지 파일
        key: 누르고자 하는 key
        targetBox: Box 좌표 튜플
        seconds: 찾고자하는 시간(초)
        confidence: 일치하는 정도 / 기본값: 0.7 (70.0%)
        wait: 다시 기다리는 정도 / 기본값: 0.1초
    
    Returns:
        찾으면 키 입력하고 True 반환하고 아니면 False 반환한다.
    """

    is_find = find.find_Image_For_N_Seconds(targetImage, targetBox, seconds, confidence, wait_seconds)
    if is_find == None:
        return False
    else:
        pyautogui.press(key)
        return True

def run_Macro(wait, configFlag = 1, fishingBtn = 'w'):
    """ 매크로를 실행하는 함수이다.
    
    Args:
        wait: 다시 기다리는 정도 / 기본값: 0.1초
        configFlag: 기록한 설정 유무 flag
        fishingBtn: 찌낚시 던지는 버튼 값
    
    Returns:
        None. 키보드 인터럽트 있기 전까지 반복
    """
    fishingFailCnt = 0; cList = []

    if configFlag:
        cList = coordinate.get_Fishing_Point_List
    else:
        cList = coordinate.get_Cursor_Position_With_Key(10)

    w, h = cf.FISHING_WIDTH, cf.FISHING_HEIGHT
    while True:
        if fishingFailCnt > 20:
            print("Confidence 값이 너무 높습니다. Confidence 값을 조정하세요.")
            return
        if len(cList) > 0:
            idx = random.randrange(0, len(cList))
            print(idx)
            pyautogui.moveTo(cList[idx][0], cList[idx][1], 1)
        else:
            print("좌표가 없습니다.")
            return

        pyautogui.press(fishingBtn); time.sleep(1)
        
        targetBox = find.make_TargetBox(find.get_Center(), w, h)
        is_Pressed = find_Image_Then_Press_Key(cf.FISHING_EXCLAMATION_MARK_IMG_NAME, targetBox, cf.FISHING_EXCLAMATION_MARK_DETECT_SECONDS, 0.7, 1, fishingBtn)
        if is_Pressed:
            time.sleep(wait)
        else:
            fishingFailCnt += 1
            time.sleep(3)
        
if __name__=="__main__":
    run_Macro(cf.FISHING_WAIT_SECONDS, 1, 'w')