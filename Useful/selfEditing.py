file_name = "selfEditing.py"

lines = open(file_name, 'r').readlines()
lines += 'print "This is added content"\n' 
f = open(file_name, 'w')
f.writelines(lines)
f.close()
