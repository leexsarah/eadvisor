#-----------------------------------------------------------------------
# User defined functions
#-----------------------------------------------------------------------
def findlinewith(text,handle):			# reads open file [handle] until line with [text] is found
	nextline = handle.readline()		# returns the line as a string
	while (nextline != ''):
		if (nextline.find(text) > -1):
			return nextline
		nextline = handle.readline()
	return -1

def checkforcomplete(text):				# reads beginning of string [text] for incomplete ('NO', '-')
	if (text.find('NO',0,5) > -1):		# returns  1 if completed, else
		print(text),					# returns -1 for a main category and prints line
		return -1						# returns  0 for a  sub-category and prints line
	elif (text.find('-',0,5) > -1):
		print(text),
		return 0
	else:
		return 1

def printclasslist(handle):				# reads open file [handle] for the nearest 'TAKE==>' list
	save = handle.tell()				# maintains the calling file position when finished
	nextline = findlinewith('TAKE==>',handle)
	print(nextline),					# also calls the 'findinprogress' function
	while (nextline != ''):
		nextline = handle.readline()
		if (len(nextline) > 4):
			if (nextline.find('           ',0,11) == -1):
				handle.seek(save)
				findinprogress(handle)
				return 0
			else:
				print(nextline),

def findinprogress(handle):				# reads open file [handle] for any classes with 'IP' flag
	save = handle.tell()				# maintains the calling file position when finished
	nextline = handle.readline()
	while (nextline != ''):
		if (nextline.find('TAKE==>') > -1):
			handle.seek(save)
			return 0
		else:
			if (nextline.find('IP',33,35) > 0):
				print('Class in-progress ==> ' + nextline[11:20] + ' (' + nextline[36:len(nextline)-1] + ')')
			nextline = handle.readline()
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Main execution code
#-----------------------------------------------------------------------
print('Choose a test method :')
print('1. CS Scan - All categories')
print('2. CS Scan - Incomplete categories')
print('3. CS Scan - Incomplete with TAKE/IP')
mode = raw_input('Choice = ')

parse = open('TDA.txt')

if mode == '1':
	major = findlinewith('PROGRAM CODE:',parse)
	if (major.find('BS  CPSC') == -1):
		print('Scan only compatible with Undergrad CS')
	else:
		print('\nPrinting all categories\n')
		print(findlinewith('A.  CORE COMPETENCIES',parse)),
		print(findlinewith('A.1 ORAL COMMUNICATION',parse)),
		print(findlinewith('A.2 WRITTEN COMMUNICATION',parse)),
		print(findlinewith('A.3 CRITICAL THINKING',parse)),
		print(findlinewith('B. SCIENTIFIC INQUIRY',parse)),
		print(findlinewith('B.1 PHYSICAL SCIENCE',parse)),
		print(findlinewith('B.2 LIFE SCIENCE',parse)),
		print(findlinewith('B.3 LABORATORY EXPERIENCE',parse)),
		print(findlinewith('B.4 MATHEMATICS',parse)),
		print(findlinewith('B.5 IMPLICATIONS AND EXPLORATIONS',parse)),
		print(findlinewith('C. ARTS AND HUMANITIES',parse)),
		print(findlinewith('C.1 INTRODUCTION TO ARTS',parse)),
		print(findlinewith('C.2 INTRODUCTION TO HUMANITIES',parse)),
		print(findlinewith('C.3 EXPLORATIONS IN THE ARTS',parse)),
		print(findlinewith('C.4 ORIGINS OF WORLD',parse)),
		print(findlinewith('D. SOCIAL SCIENCES',parse)),
		print(findlinewith('D.1 INTRODUCTION TO THE SOCIAL SCIENCES',parse)),
		print(findlinewith('D.2 WORLD CIVILIZATIONS AND CULTURES',parse)),
		print(findlinewith('D.3 AMERICAN HISTORY',parse)),
		print(findlinewith('D.4  AMERICAN GOVERNMENT',parse)),
		print(findlinewith('D.5 EXPLORATIONS IN SOCIAL SCIENCES',parse)),
		print(findlinewith('E. LIFELONG LEARNING',parse)),
		print(findlinewith('Z.  CULTURAL DIVERSITY',parse)),
		print(findlinewith('GENERAL EDUCATION RESIDENCE',parse)),
		print(findlinewith('GENERAL EDUCATION UPPER DIVISION',parse)),
		print(findlinewith('GENERAL EDUCATION UNITS',parse)),
		print(findlinewith('COMPUTER SCIENCE CORE COURSES',parse)),
		print(findlinewith('[CPSCLD]',parse)),
		print(findlinewith('[CPSCUD]',parse)),
		print(findlinewith('[CPSCMATH]',parse)),
		print(findlinewith('[CPSCPHYSSCI]',parse)),
		print(findlinewith('[CPSCBIOLSCI|CPSCBIOLAB]',parse)),
		print(findlinewith('MULTIMEDIA & DIGITAL GAME',parse)),
		print(findlinewith('INTERNET & ENTERPRISE',parse)),
		print(findlinewith('SOFTWARE ENGINEERING',parse)),
		print(findlinewith('CUSTOMIZED TRACK',parse)),
		print(findlinewith('SCIENTIFIC COMPUTING',parse)),
		print(findlinewith('UPPER-DIVISION BACCALAUREATE WRITING',parse)),
		print(findlinewith('G.P.A. OF ALL COURSES',parse)),
		print(findlinewith('UNIT REQUIREMENTS',parse)),
		print(findlinewith('UNITS EARNED AT CSUF',parse)),
		print(findlinewith('CSUF GRADE POINT AVERAGE',parse)),
		print(findlinewith('UPPER DIVISION UNITS EARNED',parse)),
		print(findlinewith('RESIDENCE UPPER DIVISION UNITS',parse)),
		print(findlinewith('MAJOR Residence UPPER DIVISION',parse)),
		print(findlinewith('TRANSFER INSTITUTION TOTALS',parse)),
		print(findlinewith('CUMULATIVE NUMBER OF UNITS',parse)),
		print(findlinewith('CUMULATIVE GRADE POINT AVERAGE',parse)),
elif mode == '2':
	major = findlinewith('PROGRAM CODE:',parse)
	if (major.find('BS  CPSC') == -1):
		print('Scan only compatible with Undergrad CS')
	else:
		print('\nPrinting incomplete categories\n')
			
		if (checkforcomplete(findlinewith('A.  CORE COMPETENCIES',parse)) == -1):
			checkforcomplete(findlinewith('A.1 ORAL COMMUNICATION',parse))
			checkforcomplete(findlinewith('A.2 WRITTEN COMMUNICATION',parse))
			checkforcomplete(findlinewith('A.3 CRITICAL THINKING',parse))
		if (checkforcomplete(findlinewith('B. SCIENTIFIC INQUIRY',parse)) == -1):
			checkforcomplete(findlinewith('B.1 PHYSICAL SCIENCE',parse))
			checkforcomplete(findlinewith('B.2 LIFE SCIENCE',parse))
			checkforcomplete(findlinewith('B.3 LABORATORY EXPERIENCE',parse))
			checkforcomplete(findlinewith('B.4 MATHEMATICS',parse))
			checkforcomplete(findlinewith('B.5 IMPLICATIONS AND EXPLORATIONS',parse))
		if (checkforcomplete(findlinewith('C. ARTS AND HUMANITIES',parse)) == -1):
			checkforcomplete(findlinewith('C.1 INTRODUCTION TO ARTS',parse))
			checkforcomplete(findlinewith('C.2 INTRODUCTION TO HUMANITIES',parse))
			checkforcomplete(findlinewith('C.3 EXPLORATIONS IN THE ARTS',parse))
			checkforcomplete(findlinewith('C.4 ORIGINS OF WORLD',parse))
		if (checkforcomplete(findlinewith('D. SOCIAL SCIENCES',parse)) == -1):
			checkforcomplete(findlinewith('D.1 INTRODUCTION TO THE SOCIAL SCIENCES',parse))
			checkforcomplete(findlinewith('D.2 WORLD CIVILIZATIONS AND CULTURES',parse))
			checkforcomplete(findlinewith('D.3 AMERICAN HISTORY',parse))
			checkforcomplete(findlinewith('D.4  AMERICAN GOVERNMENT',parse))
			checkforcomplete(findlinewith('D.5 EXPLORATIONS IN SOCIAL SCIENCES',parse))
		checkforcomplete(findlinewith('E. LIFELONG LEARNING',parse))
		checkforcomplete(findlinewith('Z.  CULTURAL DIVERSITY',parse))
		checkforcomplete(findlinewith('GENERAL EDUCATION RESIDENCE',parse))
		checkforcomplete(findlinewith('GENERAL EDUCATION UPPER DIVISION',parse))
		checkforcomplete(findlinewith('GENERAL EDUCATION UNITS',parse))
		if (checkforcomplete(findlinewith('COMPUTER SCIENCE CORE COURSES',parse)) == -1):
			checkforcomplete(findlinewith('[CPSCLD]',parse))
			checkforcomplete(findlinewith('[CPSCUD]',parse))
			checkforcomplete(findlinewith('[CPSCMATH]',parse))
			checkforcomplete(findlinewith('[CPSCPHYSSCI]',parse))
			checkforcomplete(findlinewith('[CPSCBIOLSCI|CPSCBIOLAB]',parse))
			checkforcomplete(findlinewith('MULTIMEDIA & DIGITAL GAME',parse))
			checkforcomplete(findlinewith('INTERNET & ENTERPRISE',parse))
			checkforcomplete(findlinewith('SOFTWARE ENGINEERING',parse))
			checkforcomplete(findlinewith('CUSTOMIZED TRACK',parse))
			checkforcomplete(findlinewith('SCIENTIFIC COMPUTING',parse))
		checkforcomplete(findlinewith('UPPER-DIVISION BACCALAUREATE WRITING',parse))
		checkforcomplete(findlinewith('G.P.A. OF ALL COURSES',parse))
		if (checkforcomplete(findlinewith('UNIT REQUIREMENTS',parse)) == -1):
			checkforcomplete(findlinewith('UNITS EARNED AT CSUF',parse))
			checkforcomplete(findlinewith('CSUF GRADE POINT AVERAGE',parse))
			checkforcomplete(findlinewith('UPPER DIVISION UNITS EARNED',parse))
			checkforcomplete(findlinewith('RESIDENCE UPPER DIVISION UNITS',parse))
			checkforcomplete(findlinewith('MAJOR Residence UPPER DIVISION',parse))
		checkforcomplete(findlinewith('TRANSFER INSTITUTION TOTALS',parse))
		checkforcomplete(findlinewith('CUMULATIVE NUMBER OF UNITS',parse))
		checkforcomplete(findlinewith('CUMULATIVE GRADE POINT AVERAGE',parse))
elif mode == '3':
	major = findlinewith('PROGRAM CODE:',parse)
	if (major.find('BS  CPSC') == -1):
		print('Scan only compatible with Undergrad CS')
	else:
		print('\nPrinting needed classes\n')
			
		if (checkforcomplete(findlinewith('A.  CORE COMPETENCIES',parse)) == -1):
			if (checkforcomplete(findlinewith('A.1 ORAL COMMUNICATION',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('A.2 WRITTEN COMMUNICATION',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('A.3 CRITICAL THINKING',parse)) == 0):
				printclasslist(parse)
		if (checkforcomplete(findlinewith('B. SCIENTIFIC INQUIRY',parse)) == -1):
			if (checkforcomplete(findlinewith('B.1 PHYSICAL SCIENCE',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('B.2 LIFE SCIENCE',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('B.3 LABORATORY EXPERIENCE',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('B.4 MATHEMATICS',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('B.5 IMPLICATIONS AND EXPLORATIONS',parse)) == 0):
				printclasslist(parse)
		if (checkforcomplete(findlinewith('C. ARTS AND HUMANITIES',parse)) == -1):
			if (checkforcomplete(findlinewith('C.1 INTRODUCTION TO ARTS',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('C.2 INTRODUCTION TO HUMANITIES',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('C.3 EXPLORATIONS IN THE ARTS',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('C.4 ORIGINS OF WORLD',parse)) == 0):
				printclasslist(parse)
		if (checkforcomplete(findlinewith('D. SOCIAL SCIENCES',parse)) == -1):
			if (checkforcomplete(findlinewith('D.1 INTRODUCTION TO THE SOCIAL SCIENCES',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('D.2 WORLD CIVILIZATIONS AND CULTURES',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('D.3 AMERICAN HISTORY',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('D.4  AMERICAN GOVERNMENT',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('D.5 EXPLORATIONS IN SOCIAL SCIENCES',parse)) == 0):
				printclasslist(parse)
		if (checkforcomplete(findlinewith('E. LIFELONG LEARNING',parse)) == 0):
			printclasslist(parse)
		if (checkforcomplete(findlinewith('Z.  CULTURAL DIVERSITY',parse)) == 0):
			printclasslist(parse)
		if (checkforcomplete(findlinewith('GENERAL EDUCATION RESIDENCE',parse)) == 0):
			printclasslist(parse)
		if (checkforcomplete(findlinewith('GENERAL EDUCATION UPPER DIVISION',parse)) == 0):
			printclasslist(parse)
		if (checkforcomplete(findlinewith('GENERAL EDUCATION UNITS',parse)) == 0):
			printclasslist(parse)
		if (checkforcomplete(findlinewith('COMPUTER SCIENCE CORE COURSES',parse)) == -1):
			if (checkforcomplete(findlinewith('[CPSCLD]',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('[CPSCUD]',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('[CPSCMATH]',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('[CPSCPHYSSCI]',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('[CPSCBIOLSCI|CPSCBIOLAB]',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('MULTIMEDIA & DIGITAL GAME',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('INTERNET & ENTERPRISE',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('SOFTWARE ENGINEERING',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('CUSTOMIZED TRACK',parse)) == 0):
				printclasslist(parse)
			if (checkforcomplete(findlinewith('SCIENTIFIC COMPUTING',parse)) == 0):
				printclasslist(parse)
		if (checkforcomplete(findlinewith('UPPER-DIVISION BACCALAUREATE WRITING',parse)) == 0):
			printclasslist(parse)
		if (checkforcomplete(findlinewith('G.P.A. OF ALL COURSES',parse)) == 0):
			printclasslist(parse)
		if (checkforcomplete(findlinewith('UNIT REQUIREMENTS',parse)) == -1):
			checkforcomplete(findlinewith('UNITS EARNED AT CSUF',parse))
			checkforcomplete(findlinewith('CSUF GRADE POINT AVERAGE',parse))
			checkforcomplete(findlinewith('UPPER DIVISION UNITS EARNED',parse))
			checkforcomplete(findlinewith('RESIDENCE UPPER DIVISION UNITS',parse))
			checkforcomplete(findlinewith('MAJOR Residence UPPER DIVISION',parse))
		checkforcomplete(findlinewith('TRANSFER INSTITUTION TOTALS',parse))
		checkforcomplete(findlinewith('CUMULATIVE NUMBER OF UNITS',parse))
		checkforcomplete(findlinewith('CUMULATIVE GRADE POINT AVERAGE',parse))
