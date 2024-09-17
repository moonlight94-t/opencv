from enum import Enum
import shutil
import os
#sh shell 명령어 의미

# 클래스에 내장될 기능을 번호로 설정 ? 함수에 번호매기기
class funcnum(Enum):
    resize=1
    rotate=2
    hflip=3
    vflip=4
    crop=5

funcnum.resize # 1을 넘겨주고 1을 받는다 무슨소리인지 확인/
# 번호지정논리

def a(param1, funcnum) :
    if funcnum==1:
        pass
def resize(c) :
    a(c, funcnum.resize) #1을 전달함
    
    



os.path.basename()# 경로에서 파일명만 분리
os.path.splitext()# 파일명에서 확장자 떼어냄
os.path.isdir()# 폴더가 존재한다면