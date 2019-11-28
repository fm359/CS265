#Single file, assn4, written in Python 3
#
# Farhan Muhammad
# 06/07/2018

.PHONY : build view clean

build :
	@chmod +x assn4

view :
	@less assn4

clean : # remove all cache, executables, and output files
	@find . | grep -E "(__pycache__|\.pyc|\.txt)" | xargs rm -rf
