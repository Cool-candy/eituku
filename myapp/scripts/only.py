print("<h1>HOWZAT</h1>")
import hashlib
import sys
import json
import urllib.request
from urllib.parse import urlparse

def run1():
	inp=sys.argv[2]
	#print(inp)
	def get_full_url(inp):
    		parsed_url = urlparse(inp)
    		if not parsed_url.scheme:
    		    inp = f"https://{inp}"
    		# Make a request and follow redirects using urllib
    		response = urllib.request.urlopen(inp)
    
    		# Get the final URL after redirects
    		full_url = response.geturl()
    
    		# Parse the full URL to extract its scheme (http, https, ftp, etc.)
    		parsed_url = urlparse(full_url)
    		scheme = parsed_url.scheme  # This will give you the protocol (http, https, ftp, etc.)
    
    		# Return the full URL and its scheme
    		return full_url, scheme

	# Test the function
	full_url, scheme = get_full_url(inp)
	#print(f"Full URL: {full_url}")
	#print(f"Scheme: {scheme}")
	short=hashlib.md5(full_url.encode())
	short=short.hexdigest()
	#print(short)
	#print(len(short))
	with open('myapp/scripts/dbbase.json','r') as f:
		all=json.load(f)
	for count in range(len(all)):
		if all[count]["hash"]==short:
			finshort=all[count]["short"]
			break
	else:
		finshort=''
		for catt in range(0,len(short),4):
			#print(short[catt:(catt+4)],end=" ")
			posval=0
			for countt in range(4):
				posval=(posval+int(short[(catt+countt)],16))
			#print(posval,end=" ")
			if posval>9 and posval<36:
				posval=(chr(posval+55))
			elif posval>35:
				posval=(chr(posval+61))
			else:
				posval=str(posval) 
			#print(posval)
			finshort=finshort+posval
		entryy={"url":full_url,"hash":short,"short":finshort}
		with open('myapp/scripts/dbbase.json', 'r+') as f:
			f.seek(0,2)
			a=f.tell()
			a=(a-2)
			f.seek(a)
			f.write(',\n')
			json.dump(entryy,f,indent=4)
			f.write('\n]')
	finshort=('https://eituku.onrender.com/'+finshort)
	print("<h2>",finshort,"</h2>")
	
def run2():
	inp=sys.argv[3]

	if (len(inp) > 8):
		op=urlparse(inp)
		if (not op.netloc):
			a=op._replace(path='//'+op.path)
			#print(a)
			op=urlparse(a.path)
		#print(op)
		a=op.path
		inp=a[1:]
		if (len(inp) > 9 or len(inp) < 8):
			print("wrong input")
		if (len(inp) == 9):
			inp=inp[:-1]
		#print(a)
		#print(len(a))
	
	if (len(inp) == 8):
		with open('myapp/scripts/dbbase.json','r') as f:
			all=json.load(f)
		for count in range(len(all)):
			if all[count]["short"]==inp:
				print("<h2>Your result : ",all[count]["url"],"</h2>")
				break
		else:
			print("<h2>Your result : no match</h2>")



switchh=sys.argv[1]
if switchh=='generate':
	run1()
else:
	run2()	