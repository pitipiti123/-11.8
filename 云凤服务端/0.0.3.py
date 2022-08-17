# 模块引入区域
import os
from tkinter import *
from tkinter import messagebox


# gui基础变量
root = Tk()
root.geometry('800x500')
root.title('云凤服务器启动器')
menubar = Menu(root)
msg = messagebox


# 问题反馈功能
def NoResponse():
    messagebox.askokcancel("help", '一般是电脑/服务器运行服务端的时候加载速度较慢导致，没有大问题')


# 服务器功能
def start():
    with open("start.bat", "w", encoding="utf-8") as f:
        f.write("java -jar server.jar")


# eula修改
def updateFile(file, old_str, new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


# 初始化服务器
def FirstServer():
    start()
    os.system("start.bat")


# 启动服务器
def StartServer():
    os.system("start.bat")


# 交流群
def SayTome():
    msg.showinfo("联系我们", 'qq：317410440')


# 具体GUI区域
# 创建顶级列表File
File = Menu(menubar, tearoff=False)
File.add_command(label="一键eula",
                 command=lambda: messagebox.showwarning("警告", '使用此功能默认同意eula协议 ') and updateFile(r"eula.txt", "false",
                                                                                                 "true"))
File.add_command(label="初始化服务器", command=lambda: FirstServer())
File.add_command(label="开启服务器", command=lambda: StartServer())
File.add_separator()
File.add_command(label="联系我们", command=lambda: SayTome())
menubar.add_cascade(label="云凤工具箱", menu=File)
# 创建顶级列表Question
Question = Menu(menubar, tearoff=False)
Question.add_command(label="启动器无响应", command=lambda: NoResponse())
menubar.add_cascade(label="问题中心", menu=Question)
# 显示菜单
root.config(menu=menubar)
root.mainloop()
