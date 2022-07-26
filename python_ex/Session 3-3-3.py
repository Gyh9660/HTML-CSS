# 파이썬에서 파일 읽고 쓰기

# - import os

import os
# 현재 내가 존재하는 위치 확인 하기 : os.getcwd()

print (os.getcwd())

# 파이썬에서 폴더 이동하기 : os.chdir('이동할경로')
#   -  경로를 이동시 \\를 사용
#   - 경로를 이동시 r'\'\fmf tkdyd

os.chdir('C:\\git')

# 파일 생성하기

f = open ("새파일.txt",'w') # 파일을 쓰기모드로 오픈
f.close() # 파일을 열면 닫아야 한다.

# 파일 열기모드 3가지
# r : 읽기모드
# w : 쓰기모드  : 기존의 파일이 존재할 경우 덮어씌움
# a : 추가모드  : 기존의 파일의 내용을 유지한체 이어서쓴다.

# 파일을 쓰기 모드로 열어서 출력 값을 저장 하기
f = open("새파일.txt",'w')
for i in range (1,11) :
    data = '%d번째 줄입니다.\n' %i
    f.write(data)
f.close()