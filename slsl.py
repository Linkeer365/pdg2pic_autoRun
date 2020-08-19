import os

book_dir=r"D:\uvz图片包"
for each in os.listdir(book_dir):
	os.chdir(book_dir)
	if os.path.isdir(each):
		print(each)
		each_abs=book_dir+os.sep+each
		folder_len=len(os.listdir(each_abs))
		print("len:{}".format(folder_len))
		if folder_len==1:
			os.rename(each_abs,"D:/"+each)
