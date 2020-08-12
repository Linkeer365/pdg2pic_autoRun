import pyautogui
import win32gui
import win32api
import win32con
import os
import time

# 强烈建议先下载一个spy++，否则没有可视化这个hds你不知道是什么意思！！

# 前台鼠标：是模拟鼠标点击这个动作，
# 而后台鼠标是发送“鼠标点击”这个信息
# https://blog.csdn.net/claire017/article/details/104521681/


# p2p_path=r"D:\FreePdg2Pdf\Pdg2Pic.exe"

# pos=pyautogui.position()
# print("X:{};Y:{}".format(*pyautogui.position()))

# os.startfile(p2p_path)

# time.sleep(15)

# def doClick(cx, cy,hwnd):
#     long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
#     win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
#     win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起


# choose_str="1、选择需转换的 PDG 文件所在文件夹:"
#
# # 这一行能够得到handle，但不知道为什么...
#
# # None表示桌面（第一个参数表示父窗口），最后一个参数表示子窗口（也就是要选的窗口）
# pdg2pic_hd=win32gui.FindWindowEx(None,0,0,"Pdg2Pic")
#
# # 搜索子窗口
# # 枚举子窗口
# hwndChildList = []
# win32gui.EnumChildWindows(pdg2pic_hd, lambda hwnd, param: param.append(hwnd),  hwndChildList)
#
# names=[win32gui.GetWindowText(each) for each in hwndChildList]
# hds=[hex(each) for each in hwndChildList]
# print("ChildName List:",names)
# print("Child Hds List:",hds)
#
# choose_hd=win32gui.FindWindowEx(pdg2pic_hd,0,0,choose_str)
# # print(hd)
#
# choose_rect=win32gui.GetWindowRect(choose_hd)
#
#
# # left,top,right,bottom=win32gui.GetWindowRect(hd)
#
# title=win32gui.GetWindowText(choose_hd)
# # classname=win32gui.GetClassName(hd)
# print("title:{}".format(title))

# while True:
#     tempt = win32api.GetCursorPos() # 记录鼠标所处位置的坐标
#     x = tempt[0]-choose_rect[0] # 计算相对x坐标
#     y = tempt[1]-choose_rect[1] # 计算相对y坐标
#     print(x,y)
#     # time.sleep(0.5) # 每0.5s输出一次

def click_on_pos(pos_list):
    btn_pos = pos_list
    win32api.SetCursorPos(btn_pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

def get_hd_from_child_hds(father_hd,some_idx):
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

    return child_hds[some_idx]

pdg2pic_str="Pdg2Pic"
btn_idx=3

choose_pdg_dir_str="选择存放PDG文件的文件夹"
edit_pdg_dir_idx=6

geshitongji_str="格式统计"

p2p_path=r"D:\FreePdg2Pdf\Pdg2Pic.exe"

uvz_dir=r"D:\uvz图片包2"


def make_one_folder(uvz_path):
    # uvz_path=r"D:\uvz图片包2\北京古代经济史.孙健主编.北京燕山出版社.1996"

    os.startfile(p2p_path)

    # 这个sleep也是必须有的！
    time.sleep(1)

    root_desktop_hd=None

    p2p_hd=win32gui.FindWindowEx(root_desktop_hd,0,0,pdg2pic_str)

    fst_btn_hd=get_hd_from_child_hds(p2p_hd,3)

    # left,top,right,bottom=win32gui.GetWindowRect(btn_hd)
    #
    # clickX,clickY=(left+right)//2,(top+bottom)//2
    #
    # win32api.SetCursorPos([clickX,clickY])
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)



    # win32con.BM_CLICK 试了下应该可以产生点击效果，然后post表示不等待，send表示等待
    win32api.PostMessage(fst_btn_hd,win32con.BM_CLICK)

    # 这里必须有一个sleep
    time.sleep(1)
    # print("done.")

    choose_pdg_dir_hd=win32gui.FindWindowEx(root_desktop_hd,0,0,choose_pdg_dir_str)
    write_text_btn_hd=get_hd_from_child_hds(choose_pdg_dir_hd,6)
    queding_btn_hd=get_hd_from_child_hds(choose_pdg_dir_hd,9)
    shuzhuangtu_btn_hd=get_hd_from_child_hds(choose_pdg_dir_hd,4)

    # 找到一个位置，我他妈强行点你！
    hayashi_pos=[839,333]
    click_on_pos(hayashi_pos)

    # 凡是有click都让他sleep(1)
    time.sleep(1)
    win32gui.SendMessage(write_text_btn_hd,win32con.WM_SETTEXT,0,uvz_path)
    time.sleep(1)
    win32gui.SendMessage(queding_btn_hd,win32con.BM_CLICK)

    # 格式统计，点确定

    time.sleep(1)
    geshitongji_hd=win32gui.FindWindowEx(root_desktop_hd,0,0,geshitongji_str)
    queding2_btn_hd=get_hd_from_child_hds(geshitongji_hd,0)

    win32api.PostMessage(queding2_btn_hd,win32con.BM_CLICK)

    time.sleep(1)


    # # 再次请求p2p_hd
    p2p_hd=win32gui.FindWindowEx(root_desktop_hd,0,0,pdg2pic_str)
    kaishizhuanhuan_btn_hd=get_hd_from_child_hds(p2p_hd,0)
    time.sleep(1)
    win32api.PostMessage(kaishizhuanhuan_btn_hd,win32con.BM_CLICK)

    time.sleep(1)
    # 键盘点击Esc
    win32api.keybd_event(win32con.VK_ESCAPE,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

    # time.sleep(20)



    # while True:
    #     x,y=win32api.GetCursorPos()
    #     print("X:{};Y:{}".format(x,y))
    #     time.sleep(10)

    # # 按下esc退出
    # win32api.keybd_event(win32con.VK_ESCAPE,0,0,0)
    # win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)


    # queding3_btn_pos=[1051,441]
    # click_on_pos(queding3_btn_pos)
    #
    # time.sleep(2)
    # guanbi_btn_pos=[1284,180]
    # click_on_pos(guanbi_btn_pos)

    print("One done.")

def main():
    for each in os.listdir(uvz_dir):
        # uvz_path = os.path.abspath(each)
        # print(each)
        uvz_path=uvz_dir+os.sep+each
        if os.path.isdir(uvz_path):
            make_one_folder(uvz_path)
    print("all down.")

if __name__ == '__main__':
    main()

# while True:
#     x,y=win32api.GetCursorPos()
#     print("X:{};Y:{}".format(x,y))
#     time.sleep(10)

# rect=win32gui.GetWindowRect(shuzhuangtu_btn_hd)
# left,top,right,bottom=rect
# print(left,top,right,bottom)

# while True:
#     x,y=win32api.GetCursorPos()
#     print("X:{};Y:{}".format(x,y))
#     time.sleep(10)

# clickX,clickY=(left+right)//2,(top+bottom)//2
#
# win32api.SetCursorPos([clickX,clickY])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


# menu=win32gui.GetMenu(shuzhuangtu_btn_hd)
# menu1 = win32gui.GetSubMenu(menu, 1)#第几个菜单
# print("Menu:{};Menu1:".format(menu))

# win32gui.SendMessage(write_text_btn_hd,win32con.WM_SETTEXT,0,uvz_path)
# time.sleep(1)
# win32gui.SendMessage(write_text_btn_hd,win32con.WM_COMMAND,win32con.VK_RETURN)


# time.sleep(1)

# bb_hd=get_hd_from_child_hds(write_text_btn_hd,1)
#
# get_hd_from_child_hds(bb_hd,2)




# 输入文本





# win32gui.SendMessage(write_text_btn_hd,win32con.WM_COMMAND)






# win32gui.EnumChildWindows(root_desktop_hd, lambda hwnd, param: param.append(hwnd), new_kids)
# names=[win32gui.GetWindowText(each) for each in new_kids]
# print(names)

# get_hd_from_child_hds(p2p_hd,2)
# get_hd_from_child_hds(p2p_hd,7)
# get_hd_from_child_hds(p2p_hd,9)

# choose_pdg_dir_hd=win32gui.FindWindowEx(root_desktop_hd,0,0,choose_pdg_dir_str)
# queding_hd=win32gui.FindWindowEx(choose_pdg_dir_hd,0,0,"确定")
# queding_text=win32gui.GetWindowText(queding_hd)
# print(queding_text)


# time.sleep(2)
# get_hd_from_child_hds(choose_pdg_dir_hd,2)
# edit_pdg_dir_hd=win32gui.FindWindowEx(choose_pdg_dir_hd,0,"Edit",0)
#
# yes_pdg_dir_hd=get_hd_from_child_hds(choose_pdg_dir_hd,9)
#
# for each_char in choose_pdg_dir_str:
#     win32api.SendMessage(edit_pdg_dir_hd,win32con.WM_CHAR,each_char,0)
#
# time.sleep(1)
# win32api.SendMessage(yes_pdg_dir_hd,win32con.BM_CLICK)
#
# print("done.")


# 0x1C08a0, 也就是hds[6]




# 0x550662, 0xC90938, 0x1908A0, 会被赋值
# 也就对应着 hds[2], hds[7], hds[9] 会被赋值
# 我们先必须点选'0x1f0568'这个按钮，也就是hds[3] 才能激活，但有会来到下一个窗口

