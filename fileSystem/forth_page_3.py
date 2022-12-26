import asyncio
import threading
import tkinter
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
import deal_with_file as df
from temp_storage import *
from widgets import *


class window4_3:
    # 适用于认证范围为所有且认证项目为E
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

        window.geometry('1000x500')  # 这里的乘是小x

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

        self.scbry1 = EditText(self, '生产部人员1')
        self.scbry1.text_setting(height=1, width=25)
        self.widget_list.append(self.scbry1)

        self.scbry2 = EditText(self, '生产部人员2')
        self.scbry2.text_setting(height=1, width=25)
        self.widget_list.append(self.scbry2)

        self.scbry3 = EditText(self, '生产部人员3')
        self.scbry3.text_setting(height=1, width=25)
        self.widget_list.append(self.scbry3)

        self.jyy1 = EditText(self, '检验员1')
        self.jyy1.text_setting(height=1, width=25)
        self.widget_list.append(self.jyy1)

        btngen.grid(row=0, column=1, columnspan=2)
        self.scbry1.set_position(row=1, column=0, rowspan=1, columnspan=2)
        self.scbry2.set_position(row=1, column=2, rowspan=1, columnspan=2)
        self.scbry3.set_position(row=1, column=4, rowspan=1, columnspan=2)
        self.jyy1.set_position(row=2, column=0, rowspan=1, columnspan=2)
        btn_save.grid(row=5, column=5, pady=20)


# window4_3({})
