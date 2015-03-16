import re
#-----------------------------------------------------------------------
# User defined functions
#-----------------------------------------------------------------------

# reads the open file [parse] until a line with [text] is found
# returns the line as a string if found, -1 if not found
def findlinewith(text):
	nextline = parse.readline()
	while (nextline != ''):
		if (nextline.find(text) > -1):
			return nextline
		nextline = parse.readline()
	return -1

# calls 'findinprogress' function to search for [text]
# returns -2 if string is not found
# reads beginning of the matched string for incomplete markers ('NO', '-')
# returns  1 if category is completed, else
# returns -1 for a main category
# returns  0 for a  sub-category
def checkforcomplete(text):
	text_string = findlinewith(text)
	if (text_string != -1):
		if (text_string.find('NO',0,5) > -1):
#			print(text_string),
			return -1
		elif (text_string.find('-',0,5) > -1):
#			print(text_string),
			return 0
		else:
			return 1
	else:
		return -2

# reads the open file [parse] for the nearest 'TAKE==>' string
# maintains the calling file position when finished
# also calls the 'findinprogress' function
# writes the entire 'TAKE==>' list to the [out_TAKE] file
def printclasslist():
	save = parse.tell()
	nextline = findlinewith('TAKE==>')
	out_TAKE.write(nextline[21:])
#	print(nextline),
	while (nextline != ''):
		nextline = parse.readline()
		if (len(nextline) > 4):
			if (nextline.find('           ',0,11) == -1):
				parse.seek(save)
				findinprogress()
				return 0
			else:
#				print(nextline),
				out_TAKE.write(nextline[11:])

# reads the open file [parse] for any classes with 'IP' flag
# maintains the calling file position when finished
# writes the in progress course IDs to the [out_IP] file
def findinprogress():
	save = parse.tell()
	nextline = parse.readline()			
	while (nextline != ''):
		if (nextline.find('TAKE==>') > -1):
			parse.seek(save)
			return 0
		else:
			if (nextline.find('IP',33,35) > 0):
#				print('Class in-progress ==> ' + nextline[11:20] + ' (' + nextline[36:len(nextline)-1] + ')')
				out_IP.write(nextline[11:19] + '\n')
			nextline = parse.readline()

# reads the newly created [Take.txt] file for the raw in progress list
# uses regular expressions to format the file string into a list of courses
def parseinprogress():
	with open('Take.txt','r') as myfile:
		str_TAKE = myfile.read().replace('\n', ' ').replace(',',' ')
	
	re_subs = re.compile('([A-Z][A-Z][A-Z][A-Z]?)')
	re_nums = re.compile('\d\d\d[A-Z|\d]?')

	re_list = re_subs.split(str_TAKE)
	
	for i in range(1,len(re_list),2):
		c_subject = re_list[i]
		c_numbers = re_nums.findall(re_list[i+1])
		for k in c_numbers:
			print(c_subject + '-' + k + '\n'),
			edit_TAKE.write(c_subject + '-' + k + '\n')
#-----------------------------------------------------------------------
 
#-----------------------------------------------------------------------
# Main execution code
#-----------------------------------------------------------------------
parse = open('TDA.txt','r')
out_IP = open('IP.txt','w')	
out_TAKE = open('Take.txt','w')

print('Please Choose Elective Courses from Follwoing List:')
print('1:MULTIMEDIA & DIGITAL GAME TECHNOLOGIES')
print('2:INTERNET & ENTERPRISE COMPUTING TECHNOLOGIES')
print('3:SOFTWARE ENGINEERING')
print('4:CUSTOMIZED TRACK')
print('5:SCIENTIFIC COMPUTING ')
mode = raw_input('Choice = ')
 
major = findlinewith('PROGRAM CODE:',)
if (major.find('BS  CPSC') == -1):
	print('Scan only compatible with Undergrad CS')
else:
	# ----- GENERAL EDUCATION -----
	# if (checkforcomplete('A.  CORE COMPETENCIES') == -1):
		# if (checkforcomplete('A.1 ORAL COMMUNICATION') == 0):
			# printclasslist()
		# if (checkforcomplete('A.2 WRITTEN COMMUNICATION') == 0):
			# printclasslist()
		# if (checkforcomplete('A.3 CRITICAL THINKING') == 0):
			# printclasslist()
	# if (checkforcomplete('B. SCIENTIFIC INQUIRY') == -1):
		# if (checkforcomplete('B.1 PHYSICAL SCIENCE') == 0):
			# printclasslist()
		# if (checkforcomplete('B.2 LIFE SCIENCE') == 0):
			# printclasslist()
		# if (checkforcomplete('B.3 LABORATORY EXPERIENCE') == 0):
			# printclasslist()
		# if (checkforcomplete('B.4 MATHEMATICS') == 0):
			# printclasslist()
		# if (checkforcomplete('B.5 IMPLICATIONS AND EXPLORATIONS') == 0):
			# printclasslist()
	# if (checkforcomplete('C. ARTS AND HUMANITIES') == -1):
		# if (checkforcomplete('C.1 INTRODUCTION TO ARTS') == 0):
			# printclasslist()
		# if (checkforcomplete('C.2 INTRODUCTION TO HUMANITIES') == 0):
			# printclasslist()
		# if (checkforcomplete('C.3 EXPLORATIONS IN THE ARTS') == 0):
			# printclasslist()
		# if (checkforcomplete('C.4 ORIGINS OF WORLD') == 0):
			# printclasslist()
	# if (checkforcomplete('D. SOCIAL SCIENCES') == -1):
		# if (checkforcomplete('D.1 INTRODUCTION TO THE SOCIAL SCIENCES') == 0):
			# printclasslist()
		# if (checkforcomplete('D.2 WORLD CIVILIZATIONS AND CULTURES') == 0):
			# printclasslist()
		# if (checkforcomplete('D.3 AMERICAN HISTORY') == 0):
			# printclasslist()
		# if (checkforcomplete('D.4  AMERICAN GOVERNMENT') == 0):
			# printclasslist()
		# if (checkforcomplete('D.5 EXPLORATIONS IN SOCIAL SCIENCES') == 0):
			# printclasslist()
	# if (checkforcomplete('E. LIFELONG LEARNING') == 0):
		# printclasslist()
	# if (checkforcomplete('Z.  CULTURAL DIVERSITY') == 0):
		# printclasslist()
	# ----- GENERAL EDUCATION UNITS -----
	# if (checkforcomplete('GENERAL EDUCATION RESIDENCE') == 0):
		# printclasslist()
	# if (checkforcomplete('GENERAL EDUCATION UPPER DIVISION') == 0):
		# printclasslist()
	# if (checkforcomplete('GENERAL EDUCATION UNITS') == 0):
		# printclasslist()
	# ----- COMPUTER SCIENCE CORE -----
	if (checkforcomplete('COMPUTER SCIENCE CORE COURSES') == -1):
		if (checkforcomplete('[CPSCLD]') == 0):
			printclasslist()
		if (checkforcomplete('[CPSCUD]') == 0):
			printclasslist()
		if (checkforcomplete('[CPSCMATH]') == 0):
			printclasslist()
		if (checkforcomplete('[CPSCPHYSSCI]') == 0):
			printclasslist()
		if (checkforcomplete('[CPSCBIOLSCI|CPSCBIOLAB]') == 0):
			printclasslist()
	# ----- COMPUTER SCIENCE ELECTIVE TRACKS -----
		if (mode == '1'):
			if (checkforcomplete('[CPSC-MG-ELECT]') == 0):
				printclasslist()
		elif (mode == '2'):
			if (checkforcomplete('[CPSC-IE-ELECT]') == 0):
				printclasslist()
		elif (mode == '3'):
			if (checkforcomplete('[CPSC-SE-ELECT]') == 0):
				printclasslist()
		elif (mode == '4'):
			if (checkforcomplete('[CPSC-CT-ELECT]') == 0):
				printclasslist()
		elif (mode == '5'):
			if (checkforcomplete('[CPSC-SC-ELECT]') == 0):
				printclasslist()
	if (checkforcomplete('UPPER-DIVISION BACCALAUREATE WRITING') == 0):
		printclasslist()
	# ----- OVERALL REQUIREMENTS -----
	# if (checkforcomplete('G.P.A. OF ALL COURSES') == 0):
		# printclasslist()
	# if (checkforcomplete('UNIT REQUIREMENTS') == -1):
		# checkforcomplete('UNITS EARNED AT CSUF')
		# checkforcomplete('CSUF GRADE POINT AVERAGE')
		# checkforcomplete('UPPER DIVISION UNITS EARNED')
		# checkforcomplete('RESIDENCE UPPER DIVISION UNITS')
		# checkforcomplete('MAJOR Residence UPPER DIVISION')
	# checkforcomplete('TRANSFER INSTITUTION TOTALS')
	# checkforcomplete('CUMULATIVE NUMBER OF UNITS')
	# checkforcomplete('CUMULATIVE GRADE POINT AVERAGE')
	
	parse.close()	
	out_IP.close()
	out_TAKE.close()
	
	edit_TAKE = open('Take2.txt','w')
	parseinprogress()
	edit_TAKE.close()