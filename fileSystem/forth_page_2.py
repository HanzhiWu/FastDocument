import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import deal_with_file as df






class window4_2():
    # 适用于认证范围为SC/ZZ/JJSC且认证项目为Q/QE
    def __init__(self, info_dic):
        super().__init__()
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
        self.info_dic = info_dic
        for F in (cpgxPage_2, cpczPage_2, cpxxPage_2, qtxxPage_2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(cpgxPage_2)
        window.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处

    def add_cp_info_to_dict(self, text_str, index, common_str):
        """
        处理形式如 产品x操作工/工序x的文本框
        """
        row_list = text_str.split('\n')
        if len(row_list) == 0:
            return
        for row in range(len(row_list)):
            key_str = '__产品{}{}{}__'.format(index, common_str, row)
            self.info_dic[key_str] = row_list[row]

    def add_cpxx_to_dict(self, text_str, index):
        """
        处理产品信息部分的文本框
        """
        key_list = ['产品', '产品型号', '产品数量', '产品日期', '产品客户']
        row_list = text_str.split('\n')
        if len(row_list) == 0:
            return
        item_list = [row.split(',') for row in row_list]

        for row in range(len(row_list)):
            for item in range(len(item_list[0])):
                key_str = '__生产产品{}的{}号{}__'.format(index, row, key_list[item])
                val = item_list[row][item]
                if item == 0 and val == '':
                    val = '无'
                self.info_dic[key_str] = val

    '''
    第四个页面中处理的相关函数
    '''

    def add_item_to_dict(self, edit_text, key_str):
        self.info_dic['__{}__'.format(key_str)] = edit_text.get(0.0, 20.0).strip()

    def add_radio_res_to_dict(self, radio_val, key_str, edit_text, edit_str):
        if radio_val.get() == 0:
            self.info_dic['__{}__'.format(key_str)] = '无'
            self.info_dic['__{}__'.format(edit_str)] = ''
        else:
            self.info_dic['__{}__'.format(key_str)] = '有'
            self.info_dic['__{}__'.format(edit_str)] = edit_text.get(0.0, 20.0).strip()

    def getinfo(self):
        # 将修改五个产品的工序的信息添加到字典里
        self.add_cp_info_to_dict(self.frames[cpgxPage_2].cpgx1_text.get(0.0, 20.0).strip(), 1, "工序")
        self.add_cp_info_to_dict(self.frames[cpgxPage_2].cpgx2_text.get(0.0, 20.0).strip(), 2, "工序")
        self.add_cp_info_to_dict(self.frames[cpgxPage_2].cpgx3_text.get(0.0, 20.0).strip(), 3, "工序")
        self.add_cp_info_to_dict(self.frames[cpgxPage_2].cpgx4_text.get(0.0, 20.0).strip(), 4, "工序")
        self.add_cp_info_to_dict(self.frames[cpgxPage_2].cpgx5_text.get(0.0, 20.0).strip(), 5, "工序")

        # 将修改五个产品的操作工的信息添加到字典里
        self.add_cp_info_to_dict(self.frames[cpczPage_2].cpgx1_text.get(0.0, 20.0).strip(), 1, "操作工")
        self.add_cp_info_to_dict(self.frames[cpczPage_2].cpgx2_text.get(0.0, 20.0).strip(), 2, "操作工")
        self.add_cp_info_to_dict(self.frames[cpczPage_2].cpgx3_text.get(0.0, 20.0).strip(), 3, "操作工")
        self.add_cp_info_to_dict(self.frames[cpczPage_2].cpgx4_text.get(0.0, 20.0).strip(), 4, "操作工")
        self.add_cp_info_to_dict(self.frames[cpczPage_2].cpgx5_text.get(0.0, 20.0).strip(), 5, "操作工")

        # 将修改五个产品的操作信息的信息添加到字典里
        self.add_cpxx_to_dict(self.frames[cpxxPage_2].cpgx1_text.get(0.0, 20.0).strip(), 1)
        self.add_cpxx_to_dict(self.frames[cpxxPage_2].cpgx2_text.get(0.0, 20.0).strip(), 2)
        self.add_cpxx_to_dict(self.frames[cpxxPage_2].cpgx3_text.get(0.0, 20.0).strip(), 3)
        self.add_cpxx_to_dict(self.frames[cpxxPage_2].cpgx4_text.get(0.0, 20.0).strip(), 4)
        self.add_cpxx_to_dict(self.frames[cpxxPage_2].cpgx5_text.get(0.0, 20.0).strip(), 5)

        # 第四个界面信息收集
        f_qtxx = self.frames[qtxxPage_2]
        self.add_item_to_dict(f_qtxx.jyy1, '检验员1')
        self.add_item_to_dict(f_qtxx.scbry1, '生产部人员1')
        self.add_item_to_dict(f_qtxx.scbry2, '生产部人员2')
        self.add_radio_res_to_dict(f_qtxx.tsgcjbV, '特殊过程搅拌', f_qtxx.tsgcjb, '特殊过程搅拌搅拌工')
        self.add_radio_res_to_dict(f_qtxx.tsgcbmjshV, '特殊过程薄膜金属化', f_qtxx.tsgcbmjsh,
                                   '特殊过程薄膜金属化操作工')
        self.add_radio_res_to_dict(f_qtxx.tsgchjV, '特殊过程焊接', f_qtxx.tsgchj, '特殊过程焊接操作工')
        self.add_radio_res_to_dict(f_qtxx.tsgchhV, '特殊过程混合', f_qtxx.tsgchh, '特殊过程混合操作工')
        self.add_radio_res_to_dict(f_qtxx.tsgcjcV, '特殊过程挤出', f_qtxx.tsgcjc, '特殊过程挤出操作工')
        if f_qtxx.kyjV.get() == 0:
            self.info_dic['__是否有空压机__'] = '否'
        else:
            self.info_dic['__是否有空压机__'] = '是'

        df.ReplaceProcess(self.info_dic)
        showinfo(title="提示",
                 message="文档输出完成!")


class cpgxPage_2(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: [root.show_frame(cpgxPage_2)])
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage_2))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage_2))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage_2))
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        self.cpgx1_text = Text(self, width=120, heigh=4, state=DISABLED)
        self.cpgx1win_L = Label(self, text='产品1工序：', bg='Lavender')
        self.btn_cpgx1 = tk.Button(self, text='修改产品1工序。', command=lambda: cpgx1self())
        self.cpgx1_info = [self.cpgx1_text.get(0.0, 40.0)]

        def cpgx1self():
            info_self = tk.Tk()
            info_self.title('产品1工序')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx1Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品1工序{}：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx1Add(self, cpgx1_i, infos):
                line_list = []
                cpgx1cp_L = Label(self, text='产品1工序{}：'.format(cpgx1_i), bg='Lavender')
                cpgx1cp = Text(self, height=1, width=120, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[0])
                line_list.append(cpgx1cp_L)
                line_list.append(cpgx1cp)

                btn_del = Button(info_self, text='删除该工序', command=lambda: cpgx1Del(cpgx1_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx1Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                self.cpgx1_info[0] = infos
                self.cpgx1_text.config(state=NORMAL)
                self.cpgx1_text.delete(0.0, "end")
                self.cpgx1_text.insert(0.0, infos)
                self.cpgx1_text.config(state=DISABLED)
                info_self.destroy()

            infos = self.cpgx1_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx1Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增工序信息。',
                                command=lambda: cpgx1Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx1Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx2_text = Text(self, width=120, heigh=4)
        self.cpgx2win_L = Label(self, text='产品2工序：', bg='Lavender')
        self.btn_cpgx2 = tk.Button(self, text='修改产品2工序。', command=lambda: cpgx2self())
        cpgx2_info = [self.cpgx2_text.get(0.0, 40.0)]

        def cpgx2self():
            info_self = tk.Tk()
            info_self.title('产品2工序')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx2Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品2工序{}：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx2Add(self, cpgx2_i, infos):
                line_list = []
                cpgx2cp_L = Label(self, text='产品2工序{}：'.format(cpgx2_i), bg='Lavender')
                cpgx2cp = Text(self, height=1, width=120, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx2cp.insert(0.0, infos[0])
                line_list.append(cpgx2cp_L)
                line_list.append(cpgx2cp)

                btn_del = Button(info_self, text='删除该工序', command=lambda: cpgx2Del(cpgx2_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx2Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                cpgx2_info[0] = infos
                self.cpgx2_text.delete(0.0, "end")
                self.cpgx2_text.insert(0.0, infos)
                info_self.destroy()

            infos = cpgx2_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx2Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增工序信息。',
                                command=lambda: cpgx2Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx2Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx3_text = Text(self, width=120, heigh=4)
        self.cpgx3win_L = Label(self, text='产品3工序：', bg='Lavender')
        self.btn_cpgx3 = tk.Button(self, text='修改产品3工序。', command=lambda: cpgx3self())
        cpgx3_info = [self.cpgx3_text.get(0.0, 40.0)]

        def cpgx3self():
            info_self = tk.Tk()
            info_self.title('产品3工序')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx3Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品3工序{}：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx3Add(self, cpgx3_i, infos):
                line_list = []
                cpgx3cp_L = Label(self, text='产品3工序{}：'.format(cpgx3_i), bg='Lavender')
                cpgx3cp = Text(self, height=1, width=120, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx3cp.insert(0.0, infos[0])
                line_list.append(cpgx3cp_L)
                line_list.append(cpgx3cp)

                btn_del = Button(info_self, text='删除该工序', command=lambda: cpgx3Del(cpgx3_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx3Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                cpgx3_info[0] = infos
                self.cpgx3_text.delete(0.0, "end")
                self.cpgx3_text.insert(0.0, infos)
                info_self.destroy()

            infos = cpgx3_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx3Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增工序信息。',
                                command=lambda: cpgx3Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx3Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx4_text = Text(self, width=120, heigh=4)
        self.cpgx4win_L = Label(self, text='产品4工序：', bg='Lavender')
        self.btn_cpgx4 = tk.Button(self, text='修改产品4工序。', command=lambda: cpgx4self())
        cpgx4_info = [self.cpgx4_text.get(0.0, 40.0)]

        def cpgx4self():
            info_self = tk.Tk()
            info_self.title('产品4工序')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx4Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品4工序{}：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx4Add(self, cpgx4_i, infos):
                line_list = []
                cpgx4cp_L = Label(self, text='产品4工序{}：'.format(cpgx4_i), bg='Lavender')
                cpgx4cp = Text(self, height=1, width=120, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx4cp.insert(0.0, infos[0])
                line_list.append(cpgx4cp_L)
                line_list.append(cpgx4cp)

                btn_del = Button(info_self, text='删除该工序', command=lambda: cpgx4Del(cpgx4_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx4Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                cpgx4_info[0] = infos
                self.cpgx4_text.delete(0.0, "end")
                self.cpgx4_text.insert(0.0, infos)
                info_self.destroy()

            infos = cpgx4_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx4Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增工序信息。',
                                command=lambda: cpgx4Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx4Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx5_text = Text(self, width=120, heigh=4)
        self.cpgx5win_L = Label(self, text='产品5工序：', bg='Lavender')
        self.btn_cpgx5 = tk.Button(self, text='修改产品5工序。', command=lambda: cpgx5self())
        cpgx5_info = [self.cpgx5_text.get(0.0, 40.0)]

        def cpgx5self():
            info_self = tk.Tk()
            info_self.title('产品5工序')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx5Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品5工序{}：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx5Add(self, cpgx5_i, infos):
                line_list = []
                cpgx5cp_L = Label(self, text='产品5工序{}：'.format(cpgx5_i), bg='Lavender')
                cpgx5cp = Text(self, height=1, width=120, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx5cp.insert(0.0, infos[0])
                line_list.append(cpgx5cp_L)
                line_list.append(cpgx5cp)

                btn_del = Button(info_self, text='删除该工序', command=lambda: cpgx5Del(cpgx5_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx5Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                cpgx5_info[0] = infos
                self.cpgx5_text.delete(0.0, "end")
                self.cpgx5_text.insert(0.0, infos)
                info_self.destroy()

            infos = cpgx5_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx5Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增工序信息。',
                                command=lambda: cpgx5Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx5Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btncpcz.grid(row=0, column=2)
        btnqtxx.grid(row=0, column=3)
        btngen.grid(row=0, column=4)

        self.cpgx1win_L.grid(row=1, column=0, rowspan=2)
        self.btn_cpgx1.grid(row=3, column=0, rowspan=2)
        self.cpgx1_text.grid(row=1, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx2win_L.grid(row=5, column=0, rowspan=2)
        self.btn_cpgx2.grid(row=7, column=0, rowspan=2)
        self.cpgx2_text.grid(row=5, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx3win_L.grid(row=9, column=0, rowspan=2)
        self.btn_cpgx3.grid(row=11, column=0, rowspan=2)
        self.cpgx3_text.grid(row=9, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx4win_L.grid(row=13, column=0, rowspan=2)
        self.btn_cpgx4.grid(row=15, column=0, rowspan=2)
        self.cpgx4_text.grid(row=13, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx5win_L.grid(row=17, column=0, rowspan=2)
        self.btn_cpgx5.grid(row=19, column=0, rowspan=2)
        self.cpgx5_text.grid(row=17, column=1, rowspan=4, pady=5, columnspan=4)


class cpczPage_2(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: root.show_frame(cpgxPage_2))
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage_2))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage_2))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage_2))
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        self.cpgx1_text = Text(self, width=120, heigh=4, state=DISABLED)
        self.cpgx1win_L = Label(self, text='产品1操作工：', bg='Lavender')
        self.btn_cpgx1 = tk.Button(self, text='修改产品1操作工。', command=lambda: cpgx1self())
        self.cpgx1_info = [self.cpgx1_text.get(0.0, 40.0)]

        def cpgx1self():
            info_self = tk.Tk()
            info_self.title('产品1操作工')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx1Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品1操作工{}：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx1Add(self, cpgx1_i, infos):
                line_list = []
                cpgx1cp_L = Label(self, text='产品1操作工{}：'.format(cpgx1_i), bg='Lavender')
                cpgx1cp = Text(self, height=1, width=120, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[0])
                line_list.append(cpgx1cp_L)
                line_list.append(cpgx1cp)

                btn_del = Button(info_self, text='删除该操作工', command=lambda: cpgx1Del(cpgx1_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx1Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                self.cpgx1_info[0] = infos
                self.cpgx1_text.config(state=NORMAL)
                self.cpgx1_text.delete(0.0, "end")
                self.cpgx1_text.insert(0.0, infos)
                self.cpgx1_text.config(state=DISABLED)
                info_self.destroy()

            infos = self.cpgx1_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx1Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增操作工信息。',
                                command=lambda: cpgx1Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx1Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx2_text = Text(self, width=120, heigh=4)
        self.cpgx2win_L = Label(self, text='产品2操作工：', bg='Lavender')
        self.btn_cpgx2 = tk.Button(self, text='修改产品2操作工。', command=lambda: cpgx2self())
        cpgx2_info = [self.cpgx2_text.get(0.0, 40.0)]

        def cpgx2self():
            info_self = tk.Tk()
            info_self.title('产品2操作工')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx2Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品2操作工{}：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx2Add(self, cpgx2_i, infos):
                line_list = []
                cpgx2cp_L = Label(self, text='产品2操作工{}：'.format(cpgx2_i), bg='Lavender')
                cpgx2cp = Text(self, height=1, width=120, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx2cp.insert(0.0, infos[0])
                line_list.append(cpgx2cp_L)
                line_list.append(cpgx2cp)

                btn_del = Button(info_self, text='删除该操作工', command=lambda: cpgx2Del(cpgx2_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx2Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                cpgx2_info[0] = infos
                self.cpgx2_text.delete(0.0, "end")
                self.cpgx2_text.insert(0.0, infos)
                info_self.destroy()

            infos = cpgx2_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx2Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增操作工信息。',
                                command=lambda: cpgx2Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx2Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx3_text = Text(self, width=120, heigh=4)
        self.cpgx3win_L = Label(self, text='产品3操作工：', bg='Lavender')
        self.btn_cpgx3 = tk.Button(self, text='修改产品3操作工。', command=lambda: cpgx3self())
        cpgx3_info = [self.cpgx3_text.get(0.0, 40.0)]

        def cpgx3self():
            info_self = tk.Tk()
            info_self.title('产品3操作工')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx3Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品3操作工{}：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx3Add(self, cpgx3_i, infos):
                line_list = []
                cpgx3cp_L = Label(self, text='产品3操作工{}：'.format(cpgx3_i), bg='Lavender')
                cpgx3cp = Text(self, height=1, width=120, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx3cp.insert(0.0, infos[0])
                line_list.append(cpgx3cp_L)
                line_list.append(cpgx3cp)

                btn_del = Button(info_self, text='删除该操作工', command=lambda: cpgx3Del(cpgx3_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx3Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                cpgx3_info[0] = infos
                self.cpgx3_text.delete(0.0, "end")
                self.cpgx3_text.insert(0.0, infos)
                info_self.destroy()

            infos = cpgx3_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx3Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增操作工信息。',
                                command=lambda: cpgx3Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx3Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx4_text = Text(self, width=120, heigh=4)
        self.cpgx4win_L = Label(self, text='产品4操作工：', bg='Lavender')
        self.btn_cpgx4 = tk.Button(self, text='修改产品4操作工。', command=lambda: cpgx4self())
        cpgx4_info = [self.cpgx4_text.get(0.0, 40.0)]

        def cpgx4self():
            info_self = tk.Tk()
            info_self.title('产品4操作工')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx4Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品4操作工{}：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx4Add(self, cpgx4_i, infos):
                line_list = []
                cpgx4cp_L = Label(self, text='产品4操作工{}：'.format(cpgx4_i), bg='Lavender')
                cpgx4cp = Text(self, height=1, width=120, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx4cp.insert(0.0, infos[0])
                line_list.append(cpgx4cp_L)
                line_list.append(cpgx4cp)

                btn_del = Button(info_self, text='删除该操作工', command=lambda: cpgx4Del(cpgx4_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx4Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                cpgx4_info[0] = infos
                self.cpgx4_text.delete(0.0, "end")
                self.cpgx4_text.insert(0.0, infos)
                info_self.destroy()

            infos = cpgx4_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx4Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增操作工信息。',
                                command=lambda: cpgx4Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx4Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx5_text = Text(self, width=120, heigh=4)
        self.cpgx5win_L = Label(self, text='产品5操作工：', bg='Lavender')
        self.btn_cpgx5 = tk.Button(self, text='修改产品5操作工。', command=lambda: cpgx5self())
        cpgx5_info = [self.cpgx5_text.get(0.0, 40.0)]

        def cpgx5self():
            info_self = tk.Tk()
            info_self.title('产品5操作工')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx5Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品5操作工{}：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx5Add(self, cpgx5_i, infos):
                line_list = []
                cpgx5cp_L = Label(self, text='产品5操作工{}：'.format(cpgx5_i), bg='Lavender')
                cpgx5cp = Text(self, height=1, width=120, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx5cp.insert(0.0, infos[0])
                line_list.append(cpgx5cp_L)
                line_list.append(cpgx5cp)

                btn_del = Button(info_self, text='删除该操作工', command=lambda: cpgx5Del(cpgx5_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx5Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                cpgx5_info[0] = infos
                self.cpgx5_text.delete(0.0, "end")
                self.cpgx5_text.insert(0.0, infos)
                info_self.destroy()

            infos = cpgx5_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx5Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增操作工信息。',
                                command=lambda: cpgx5Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx5Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btncpcz.grid(row=0, column=2)
        btnqtxx.grid(row=0, column=3)
        btngen.grid(row=0, column=4)

        self.cpgx1win_L.grid(row=1, column=0, rowspan=2)
        self.btn_cpgx1.grid(row=3, column=0, rowspan=2)
        self.cpgx1_text.grid(row=1, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx2win_L.grid(row=5, column=0, rowspan=2)
        self.btn_cpgx2.grid(row=7, column=0, rowspan=2)
        self.cpgx2_text.grid(row=5, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx3win_L.grid(row=9, column=0, rowspan=2)
        self.btn_cpgx3.grid(row=11, column=0, rowspan=2)
        self.cpgx3_text.grid(row=9, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx4win_L.grid(row=13, column=0, rowspan=2)
        self.btn_cpgx4.grid(row=15, column=0, rowspan=2)
        self.cpgx4_text.grid(row=13, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx5win_L.grid(row=17, column=0, rowspan=2)
        self.btn_cpgx5.grid(row=19, column=0, rowspan=2)
        self.cpgx5_text.grid(row=17, column=1, rowspan=4, pady=5, columnspan=4)


class cpxxPage_2(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: root.show_frame(cpgxPage_2))
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage_2))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage_2))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage_2))
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        self.cpgx1_text = Text(self, width=120, heigh=4, state=DISABLED)
        self.cpgx1win_L = Label(self, text='产品1信息：', bg='Lavender')
        self.btn_cpgx1 = tk.Button(self, text='修改产品1信息。', command=lambda: cpgx1self())
        self.cpgx1_info = [self.cpgx1_text.get(0.0, 40.0)]

        def cpgx1self():
            info_self = tk.Tk()
            info_self.title('产品1信息')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx1Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品1的{}号产品：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                    elem_list[j][2].config(text='{}号产品型号：'.format(j + 1))
                    elem_list[j][3].delete(0.0, "end")
                    elem_list[j][3].insert(0.0, elem_list[j + 1][3].get(0.0, 2.0).strip())
                    elem_list[j][4].config(text='{}号产品数量：'.format(j + 1))
                    elem_list[j][5].delete(0.0, "end")
                    elem_list[j][5].insert(0.0, elem_list[j + 1][5].get(0.0, 2.0).strip())
                    elem_list[j][6].config(text='{}号产品日期：'.format(j + 1))
                    elem_list[j][7].delete(0.0, "end")
                    elem_list[j][7].insert(0.0, elem_list[j + 1][7].get(0.0, 2.0).strip())
                    elem_list[j][8].config(text='{}号产品客户：'.format(j + 1))
                    elem_list[j][9].delete(0.0, "end")
                    elem_list[j][9].insert(0.0, elem_list[j + 1][9].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx1Add(self, cpgx1_i, infos):
                line_list = []
                cpgx1cp_L = Label(self, text='产品1的{}号产品：'.format(cpgx1_i), bg='Lavender')
                cpgx1cp = Text(self, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[0])
                line_list.append(cpgx1cp_L)
                line_list.append(cpgx1cp)

                cpgx1xh_L = Label(self, text='{}号产品型号：'.format(cpgx1_i), bg='Lavender')
                cpgx1xh = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[1])
                line_list.append(cpgx1xh_L)
                line_list.append(cpgx1xh)

                cpgx1sl_L = Label(self, text='{}号产品数量：'.format(cpgx1_i), bg='Lavender')
                cpgx1sl = Text(self, height=1, width=8, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[2])
                line_list.append(cpgx1sl_L)
                line_list.append(cpgx1sl)

                cpgx1rq_L = Label(self, text='{}号产品日期：'.format(cpgx1_i), bg='Lavender')
                cpgx1rq = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[3])
                line_list.append(cpgx1rq_L)
                line_list.append(cpgx1rq)

                cpgx1kh_L = Label(self, text='{}号产品客户：'.format(cpgx1_i), bg='Lavender')
                cpgx1kh = Text(self, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[2])
                line_list.append(cpgx1kh_L)
                line_list.append(cpgx1kh)

                btn_del = Button(info_self, text='删除该产品', command=lambda: cpgx1Del(cpgx1_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx1Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                self.cpgx1_info[0] = infos
                self.cpgx1_text.config(state=NORMAL)
                self.cpgx1_text.delete(0.0, "end")
                self.cpgx1_text.insert(0.0, infos)
                self.cpgx1_text.config(state=DISABLED)
                info_self.destroy()

            infos = self.cpgx1_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx1Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增产品信息。',
                                command=lambda: cpgx1Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx1Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx2_text = Text(self, width=120, heigh=4)
        self.cpgx2win_L = Label(self, text='产品2信息：', bg='Lavender')
        self.btn_cpgx2 = tk.Button(self, text='修改产品2信息。', command=lambda: cpgx2self())

        def cpgx2self():
            info_self = tk.Tk()
            info_self.title('产品2信息')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx1Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品2的{}号产品：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                    elem_list[j][2].config(text='{}号产品型号：'.format(j + 1))
                    elem_list[j][3].delete(0.0, "end")
                    elem_list[j][3].insert(0.0, elem_list[j + 1][3].get(0.0, 2.0).strip())
                    elem_list[j][4].config(text='{}号产品数量：'.format(j + 1))
                    elem_list[j][5].delete(0.0, "end")
                    elem_list[j][5].insert(0.0, elem_list[j + 1][5].get(0.0, 2.0).strip())
                    elem_list[j][6].config(text='{}号产品日期：'.format(j + 1))
                    elem_list[j][7].delete(0.0, "end")
                    elem_list[j][7].insert(0.0, elem_list[j + 1][7].get(0.0, 2.0).strip())
                    elem_list[j][8].config(text='{}号产品客户：'.format(j + 1))
                    elem_list[j][9].delete(0.0, "end")
                    elem_list[j][9].insert(0.0, elem_list[j + 1][9].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx2Add(self, cpgx1_i, infos):
                line_list = []
                cpgx1cp_L = Label(self, text='产品2的{}号产品：'.format(cpgx1_i), bg='Lavender')
                cpgx1cp = Text(self, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[0])
                line_list.append(cpgx1cp_L)
                line_list.append(cpgx1cp)

                cpgx1xh_L = Label(self, text='{}号产品型号：'.format(cpgx1_i), bg='Lavender')
                cpgx1xh = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[1])
                line_list.append(cpgx1xh_L)
                line_list.append(cpgx1xh)

                cpgx1sl_L = Label(self, text='{}号产品数量：'.format(cpgx1_i), bg='Lavender')
                cpgx1sl = Text(self, height=1, width=8, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[2])
                line_list.append(cpgx1sl_L)
                line_list.append(cpgx1sl)

                cpgx1rq_L = Label(self, text='{}号产品日期：'.format(cpgx1_i), bg='Lavender')
                cpgx1rq = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[3])
                line_list.append(cpgx1rq_L)
                line_list.append(cpgx1rq)

                cpgx1kh_L = Label(self, text='{}号产品客户：'.format(cpgx1_i), bg='Lavender')
                cpgx1kh = Text(self, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[2])
                line_list.append(cpgx1kh_L)
                line_list.append(cpgx1kh)

                btn_del = Button(info_self, text='删除该产品', command=lambda: cpgx1Del(cpgx1_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx2Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                self.cpgx1_info[0] = infos
                self.cpgx1_text.config(state=NORMAL)
                self.cpgx1_text.delete(0.0, "end")
                self.cpgx1_text.insert(0.0, infos)
                self.cpgx1_text.config(state=DISABLED)
                info_self.destroy()

            infos = self.cpgx1_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx2Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增产品信息。',
                                command=lambda: cpgx2Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx2Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx3_text = Text(self, width=120, heigh=4)
        self.cpgx3win_L = Label(self, text='产品3信息：', bg='Lavender')
        self.btn_cpgx3 = tk.Button(self, text='修改产品3信息。', command=lambda: cpgx3self())
        cpgx3_info = [self.cpgx3_text.get(0.0, 40.0)]

        def cpgx3self():
            info_self = tk.Tk()
            info_self.title('产品3信息')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx1Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品3的{}号产品：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                    elem_list[j][2].config(text='{}号产品型号：'.format(j + 1))
                    elem_list[j][3].delete(0.0, "end")
                    elem_list[j][3].insert(0.0, elem_list[j + 1][3].get(0.0, 2.0).strip())
                    elem_list[j][4].config(text='{}号产品数量：'.format(j + 1))
                    elem_list[j][5].delete(0.0, "end")
                    elem_list[j][5].insert(0.0, elem_list[j + 1][5].get(0.0, 2.0).strip())
                    elem_list[j][6].config(text='{}号产品日期：'.format(j + 1))
                    elem_list[j][7].delete(0.0, "end")
                    elem_list[j][7].insert(0.0, elem_list[j + 1][7].get(0.0, 2.0).strip())
                    elem_list[j][8].config(text='{}号产品客户：'.format(j + 1))
                    elem_list[j][9].delete(0.0, "end")
                    elem_list[j][9].insert(0.0, elem_list[j + 1][9].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx1Add(self, cpgx1_i, infos):
                line_list = []
                cpgx1cp_L = Label(self, text='产品3的{}号产品：'.format(cpgx1_i), bg='Lavender')
                cpgx1cp = Text(self, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[0])
                line_list.append(cpgx1cp_L)
                line_list.append(cpgx1cp)

                cpgx1xh_L = Label(self, text='{}号产品型号：'.format(cpgx1_i), bg='Lavender')
                cpgx1xh = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[1])
                line_list.append(cpgx1xh_L)
                line_list.append(cpgx1xh)

                cpgx1sl_L = Label(self, text='{}号产品数量：'.format(cpgx1_i), bg='Lavender')
                cpgx1sl = Text(self, height=1, width=8, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[2])
                line_list.append(cpgx1sl_L)
                line_list.append(cpgx1sl)

                cpgx1rq_L = Label(self, text='{}号产品日期：'.format(cpgx1_i), bg='Lavender')
                cpgx1rq = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[3])
                line_list.append(cpgx1rq_L)
                line_list.append(cpgx1rq)

                cpgx1kh_L = Label(self, text='{}号产品客户：'.format(cpgx1_i), bg='Lavender')
                cpgx1kh = Text(self, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[2])
                line_list.append(cpgx1kh_L)
                line_list.append(cpgx1kh)

                btn_del = Button(info_self, text='删除该产品', command=lambda: cpgx1Del(cpgx1_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx1Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                self.cpgx1_info[0] = infos
                self.cpgx1_text.config(state=NORMAL)
                self.cpgx1_text.delete(0.0, "end")
                self.cpgx1_text.insert(0.0, infos)
                self.cpgx1_text.config(state=DISABLED)
                info_self.destroy()

            infos = self.cpgx1_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx1Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增产品信息。',
                                command=lambda: cpgx1Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx1Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx4_text = Text(self, width=120, heigh=4)
        self.cpgx4win_L = Label(self, text='产品4信息：', bg='Lavender')
        self.btn_cpgx4 = tk.Button(self, text='修改产品4信息。', command=lambda: cpgx4self())
        cpgx4_info = [self.cpgx4_text.get(0.0, 40.0)]

        def cpgx4self():
            info_self = tk.Tk()
            info_self.title('产品4信息')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx1Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品4的{}号产品：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                    elem_list[j][2].config(text='{}号产品型号：'.format(j + 1))
                    elem_list[j][3].delete(0.0, "end")
                    elem_list[j][3].insert(0.0, elem_list[j + 1][3].get(0.0, 2.0).strip())
                    elem_list[j][4].config(text='{}号产品数量：'.format(j + 1))
                    elem_list[j][5].delete(0.0, "end")
                    elem_list[j][5].insert(0.0, elem_list[j + 1][5].get(0.0, 2.0).strip())
                    elem_list[j][6].config(text='{}号产品日期：'.format(j + 1))
                    elem_list[j][7].delete(0.0, "end")
                    elem_list[j][7].insert(0.0, elem_list[j + 1][7].get(0.0, 2.0).strip())
                    elem_list[j][8].config(text='{}号产品客户：'.format(j + 1))
                    elem_list[j][9].delete(0.0, "end")
                    elem_list[j][9].insert(0.0, elem_list[j + 1][9].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx1Add(self, cpgx1_i, infos):
                line_list = []
                cpgx1cp_L = Label(self, text='产品4的{}号产品：'.format(cpgx1_i), bg='Lavender')
                cpgx1cp = Text(self, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[0])
                line_list.append(cpgx1cp_L)
                line_list.append(cpgx1cp)

                cpgx1xh_L = Label(self, text='{}号产品型号：'.format(cpgx1_i), bg='Lavender')
                cpgx1xh = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[1])
                line_list.append(cpgx1xh_L)
                line_list.append(cpgx1xh)

                cpgx1sl_L = Label(self, text='{}号产品数量：'.format(cpgx1_i), bg='Lavender')
                cpgx1sl = Text(self, height=1, width=8, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[2])
                line_list.append(cpgx1sl_L)
                line_list.append(cpgx1sl)

                cpgx1rq_L = Label(self, text='{}号产品日期：'.format(cpgx1_i), bg='Lavender')
                cpgx1rq = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[3])
                line_list.append(cpgx1rq_L)
                line_list.append(cpgx1rq)

                cpgx1kh_L = Label(self, text='{}号产品客户：'.format(cpgx1_i), bg='Lavender')
                cpgx1kh = Text(self, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[2])
                line_list.append(cpgx1kh_L)
                line_list.append(cpgx1kh)

                btn_del = Button(info_self, text='删除该产品', command=lambda: cpgx1Del(cpgx1_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx1Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                self.cpgx1_info[0] = infos
                self.cpgx1_text.config(state=NORMAL)
                self.cpgx1_text.delete(0.0, "end")
                self.cpgx1_text.insert(0.0, infos)
                self.cpgx1_text.config(state=DISABLED)
                info_self.destroy()

            infos = self.cpgx1_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx1Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增产品信息。',
                                command=lambda: cpgx1Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx1Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        self.cpgx5_text = Text(self, width=120, heigh=4)
        self.cpgx5win_L = Label(self, text='产品5信息：', bg='Lavender')
        self.btn_cpgx5 = tk.Button(self, text='修改产品5信息。', command=lambda: cpgx5self())
        cpgx5_info = [self.cpgx5_text.get(0.0, 40.0)]

        def cpgx5self():
            info_self = tk.Tk()
            info_self.title('产品5信息')
            info_self.config(background='Lavender')

            info_self.geometry('1080x600')  # 这里的乘是小x
            elem_list = []

            def rendering():
                for row, lin_list in enumerate(elem_list, start=1):
                    for col, elem in enumerate(lin_list):
                        elem.grid(row=row, column=col)

            def cpgx1Del(i):
                for j in range(i, len(elem_list) - 1):
                    elem_list[j][0].config(text='产品5的{}号产品：'.format(j + 1))
                    elem_list[j][1].delete(0.0, "end")
                    elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                    elem_list[j][2].config(text='{}号产品型号：'.format(j + 1))
                    elem_list[j][3].delete(0.0, "end")
                    elem_list[j][3].insert(0.0, elem_list[j + 1][3].get(0.0, 2.0).strip())
                    elem_list[j][4].config(text='{}号产品数量：'.format(j + 1))
                    elem_list[j][5].delete(0.0, "end")
                    elem_list[j][5].insert(0.0, elem_list[j + 1][5].get(0.0, 2.0).strip())
                    elem_list[j][6].config(text='{}号产品日期：'.format(j + 1))
                    elem_list[j][7].delete(0.0, "end")
                    elem_list[j][7].insert(0.0, elem_list[j + 1][7].get(0.0, 2.0).strip())
                    elem_list[j][8].config(text='{}号产品客户：'.format(j + 1))
                    elem_list[j][9].delete(0.0, "end")
                    elem_list[j][9].insert(0.0, elem_list[j + 1][9].get(0.0, 2.0).strip())
                for j in range(len(elem_list[-1])):
                    elem_list[-1][j].destroy()
                del elem_list[-1]
                rendering()

            def cpgx1Add(self, cpgx1_i, infos):
                line_list = []
                cpgx1cp_L = Label(self, text='产品5的{}号产品：'.format(cpgx1_i), bg='Lavender')
                cpgx1cp = Text(self, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[0])
                line_list.append(cpgx1cp_L)
                line_list.append(cpgx1cp)

                cpgx1xh_L = Label(self, text='{}号产品型号：'.format(cpgx1_i), bg='Lavender')
                cpgx1xh = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[1])
                line_list.append(cpgx1xh_L)
                line_list.append(cpgx1xh)

                cpgx1sl_L = Label(self, text='{}号产品数量：'.format(cpgx1_i), bg='Lavender')
                cpgx1sl = Text(self, height=1, width=8, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[2])
                line_list.append(cpgx1sl_L)
                line_list.append(cpgx1sl)

                cpgx1rq_L = Label(self, text='{}号产品日期：'.format(cpgx1_i), bg='Lavender')
                cpgx1rq = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[3])
                line_list.append(cpgx1rq_L)
                line_list.append(cpgx1rq)

                cpgx1kh_L = Label(self, text='{}号产品客户：'.format(cpgx1_i), bg='Lavender')
                cpgx1kh = Text(self, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
                if infos != []:
                    cpgx1cp.insert(0.0, infos[2])
                line_list.append(cpgx1kh_L)
                line_list.append(cpgx1kh)

                btn_del = Button(info_self, text='删除该产品', command=lambda: cpgx1Del(cpgx1_i - 1))
                line_list.append(btn_del)

                elem_list.append(line_list)

                rendering()

            def cpgx1Done():
                infos = ''
                for row, lin_list in enumerate(elem_list):
                    for col, elem in enumerate(lin_list):
                        if col % 2 == 0:
                            continue
                        infos += elem.get(0.0, 2.0).strip()
                        infos += ','
                    infos = infos[:-1]
                    infos += '\n'
                self.cpgx1_info[0] = infos
                self.cpgx1_text.config(state=NORMAL)
                self.cpgx1_text.delete(0.0, "end")
                self.cpgx1_text.insert(0.0, infos)
                self.cpgx1_text.config(state=DISABLED)
                info_self.destroy()

            infos = self.cpgx1_info[0].split('\n')
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cpgx1Add(info_self, i, info.split(','))

            btn_gen = tk.Button(info_self, text='新增产品信息。',
                                command=lambda: cpgx1Add(info_self, len(elem_list) + 1, []))
            btn_done = tk.Button(info_self, text='信息确认完成。', command=lambda: cpgx1Done())

            btn_gen.grid(row=0, column=0, columnspan=1)
            btn_done.grid(row=0, column=2, columnspan=1)

            info_self.mainloop()

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btncpcz.grid(row=0, column=2)
        btnqtxx.grid(row=0, column=3)
        btngen.grid(row=0, column=4)

        self.cpgx1win_L.grid(row=1, column=0, rowspan=2)
        self.btn_cpgx1.grid(row=3, column=0, rowspan=2)
        self.cpgx1_text.grid(row=1, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx2win_L.grid(row=5, column=0, rowspan=2)
        self.btn_cpgx2.grid(row=7, column=0, rowspan=2)
        self.cpgx2_text.grid(row=5, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx3win_L.grid(row=9, column=0, rowspan=2)
        self.btn_cpgx3.grid(row=11, column=0, rowspan=2)
        self.cpgx3_text.grid(row=9, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx4win_L.grid(row=13, column=0, rowspan=2)
        self.btn_cpgx4.grid(row=15, column=0, rowspan=2)
        self.cpgx4_text.grid(row=13, column=1, rowspan=4, pady=5, columnspan=4)

        self.cpgx5win_L.grid(row=17, column=0, rowspan=2)
        self.btn_cpgx5.grid(row=19, column=0, rowspan=2)
        self.cpgx5_text.grid(row=17, column=1, rowspan=4, pady=5, columnspan=4)


class qtxxPage_2(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: root.show_frame(cpgxPage_2))
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage_2))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage_2))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage_2))
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        jyy1_L = Label(self, text='检验员1：', bg='Lavender')
        self.jyy1 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        scbry1_L = Label(self, text='生产部人员1：', bg='Lavender')
        self.scbry1 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        scbry2_L = Label(self, text='生产部人员2：', bg='Lavender')
        self.scbry2 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        scbry3_L = Label(self, text='生产部人员3：', bg='Lavender')
        self.scbry3 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        self.tsgcjbV = tk.IntVar(master=self)

        def tsgcjbbool():
            if self.tsgcjbV.get() == 0:
                self.tsgcjb.config(state=DISABLED)
            else:
                self.tsgcjb.config(state=NORMAL)

        tsgcjbC1 = tk.Radiobutton(self, text="有搅拌过程", variable=self.tsgcjbV, value=1, command=tsgcjbbool,
                                  bg='Lavender')
        tsgcjbC2 = tk.Radiobutton(self, text="无搅拌过程", variable=self.tsgcjbV, value=0, command=tsgcjbbool,
                                  bg='Lavender')
        tsgcjb_L = Label(self, text='特殊过程搅拌搅拌工：', bg='Lavender')
        self.tsgcjb = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgcjbbool()

        self.tsgcbmjshV = tk.IntVar(master=self)

        def tsgcbmjshbool():
            if self.tsgcbmjshV.get() == 0:
                self.tsgcbmjsh.config(state=DISABLED)
            else:
                self.tsgcbmjsh.config(state=NORMAL)

        tsgcbmjshC1 = tk.Radiobutton(self, text="有薄膜金属化过程", variable=self.tsgcbmjshV, value=1,
                                     command=tsgcbmjshbool,
                                     bg='Lavender')
        tsgcbmjshC2 = tk.Radiobutton(self, text="无薄膜金属化过程", variable=self.tsgcbmjshV, value=0,
                                     command=tsgcbmjshbool,
                                     bg='Lavender')
        tsgcbmjsh_L = Label(self, text='特殊过程薄膜金属化操作工：', bg='Lavender')
        self.tsgcbmjsh = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgcbmjshbool()

        self.tsgchjV = tk.IntVar(master=self)

        def tsgchjbool():
            if self.tsgchjV.get() == 0:
                self.tsgchj.config(state=DISABLED)
            else:
                self.tsgchj.config(state=NORMAL)

        tsgchjC1 = tk.Radiobutton(self, text="有焊接过程", variable=self.tsgchjV, value=1, command=tsgchjbool,
                                  bg='Lavender')
        tsgchjC2 = tk.Radiobutton(self, text="无焊接过程", variable=self.tsgchjV, value=0, command=tsgchjbool,
                                  bg='Lavender')
        tsgchj_L = Label(self, text='特殊过程焊接操作工：', bg='Lavender')
        self.tsgchj = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgchjbool()

        self.tsgchhV = tk.IntVar(master=self)

        def tsgchhbool():
            if self.tsgchhV.get() == 0:
                self.tsgchh.config(state=DISABLED)
            else:
                self.tsgchh.config(state=NORMAL)

        tsgchhC1 = tk.Radiobutton(self, text="有混合过程", variable=self.tsgchhV, value=1, command=tsgchhbool,
                                  bg='Lavender')
        tsgchhC2 = tk.Radiobutton(self, text="无混合过程", variable=self.tsgchhV, value=0, command=tsgchhbool,
                                  bg='Lavender')
        tsgchh_L = Label(self, text='特殊过程混合操作工：', bg='Lavender')
        self.tsgchh = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgchhbool()

        self.tsgcjcV = tk.IntVar(master=self)

        def tsgcjcbool():
            if self.tsgcjcV.get() == 0:
                self.tsgcjc.config(state=DISABLED)
            else:
                self.tsgcjc.config(state=NORMAL)

        tsgcjcC1 = tk.Radiobutton(self, text="有挤出过程", variable=self.tsgcjcV, value=1, command=tsgcjcbool,
                                  bg='Lavender')
        tsgcjcC2 = tk.Radiobutton(self, text="无挤出过程", variable=self.tsgcjcV, value=0, command=tsgcjcbool,
                                  bg='Lavender')
        tsgcjc_L = Label(self, text='特殊过程挤出操作工：', bg='Lavender')
        self.tsgcjc = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgcjcbool()

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

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btncpcz.grid(row=0, column=2)
        btnqtxx.grid(row=0, column=3)
        btngen.grid(row=0, column=4)

        jyy1_L.grid(row=1, column=0)
        self.jyy1.grid(row=1, column=1)

        scbry1_L.grid(row=2, column=0)
        self.scbry1.grid(row=2, column=1)
        scbry2_L.grid(row=2, column=2)
        self.scbry2.grid(row=2, column=3)
        scbry3_L.grid(row=2, column=4)
        self.scbry3.grid(row=2, column=5)

        tsgcjbC1.grid(row=3, column=0)
        tsgcjbC2.grid(row=3, column=1)
        tsgcjb_L.grid(row=3, column=2)
        self.tsgcjb.grid(row=3, column=3, columnspan=4)

        tsgcbmjshC1.grid(row=4, column=0)
        tsgcbmjshC2.grid(row=4, column=1)
        tsgcbmjsh_L.grid(row=4, column=2)
        self.tsgcbmjsh.grid(row=4, column=3, columnspan=4)

        tsgchjC1.grid(row=5, column=0)
        tsgchjC2.grid(row=5, column=1)
        tsgchj_L.grid(row=5, column=2)
        self.tsgchj.grid(row=5, column=3, columnspan=4)

        tsgchhC1.grid(row=6, column=0)
        tsgchhC2.grid(row=6, column=1)
        tsgchh_L.grid(row=6, column=2)
        self.tsgchh.grid(row=6, column=3, columnspan=4)

        tsgcjcC1.grid(row=7, column=0)
        tsgcjcC2.grid(row=7, column=1)
        tsgcjc_L.grid(row=7, column=2)
        self.tsgcjc.grid(row=7, column=3, columnspan=4)

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
