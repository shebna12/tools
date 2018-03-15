"""
File name: getname.py
    Author: Shebna Rose Fabilloren
    Date created: 03/15/2018
    Date last modified: 03/15/2018
    Python Version: 2.7
"""
"""
Tool for creating train.txt and val.txt.
Requirements:
	*image files must be in its category folder 
	*category folders must be in a general folder
Input: general folder
Output: .txt file
Directory tree sample:
[train] #general folder
---a #category folder
   ---a_0.jpg #images
   ---a_1.jpg 
---b #category folder
   ---b_0.jpg #images
   ---b_2.jpg

"""


import os
import glob
def store_output(out):
	file = open("train.txt","a+")
	file.write(out + "\n")
	file.close()
	
def getname_tool(folder_path):
	n=0 
	for root,dirs,files in os.walk(folder_path):
		# Uncomment this if you are working with ordered categories such as alphabets,digits, etc.
		#dirs.sort()
		if(len(files)!=0):
			for f in files:
				output = (f + " "+str(n))
				store_output(output)
			n = n + 1
if __name__ == '__main__':
	getname_tool('train')
