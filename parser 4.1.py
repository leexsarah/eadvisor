import re
from sets import Set
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
			return -1
		elif (text_string.find('-',0,5) > -1):
			return 0
		else:
			return 1
	else:
		return -2

# reads the open file [parse] for the nearest 'TAKE==>' string
# maintains the calling file position when finished
# also calls the 'findinprogress' function
# copy the entire 'TAKE==>' list to string take_c
def printclasslist():
	save = parse.tell()
	nextline = findlinewith('TAKE==>')
	
	global take_c
	take_c=take_c + (nextline[21:])
	
	while (nextline != ''):
		nextline = parse.readline()
		if (len(nextline) > 4):
			if (nextline.find('           ',0,11) == -1):
				parse.seek(save)
				findinprogress()
				return 0
			else:
			        take_c=take_c + (nextline[11:])

# reads the open file [parse] for any classes with 'IP' flag
# maintains the calling file position when finished
# copy courses in progress to list ip_c
def findinprogress():
	save = parse.tell()
	nextline = parse.readline()			
	while (nextline != ''):
		if (nextline.find('TAKE==>') > -1):
			parse.seek(save)
			return 0
		else:
			if (nextline.find('IP',33,35) > 0):
				ip_c.append(nextline[11:15]+' '+nextline[16:19])
			nextline = parse.readline()

# uses regular expressions to format the file string into a list of courses
def parseinprogress():
	str_TAKE = take_c.replace('\n', ' ').replace(',',' ')

	re_subs = re.compile('([A-Z][A-Z][A-Z][A-Z]?)')
	re_nums = re.compile('\d\d\d[A-Z|\d]?')
	
	re_list = re_subs.split(str_TAKE)

	#take care of "OR" expression
	re_OR=''
	re_OR_title = ''

	for i in range(len(re_list)):
		if(re_list[i].find('OR')>-1):
			re_OR = re_list[i]
			re_OR_title = re_list[i-1]+' '
			re_list[i] = '***'
			re_list[i-1]='***'

	OR_nums=re_nums.findall(re_OR)
        
	for e in OR_nums:
		temp = re_OR_title+' '+e
		re_OR_list.append(temp)
	
	for i in range(1,len(re_list),2):
		c_subject = re_list[i]
		c_numbers = re_nums.findall(re_list[i+1])
		for k in c_numbers:
			take_list.append(c_subject +' '+k )

	# use set to delete in progress courses from take courses
	# write final take course list to TAKE2.txt file
	take = Set(take_list)
	IP = Set(ip_c)
	OR = Set(re_OR_list)
	final_take = take.difference(IP)

	if (len(IP&OR)>1):
		for a in final_take:
			NEED_list.append(a)
	else:
		for a in final_take:
			NEED_list.append(a)
			NEED_list.append(re_OR_title+re_OR)

	for x in IP:
		IP_list.append(x)
#-----------------------------------------------------------------------
 
#-----------------------------------------------------------------------
# Main execution code
#-----------------------------------------------------------------------
parse = open('2.txt','r')
info1=parse.readline()
info2=parse.readline()
CSUF_id=info1[52:61]
name=info2[:40]

ip_c=['']
take_c =''
re_OR_list = ['']
take_list = ['']

GE_list =['']
NEED_list =['']
IP_list = ['']
GRAD_list = ['']
STU_info = ['']

print('Please Choose Elective Courses from Follwoing List:')
print('1:MULTIMEDIA & DIGITAL GAME TECHNOLOGIES')
print('2:INTERNET & ENTERPRISE COMPUTING TECHNOLOGIES')
print('3:SOFTWARE ENGINEERING')
print('4:CUSTOMIZED TRACK')
print('5:SCIENTIFIC COMPUTING ')
mode = raw_input('Choice = ')
 
major = findlinewith('PROGRAM CODE:',)
major_info=major[14:22]
if (major.find('BS  CPSC') == -1):
	print('Scan only compatible with Undergrad CS')
else:
	STU_info.append(CSUF_id)
	STU_info.append(name)
	STU_info.append(major_info)
	# ----- GENERAL EDUCATION -----
	if (checkforcomplete('A.  CORE COMPETENCIES') == 1):
		GE_list.append(‘complete’)
	else:
		GE_list.append(‘incomplete’)
	if (checkforcomplete('B. SCIENTIFIC INQUIRY') == 1):
		GE_list.append(‘complete’)
  	else:
		GE_list.append(‘incomplete’)
	if (checkforcomplete('C. ARTS AND HUMANITIES') == 1):
		GE_list.append(‘complete’)
	else:
		GE_list.append(‘incomplete’)
	if (checkforcomplete('D. SOCIAL SCIENCES') == 1):
		GE_list.append(‘complete’)
	else:
		GE_list.append(‘incomplete’)
	if (checkforcomplete('E. LIFELONG LEARNING') == 1):
		GE_list.append(‘complete’)
	else:
		GE_list.append(‘incomplete’)
	if (checkforcomplete('Z.  CULTURAL DIVERSITY') == 1):
		GE_list.append(‘complete’)
	else:
		GE_list.append(‘incomplete’)
	# ----- GENERAL EDUCATION UNITS -----
	if (checkforcomplete('GENERAL EDUCATION RESIDENCE') == 1):
		GE_list.append(‘complete’)
	else:
		GE_list.append(‘incomplete’)
	if (checkforcomplete('GENERAL EDUCATION UPPER DIVISION') == 1):
		GE_list.append(‘complete’)
	else:
		GE_list.append(‘incomplete’)
	if (checkforcomplete('GENERAL EDUCATION UNITS') == 1):
		GE_list.append(‘complete’)
	else:
		GE_list.append(‘incomplete’)
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
	if (checkforcomplete('G.P.A. OF ALL COURSES') == 1):
		GRAD_list.append(‘complete’)
	else:
		GRAD_list.append(‘incomplete’)
	if (checkforcomplete('UNIT REQUIREMENTS') == -1):
		if (checkforcomplete('UNITS EARNED AT CSUF') == 1):
			GRAD_list.append(‘complete’)
		else:
			GRAD_list.append(‘incomplete’)
		if (checkforcomplete('CSUF GRADE POINT AVERAGE') == 1):
			GRAD_list.append(‘complete’)
		else:
			GRAD_list.append(‘incomplete’)
		if (checkforcomplete('UPPER DIVISION UNITS EARNED') == 1):
			GRAD_list.append(‘complete’)
		else:
			GRAD_list.append(‘incomplete’)
		if (checkforcomplete('RESIDENCE UPPER DIVISION UNITS') == 1):
			GRAD_list.append(‘complete’)
		else:
			GRAD_list.append(‘incomplete’)
		if (checkforcomplete('MAJOR Residence UPPER DIVISION') == 1):
			GRAD_list.append(‘complete’)
		else:
			GRAD_list.append(‘incomplete’)
	if (checkforcomplete('TRANSFER INSTITUTION TOTALS') == 1):
		GRAD_list.append(‘complete’)
	else:
		GRAD_list.append(‘incomplete’)
	if (checkforcomplete('CUMULATIVE NUMBER OF UNITS') == 1):
		GRAD_list.append(‘complete’)
	else:
		GRAD_list.append(‘incomplete’)
	if (checkforcomplete('CUMULATIVE GRADE POINT AVERAGE') == 1):
		GRAD_list.append(‘complete’)
	else:
		GRAD_list.append(‘incomplete’)
	
	parse.close()	
	parseinprogress()
	
	print 'GE\n'
	for i in GE_list:
		print i
	print 'take\n'
	for j in NEED_list:
		print j
	print 'in-p\n'
	for k in IP_list:
		print k
	print 'units\n'
	for l in GRAD_list:
		print l
	print 'name\n'
	for m in STU_info:
		print m
