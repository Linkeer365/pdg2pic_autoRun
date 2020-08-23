import os
import zipfile
# from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
# old_dir=input("Please input old dir")
# old_dir=r"D:\AllDowns\pp"
target_dir=r"D:\uvz图片包2"
root_dir=r"D:\AllDowns"

def get_idxs():
	fst_idx=int(input("从上往下数，第一个目标位置：（1 base）:"))-1
	num=int(input("一共几个:"))
	last_idx=fst_idx+num-1
	return fst_idx,last_idx

def get_old_dir_list(root_dir,fst_idx,last_idx):
	files=sorted(os.listdir(root_dir),key=lambda x: os.path.getmtime(os.path.join(root_dir, x)),reverse=True)
	old_dirs=list(map(lambda x: root_dir+os.sep+x,files[fst_idx:last_idx]))
	return old_dirs

def single_unzip(old_dir,one_file):
	os.chdir(old_dir)
	flag=0
	if one_file.endswith(".uvz") or one_file.endswith(".zip"):
		if one_file.endswith(".uvz"):
			print("gg!")
			new_zip=one_file[:-4]+".zip"
			os.rename(one_file,new_zip)
			one_file=new_zip
		zfile=zipfile.ZipFile(one_file,"r")
		# zfile.printdir()
		for filename in zfile.namelist():
			td=target_dir
			some_list=filename.split("/")
			if len(some_list)==1:
				# 压缩包内直接装着的就是pdg文件，没有再多的文件夹
				tmp_dir=one_file.strip(".zip")
				flag=1
			elif len(some_list)==2:
				tmp_dir=some_list[0]
				# 压缩包里还有一个文件夹，装着所有的pdg文件
				flag=2
			# print(filename)
			# if filename.endswith(".pdg"):
			# 	td2=td+os.sep+one_file.strip(".zip")
			# 	os.makedirs(td2)
			# 	td=td2
			data=zfile.read(filename)
			if not os.path.exists(td+os.sep+tmp_dir):
				os.makedirs(td+os.sep+tmp_dir)
			if flag==1:
				td2=td+os.sep+tmp_dir
				td=td2
			with open(td+os.sep+filename,"w+b") as f:
				f.write(data)
	print("one done.")

def main():
	fst_idx,last_idx=get_idxs()
	old_dirs=get_old_dir_list(root_dir,fst_idx,last_idx)
	# pool=Pool(processes=32)
	thread_pool = ThreadPoolExecutor(max_workers=33)
	for old_dir in old_dirs:
		for one_file in os.listdir(old_dir):
			future=thread_pool.submit(single_unzip,old_dir,one_file)
	thread_pool.shutdown(wait=False)
	print("ThreadPool: All done.")
			# pool.apply_async(single_unzip,args=(old_dir,one_file))
	# pool.close()
	# pool.join()
	# print("all done.")

if __name__=="__main__":
	main()