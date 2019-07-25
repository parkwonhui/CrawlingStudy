
f = open('value.txt', 'r')

list = []
while True:
    line = f.readline()
    if not line: break
    list.append(line.rstrip('\n'))

f.close()
print(len(list))

# 파일 쓰기
w = open('result.txt', 'w')
for i in list:
    w.write("console.log("+"'"+i+":'"+"+"+i+");\n")

w.close()