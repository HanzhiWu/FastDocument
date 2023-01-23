import asyncio
import threading
import tkinter
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
import deal_with_file as df
from temp_storage import *
from widgets import *


class window4_5:
    # 适用于认证范围为JC/XS/FW/WL/JCXS/FWXS/WL且认证项目为QS/QES
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

        self.sjaqjyspxr1 = EditText(self, '三级安全教育受培训人1')
        self.sjaqjyspxr1.text_setting(height=1, width=25)
        self.widget_list.append(self.sjaqjyspxr1)

        self.sjaqjyspxr2 = EditText(self, '三级安全教育受培训人2')
        self.sjaqjyspxr2.text_setting(height=1, width=25)
        self.widget_list.append(self.sjaqjyspxr2)

        self.sjaqjyrq1 = EditText(self, '三级安全教育第一天日期')
        self.sjaqjyrq1.text_setting(height=1, width=12)
        self.widget_list.append(self.sjaqjyrq1)

        self.sjaqjyrq2 = EditText(self, '三级安全教育第二天日期')
        self.sjaqjyrq2.text_setting(height=1, width=12)
        self.widget_list.append(self.sjaqjyrq2)

        self.sjaqjyrq3 = EditText(self, '三级安全教育第三天日期')
        self.sjaqjyrq3.text_setting(height=1, width=12)
        self.widget_list.append(self.sjaqjyrq3)

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

        self.sjaqjybzpxr = EditText(self, '三级安全教育班组培训人')
        self.sjaqjybzpxr.text_setting(height=1, width=12)
        self.widget_list.append(self.sjaqjybzpxr)

        self.tsgcxs = GroupButtonWithText(self, "特殊过程销售", "有销售过程", "无销售过程", "特殊过程销售业务员")
        self.widget_list.append(self.tsgcxs)

        self.xsbry1 = EditText(self, '销售部人员1')
        self.xsbry1.text_setting(height=1, width=25)
        self.widget_list.append(self.xsbry1)

        self.xsbry2 = EditText(self, '销售部人员2')
        self.xsbry2.text_setting(height=1, width=25)
        self.widget_list.append(self.xsbry2)

        rzfw, _, _, _ = root.info_dic['template_id'].split('-')
        btngen.grid(row=0, column=1, columnspan=2)
        self.sjaqjyspxr1.set_position(row=1, column=0, rowspan=1, columnspan=2)
        self.sjaqjyspxr2.set_position(row=1, column=2, rowspan=1, columnspan=2)
        self.sjaqjyrq1.set_position(row=2, column=0, rowspan=1, columnspan=2)
        self.sjaqjyrq2.set_position(row=2, column=2, rowspan=1, columnspan=2)
        self.sjaqjyrq3.set_position(row=2, column=4, rowspan=1, columnspan=2)
        self.scbry1.set_position(row=3, column=0, rowspan=1, columnspan=2)
        self.scbry2.set_position(row=3, column=2, rowspan=1, columnspan=2)
        self.scbry3.set_position(row=3, column=4, rowspan=1, columnspan=2)
        self.jyy1.set_position(row=4, column=0, rowspan=1, columnspan=2)
        self.sjaqjybzpxr.set_position(row=4, column=2, rowspan=1, columnspan=2)
        self.tsgcxs.set_position(row=5, column=0, rowspan=1, columnspan=5)
        if 'XS' in rzfw:
            self.xsbry1.set_position(row=6, column=0, rowspan=1, columnspan=2)
            self.xsbry2.set_position(row=6, column=2, rowspan=1, columnspan=2)
        btn_save.grid(row=7, column=5, pady=20)

# window4_5({})
