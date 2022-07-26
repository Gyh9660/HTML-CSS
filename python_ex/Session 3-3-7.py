# readlines(): 각라인을 읽어서 리스트 형식으로 리턴
#       - for 문을 사용해서 list의 내용을 출력


import os
f=open('C:\\git\\html_gyh\\python_ex\\새파일.txt','r',encoding='utf-8')
lines=f.readlines()     #lines 는 각 라인을 읽은 리스트 정보를 가짐

#print(lines)
for line in lines :
    line = line.strip() #\n을 제거
    print(line)

f.close()