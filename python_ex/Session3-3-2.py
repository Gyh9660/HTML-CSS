# 정규 표현식의 기초 메타 문자
# - 메타 문자 : 특별한 용도로 사용하는 문자
# = - . , ^ , ? , {} , [] , \ , | , () <== 메타문자

# 문자 클래스 : [] <= 문자클래스 (charactor class)
# - [] 내의 문자들과 매칭 시키는 의미
# - [abc] : 정규 표현식이 잇을대, a,b,c, 중 한개의 문자가 배치됨을 뜻함
#   - "a" : 매치됨
#   - "before" : 매치됨
#   - "dudle" : 매치되지 않음.

#   - [a-z] : [abcdefghijklmnopqrstuvwxyz] <== 소문자만 매칭
#   - [A-Z] : [ABCDEFGHIJKLMNOPQRSTUVWXYZ] <== 대문자 A~Z
#   - [a-zA-Z] : 알파벳 전체 (소,대문자)
#   - [0-9] : 숫자만 매칭
#   - [^0-9] : ^ (not), 숫자가 아닌 문자만 매칭

#   - \d    : 숫자만 매칭 , [0-9]
#   - \D    : 숫자가 아난것과 매칭, [^0-9]와 동일
#   - \s    : 공백(whitespace)과 매칭, [ \t\n\r\f\v] 와 동일
#   - \S    : 공백이 아닌 것과 매칭. [^ \t\n\r\f\v]와 동일
#   - \w    : 문자+숫자와 매칭 , [a-zA-Z0-9]
#   - \W    : 문자 + 숫자가 아닌것과 매칭 , [^a-zA-Z0-9] , 특수문자

#   Dot (.) : 모든 문자와 매칭, 여러개의 문자가 와도 상관없음.
#   -   \n (줄바꿈)을 제외한 모든 문자와 매칭

#   정규표현식 : a.b
#           - "a + 모든문자 + b"
#           - "aab" : 매칭
#           - "a0b" : 매칭
#           - "abcdefb" : 매칭
#           - "ab" : .이 0개들어있어도 매칭
#           - "abc" : 매칭이 안됨
#   정규표현식 : a[.]b  <== a.b 자체를 뜻함


# 반복 (*) : 바로 앞의 문자의 반복을 뜻함.
#   정규표현식 : ca*t
#       - "ct"     :  a가 0개가 반복됨 , 매칭
#       - "cat"    :  a가 1번 반복됨 , 매칭
#       - "caat"   :  a가 2번 반복됨, 매칭
#       - "caaaat" :  a가 4번 반복됨, 매칭

# 반복 (+) : 바로 앞 문자의 반복을 뜻함. 0번 반복은 매칭못함
#   정규표현식 : ca+t
#       - "ct"     :  a가 0개가 반복됨 , 매칭되지 않는다.
#       - "cat"    :  a가 1번 반복됨 , 매칭
#       - "caat"   :  a가 2번 반복됨, 매칭
#       - "caaaat" :  a가 4번 반복됨, 매칭

# 반복 ({m,n},?) : 반복 횟수를 제한을 가할수가 있다.
#   1. {m} : 앞의 문자가 m번 반복되는것을 매칭
#   -정규 표현식 : ca{2}t
#       -"cat"  : 매칭 되지 않음    (), a 가 한번반복
#       -"caat" : 매칭됨, a가 2번 반복됨 
#   2. {m,n} : 앞의 문자가 m번이상, n번이하 반복되는 것을 매칭
#       -정규 표현식 : ca{2,5}t     <== c로 시작하고 t로끝나는데 a가 2번이상 5번이하 반복되는것을 매칭
#             - "cat" : 매칭 안됨, a가 1번 반복
#             - "caat"   :  a가 2번 반복됨, 매칭
#             - "caaat" :  a가 3번 반복됨, 매칭
#             - "caaaaat" : 매칭됨, a가 5번 반복됨
#   3. ?    <== {0,1}   : 0번이상 1번이하 반복 되는 것을 매칭
#       - 정규 표현식 : ab?c : b가 0번 반복, 1번 반복 매칭
#       - "abc"     : 매칭, b가 1번 반복
#       - "ac"      : 매칭, b가 0번 반복

# 정규 표현식 사용 모듈 : re
#   import re
#   p = re.compile(정규표현식)
#           p: 정규 표현식이 적용된 패턴 객체로 리턴

#   정규 표현식을 이용한 문자열 검색 , (4가지 메소드)
#   1. match() : 문자열의 처음부터 정규식과 매치되는지 
#       - match안되면 오류발생 해당 패턴이 매칭이 안되면 오류 발생
#       - 검색하는 내용중 어긋나느것이 존재하면 오류발생
#   2. search() : 문자열 전체를 검색해서 정규식과 매칭되는지 조사
#       - match안되면 건너뛰고 검색해서 매칭 / 해당 패턴이 없을때 다음 패턴을 검색
#       - 검색하는
#   3. findall() : 정규식과 매칭되는 모든 문자열을 리스트로 돌려준다.
#   4. finditer() : 정규식과 매칭되는 모든 문자열을 반복 가능한 객체로 돌려준다.

#   1. match() : 정확하게 정규식과 일치하는  패턴을 돌려줌
#       - match안되면 오류발생 해당 패턴이 매칭이 안되면 오류 발생

#   2. search() : 정규식과 일치하는 패턴을 검색
#       - match안되면 건너뛰고 검색해서 매칭 / 해당 패턴이 없을때 다음 패턴을 검색

from platform import machine
import re   # 파이썬에서 정규표현식을 사용하는 라이브러리
p = re.compile('[a-z]+')    # a-z : 소문자를 반복해서 검색하는 패턴

m = p.match("python")
print (m)
print(m.group())

#n = p.match("3 python") # 3은 패턴에 존재하지 않으므로 match에서는 오류
n = p.search("3 python")
print(n)
print(n.group())    # group()는 매칭된 정보를 출력

#3. findall : 패턴에 일치하는 정보를 찾아서 list 형식으로 리턴

result = p.findall("life 456 LIFE is 789 IS to 123 TO short ")
print(result)

#4. finditer : 패턴에 일치하는 정보를 찾아서 반복 가능한 객체로 출력
result2 = p.finditer('life is to short')
print(result2)  #단순한 정보를 담고 있는 객체 주만
for r in result2:   #매치된 정보가 출력
    print (r.group())


# match객체의 메서드
#   - group() : 매치된 문자열
#   - start() : 매치된 문자열의 시작 index 값
#   - end() : 매치된 문자열의 마지막 index 값
#   - sapn() : 매치된 문자열의 (시작,끝)에 해당하는 튜플을 돌려준다.
print("=============================")
pp = re.compile('[A-Z]+') # 대문자만 검색
#kk = pp.match('LIFE Is To SHORT') #LIFE만 출력
kk = pp.findall('LIFE Is To SHORT ABCD') #LIFE만 출력
print (kk)
#print (kk.start())
#print(kk.end())
#print(kk.span())

# 컴파일 옵션
# 1. DOTTALL (S) : .에서 줄바꿈 문자를 포함 할 수 있도록 매칭
# 2. IGNORECASE (I) : 대, 소문자 관계없이 매칭 할 수 있도록 매칭
# 3. MULTILINE (M) : 여러 라인에서 적용 될 수 있도록 매칭 ( ^ : 시작하는 값, $ : 마지막 값)
# 4. VERBOSE (X) : 정규표현식을 보기 편하게 공백이나 주석을 사용할 수 있도록 한다.

print("==========================")
# 1. DOTALL (S)
# import re
p1 = re.compile('a.b',re.DOTALL) #a로 시작 b로 끝남, 중간에 라인(\n)을 제외한 어떤문자가 와도 상관없다.
m1 = p1.match('a\nb') # 라인이 들어 있으므로 매칭 되지 않음. (DOTALL넣으면 됨)
print(m1.group())

#2. IGNORECASE (I)
# import re
p2 = re.compile('[a-z]+',re.IGNORECASE) #대소문자를 무시해서 패턴을 매칭 (소문자로 매칭해라.) 옵션: 대소문자 무시
m2 = p2.match('PYTHON')
print (m2.group())

print("===============")
#3. MULTILINE (M)

# import re
p3 = re.compile('^python\s\w+' ,re.MULTILINE) # ^ : python으로 시작, $ : 끝나는 것

data = """python one
life is to short
python two
you need python
python three"""

print(p3.findall(data))

p4 = re.compile('python$',re.MULTILINE)
data4 = """one python
two python
three python
four python"""

print (p4.findall(data4))

# 4. VERBOSE (X) : 정규표현식은 거의 암호화 수준입니다. 초급자들이 보면 알 수 없다.
#       - 정규 표현식에 주석을 달아서 작동 되도록 처리 ( 공백, 주석)

# import re
charref = re.compile(r"""
                    $[#]
                    (
                        0[0-7]+     # 8진수 : 0-7까지
                        |[0-9]+     # 10진수 : 0-9까지
                        |x[0-9a-fA-F]+  # 16진수 : 0-9, a-f, A-F
                        )
                        ;
                        """,re.VERBOSE)

# 백슬래시 문제 : 정규 표현식에서 제일 혼란을 초래하는 것이 \
#   '\section'을 검색하는 정규 표현식을 사용 할때 문제점 : \s : 공백을 의미
#   '\\section' ===> '\section' 문자열을 매칭
#   r'\section' ===> '\section' 문자열을 매칭

# | : or

# import re

p6 = re.compile('Crow|Servo')
m6 = p6.match("CrowHello")
print(m6)

# ^ : 문자열의 맨처음, 컴파일시 re.MULTILINE을 사용할 경우 여러줄에서 맨처음
print (re.search('^Life','Life is to short'))

# $ : 문자열의 마지막
print (re.search('short$','Life is to short'))


# 예제 : 9이동민, 2022) ,(최재영,2022), (Lion, 2018)
# import re
example = '이동민 교수님은 다음과 같이 설명했습니다.(이동민, 2022). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있습니다(최재영, 2022). 또 다른 견해도 있었습니다. (Lion, 2018)'
result = re.findall(r'\([a-zA-Z가-힣]+, \d+\)', example)
print(result)

result2 = re.findall(r'\(.\)', example)
print(result2)

#\A : ^왇 동일하게 문자열의 처음과 매칭됨,
#       -re.MULTILINE 라인 옵션이 적용되어 있더라도 처음라인에서만 매칭
#\Z : $와 동일하게 문자열의 마지막과 매칭됨
#       -re.MULTILINE 라인 옵션이 적용되어 있더라도 마지막 라인에서만 매칭
#\b : 단어를 매칭, 공백(whitespace)까지

p= re.compile(r'\bclass\b') #class 라는 단어를 검색
m = p.findall('no class at all')
print(m)

m1 = p.findall('the declassifiod algorithm') # 앞뒤 공백이 없어 내부에 폼함, 매칭되지 않는다.
print (m1)

# 그룹핑 : () : 특정 문자열이나 숫자나 묶어서 반복되는것을 조사하는 정규식.
#   정규표현식 : (abc)+ <== abc가 계속 반복

p = re.compile('(ABC)+')
m = p.search('ABCABCABCABC')
m1 = p.findall('ABCABC ABC ABCABCABC ABCAB ABCA')
print(m.group())
print (m1)

p = re.compile (r'\w+\s+\d+[-]\d+[-]\d+') # \w : [\a-zA-Z0-9], 영문 대소문자 숫자
m = p.search('park 010-1234-5678')
print(m.group())
print("=========================")


p = re.compile (r'(\w+)\s+(\d+)[-](\d+)[-](\d+)') # \w : [\a-zA-Z0-9], 영문 대소문자 숫자
m = p.search('park 010-1234-5678')
print(m.group())    # 매칭된 전체 문자열 출력
print(m.group(0))   # 매칭된 전체 문자열 출력
print(m.group(1))   # park
print(m.group(2))   # 010
print(m.group(3))   # 1234
print(m.group(4))   # 5678


#그릅의 인덱스값으로 출력, 정규표현식에서 ()를 사용해서 그룹핑 할경우 group()의 index값으로 출력 가능
# group(0) : 매치된 전체 문자열 출력
# group(!) : 

# 전방 탐색 (Lookahead Assertions)
#   - 긍정형 전방 탐색 (Postivie) : (?=...) : ...에 해당되는 정규표혀닉과 매치되어야 하며  
#       조건이 통과되어도 문자열이 소멸되지 않는다.

#   - 부정형 전방 탐색 (Negative) : (?!...) : ...에 해당되는 정규표션식과 매치되지 않아야 하며
#       조건이 통과 되어도 문자열이 소멸되지 않는다.

p = re.compile('.+:') # . : 문자, 숫자, 특수문자 (http://www.google.co.kr) http:
m = p.search('http://www.google.co.kr')
print(m.group()) # http:


p= re.compile('.+(?=:)') # http: ==> http , 검색에는 : 포함, 출력 : :제거후 출력
m= p.search('http://www.google.co.kr')

print(m.group()) # http

#2. 부정형 전방 탐색

# 문자열 바꾸어서 출력 하기