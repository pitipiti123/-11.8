import easygui as g
import os

firstline = ''
run = True


def read():
    global firstline
    o = open("YFconfig.txt", "r", encoding="UTF-8")
    firstline = o.readline().rstrip()
    return firstline


def updateFile(file, old_str, new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


def start():
    with open("start.bat", "w", encoding="utf-8") as f:
        f.write("java -jar server.jar")


def use(mane):
    with open("server.txt", "w", encoding="UTF-8") as name:
        name.write(mane)


def mune():
    global run
    l = ["一键eula", "初始化服务器", "启动服务器", "更改server配置文件", "退出"]
    m = g.choicebox(choices=l, msg="YunFeng服务器开发工具", title="YunFengMC")
    if m == "一键eula":
        p = g.msgbox(msg="确定即同意eula协议", ok_button="确定", title="YunFengMC")
        if p == "确定":
            updateFile(r"eula.txt", "false", "true")
            g.msgbox(msg="更改成功", title="YunFengMC")
    if m == "启动服务器":
        os.system("start.bat")
    if m == "初始化服务器":
        start()
        os.system("start.bat")
    if m == "退出":
        run = False
    if m == "更改server配置文件":
        file_object = open('server.properties', "r")
        try:
            all_the_text = file_object.read()
            use(all_the_text)
        finally:
            file_object.close()


while run:
    mune()
