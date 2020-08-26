import os
import zipfile
# from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
# old_dir=input("Please input old dir")
# old_dir=r"D:\AllDowns\pp"
target_dir=r"D:\uvz图片包2"
root_dir=r"D:\AllDowns"

# 张伯苓的那几个文件有问题，他的namelist返回的是这样的东西	->	张伯苓全集第9卷规章制度13937068/...
# 这个手动吧，我也不知道具体怎么办了...

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

def single_unzip(old_dir,one_file):
	os.chdir(old_dir)
	flag=0
	# assert one_file.enswith(".uvz") or one_file.endswith(".zip")
	if one_file.endswith(".uvz"):
		# print("gg!")
		new_zip=one_file[:-4]+".zip"
		os.rename(one_file,new_zip)
		one_file=new_zip
	# elif one_file.endswith(".zip"):
		# print("one file:",one_file)
		# print("cc!")
	zfile=zipfile.ZipFile(one_file,"r")
	zInfo=zipfile.ZipInfo(one_file)
	# zfile.printdir()
	# zfile.printdir()
	# print("Type:",zInfo.compress_type)
	for filename in zfile.namelist():
		# print(filename)
		td=target_dir
		some_list=filename.split("/")
		if len(some_list)==1:
			# 压缩包内直接装着的就是pdg文件，没有再多的文件夹
			tmp_dir=one_file.strip(".zip")
			flag=1
		elif len(some_list)==2:
			# print("mm")
			if some_list[1]!='':
				tmp_dir=some_list[0]
				# 压缩包里还有一个文件夹，装着所有的pdg文件
				# 这里是这样的形式，就是 文件夹/pdg文件
				# 这里文件一定会露出来，而不是隐藏着的
				flag=2
			elif some_list[1]=='':
				# 这里文件是隐藏着的，不要紧，跳过他就可以了...
				continue
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
	thread_pool = ThreadPoolExecutor(max_workers=257)
	for old_dir in old_dirs:
		for one_file in os.listdir(old_dir):
			if one_file.endswith(".uvz") or one_file.endswith(".zip"):
			# print("old dir:",old_dir)
			# print("One file:",one_file)
			# single_unzip(old_dir,one_file)
				future=thread_pool.submit(single_unzip,old_dir,one_file)
	thread_pool.shutdown(wait=False)
	print("ThreadPool: All done.")
			# pool.apply_async(single_unzip,args=(old_dir,one_file))
	# pool.close()
	# pool.join()
	# print("all done.")

if __name__=="__main__":
	main()