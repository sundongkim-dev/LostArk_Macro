import os
import configparser
import mouse
import keyboard
from ast import literal_eval

# --------------------- F12 를 누르면 현제 마우스 커서의 좌표를 돌려주는 함수 -------
def getCursorPositionWithKey(cnt):
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

# --------------------- 낚시 장소 및 좌표 저장 -------------------------------
def writeOptionOnConfig(section, option, val):
    flag = False
    # os.path_realpath(__file__) -> 현재파일의 절대경로
    configFile = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'init.txt'
    # print(str(configFile))
    # ConfigParser모듈 -> 프로그램을 실행할 때마다 설정을 다르게 해주고 싶을 때 유용
    config = configparser.ConfigParser()
    # 설정파일 읽기
    config.read(configFile)
    # 섹션리스트 가져와서 포인트에 따른 좌표 기입하기
    for idx, sec in enumerate(config.sections()):
        if sec == section:
            config[section][option] = val
            flag = True
    # 섹션리스트에 해당 섹션 없었다면 섹션 추가하고 포인트에 따른 좌표 기입하기
    if not flag:
        config.add_section(section)
        config[section][option] = val
    # 꼭 write 해주어야 함
    with open(configFile, 'w') as configfile:
        config.write(configfile)

def writeFishingPos(name):
    # 좌표 10개 받아오기
    poss = getCursorPositionWithKey(10)
    fishingSiteName = 'fishingSite_' + name
    for i, pos in enumerate(poss):
        opt = 'point' + str(i+1)
        print(opt, ' ', pos)
        writeOptionOnConfig(fishingSiteName, opt, str(pos))

def saveFishingSiteAndPoint():
    siteName = input('낚시터 이름을 입력하세요:')
    print("물가로 커서를 이동한 후 F12를 눌러주세요!")
    writeFishingPos(siteName)

# --------------------- 낚시 장소 및 좌표 조회 -------------------------------
def getFishingSiteList():
    configFile = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'init.txt'
    fishingSiteList = []
    config = None
    try:
        config = configparser.ConfigParser()
        config.read(configFile)
        for section in config.sections():
            if section.find('fishingSite') >= 0:
                fishingSiteList.append(section)

    except Exception as e:
        print(str(e))

    return fishingSiteList, config

def getFishingPointList():
    fishingSiteList, config = getFishingSiteList()
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

if __name__ == "__main__":
    saveFishingSiteAndPoint()
    # cList = getCursorPositionWithKey(10)
    result = getFishingPointList()
