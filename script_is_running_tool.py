import multiprocessing
from runpy import run_path
from tkinter import *
import multiprocessing
import os

# [script] --> func1 --> func2
# [app]  --> display() & if do() --> display() & if do()

def make_app():
    app = Tk()
    Label(text="运行脚本小工具").pack()
    Listbox(name="listb", bg="#f2f2f2").pack(fill=BOTH, expand=True)
    Button(text="运行", command=run_script).pack()
    Button(text="停止", command=stop_script).pack()
    app.geometry("300x400")
    return app

def ui_make_list():
    listb = app.children["listb"]
    for d in os.listdir():
        listb.insert(END, d)

def run_script():
    listb = app.children["listb"]
    s_path = listb.get(ACTIVE)
    p = multiprocessing.Process(name="print", target=lambda:run_path(s_path))
    p.start()

def stop_script():
    for p in multiprocessing.active_children():  # 返回一个正在运行的进程的列表
        if p.name == "print":
            p.terminate()

def watcher():
    print(multiprocessing.active_children())
    listb = app.children["listb"]
    s_path = listb.get(ACTIVE)
    print(s_path)
    app.after(1000, watcher)

app = make_app()
app.after(100, ui_make_list)
app.after(0, watcher)
app.mainloop()
