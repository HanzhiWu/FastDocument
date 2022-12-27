from re import template
import tkinter as tk
from tkinter import *
from tkinter import ttk
from unicodedata import decimal

from second_window import InfoWindow_1, InfoWindow_2, InfoWindow_3, InfoWindow_4
from tkinter.filedialog import askopenfilename
from temp_storage import read_file_to_temp_list, clear_temp_storage, add_item_temp_storage


# 第一层界面
def mainWindow():
    window = tk.Tk()
    print(window.tk.exprstring('$tcl_library'))
    print(window.tk.exprstring('$tk_library'))
    range2code = {
        '通用生产': 'SC',
        '通用生产和销售': 'SCXS',
        '组装生产（无三废）': 'ZZ',
        '组装生产（无三废）和销售': 'ZZXS',
        '家具生产': 'JJSC',
        '通用销售': 'XS',
        '软件': 'RJ',
        '施工': 'SG',
        '通用服务': 'FW',
        '物流服务': 'WL',
        '检测服务': 'JC',
        '家具生产和销售': 'JJSCXS',
        '通用服务和销售': 'FWXS',
        '物流服务和销售': 'WLXS',
        '检测服务和销售': 'JCXS',
        '预拌混凝土绿建': 'YBHNTLJ',
        '砌体材料绿建': 'QTCLLJ',
        '预制砂浆绿建': 'YZSJLJ',
        '预制构件绿建': 'YZGJLJ',
        '保温系统材料绿建': 'BWXTCLLJ'
    }
    # 给窗口的可视化起名字
    window.title('认证文件管理系统')

    # 设定窗口的大小(长 * 宽)
    window.geometry('600x400')  # 这里的乘是小x
    window.resizable(0, 0)

    """第一个界面，模板选择"""
    """认证范围选择"""
    domain_L = Label(window, text='认证范围：')
    domain = ttk.Combobox(window)
    domain['value'] = (
        '通用生产', '通用生产和销售', '组装生产（无三废）', '组装生产（无三废）和销售', '家具生产', '通用销售', '软件',
        '施工',
        '通用服务', '物流服务', '检测服务', '家具生产和销售', '通用服务和销售', '物流服务和销售', '检测服务和销售',
        '预拌混凝土绿建', '砌体材料绿建', '预制砂浆绿建', '预制构件绿建', '保温系统材料绿建')
    domain.current(0)

    # 下拉框颜色
    combostyle = ttk.Style()
    combostyle.theme_create('combostyle', parent='alt',
                            settings={'TCombobox':
                                {'configure':
                                    {
                                        'foreground': 'blue',  # 前景色
                                        'selectbackground': 'black',  # 选择后的背景颜色
                                        'fieldbackground': 'white',  # 下拉框颜色
                                        'background': 'red',  # 下拉按钮颜色
                                    }}}
                            )
    combostyle.theme_use('combostyle')

    domain['state'] = 'readonly'

    """涉及部门选择"""
    depart_L = Label(window, text='涉及部门')

    departselected = []
    departV1 = tk.IntVar(master=window)
    departV2 = tk.IntVar(master=window)
    departV3 = tk.IntVar(master=window)
    departV4 = tk.IntVar(master=window)
    departV5 = tk.IntVar(master=window)
    departV6 = tk.IntVar(master=window)
    departV7 = tk.IntVar(master=window)
    departV8 = tk.IntVar(master=window)
    departV9 = tk.IntVar(master=window)

    def depart_select():
        global departselected
        departselected = []
        if departV1.get() == 1:
            departselected.append(1)
        if departV2.get() == 1:
            departselected.append(2)
        if departV3.get() == 1:
            departselected.append(3)
        if departV4.get() == 1:
            departselected.append(4)
        if departV5.get() == 1:
            departselected.append(5)
        if departV6.get() == 1:
            departselected.append(6)
        if departV7.get() == 1:
            departselected.append(7)
        if departV8.get() == 1:
            departselected.append(8)
        if departV9.get() == 1:
            departselected.append(9)

    departC1 = tk.Checkbutton(window, text='行政部门', variable=departV1, onvalue=1, offvalue=0, command=depart_select)
    departC2 = tk.Checkbutton(window, text='采购部门', variable=departV2, onvalue=1, offvalue=0, command=depart_select)
    departC3 = tk.Checkbutton(window, text='生产部门', variable=departV3, onvalue=1, offvalue=0, command=depart_select)
    departC4 = tk.Checkbutton(window, text='质检部门', variable=departV4, onvalue=1, offvalue=0, command=depart_select)
    departC5 = tk.Checkbutton(window, text='销售部门', variable=departV5, onvalue=1, offvalue=0, command=depart_select)
    departC6 = tk.Checkbutton(window, text='财务部门', variable=departV6, onvalue=1, offvalue=0, command=depart_select)
    departC7 = tk.Checkbutton(window, text='技术部门', variable=departV7, onvalue=1, offvalue=0, command=depart_select)
    departC8 = tk.Checkbutton(window, text='销售采购部门', variable=departV8, onvalue=1, offvalue=0,
                              command=depart_select)
    departC9 = tk.Checkbutton(window, text='行政采购部门', variable=departV9, onvalue=1, offvalue=0,
                              command=depart_select)
    departlist = [departC1, departC2, departC3, departC4, departC5, departC6, departC7, departC8, departC9]

    '''认证项目选择'''
    project_L = Label(window, text='认证项目')

    projectselected = []
    projectV1 = tk.IntVar(master=window)
    projectV2 = tk.IntVar(master=window)
    projectV3 = tk.IntVar(master=window)
    projectV4 = tk.IntVar(master=window)

    def project_select():
        global projectselected
        projectselected = []
        if projectV1.get() == 1:
            projectselected.append('Q')
        if projectV2.get() == 1:
            projectselected.append('E')
        if projectV3.get() == 1:
            projectselected.append('S')
        if projectV4.get() == 1:
            projectselected.append('L')

    projectC1 = tk.Checkbutton(window, text='质量管理体系', variable=projectV1, onvalue=1, offvalue=0,
                               command=project_select)
    projectC2 = tk.Checkbutton(window, text='环境管理体系', variable=projectV2, onvalue=1, offvalue=0,
                               command=project_select)
    projectC3 = tk.Checkbutton(window, text='职业健康安全管理体系', variable=projectV3, onvalue=1, offvalue=0,
                               command=project_select)
    projectC4 = tk.Checkbutton(window, text='绿色建材产品认证', variable=projectV4, onvalue=1, offvalue=0,
                               command=project_select)
    projdict = {
        'Q': projectC1,
        'E': projectC2,
        'S': projectC3,
        'L': projectC4
    }
    '''设计开发选择'''
    design_L = Label(window, text='设计开发')

    designV = tk.IntVar(master=window)

    def design_select():
        pass

    designC1 = tk.Radiobutton(window, text="有", variable=designV, value=1, command=design_select)
    designC2 = tk.Radiobutton(window, text="无", variable=designV, value=0, command=design_select)

    def pageJump(re=False):
        info_dic = {}
        if re:
            file = askopenfilename(title='Please choose a file',
                                   initialdir='save/', filetypes=[('纯文本', '*.txt')])
            temp = read_file_to_temp_list(file)
            info_dic['tmp'] = file
            template_id = temp['template_id']
            s1, s2, s3, s4 = template_id.split('-')
            all_unset()
            for key, val in range2code.items():
                if val == s1:
                    domain.current(domain['value'].index(key))
            for i in s2:
                departlist[int(i) - 1].select()
            depart_select()
            for i in s3:
                projdict[i].select()
            project_select()
            if s4 == 'Y':
                designC1.select()
            else:
                designC2.select()

        global projectselected, departselected
        template_id = ''  # 模板代码
        template_id += range2code[domain.get()]
        template_id += '-'
        sort_depart_selected = sorted(departselected)
        template_id += ''.join(str(i) for i in sort_depart_selected)
        template_id += '-'
        if 'Q' in projectselected:
            template_id += 'Q'
        if 'E' in projectselected:
            template_id += 'E'
        if 'S' in projectselected:
            template_id += 'S'
        if 'L' in projectselected:
            template_id += 'L'
        template_id += '-'
        template_id += 'Y' if designV.get() == 1 else 'N'
        print(template_id)
        info_dic['template_id'] = template_id  # yml中原本没有，用来选择模板，且用于生成输出路径名，所以后续会写入替换字典中
        add_item_temp_storage('template_id', template_id)
        # Q界面
        if 'Q' in projectselected and len(projectselected) == 1:
            InfoWindow_1(info_dic, re=re)
            return
            # E/QE 界面
        if 'E' in projectselected and len(projectselected) == 1 or 'S' not in projectselected and len(
                projectselected) == 2:
            InfoWindow_2(info_dic, re=re)
            return
        # S/QS/ES/QES界面
        if 'S' in projectselected and len(projectselected) == 1 or 'E' not in projectselected and len(
                projectselected) == 2 \
                or 'Q' not in projectselected and len(projectselected) == 2 or len(projectselected) == 3:
            InfoWindow_3(info_dic, re=re)
            return
        # L界面
        if 'L' in projectselected and len(projectselected) == 1:
            InfoWindow_4(info_dic, re=re)
            return

    def all_unset():
        for d in departlist:
            d.deselect()
            depart_select()
        for d in projdict.values():
            d.deselect()
            project_select()

    def load_file():
        file = askopenfilename(title='Please choose a file',
                               initialdir='save/', filetypes=[('纯文本', '*.txt')])
        temp = read_file_to_temp_list(file)
        template_id = temp['template_id']
        s1, s2, s3, s4 = template_id.split('-')
        all_unset()
        for key, val in range2code.items():
            if val == s1:
                domain.current(domain['value'].index(key))
        for i in s2:
            departlist[int(i) - 1].select()
        depart_select()
        for i in s3:
            projdict[i].select()
        project_select()
        if s4 == 'Y':
            designC1.select()
        else:
            designC2.select()

    '''跳转按钮'''
    btn_login = tk.Button(window, text='初审模式。', command=lambda: [pageJump()])
    btn_re = tk.Button(window, text='监督复评模式。', command=lambda: [pageJump(True)])
    btn_load = tk.Button(window, text='加载历史数据。', command=load_file)
    btn_clear = tk.Button(window, text='清除历史数据。', command=lambda: [clear_temp_storage(), all_unset()])

    '''place布局'''
    domain_L.place(relx=0.22, rely=0.05)
    domain.place(relx=0.36, rely=0.05)

    departC1.place(relx=0.15, rely=0.20)
    departC2.place(relx=0.4, rely=0.20)
    departC3.place(relx=0.65, rely=0.20)
    departC4.place(relx=0.15, rely=0.27)
    departC5.place(relx=0.4, rely=0.27)
    departC6.place(relx=0.65, rely=0.27)
    departC7.place(relx=0.15, rely=0.34)
    departC8.place(relx=0.4, rely=0.34)
    departC9.place(relx=0.65, rely=0.34)

    Label(window, text=str('~-' * 40)).place(relx=0.03, rely=0.395)  # 分隔符

    project_L.place(relx=0.42, rely=0.45)
    projectC1.place(relx=0.09, rely=0.52)
    projectC2.place(relx=0.33, rely=0.52)
    projectC3.place(relx=0.57, rely=0.52)
    projectC4.place(relx=0.33, rely=0.60)

    Label(window, text=str('~-' * 40)).place(relx=0.03, rely=0.655)  # 分隔符

    design_L.place(relx=0.42, rely=0.73)
    designC1.place(relx=0.35, rely=0.82)
    designC2.place(relx=0.5, rely=0.82)

    btn_login.place(relx=0.05, rely=0.9)
    btn_re.place(relx=0.25, rely=0.9)
    btn_load.place(relx=0.5, rely=0.9)
    btn_clear.place(relx=0.75, rely=0.9)

    window.mainloop()


mainWindow()
