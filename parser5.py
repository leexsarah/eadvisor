import re
import sys

GE_list =['']
TAKE_list =['']
IP_list = ['']
GRAD_list = ['']
STU_info = ['']
##########################################################################
def parse_findLine(text):
	# Scan for input text in open file
	# Success: returns the line as a string / Failure: returns -1
	nextline = tda_file.readline()
	while (nextline != ''):
		if (nextline.find(text) > -1):
			return nextline
		nextline = tda_file.readline()
	return -1
##########################################################################
def parse_checkReqs(text):
	# Parse TDA format for status flags before input text
	# (0: Input not found) ( 2: OK) (-2: NO) ( 1: + ) (-1: - )
	text_string = parse_findLine(text)
	if (text_string != -1):
		if (text_string.find('OK',0,5) > -1):
			return 2
		elif (text_string.find('+',0,5) > -1):
			return 1
		elif (text_string.find('-',0,5) > -1):
			return -1
		elif (text_string.find('NO',0,5) > -1):
			return -2
	else:
		return 0
##########################################################################
def check_GenEdUnits(text,repeat=1):
	global GE_list
	# Interprets status flags for GE section
	result = parse_checkReqs(text)
	if (result == 2):
		for i in range(repeat):
			GE_list.append('Y')
	elif (result == 1):
		GE_list.append('Y')
	elif (result == -1):
		GE_list.append('N')
	elif (result == -2):
		GE_list.append('N')
	else:
		GE_list.append('parse error')
	return result
##########################################################################
def check_CoreUnits(text):
	# Interprets status flags for Major section
	result = parse_checkReqs(text)
	if (result == -1):
		update_classBuffer()
	return result
##########################################################################
def check_GradUnits(text,unit=1):
	global GRAD_raw
	# Interprets status flags for GE section
	result = parse_checkReqs(text)
	if (result == 2):
		temp = 'Y'
	elif (result == 1):
		temp = 'Y'
	elif (result == -1):
		temp = 'N'
	elif (result == -2):
		temp = 'N'
	else:
		temp = 'parse error'

	if (unit == 1):
		save = tda_file.tell()
		nextline = parse_findLine('.0 UNITS')
		temp += ' := ' + nextline.replace('\n', '')
	
	GRAD_raw.append(temp)
	return result
##########################################################################
def update_classBuffer():
	global TAKE_raw
	# Parse TDA format for TAKE==>s and IPs
	# Saves string blocks into TAKE_raw, class values in IP_list
	save = tda_file.tell()
	nextline = parse_findLine('TAKE==>')	
	TAKE_raw += (nextline[21:])
	
	while (nextline != ''):
		nextline = tda_file.readline()
		if (len(nextline) > 4):
			if (nextline.find('           ',0,11) != -1):
				TAKE_raw += (nextline[11:])
			else:
				tda_file.seek(save)
				break
	
	nextline = tda_file.readline()			
	while (nextline != ''):
		if (nextline.find('TAKE==>') == -1):
			if (nextline.find('IP',33,35) > 0):
				IP_list.append(nextline[11:15]+' '+nextline[16:19])
			nextline = tda_file.readline()
		else:
			tda_file.seek(save)
			return 0
##########################################################################
def update_classList():
	global TAKE_raw
	global TAKE_list
	global GRAD_raw
	global GRAD_list
	global GE_list
	# Formats the parsed class data into usable lists
	regex_subject = re.compile('([A-Z]{3,4})')
	regex_classid = re.compile('(\d{3}[A-Z|\d]?)')
	regex_courses = re.compile('[A-Z]{3,4} \d{3}[A-Z|\d]?(?: *OR *[A-Z]{3,4} \d{3}[A-Z|\d]?)*')

	TAKE_str = TAKE_raw.replace('\n', ' ').replace(',',' ')	
	regex_list = regex_subject.split(TAKE_str)
	regex_str = ''
	
	for i in range(1,len(regex_list),2):
		current_subject = regex_list[i]
		regex_str += regex_classid.sub(current_subject+' \g<1>',regex_list[i+1])
	TAKE_list = regex_courses.findall(regex_str)
	
	IP_list.remove('')
	for j in IP_list:
		for k in range(len(TAKE_list)):
			if (TAKE_list[k] == j):
				TAKE_list[k] = ''
				TAKE_list.remove('')
				break
	
	regex_unit = re.compile('(\d{0,3}\.\d) UNITS')
	regex_gpas = re.compile('(\d\.\d{2}) GPA')
	
	for k in range(len(GRAD_raw)):
		GRAD_list.append([GRAD_raw[k][0]])
		
		match1 = regex_unit.split(GRAD_raw[k])
		if len(match1) > 1:
			GRAD_list[k].append(match1[1])
		
		match2 = regex_gpas.split(GRAD_raw[k])
		if len(match2) > 1:
			GRAD_list[k].append(match2[1])
	
	GE_list.append(GRAD_list.pop(0))
	GE_list.append(GRAD_list.pop(0))
	GE_list.append(GRAD_list.pop(0))
##########################################################################
def PARSER_MAIN(FILENAME='TDA.txt',TRACK=3):
	global tda_file
	global TAKE_raw
	global GRAD_raw
	
	print FILENAME
	tda_file = open(FILENAME,'r')
	TAKE_raw = ''
	GRAD_raw = ['']
	
	GRAD_raw.pop()
	GE_list.pop()
	TAKE_list.pop()
	GRAD_list.pop()
	STU_info.pop()
	
	CWID = tda_file.readline()
	NAME = tda_file.readline()
	MAJOR = parse_findLine('PROGRAM CODE:')
	if (MAJOR.find('BS  CPSC') == -1):
		print('Scan only compatible with Undergrad CS')
	else:
		STU_info.append(CWID[52:61])
		STU_info.append(NAME[:40])
		STU_info.append(MAJOR[14:22])
		
		# 1. Mult / Game | 2. INET / Entr | 3. Soft Eng | 4. Custom | 5. Scint CPU
		mode = TRACK
		# ----- GENERAL EDUCATION -----
		if (check_GenEdUnits('A.  CORE COMPETENCIES',4) != 2):
			check_GenEdUnits('A.1 ORAL COMMUNICATION')
			check_GenEdUnits('A.2 WRITTEN COMMUNICATION')
			check_GenEdUnits('A.3 CRITICAL THINKING')
		if (check_GenEdUnits('B. SCIENTIFIC INQUIRY',6) != 2):
			check_GenEdUnits('B.1 PHYSICAL SCIENCE')
			check_GenEdUnits('B.2 LIFE SCIENCE')
			check_GenEdUnits('B.3 LABORATORY EXPERIENCE')
			check_GenEdUnits('B.4 MATHEMATICS')
			check_GenEdUnits('B.5 IMPLICATIONS AND EXPLORATIONS')
		if (check_GenEdUnits('C. ARTS AND HUMANITIES',5) != 2):
			check_GenEdUnits('C.1 INTRODUCTION TO ARTS')
			check_GenEdUnits('C.2 INTRODUCTION TO HUMANITIES')
			check_GenEdUnits('C.3 EXPLORATIONS IN THE ARTS')
			check_GenEdUnits('C.4 ORIGINS OF WORLD')
		if (check_GenEdUnits('D. SOCIAL SCIENCES',6) != 2):
			check_GenEdUnits('D.1 INTRODUCTION TO THE SOCIAL SCIENCES')
			check_GenEdUnits('D.2 WORLD CIVILIZATIONS AND CULTURES')
			check_GenEdUnits('D.3 AMERICAN HISTORY')
			check_GenEdUnits('D.4  AMERICAN GOVERNMENT')
			check_GenEdUnits('D.5 EXPLORATIONS IN SOCIAL SCIENCES')
		check_GenEdUnits('E. LIFELONG LEARNING')
		check_GenEdUnits('Z.  CULTURAL DIVERSITY')
		# ----- GENERAL EDUCATION UNITS -----
		check_GradUnits('GENERAL EDUCATION RESIDENCE',1)
		check_GradUnits('GENERAL EDUCATION UPPER DIVISION',1)
		check_GradUnits('GENERAL EDUCATION UNITS',1)
		# ----- COMPUTER SCIENCE CORE -----
		if (check_CoreUnits('COMPUTER SCIENCE CORE COURSES') == -2):
			check_CoreUnits('[CPSCLD]')
			check_CoreUnits('[CPSCUD]')
			check_CoreUnits('[CPSCMATH]')
			check_CoreUnits('[CPSCPHYSSCI]')
			check_CoreUnits('[CPSCBIOLSCI|CPSCBIOLAB]')
		if (mode == 1):
			print 'mode1'
			check_CoreUnits('[CPSC-MG-ELECT]')				
		elif (mode == 2):
			print 'mode2'
			check_CoreUnits('[CPSC-IE-ELECT]')
		elif (mode == 3):
			print 'mode3'
			check_CoreUnits('[CPSC-SE-ELECT]')
		elif (mode == 4):
			print 'mode4'
			check_CoreUnits('[CPSC-CT-ELECT]')
		elif (mode == 5):
			print 'mode5'
			check_CoreUnits('[CPSC-SC-ELECT]')
		check_CoreUnits('UPPER-DIVISION BACCALAUREATE WRITING')
		# ----- OVERALL REQUIREMENTS -----
		check_GradUnits('G.P.A. OF ALL COURSES')
		if (check_GradUnits('UNIT REQUIREMENTS',0) == -2):
			check_GradUnits('UNITS EARNED AT CSUF')
			check_GradUnits('CSUF GRADE POINT AVERAGE')
			check_GradUnits('UPPER DIVISION UNITS EARNED')
			check_GradUnits('RESIDENCE UPPER DIVISION UNITS')
			check_GradUnits('MAJOR Residence UPPER DIVISION')
		check_GradUnits('TRANSFER INSTITUTION TOTALS')
		check_GradUnits('CUMULATIVE NUMBER OF UNITS')
		check_GradUnits('CUMULATIVE GRADE POINT AVERAGE')
		
		tda_file.close()	
		update_classList()
		
		print('[  GE_list  ]')
		for i in GE_list:
			print('\t'),i
		print('[  TAKE_list  ]')
		for j in TAKE_list:
			print('\t'),j
		print('[  IP_list  ]')
		for k in IP_list:
			print('\t'),k
		print('[  GRAD_list  ]')
		for l in GRAD_list:
			print('\t'),l
		print('[  STU_info  ]')
		for m in STU_info:
			print('\t'),m
##########################################################################
if __name__ == "__main__":
	if len(sys.argv) == 1:
		PARSER_MAIN()
	elif len(sys.argv) == 2:
		PARSER_MAIN(sys.argv[1])
	elif len(sys.argv) == 3:
		PARSER_MAIN(sys.argv[1],sys.argv[2])