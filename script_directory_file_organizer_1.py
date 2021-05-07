#!/usr/bin/python

import os
import shutil

current_dir = os.getcwd()
dest_dir = os.path.join(current_dir, "project_directory_folder")

try:
	os.mkdir(dest_dir)
except:
	pass
	
fh = open("/users/jmoe5/human_ca_full_QC.txt")
for line in fh:
	
	current_line = line.rstrip().split("\t")
	
	if current_line[0] != "DCid":
	
		folder = current_line[4] + ":" + current_line[5] + ":" + current_line[6]
		
		try:
			path = os.path.join(dest_dir,folder)
			os.mkdir(path)
		except:
			pass
		
		source_file = "/users/jmoe5/human_ca/" + current_line[0] + "_sort_peaks.narrowPeak.bed"
		dest_file = os.path.join(dest_dir, folder, current_line[0] + "_sort_peaks.narrowPeak.bed." + current_line[3])
		shutil.copyfile(source_file, dest_file)