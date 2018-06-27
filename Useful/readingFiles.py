FIN="datain"
try:
   f=open(FIN,'r')
except:
   print "ERR: file",FIN,"is not present or can't be opened"

lines=f.readlines()

for line in lines:
   print line.split('\n')[0]

f.close()
