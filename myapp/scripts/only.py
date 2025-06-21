print("<h1>HOWZAT</h1>")
import hashlib
import sys
import json

def run1():
	inp=sys.argv[2]
	#print(inp)
	short=hashlib.md5(inp.encode())
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
		entryy={"url":inp,"hash":short,"short":finshort}
		with open('myapp/scripts/dbbase.json', 'r+') as f:
			f.seek(0,2)
			a=f.tell()
			a=(a-2)
			f.seek(a)
			f.write(',\n')
			json.dump(entryy,f,indent=4)
			f.write('\n]')
	finshort=('http://ei.tuku/'+finshort)
	print(finshort)
	
def run2():
	inp=sys.argv[3]
	with open('myapp/scripts/dbbase.json','r') as f:
		all=json.load(f)
	for count in range(len(all)):
		if all[count]["short"]==inp:
			print(all[count]["url"])
			break
	else:
		print("no match")



switchh=sys.argv[1]
if switchh=='generate':
	run1()
else:
	run2()	