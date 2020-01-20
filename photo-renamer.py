import os
import shutil
import re

directory = os.getcwd()
#print(directory)

files = os.listdir(directory)

base_file_name = "South Americ2018 "
time_zone_offset = 5

for file in files:
    file_name = file
    long_name = os.getcwd() + "\\" + file_name 
    #print (long_name)
    pattern1 = "IMG_\d{8}_\d{6}" # IMG_yyyymmdd_hhmmss
    pattern2 = "\d{4}-\d{2}-\d{2} \d{2}.\d{2}.\d{2}" # yyyy-mm-dd hh.mm.ss
    match = False
    if re.match(pattern1, file_name):
        #print("Type 1")
        match = True
        year = file_name[4:8]
        month = file_name[8:10]
        day = file_name[10:12]
        hour = file_name[13:15]
        minute = file_name[15:17]
        second = file_name[17:19]
        ext = file_name[19:]
    if re.match(pattern2, file_name):
        #print("Type 2")
        match = True
        year=file_name[0:4]
        month=file_name[5:7]
        day = file_name[8:10]
        hour = file_name[11:13]
        minute = file_name[14:16]
        second = file_name[17:19]
        ext = file_name[19:]
    if match:
        #print(year + "-" + month + "-" + day + "... " + hour + ":" + minute + ":" + second)
        hour_tz = int(hour) + time_zone_offset
        if hour_tz>24:
            hour_tz = hour_tz - 24
        hour_format = "{:0>2d}"
        hour = hour_format.format(hour_tz)
        new_file_name = base_file_name + year + "-" + month + "-" + day + " " + hour + "-" + minute + "-" + second + ext
        #print (new_file_name)
        print ("renaming " + file_name + " to " + new_file_name)
        # need to check for files that don't match
			#os.rename(long_name, name)	 		
    else:
        print("No match for: " + file_name)

