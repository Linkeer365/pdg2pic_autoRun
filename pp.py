import os
import pyautogui
import win32gui
import win32api
import win32con
import os
import time

root_desktop_hd=None
p2p_path=r"D:\FreePdg2Pdf\Pdg2Pic.exe"
pdg2pic_str="Pdg2Pic"
pdg2pic_str2="选择存放PDG文件的文件夹"

def get_hd_from_child_hds(father_hd,some_idx,expect_name):
    child_hds=[]
    win32gui.EnumChildWindows(father_hd,lambda hwnd, param: param.append(hwnd),child_hds)

    names=[win32gui.GetWindowText(each) for each in child_hds]
    hds=[hex(each) for each in child_hds]
    print("ChildName List:",names)
    print("Child Hds List:",hds)

    name=names[some_idx]
    hd=hds[some_idx]

    print("The {} Child.".format(some_idx))
    print("The Name:{}".format(name))
    print("The HD:{}".format(hd))

    if name==expect_name:
        return child_hds[some_idx]
    else:
        print("窗口不对！")
        return None

os.startfile(p2p_path)

childs=[]

time.sleep(0.5)

root_desktop_hd=None

p2p_hd=win32gui.FindWindowEx(root_desktop_hd,0,0,pdg2pic_str)

# 第一下我们点选的按钮没有名字
fst_btn_hd=get_hd_from_child_hds(p2p_hd,3,expect_name="")
win32api.PostMessage(fst_btn_hd,win32con.BM_CLICK)
time.sleep(0.5)
p2p_hd=win32gui.FindWindowEx(root_desktop_hd,0,0,pdg2pic_str)
names=[win32gui.GetWindowText(each) for each in childs]

win32gui.EnumChildWindows(p2p_hd,lambda hwnd, param: param.append(hwnd),childs)

names=[win32gui.GetWindowText(each) for each in childs]

list1_hd=names[18]
win32gui.SendMessage(list1_hd,win32con.BM_CLICK)

for idx,name in enumerate(names):
	print(name,"\t\t",idx+1)