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

def printclasslist(take_c,ip_c,handle):				# reads open file [handle] for the nearest 'TAKE==>' list
	save = handle.tell()                                     # maintains the calling file position when finished
	nextline = findlinewith('TAKE==>',handle)
	take_c.append(nextline[21:])
	take.write(nextline[21:])     
	print(nextline),				# also calls the 'findinprogress' function
	while (nextline != ''):
		nextline = handle.readline()
		if (len(nextline) > 4):
			if (nextline.find('           ',0,11) == -1):
				handle.seek(save)
				findinprogress(ip_c,handle)
				return 0
			else:
				print(nextline),
				take_c.append(nextline[11:])
                                take.write(nextline[11:])
         
	                   
	

def findinprogress(ip_c,handle):				# reads open file [handle] for any classes with 'IP' flag
	save = handle.tell()				# maintains the calling file position when finished
	nextline = handle.readline()
	while (nextline != ''):
		if (nextline.find('TAKE==>') > -1):
			handle.seek(save)
			return 0
		else:
			if (nextline.find('IP',33,35) > 0):
				print('Class in-progress ==> ' + nextline[11:20] + ' (' + nextline[36:len(nextline)-1] + ')')
				ip_c.append(nextline[11:20])
				output.write(nextline[11:20])           
			nextline = handle.readline()
	 
			
	

                        
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Main execution code
#-----------------------------------------------------------------------


parse = open('TDA.txt')
output=open('Inprocess.txt','w') 
take=open('Take.txt','w')
take_c=['']
ip_c=['']

print('Please Choose Elective Courses from Follwoing List:')
print('1:MULTIMEDIA & DIGITAL GAME TECHNOLOGIES')
print('2:INTERNET & ENTERPRISE COMPUTING TECHNOLOGIES')
print('3:SOFTWARE ENGINEERING')
print('4:CUSTOMIZED TRACK')
print('5:SCIENTIFIC COMPUTING ')

mode=raw_input('Choice = ')

if (checkforcomplete(findlinewith('COMPUTER SCIENCE CORE COURSES',parse)) == -1):
	if (checkforcomplete(findlinewith('[CPSCLD]',parse)) == 0):
	    printclasslist(take_c,ip_c,parse)
	    
	if (checkforcomplete(findlinewith('[CPSCUD]',parse)) == 0):
	    printclasslist(take_c,ip_c,parse)
	    
	if (checkforcomplete(findlinewith('[CPSCMATH]',parse)) == 0):
	    printclasslist(take_c,ip_c,parse)
	    
	if (checkforcomplete(findlinewith('[CPSCPHYSSCI]',parse)) == 0):
	    printclasslist(take_c,ip_c,parse)
	    
	if (checkforcomplete(findlinewith('[CPSCBIOLSCI|CPSCBIOLAB]',parse)) == 0):
	    printclasslist(take_c,ip_c,parse)
	    
	if (mode=='1'):
	    if (checkforcomplete(findlinewith('[CPSC-MG-ELECT]',parse)) == 0):
		printclasslist(take_c,ip_c,parse)
		
	elif (mode=='2'):
	    if (checkforcomplete(findlinewith('[CPSC-IE-ELECT]',parse)) == 0):
		printclasslist(take_c,ip_c,parse)
		
	elif (mode=='3'):
	    if (checkforcomplete(findlinewith('[CPSC-SE-ELECT]',parse)) == 0):
                printclasslist(take_c,ip_c,parse)
                
        elif (mode=='4'):
	     if (checkforcomplete(findlinewith('[CPSC-CT-ELECT]',parse)) == 0):
		printclasslist(take_c,ip_c,parse)
		
	elif (mode=='5'):
	     if (checkforcomplete(findlinewith('[CPSC-SC-ELECT]',parse)) == 0):
		printclasslist(take_c,ip_c,parse)
		

output.close()
take.close()
parse.close()
   


