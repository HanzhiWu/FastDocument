import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import deal_with_file as df


class window4_4():
    # 适用于认证范围为SC/ZZ/JJSC且认证项目为S/ES
    def __init__(self, info_dic):
        super().__init__()
        self.info_dic = info_dic
        window = tk.Tk()

        # 给窗口的可视化起名字
        window.title('认证文件管理系统')
        window.config(background='Lavender')

        window.geometry('1280x650')  # 这里的乘是小x

        container = tk.Frame(window, background='Lavender')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = qtxxPage_4(container, self)
        self.frames[qtxxPage_4] = frame
        frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(qtxxPage_4)
        window.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处

    def add_item_to_dict(self, edit_text, key_str):
        self.info_dic['__{}__'.format(key_str)] = edit_text.get(0.0, 20.0).strip()

    def getinfo(self):
        f_qtxx = self.frames[qtxxPage_4]
        self.add_item_to_dict(f_qtxx.sjaqjyspxr1, '三级安全教育受培训人1')
        self.add_item_to_dict(f_qtxx.sjaqjyspxr2, '三级安全教育受培训人2')
        self.add_item_to_dict(f_qtxx.sjaqjyrq1, '三级安全教育第一天日期')
        self.add_item_to_dict(f_qtxx.sjaqjyrq2, '三级安全教育第二天日期')
        self.add_item_to_dict(f_qtxx.sjaqjyrq3, '三级安全教育第三天日期')
        self.add_item_to_dict(f_qtxx.sjaqjybzpxr3, '三级安全教育班组培训人')
        if f_qtxx.kyjV.get() == 0:
            self.info_dic['__是否有空压机__'] = '否'
        else:
            self.info_dic['__是否有空压机__'] = '是'
        df.ReplaceProcess(self.info_dic)
        showinfo(title="提示",
                 message="文档输出完成!")


class qtxxPage_4(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        super().__init__(parent)
        self.config(bg='Lavender')
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        sjaqjyspxr1_L = Label(self, text='三级安全教育受培训人1：', bg='Lavender')
        self.sjaqjyspxr1 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyspxr2_L = Label(self, text='三级安全教育受培训人2：', bg='Lavender')
        self.sjaqjyspxr2 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyrq1_L = Label(self, text='三级安全教育第一天日期：', bg='Lavender')
        self.sjaqjyrq1 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyrq2_L = Label(self, text='三级安全教育第二天日期：', bg='Lavender')
        self.sjaqjyrq2 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyrq3_L = Label(self, text='三级安全教育第三天日期：', bg='Lavender')
        self.sjaqjyrq3 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjybzpxr3_L = Label(self, text='三级安全教育班组培训人：', bg='Lavender')
        self.sjaqjybzpxr3 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        self.kyjV = tk.IntVar(master=self)
        kyjC1 = tk.Radiobutton(self, text="有空压机", variable=self.kyjV, value=1, bg='Lavender')
        kyjC2 = tk.Radiobutton(self, text="无空压机", variable=self.kyjV, value=0, bg='Lavender')

        btngen.grid(row=0, column=2)

        sjaqjyspxr1_L.grid(row=8, column=0)
        self.sjaqjyspxr1.grid(row=8, column=1)
        sjaqjyspxr2_L.grid(row=8, column=2)
        self.sjaqjyspxr2.grid(row=8, column=3)

        sjaqjyrq1_L.grid(row=9, column=0)
        self.sjaqjyrq1.grid(row=9, column=1)
        sjaqjyrq2_L.grid(row=9, column=2)
        self.sjaqjyrq2.grid(row=9, column=3)
        sjaqjyrq3_L.grid(row=9, column=4)
        self.sjaqjyrq3.grid(row=9, column=5)

        sjaqjybzpxr3_L.grid(row=10, column=0)
        self.sjaqjybzpxr3.grid(row=10, column=1)

        kyjC1.grid(row=10, column=2)
        kyjC2.grid(row=10, column=3)
