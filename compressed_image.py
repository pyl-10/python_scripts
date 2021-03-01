# 压缩图片
# 点击 -》 压缩

from PIL import Image as Img

# path = ""
# new_path = ""
# image = Image.open(path)
# image.save(new_path, quality=60)  # quality=60 质量压缩为原来的百分之六十

from tkinter import *
from tkinter.filedialog import *

# def do():
#     print(1)

# app = Tk()
# Button(text="click", command=do).pack()

# app.mainloop()

# ui
# ui update
# business
info = {
    "path": []
}

def make_app():
    app = Tk()
    Label(app, text="压缩图片工具").pack()
    Listbox(app, name="lbox", bg="#f2f2f2").pack(fill=BOTH, expand=True)
    Button(app, text="打开图片", command=ui_getdata).pack()
    Button(app, text="压缩", command=compress).pack()
    app.geometry("300x400")
    return app

def ui_getdata():
    f_names = askopenfilenames()
    lbox = app.children["lbox"]
    info["path"] = f_names
    if info["path"]:
        for name in f_names:
            lbox.insert(END, name.split("/")[-1])

def compress():
    for f_path in info["path"]:
        output = "/Users/xing_zhi/Downloads/"
        name = f_path.split("/")[-1]
        image = Img.open(f_path)
        image.save(output+"c_"+name, quality=60)

app = make_app()
app.mainloop()

