import threading
import tkinter
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
import deal_with_file as df

# 第四层界面
from widgets import *


class window4_2:
    def __init__(self, info_dic, re=False, old2new=None):
        super().__init__()
        window = tk.Tk()
        self.re = re
        self.old2new = old2new

        # 给窗口的可视化起名字
        if re:
            window.title('监督复评模式')
        else:
            window.title('初审模式')
        window.config(background='Lavender')

        window.geometry('1280x650')  # 这里的乘是小x

        container = tk.Frame(window, background='Lavender')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.info_dic = info_dic

        for F in (cpgxPage, cpxxPage, qtxxPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(cpgxPage)
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


class cpgxPage(tk.Frame):
    """主页"""

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: [root.show_frame(cpgxPage)])
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
        btngen = tk.Button(self, text='信息无误开始生成文档！',
                           command=lambda: threading.Thread(target=root.get_info).start())

        self.cpgx1 = AddText(self, "产品1工序信息", "产品1", "修改产品1工序信息", [60, 60], ["工序", "操作工"],
                             position=AddText.PositionEnum.END)
        self.cpgx2 = AddText(self, "产品2工序信息", "产品2", "修改产品2工序信息", [60, 60], ["工序", "操作工"],
                             position=AddText.PositionEnum.END)
        self.cpgx3 = AddText(self, "产品3工序信息", "产品3", "修改产品3工序信息", [60, 60], ["工序", "操作工"],
                             position=AddText.PositionEnum.END)
        self.cpgx4 = AddText(self, "产品4工序信息", "产品4", "修改产品4工序信息", [60, 60], ["工序", "操作工"],
                             position=AddText.PositionEnum.END)
        self.cpgx5 = AddText(self, "产品5工序信息", "产品5", "修改产品5工序信息", [60, 60], ["工序", "操作工"],
                             position=AddText.PositionEnum.END)
        self.widget_list = [self.cpgx1, self.cpgx2, self.cpgx3, self.cpgx4, self.cpgx5]
        btn_save = tk.Button(self, text='缓存信息。', command=lambda: root.temp_save_to_local())

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btnqtxx.grid(row=0, column=2)
        btngen.grid(row=0, column=3, columnspan=2)
        self.cpgx1.set_position(row=1, column=0, rowspan=4, columnspan=4)
        self.cpgx2.set_position(row=5, column=0, rowspan=4, columnspan=4)
        self.cpgx3.set_position(row=9, column=0, rowspan=4, columnspan=4)
        self.cpgx4.set_position(row=13, column=0, rowspan=4, columnspan=4)
        self.cpgx5.set_position(row=17, column=0, rowspan=4, columnspan=4)
        btn_save.grid(row=21, column=4, pady=20)


class cpxxPage(tk.Frame):
    """主页"""

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: [root.show_frame(cpgxPage)])
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
        btngen = tk.Button(self, text='信息无误开始生成文档！',
                           command=lambda: threading.Thread(target=root.get_info).start())

        self.cpxx1 = AddText(self, "产品1信息", "生产产品1的", "修改产品1信息", [10, 10, 8, 10, 10, 8, 10],
                             ['号产品', '号产品型号', '号产品数量', '号产品日期', '号产品客户', '号产品批号',
                              '号产品订货时间'])
        self.cpxx2 = AddText(self, "产品2信息", "生产产品2的", "修改产品2信息", [10, 10, 8, 10, 10, 8, 10],
                             ['号产品', '号产品型号', '号产品数量', '号产品日期', '号产品客户', '号产品批号',
                              '号产品订货时间'])
        self.cpxx3 = AddText(self, "产品3信息", "生产产品3的", "修改产品3信息", [10, 10, 8, 10, 10, 8, 10],
                             ['号产品', '号产品型号', '号产品数量', '号产品日期', '号产品客户', '号产品批号',
                              '号产品订货时间'])
        self.cpxx4 = AddText(self, "产品4信息", "生产产品4的", "修改产品4信息", [10, 10, 8, 10, 10, 8, 10],
                             ['号产品', '号产品型号', '号产品数量', '号产品日期', '号产品客户', '号产品批号',
                              '号产品订货时间'])
        self.cpxx5 = AddText(self, "产品5信息", "生产产品5的", "修改产品5信息", [10, 10, 8, 10, 10, 8, 10],
                             ['号产品', '号产品型号', '号产品数量', '号产品日期', '号产品客户', '号产品批号',
                              '号产品订货时间'])
        self.widget_list = [self.cpxx1, self.cpxx2, self.cpxx3, self.cpxx4, self.cpxx5]

        btn_save = tk.Button(self, text='缓存信息。', command=lambda: root.temp_save_to_local())

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btnqtxx.grid(row=0, column=2)
        btngen.grid(row=0, column=3, columnspan=2)
        self.cpxx1.set_position(row=1, column=0, rowspan=4, columnspan=4)
        self.cpxx2.set_position(row=5, column=0, rowspan=4, columnspan=4)
        self.cpxx3.set_position(row=9, column=0, rowspan=4, columnspan=4)
        self.cpxx4.set_position(row=13, column=0, rowspan=4, columnspan=4)
        self.cpxx5.set_position(row=17, column=0, rowspan=4, columnspan=4)
        btn_save.grid(row=21, column=4, pady=20)


class qtxxPage(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: root.show_frame(cpgxPage))
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
        btngen = tk.Button(self, text='信息无误开始生成文档！',
                           command=lambda: threading.Thread(target=root.get_info).start())

        self.widget_list = []
        self.jyy1 = EditText(self, '检验员1')
        self.jyy1.text_setting(height=1, width=25)
        self.widget_list.append(self.jyy1)

        self.scbry1 = EditText(self, '生产部人员1')
        self.scbry1.text_setting(height=1, width=25)
        self.widget_list.append(self.scbry1)

        self.scbry2 = EditText(self, '生产部人员2')
        self.scbry2.text_setting(height=1, width=25)
        self.widget_list.append(self.scbry2)

        self.scbry3 = EditText(self, '生产部人员3')
        self.scbry3.text_setting(height=1, width=25)
        self.widget_list.append(self.scbry3)

        self.tsgcjb = GroupButtonWithText(self, "特殊过程搅拌", "有搅拌过程", "无搅拌过程", "特殊过程搅拌搅拌工")
        self.widget_list.append(self.tsgcjb)
        self.tsgcbmjsh = GroupButtonWithText(self, "特殊过程薄膜金属化", "有薄膜金属化过程", "无薄膜金属化过程",
                                             "特殊过程薄膜金属化操作工")
        self.widget_list.append(self.tsgcbmjsh)
        self.tsgchj = GroupButtonWithText(self, "特殊过程焊接", "有焊接过程", "无焊接过程", "特殊过程焊接操作工")
        self.widget_list.append(self.tsgchj)
        self.tsgchh = GroupButtonWithText(self, "特殊过程混合", "有混合过程", "无混合过程", "特殊过程混合操作工")
        self.widget_list.append(self.tsgchh)
        self.tsgcjc = GroupButtonWithText(self, "特殊过程挤出", "有挤出过程", "无挤出过程", "特殊过程挤出操作工")
        self.widget_list.append(self.tsgcjc)
        self.tsgcxs = GroupButtonWithText(self, "特殊过程销售", "有销售过程", "无销售过程", "特殊过程销售操作工")
        self.widget_list.append(self.tsgcxs)

        self.kyj = GroupButton(self, "有无空压机", "有空压机", "无空压机")
        self.widget_list.append(self.kyj)

        self.xsbry1 = EditText(self, '销售部人员1')
        self.xsbry1.text_setting(height=1, width=25)
        self.widget_list.append(self.xsbry1)

        self.xsbry2 = EditText(self, '销售部人员2')
        self.xsbry2.text_setting(height=1, width=25)
        self.widget_list.append(self.xsbry2)

        btn_save = tk.Button(self, text='缓存信息。', command=lambda: root.temp_save_to_local())

        rzfw, _, _, _ = root.info_dic['template_id'].split('-')
        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btnqtxx.grid(row=0, column=2)
        btngen.grid(row=0, column=3, columnspan=3)
        self.jyy1.set_position(row=1, column=0, columnspan=2)
        self.scbry1.set_position(row=2, column=0, columnspan=2)
        self.scbry2.set_position(row=2, column=2, columnspan=2)
        self.scbry3.set_position(row=2, column=4, columnspan=2)
        self.tsgcjb.set_position(row=3, column=0, rowspan=2, columnspan=6)
        self.tsgcbmjsh.set_position(row=5, column=0, rowspan=2, columnspan=6)
        self.tsgchj.set_position(row=7, column=0, rowspan=2, columnspan=6)
        self.tsgchh.set_position(row=9, column=0, rowspan=2, columnspan=6)
        self.tsgcjc.set_position(row=11, column=0, rowspan=2, columnspan=6)
        self.tsgcxs.set_position(row=13, column=0, rowspan=2, columnspan=6)
        self.kyj.set_position(row=15, column=0, rowspan=1, columnspan=2)
        if 'XS' in rzfw:
            self.xsbry1.set_position(row=16, column=0, rowspan=1, columnspan=2)
            self.xsbry2.set_position(row=16, column=2, rowspan=1, columnspan=2)
        btn_save.grid(row=17, column=4, pady=20)


# window4_2({})
