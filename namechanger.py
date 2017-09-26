import os
import re

print "Hi Nami, I am Luffy, Please enter your parent directory!"
input_dir = raw_input()
print "Thanks! Can you enter the string which you wnat to be replaced in the file names"
replacble_string = raw_input()
print "Now with which string do you want it to be replaced Nami"
replaced_string = raw_input()
if (replaced_string == '\n'):
	print ""
else:
	print replaced_string

for file in os.listdir(input_dir):
	if replacble_string in file:
		print file
		file_name = os.path.splitext(file)[0]
		print replacble_string
		extension = os.path.splitext(file)[1]
		new_name = re.sub(r""+ re.escape(replacble_string)+"",replaced_string,file_name)
		os.rename(os.path.join(input_dir,file),os.path.join(input_dir,new_name + extension))
	
