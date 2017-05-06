import os

current_path = os.path.realpath('.')
dir_list = os.listdir(current_path)


for folder in dir_list:
	os.chdir(current_path)
	if  not os.path.isdir(folder):
		continue
	if	os.path.isdir("./%s/.git"%folder):
		os.chdir("./%s/"%folder)
		os.system("git stash; git pull")
		os.chdir(current_path)


