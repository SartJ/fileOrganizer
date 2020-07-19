import os, shutil


path = 'C:\\Users\\sarta\\Desktop\\Drop Here'
video_path = 'C:\\Users\\sarta\\Desktop\\Drop Here\\Videos'
audio_path = 'C:\\Users\\sarta\\Desktop\\Drop Here\\Audios'
# r=root, d=directories, f = files
def sort_them_files_babe():
	for r, d, f in os.walk(path):
	    for file in f:
	        if '.mp4' in file:
	        	src = os.path.join(r, file)
	        	print(src)
	        	shutil.move(src,video_path, copy_function = shutil.copytree)
	        elif '.mp3' in file:
	        	src = os.path.join(r, file)
	        	shutil.move(src,audio_path, copy_function = shutil.copytree)
	        os.chdir(path)
	    break;
	    os.chdir(path)


sort_them_files_babe()
