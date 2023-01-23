import asyncio
import threading
import tkinter
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
import deal_with_file as df
from temp_storage import *
from widgets import *


class window4_6:
    # 适用于认证范围为YBHNTLJ
    def __init__(self, info_dic, re=False, old2new=None):
        super().__init__()
        self.info_dic = info_dic
        window = tk.Tk()
        self.re = re
        self.old2new = old2new

        # 给窗口的可视化起名字
        if re:
            window.title('监督复评模式')
        else:
            window.title('初审模式')
        window.config(background='Lavender')

        window.geometry('900x500')  # 这里的乘是小x

        container = tk.Frame(window, background='Lavender')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = qtxxPage(container, self)
        self.frames[qtxxPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(qtxxPage)
        window.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处

    def get_info(self):
        for frame in self.frames.keys():
            for widget in self.frames[frame].widget_list:
                widget.save_value_into_info_dic(self.info_dic)
                widget.temp_save()
        gen_temp_storage()
        print('生成缓存文件成功')
        print(self.info_dic)
        df.replace_process(self.info_dic, re=self.re, old2new=self.old2new)
        showinfo(title="提示",
                 message="文档输出完成!")

    def temp_save_to_local(self):
        for frame in self.frames.keys():
            for widget in self.frames[frame].widget_list:
                widget.temp_save()
        gen_temp_storage()
        tkinter.messagebox.showinfo("success", "生成缓存文件成功")


class qtxxPage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        super().__init__(parent)
        self.config(bg='Lavender')
        btngen = tk.Button(self, text='信息无误开始生成文档！',
                           command=lambda: threading.Thread(target=root.get_info).start())
        btn_save = tk.Button(self, text='缓存信息。', command=lambda: root.temp_save_to_local())

        self.widget_list = []

        self.sjkfqdsj = EditText(self, '设计开发启动时间')
        self.sjkfqdsj.text_setting(height=1, width=25)
        self.widget_list.append(self.sjkfqdsj)

        self.sjkfjssj = EditText(self, '设计开发结束时间')
        self.sjkfjssj.text_setting(height=1, width=25)
        self.widget_list.append(self.sjkfjssj)

        self.sjkfscsj = EditText(self, '设计开发输出时间')
        self.sjkfscsj.text_setting(height=1, width=25)
        self.widget_list.append(self.sjkfscsj)

        self.sjkfcsjssj = EditText(self, '设计开发测试结束时间')
        self.sjkfcsjssj.text_setting(height=1, width=25)
        self.widget_list.append(self.sjkfcsjssj)

        self.c15bh = EditText(self, '测试C15样品编号')
        self.c15bh.text_setting(height=1, width=10)
        self.widget_list.append(self.c15bh)

        self.c20bh = EditText(self, '测试C20样品编号')
        self.c20bh.text_setting(height=1, width=10)
        self.widget_list.append(self.c20bh)

        self.c25bh = EditText(self, '测试C25样品编号')
        self.c25bh.text_setting(height=1, width=10)
        self.widget_list.append(self.c25bh)

        self.c30bh = EditText(self, '测试C30样品编号')
        self.c30bh.text_setting(height=1, width=10)
        self.widget_list.append(self.c30bh)

        self.c35bh = EditText(self, '测试C35样品编号')
        self.c35bh.text_setting(height=1, width=10)
        self.widget_list.append(self.c35bh)

        self.c40bh = EditText(self, '测试C40样品编号')
        self.c40bh.text_setting(height=1, width=10)
        self.widget_list.append(self.c40bh)

        self.c45bh = EditText(self, '测试C45样品编号')
        self.c45bh.text_setting(height=1, width=10)
        self.widget_list.append(self.c45bh)

        self.c50bh = EditText(self, '测试C50样品编号')
        self.c50bh.text_setting(height=1, width=10)
        self.widget_list.append(self.c50bh)

        self.c55bh = EditText(self, '测试C55样品编号')
        self.c55bh.text_setting(height=1, width=10)
        self.widget_list.append(self.c55bh)

        self.c60bh = EditText(self, '测试C60样品编号')
        self.c60bh.text_setting(height=1, width=10)
        self.widget_list.append(self.c60bh)

        self.yhsj7 = EditText(self, '7天养护时间')
        self.yhsj7.text_setting(height=1, width=25)
        self.widget_list.append(self.yhsj7)

        self.yhsj28 = EditText(self, '28天养护时间')
        self.yhsj28.text_setting(height=1, width=25)
        self.widget_list.append(self.yhsj28)

        btngen.grid(row=0, column=1, columnspan=2)
        self.sjkfqdsj.set_position(row=1, column=0, rowspan=1, columnspan=2)
        self.sjkfjssj.set_position(row=1, column=2, rowspan=1, columnspan=2)
        self.sjkfscsj.set_position(row=2, column=0, rowspan=1, columnspan=2)
        self.sjkfcsjssj.set_position(row=2, column=2, rowspan=1, columnspan=2)
        self.c15bh.set_position(row=3, column=0, rowspan=1, columnspan=1)
        self.c20bh.set_position(row=3, column=1, rowspan=1, columnspan=1)
        self.c25bh.set_position(row=3, column=2, rowspan=1, columnspan=1)
        self.c30bh.set_position(row=3, column=3, rowspan=1, columnspan=1)
        self.c35bh.set_position(row=4, column=0, rowspan=1, columnspan=1)
        self.c40bh.set_position(row=4, column=1, rowspan=1, columnspan=1)
        self.c45bh.set_position(row=4, column=2, rowspan=1, columnspan=1)
        self.c50bh.set_position(row=4, column=3, rowspan=1, columnspan=1)
        self.c55bh.set_position(row=5, column=0, rowspan=1, columnspan=1)
        self.c60bh.set_position(row=5, column=1, rowspan=1, columnspan=1)
        self.yhsj7.set_position(row=6, column=0, rowspan=1, columnspan=2)
        self.yhsj28.set_position(row=6, column=2, rowspan=1, columnspan=2)
        btn_save.grid(row=7, column=5, pady=20)
