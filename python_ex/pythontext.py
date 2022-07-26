import os

#1

f1 = open("test.txt",'w')
f1.write('Life is too short')

f1.close()
f2 = open('test.txt','r')
print(f2.read())
f2.close()


#2
f3 = open('test.txt','a')
f3.write('\nyou need java')

f3.close()
#3
f4 = open ('test.txt','w')
#f4.write(f4.read().replace('java','python'))
f4.write('Life is too short\nyou need java'.replace('java','python'))