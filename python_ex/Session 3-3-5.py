# readline 함수를 사용해서 파일 읽어오기ㅣ
#          - 한 라인만 읽어들임
import os


f = open ('새파일.txt', 'r', encoding='utf-8')
line = f.readline()
print(line)
f.close()