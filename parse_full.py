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

# reads beginning of string [text] for incomplete ('NO', '-')
# returns  1 if category is completed, else
# returns -1 for a main category and prints line
# returns  0 for a  sub-category and prints line
def checkforcomplete(text):
	if (text.find('NO',0,5) > -1):
		print(text),
		return -1
	elif (text.find('-',0,5) > -1):
		print(text),
		return 0
	else:
		return 1

# reads the open file [parse] for the nearest 'TAKE==>' string
# maintains the calling file position when finished
# also calls the 'findinprogress' function
# writes the entire 'TAKE==>' list to the [out_TAKE] file
def printclasslist():
	save = parse.tell()
	nextline = findlinewith('TAKE==>')
	out_TAKE.write(nextline[21:])
	print(nextline),
	while (nextline != ''):
		nextline = parse.readline()
		if (len(nextline) > 4):
			if (nextline.find('           ',0,11) == -1):
				parse.seek(save)
				findinprogress()
				return 0
			else:
				print(nextline),
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
				print('Class in-progress ==> ' + nextline[11:20] + ' (' + nextline[36:len(nextline)-1] + ')')
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
 
mode=raw_input('Choice = ')
 
major = findlinewith('PROGRAM CODE:',)
if (major.find('BS  CPSC') == -1):
	print('Scan only compatible with Undergrad CS')
else:

	# if (checkforcomplete(findlinewith('A.  CORE COMPETENCIES',)) == -1):
		# if (checkforcomplete(findlinewith('A.1 ORAL COMMUNICATION',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('A.2 WRITTEN COMMUNICATION',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('A.3 CRITICAL THINKING',)) == 0):
			# printclasslist()
	# if (checkforcomplete(findlinewith('B. SCIENTIFIC INQUIRY',)) == -1):
		# if (checkforcomplete(findlinewith('B.1 PHYSICAL SCIENCE',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('B.2 LIFE SCIENCE',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('B.3 LABORATORY EXPERIENCE',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('B.4 MATHEMATICS',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('B.5 IMPLICATIONS AND EXPLORATIONS',)) == 0):
			# printclasslist()
	# if (checkforcomplete(findlinewith('C. ARTS AND HUMANITIES',)) == -1):
		# if (checkforcomplete(findlinewith('C.1 INTRODUCTION TO ARTS',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('C.2 INTRODUCTION TO HUMANITIES',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('C.3 EXPLORATIONS IN THE ARTS',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('C.4 ORIGINS OF WORLD',)) == 0):
			# printclasslist()
	# if (checkforcomplete(findlinewith('D. SOCIAL SCIENCES',)) == -1):
		# if (checkforcomplete(findlinewith('D.1 INTRODUCTION TO THE SOCIAL SCIENCES',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('D.2 WORLD CIVILIZATIONS AND CULTURES',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('D.3 AMERICAN HISTORY',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('D.4  AMERICAN GOVERNMENT',)) == 0):
			# printclasslist()
		# if (checkforcomplete(findlinewith('D.5 EXPLORATIONS IN SOCIAL SCIENCES',)) == 0):
			# printclasslist()
	# if (checkforcomplete(findlinewith('E. LIFELONG LEARNING',)) == 0):
		# printclasslist()
	# if (checkforcomplete(findlinewith('Z.  CULTURAL DIVERSITY',)) == 0):
		# printclasslist()
	# if (checkforcomplete(findlinewith('GENERAL EDUCATION RESIDENCE',)) == 0):
		# printclasslist()
	# if (checkforcomplete(findlinewith('GENERAL EDUCATION UPPER DIVISION',)) == 0):
		# printclasslist()
	# if (checkforcomplete(findlinewith('GENERAL EDUCATION UNITS',)) == 0):
		# printclasslist()
	
	
	if (checkforcomplete(findlinewith('COMPUTER SCIENCE CORE COURSES',)) == -1):
		if (checkforcomplete(findlinewith('[CPSCLD]',)) == 0):
			printclasslist()
		if (checkforcomplete(findlinewith('[CPSCUD]',)) == 0):
			printclasslist()
		if (checkforcomplete(findlinewith('[CPSCMATH]',)) == 0):
			printclasslist()
		if (checkforcomplete(findlinewith('[CPSCPHYSSCI]',)) == 0):
			printclasslist()
		if (checkforcomplete(findlinewith('[CPSCBIOLSCI|CPSCBIOLAB]',)) == 0):
			printclasslist()
		if (checkforcomplete(findlinewith('MULTIMEDIA & DIGITAL GAME',)) == 0):
			printclasslist()
		if (checkforcomplete(findlinewith('INTERNET & ENTERPRISE',)) == 0):
			printclasslist()
		if (checkforcomplete(findlinewith('SOFTWARE ENGINEERING',)) == 0):
			printclasslist()
		if (checkforcomplete(findlinewith('CUSTOMIZED TRACK',)) == 0):
			printclasslist()
		if (checkforcomplete(findlinewith('SCIENTIFIC COMPUTING',)) == 0):
			printclasslist()
	if (checkforcomplete(findlinewith('UPPER-DIVISION BACCALAUREATE WRITING',)) == 0):
		printclasslist()
	# if (checkforcomplete(findlinewith('G.P.A. OF ALL COURSES',)) == 0):
		# printclasslist()
	# if (checkforcomplete(findlinewith('UNIT REQUIREMENTS',)) == -1):
		# checkforcomplete(findlinewith('UNITS EARNED AT CSUF',))
		# checkforcomplete(findlinewith('CSUF GRADE POINT AVERAGE',))
		# checkforcomplete(findlinewith('UPPER DIVISION UNITS EARNED',))
		# checkforcomplete(findlinewith('RESIDENCE UPPER DIVISION UNITS',))
		# checkforcomplete(findlinewith('MAJOR Residence UPPER DIVISION',))
	# checkforcomplete(findlinewith('TRANSFER INSTITUTION TOTALS',))
	# checkforcomplete(findlinewith('CUMULATIVE NUMBER OF UNITS',))
	# checkforcomplete(findlinewith('CUMULATIVE GRADE POINT AVERAGE',))
	
	parse.close()	
	out_IP.close()
	out_TAKE.close()
	
	edit_TAKE = open('Take2.txt','w')
	parseinprogress()
	edit_TAKE.close()