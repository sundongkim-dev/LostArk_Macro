import os
import configparser
import mouse
import keyboard
from pathlib import Path
from ast import literal_eval

def save_Fishing_Site_And_Point():
    """ 낚시 장소와 좌표 저장하는 함수이다.
    
    Args:
        None
    
    Returns:
        None
    """
    siteName = input('낚시터 이름을 입력하세요:')
    print("물가로 커서를 이동한 후 F12를 눌러주세요!")
    write_Fishing_Pos(siteName)

def write_Fishing_Pos(siteName):
    """ config/config.txt에 좌표들을 기록해주는 함수이다.
    
    Args:
        siteName: 저장할 지역 이름 ex) 파푸니카
    
    Returns:
        None
    """
    # 좌표 받아오기
    cList = getCursorPositionWithKey(10)
    fishingSiteName = 'fishing_site_' + siteName
    for i, pos in enumerate(cList):
        opt = 'pos' + str(i+1)
        write_Config_On_File(fishingSiteName, opt, str(pos))

def get_Cursor_Position_With_Key(cnt):
    """ 이것은 F12키를 누를 때의 현재 마우스 커서의 좌표를 돌려주는 함수이다.
    
    Args:
        cnt: 커서 저장 횟수
    
    Returns:
        cnt개의 좌표들을 list에 담아서 반환한다.
    """
    print('좌표를 기록하십시오.')
    reps = 0
    flag = False
    coordinateList = []

    while True:
        # is_pressed() 문자 입력으로 취하고 사용자가 누른 키와 일치하면 True
        val = keyboard.is_pressed('F12')
        if flag != val:
            if val:
                reps += 1
                coordinateList.append(mouse.get_position())
                if cnt-reps > 1:
                    print(cnt-reps, '번 더 누르세요.')
                else:
                    print(cnt-reps, '번 더 누르세요.')
            flag = val

        if reps >= cnt:
            return coordinateList

def write_Config_On_File(section, key, val):
    """ 이것은 config/config.txt에 기본 설정을 기록하는 함수입니다.
    
    Args:
        section: 설정의 종류
        key: 키
        val: 값
    
    Returns:
        None
    """
    flag = False
    # os.path_realpath(__file__) -> 현재파일의 절대경로
    configFilePath = str(Path(os.path.realpath(__file__)).parent.parent) + '\\' + 'config' + '\\' + 'config.txt'

    # ConfigParser모듈 -> 프로그램을 실행할 때마다 설정을 다르게 해주고 싶을 때 유용
    config = configparser.ConfigParser()
    # 설정파일 읽기
    config.read(configFile)
    
    # 섹션리스트 가져와서 포인트에 따른 좌표 기입하기
    for idx, sec in enumerate(config.sections()):
        if sec == section:
            config[section][key] = val
            flag = True
    
    # 섹션리스트에 해당 섹션 없었다면 섹션 추가하고 포인트에 따른 좌표 기입하기
    if not flag:
        config.add_section(section)
        config[section][option] = val

    # 꼭 write 해주어야 함
    with open(configFilePath, 'w') as configFile:
        config.write(configFile)

def get_Fishing_Point_List():
    """ 이것은 /config/config.txt에서 낚시할 좌표들을 얻는 함수입니다.
    
    Args:
        None
    
    Returns:
        낚시 장소 리스트와 설정들을 반환합니다.
    """
    fishingSiteList, config = get_Fishing_Site_List()
    coordList = []  # 좌표를 저장할 리스트
    siteList = []   # 낚시터 이름을 저장할 리스트
    if len(fishingSiteList) > 0:
        init = ''
        for idx, site in enumerate(fishingSiteList):
            init += str(idx) + '. ' + site + '\n'
            siteList.append(site)

        init += '낚시터를 골라주세요: '
        index = int(input(init))
        # 인덱스 잘못 기입
        if 0 > index > len(fishingSiteList):
            print('invalid Index')
            return False
        # literal_eval: 문자열을 딕셔너리/리스트 형태로 바꿔줌
        if config is not None:
            for i in config[fishingSiteList[index]]:
                coordList.append(literal_eval(config[fishingSiteList[index]][i]))
                
    return coordList

def get_Fishing_Site_List():
    """ 이것은 config/config.txt에 기록된 기본 설정을 바탕으로 조회하는 함수입니다.
    
    Args:
        None
    
    Returns:
        낚시 장소 리스트와 설정들을 반환합니다.
    """
    configFilePath = str(Path(os.path.realpath(__file__)).parent.parent) + '\\' + 'config' + '\\' + 'config.txt'
    fishingSiteList = [];  config = None
    
    try:
        config = configparser.ConfigParser()
        config.read(configFilePath)
        for section in config.sections():
            if section.find('fishing_site_') >= 0:
                fishingSiteList.append(section)

    except Exception as e:
        print(str(e))

    return fishingSiteList, config

if __name__ == "__main__":
    save_Fishing_Site_And_Point()
    cList = get_Cursor_Position_With_Key(10)
    result = get_Fishing_Point_List()
    