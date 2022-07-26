# readline() 메소드 를사용해서 전체 내용 출력하기
#

import os


f = open('새파일.txt' , 'r' , encoding = 'utf-8')
while True:
    line = f.readline()
    if not line: break  # 라인의끝일때 while 문을 빠져나옴
    print(line)

f.close()