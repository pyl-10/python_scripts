import os
import pip
from tkinter import *

# 获取python安装的第三方包，存入字典类型变量中
# install_packages = pip.get_installed_distributions()

app = Tk()
label = Label(text="all hidden files")
label.pack()
listbox = Listbox(bg="#f2f2f2", fg="red")
listbox.pack(fill=BOTH, expand=True)
path = "/Users/xing_zhi"
files = os.listdir(path)
for f in files:
    if f.startswith("."):
        listbox.insert(END, f)
app.mainloop()

