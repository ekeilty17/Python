FIN="dataout.txt"
#If you want to make sure the file is already present
"""
try:
   g=open(FIN,'w')
except:
   raise TypeError("file",FIN,"is not present or can't be opened")
"""

#The + means if the file does not exist, then python will create it
g=open(FIN,'w+')

g.write("This is content\n")
g.write("This is more content\n")

g.close()

#function that replaces a line in a textfile
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    print lines[line_num] #line being replaced

    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
