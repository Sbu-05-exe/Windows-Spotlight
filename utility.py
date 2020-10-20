import os

'''
====================================================================================
					Functions that help our program execute smoothly
====================================================================================
'''

def getPaths():
	'''A function that extract paths out of a textfile'''
	
	# create empty dictionary
	paths = {}

	default_dir = os.getcwd() + '\\files'
	# default_dir = input(os.system('cd')) + '/files'

	with open('config.txt') as f:
		path_lst = f.readlines()

		if path_lst:
			for item in path_lst:
				# Add key value pairs from within the config file
				key, path = None, None

				split_line = item.split(';')
				if len(split_line) == 2:
					key, path = split_line[0].strip(), split_line[1].strip()
				
					if key:
						if not(path) or path == '\n': 
							path = default_dir

						paths[key] = path
		else:
			
			paths['cd'] = default_dir
			paths['destdir'] = default_dir
	
	return paths

def getImages(dir_):
	'''A funciton that retrieves all files with an image file extension in a specific directory'''
	# First check if a the file is
	os.chdir(dir_)
	if (os.path.isdir(dir_)):
		# sifting out files with a picture file extension
		file_extensions = ['jpg','png','tiff','jpeg']
		images = [filename for filename in os.listdir(dir_) if (filename[len(filename) - 3:]) in file_extensions]

		filtered_images = [filename for filename in images if os.path.getsize(dir_ + '\\' + filename) > 150000]

		for image in images:
			if not(image in filtered_images):
				os.system(f'del {image}')

		return filtered_images

	return []

def setup():
	'''Initial setup for the applicaiton. Store and look for files here by default'''
	if not('files' in os.listdir()):
		os.mkdir('files')
