# read() : 파일의 처음 라인에서 끝라인까지 통째로 저장
#       - 파일의 전체 내용을 통째로 돌려준다.

import os
f= open(r'c:\git\html_gyh\python_ex\새파일.txt','r',encoding='utf-8')
data = f.read()
print(data)
f.close()
