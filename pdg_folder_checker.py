import os
import shutil
target_dir=r"D:\uvz图片包2"

for each in os.listdir(target_dir):
	new_td=target_dir+os.sep+each
	if os.path.isdir(new_td):
		print("new folder",new_td)
		new_fd=new_td
		for each2 in os.listdir(new_fd):
			inner_td=new_fd+os.sep+each2
			if os.path.isdir(inner_td):
				print("inner folder",inner_td)
				inner_fd=inner_td
				if len(os.listdir(inner_fd))==0:
					shutil.rmtree(inner_fd)
print("done.")