# 기존의 파일에 새로운 내용을 추가해서 쓰기

import os

f= open(r'c:\git\html_gyh\python_ex\새파일.txt','a',encoding='utf-8')


for i in range(11,20) :
    data = '%d번째 줄입니다. \n' %i
    f.write(data)

f.close()