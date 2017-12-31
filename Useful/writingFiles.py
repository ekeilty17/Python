FIN="dataout"
try:
   g=open(FIN,'w')
except:
   print "ERR: file",FIN,"is not present or can't be opened"

g.write("This is content\n")
g.write("This is more content\n")

g.close()

#function that replaces a line in a textfule
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    print lines[line_num] #line being replaced

    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
