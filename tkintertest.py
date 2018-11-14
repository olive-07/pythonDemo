from tkinter import *

root = Tk()

root.title("button组件")

# def wm_geometry(self, newGeometry=None):...
# geometry = wm_geometry
root.geometry("600x600+800+400")

li = ['C','python','php','html','SQL','java']
movie = ['CSS','jQuery','Bootstrap']

listb = Listbox(root, font=("楷体", 15), highlightbackground="red")
listb2 = Listbox(root, font=("微软雅黑", 20), highlightbackground="black")

# 列表小部件插入数据
for item in li:
    listb.insert(0, item)

for item2 in movie:
    listb2.insert(0, item2)

listb.pack()
listb2.pack()

# class Button(Widget):... def __init__(self, master=None, cnf={}, **kw):
# STANDARD OPTIONS
#
#             activebackground, activeforeground, anchor,
#             background, bitmap, borderwidth, cursor,
#             disabledforeground, font, foreground
#             highlightbackground, highlightcolor,
#             highlightthickness, image, justify,
#             padx, pady, relief, repeatdelay,
#             repeatinterval, takefocus, text,
#             textvariable, underline, wraplength
#
#         WIDGET-SPECIFIC OPTIONS
#
#             command, compound, default, height（非像素高度）,
#             overrelief, state, width（非像素高度）
bm1 = Button(text="button1控件", borderwidth="2", font=("微软雅黑", 15), background="white")
# bm1.pack()

# def grid_configure(self, cnf={}, **kw):
# bm1.grid()

# def place_configure(self, cnf={}, **kw):
# x,y : 小部件在主控中的位置
# width,height : 小部件的像素宽和像素高
bm1.place(x=10, y=10, width=150, height=100)

root.mainloop()