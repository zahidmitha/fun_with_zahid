
#dict()

#{'':''}

#if k:


#1. Convert to characters
#2. Check if values are in  convert list
#3. Replace values if so
#4. Put back as a string
	
d = dict()
	
string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
string = "map"	
string_out = ""

	
for i in string:
	#try:
    #	d[i]
	convert = ord(i)
	if 97<= convert <= 120:
		string_out += chr(convert + 2)
	elif 120< convert <= 122:
		string_out += chr(97 + (convert - 121))
	else:
		string_out += i
	#catch KeyError:
	
print string_out


	