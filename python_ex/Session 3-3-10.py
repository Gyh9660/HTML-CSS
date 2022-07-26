# with문과 함께 사용하기
#   - open을 사용하면 반드시 close해야 한다.
#   - with문은 close를 자동으로 한다.

import os

with open('새파일.txt','a',encoding='utf-8') as f :
    f.write('Life is to short, you need python')