from os import listdir # 특정 폴더의 파일을 가져오기 위해서 사용

#결과를 작성할 csv파일을 만들고 write 한다
write_file = open('statistics.csv', 'w')
write_file.write('년원,매출\n')

csv_files = 'csv_files/'
file_list = listdir(csv_files)
file_list.sort()

for f_name in file_list:
	#마지막 3개 글자가 csv인지 확인
	if f_name[-3:] != 'csv':
		continue
		
	sum_value = 0
	# 순서대로 csv 파일 열기
	f = open(csv_files+f_name, 'r', encoding='UTF-8')
	
	while True:
		row = f.readline()
		# 빈문자열을 체크해 파일이 끝이 났는지 확인
		if not row:
			break
			
		data = row.split(',')
		# 2번째 데이터가 숫자라면 더한다(수강료)
		if data[1].isdigit():
			sum_value = sum_value + int(data[1])
		
	#파일의 이름을 슬라이싱하여 CSV파일에 출력한다
	write_file.write('%s,%d\n'%(f_name[:7], sum_value))
	f.close()
	
write_file.close()	
	
			