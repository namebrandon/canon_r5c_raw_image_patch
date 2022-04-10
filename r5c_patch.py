# File: 		r5c_patch.py
# Author:		Brandon Harris
# Email:		brandon.harris@gmail.com
# Date:			2022/04/10
# Description:	This script iterates on every .CR3 file in the present directory
#				and overwites the camera model name (R5 C) with the original R5
#				model name. This will impact EXIF and metadata.

#				WARNING! This program overwites your original image data.
#				PLEASE make a copy of the images before modifying them.
#				Images are overwritten and saved in place.

# License:		None. Modify and use at will.
# Disclaimer:	I am not responsible for any use, misuse or other impact of
#				executing this code. I provide no warranty, implied, fit for purpose
#				or otherwise.

# Usage:		save python script to directory with .CR3 images. open a command prompt
#				or terminal shell and execute the following
#					 python3 r5c_patch.py


import os
patch = b'\00\00'
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if f.endswith('.CR3'):
		with open(f, 'r+b') as fh:
			fh.seek(0x00000202)
			fh.write(patch)
		fh.close()
