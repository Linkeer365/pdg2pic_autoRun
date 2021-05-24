import win32api

while True:
    tempt = win32api.GetCursorPos() # 记录鼠标所处位置的坐标
    x = tempt[0]-choose_rect[0] # 计算相对x坐标
    y = tempt[1]-choose_rect[1] # 计算相对y坐标
    print(x,y)
    # time.sleep(0.5) # 每0.5s输出一次