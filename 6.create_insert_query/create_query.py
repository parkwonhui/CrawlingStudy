f = open('createQuery.txt', 'r',  encoding='UTF8')

# 첫번째 자리에 *나 @가 올 수 있다
# 옵션없음 : 0
# +은 1부터 자동증가 : 1
# @은 랜덤값 : 2
# !은 abcd+index : 3

TABLE_NAME = "user"
QUERY_COUNT = 10

options = []
columns = []
values = []

def optionValueInsert(line):
	if line[0] == '+':
		options.append(1)
		line = line[1:]
	elif line[0] == '@':
		options.append(2)
		line = line[1:]
	elif line[0] == '!':
		options.append(3)
		line = line[1:]
	else :
		options.append(0)		
		
	return line
	

while True:
	line = f.readline()
	if not line: break
	line = optionValueInsert(line)

	value = line.split(':')
	columns.append(value[0])
	values.append(value[1])

f.close()

# 파일 쓰기
w = open('result.txt', 'w', encoding='UTF8')
size = len(columns)
for i in range(QUERY_COUNT):
	query = "insert into "+TABLE_NAME+"(";
	for j in columns:
		query += j
		query += ','
	
	query = query[0:-1]
	query += ") values("
	
	index = 0
	for j in values:
		k = j.rstrip('\n')
		if options[index] == 1 :
			query += str(i)
		elif options[index] == 3 :
			k = '"' + k.replace('"', '') + str(i) + '"'
			query += k
		else :
			query += k
		
		query += ','.rstrip('\n')
		index += 1

	
	query = query[0:-1]
	
	query += ");\n"
	w.write(query)
        
w.close()