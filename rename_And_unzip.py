import os
import zipfile
import subprocess
from concurrent.futures import ThreadPoolExecutor
target_dir=r"D:\uvz图片包2"
root_dir=r"D:\AllDowns"

def get_idxs():
	files=sorted(os.listdir(root_dir),key=lambda x: os.path.getmtime(os.path.join(root_dir, x)),reverse=True)[0:8]
	print("参考顺序：\n")
	for each_idx,each_file in enumerate(files,1):
		print(each_file,each_idx,sep='\t')
	print("")
	fst_idx=int(input("从上往下数，第一个目标位置：（1 base）:"))-1
	num=int(input("一共几个:"))
	last_idx=fst_idx+num-1
	return fst_idx,last_idx

def get_old_dir_list(root_dir,fst_idx,last_idx):
	files=sorted(os.listdir(root_dir),key=lambda x: os.path.getmtime(os.path.join(root_dir, x)),reverse=True)
	if fst_idx!=last_idx:
		old_dirs=list(map(lambda x: root_dir+os.sep+x,files[fst_idx:last_idx]))
	elif fst_idx==last_idx:
		# assert fst_idx==0
		old_dir=root_dir+os.sep+files[fst_idx]
		old_dirs=[old_dir]
	return old_dirs


def get_flag(zip_file_path):
	flag=0
	zfile=zipfile.ZipFile(zip_file_path,"r")
	for each_file in zfile.namelist():
		if "/" in each_file:
			flag=2
			break
		else:
			flag=1
			break
	return flag

def get_command_from_flag(flag,zip_file_path):
	assert flag==1 or flag==2
	zip_file_name=zip_file_path.rsplit(os.sep,maxsplit=1)[-1].rstrip(".zip")
	if flag==1:
		td=target_dir+os.sep+zip_file_name
		command="C:/7-Zip/7z.exe e \"{}\" -o\"{}\"".format(zip_file_path,td)
	elif flag==2:
		td=target_dir+os.sep+zip_file_name
		command="C:/7-Zip/7z.exe e \"{}\" -o\"{}\"".format(zip_file_path,td)
	return command

def single_file_unzip(zip_file_name,old_dir):
	assert zip_file_name.endswith(".zip")
	if not old_dir in zip_file_name:
		zip_file_path=old_dir+os.sep+zip_file_name
	else:
		zip_file_path=zip_file_name
	flag=get_flag(zip_file_path)
	command=get_command_from_flag(flag,zip_file_path)
	os.system(command)


def single_dir_unzip(old_dir):
	for each in os.listdir(old_dir):
		if each.endswith(".zip"):
			single_file_unzip(each,old_dir)
	print("one done.")

def rename_uvz(uvz_file_name,old_dir):
	if not old_dir in uvz_file_name:
		uvz_file_path=old_dir+os.sep+uvz_file_name
	else:
		uvz_file_path=uvz_file_name
	if uvz_file_path.endswith(".zip"):
		return uvz_file_path
	elif uvz_file_path.endswith(".uvz"):
		new_zip=uvz_file_path[:-4]+".zip"
		os.rename(uvz_file_path,new_zip)
		return new_zip



def main():
	fst_idx,last_idx=get_idxs()
	old_dirs=get_old_dir_list(root_dir,fst_idx,last_idx)
	# pool=Pool(processes=32)
	thread_pool = ThreadPoolExecutor(max_workers=257)
	for old_dir in old_dirs:
		for one_file in os.listdir(old_dir):
			if one_file.endswith(".uvz") or one_file.endswith(".zip"):
			# print("old dir:",old_dir)
			# print("One file:",one_file)
			# single_unzip(old_dir,one_file)
				zip_file_name=rename_uvz(one_file,old_dir)
				future=thread_pool.submit(single_file_unzip,zip_file_name,old_dir)
	thread_pool.shutdown(wait=False)
	print("ThreadPool: All done.")
			# pool.apply_async(single_unzip,args=(old_dir,one_file))
	# pool.close()
	# pool.join()
	# print("all done.")

if __name__=="__main__":
	main()
	

# single_dir_unzip("D:\AllDowns\中国地域文化通览（清晰pdg）")

