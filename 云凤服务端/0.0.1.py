import os
import easygui
import subprocess
run = True

with open("chois.txt", "w", encoding="utf-8") as f:
    lines = f.write("0")


def start():
    with open("start.bat", "a", encoding="utf-8") as f:
        f.write("java -jar server.jar")

def gongju():
    global run
    with open("YFconfig.txt", "r", encoding="utf-8") as f:
        lines = f.read()
    m = ["启动服务器（只能用一次）", "启动服务器", "exit"]
    l = easygui.buttonbox(msg="YunFengServer工具箱", title="YunFeng Server", choices=m)
    if l == "启动服务器（只能用一次）" and lines == "0":
        start()
        os.system("start.bat")
        updateFile(r"eula.txt", "false", "true")
        os.system("start.bat")
        with open("chois.txt", "w", encoding="utf-8") as f:
            f.write("1")
        run = False
    if l == "启动服务器":
        os.system("start.bat")
    if l == "exit":
        run = False


def updateFile(file, old_str, new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


while run:
    gongju()
