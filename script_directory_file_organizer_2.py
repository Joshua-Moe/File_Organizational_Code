#!/usr/bin/python

import os
import shutil
import glob 

current_dir = os.getcwd()
dest_dir = os.path.join(current_dir, "project_directory_folder")


try:
	os.mkdir(dest_dir)
except:
	pass
	
fh = open("/users/jmoe5/Human_Histone_Modifications/human_hm_full_QC.txt")
hm_file_directory = "/users/jmoe5/Human_Histone_Modifications/human_hm"

for line in fh:
	
	current_line = line.rstrip().split("\t")
	current_folder = current_line[4] + ":" + current_line[5] + ":" + current_line[6]
	
	if current_line[0] != "DCid":
		if current_folder in os.listdir(dest_dir):
		
			partial_filename = current_line[0] + "*"
			source_file = glob.glob(os.path.join(hm_file_directory, partial_filename))
			
			for i in source_file:
			
				new_name = i.split('/')[-1] + "." + current_line[3]
				dest_file = os.path.join(dest_dir, current_folder, new_name) 
				shutil.copyfile(i, dest_file)