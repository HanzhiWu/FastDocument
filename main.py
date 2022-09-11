from asyncore import close_all
from cmath import cos
from lib2to3.pgen2.token import RPAR
from operator import le
from re import template
from socket import inet_aton
from statistics import pvariance
from textwrap import indent
import tkinter.messagebox
import pickle
from tkinter import Label
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import bgcolor
from xml import dom

import os
# import yaml
# from docx import Document
import random

import yaml

'''
def GetDictionary(yamlFile):
    """
    从yamlFile中读取替换字典
    """
    with open(yamlFile, 'r', encoding='utf8') as y:
        return yaml.safe_load(y.read())


def ReplaceInRuns(paragraph, replaceDict: dict, paragraphType):
    """
    将paragraph中所有runs根据replaceDict进行替换
    """
    text = ""
    if paragraphType == "plain" or "header":
        for run in paragraph.runs:
            if text == "":
                if run.text.count("__") % 2 != 0:  # 发生了截断
                    text = run.text
                    run.text = ""
                    continue
            else:
                run.text = text + run.text
                if run.text.count("__") % 2 != 0:  # 发生了截断
                    text = run.text
                    run.text = ""
                    continue
            text = ""
            for old, new in replaceDict.items():
                # 进行替换
                if old in run.text:
                    if "随机日期" in old:
                        start, end = new.split('-')
                        new = str(random.randint(int(start), int(end)))
                    run.text = run.text.replace(old, new)
    else:
        if paragraphType == "table":
            for run in paragraph.runs:
                text += run.text.strip()
            for old, new in replaceDict.items():
                # 进行替换
                if old in text:
                    if "随机日期" in old:
                        start, end = new.split('-')
                        new = str(random.randint(int(start), int(end)))
                    text = text.replace(old, new)
            if text != "":
                paragraph.runs[0].text = text
            for run in paragraph.runs[1:]:
                run.text = ""


def ReplaceIn(docxFile, workdir, replaceDict: dict):
    """
    将docxFile按replaceDict进行全局替换
    """
    if docxFile[-4:] == '.doc':
        print('无法加载doc文件： ', docxFile, '\n请转换成docx类型！')
        return

    # document = Document(docxFile)

    # 页眉
    for section in document.sections:
        for paragraph in section.header.paragraphs:
            ReplaceInRuns(paragraph, replaceDict, "header")

    # 文本段落
    for paragraph in document.paragraphs:
        ReplaceInRuns(paragraph, replaceDict, "plain")

    # 表格
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    ReplaceInRuns(paragraph, replaceDict, "table")

    res_path = os.path.join(workdir, 'result/', os.path.relpath(docxFile, workdir))
    res_dir = os.path.dirname(res_path)
    if not os.path.exists(res_dir):
        os.makedirs(res_dir)
    document.save(res_path)


def ReplaceAll(path: str, workdir: str, replaceDict: dict):
    """
    将path路径下所有word文件按replaceDict进行全局替换
    """
    directories = os.listdir(path)
    folders = [os.path.join(path, i) for i in directories if
               os.path.isdir(os.path.join(path, i)) and not i.startswith('.')]  # 所有非隐藏文件夹
    for folder in folders:
        ReplaceAll(os.path.join(path, folder), workdir, replaceDict)
    files = [os.path.join(path, i) for i in directories if
             os.path.isfile(os.path.join(path, i)) and os.path.splitext(i)[-1] in ['.doc', '.docx']]  # 所有word文件
    for file in files:
        print(file)
        ReplaceIn(file, workdir, replaceDict)
'''


# 第一层界面
def mainWindow():
    window = tk.Tk()

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
        '检测服务': 'JC'
    }
    # 给窗口的可视化起名字
    window.title('认证文件管理系统')

    # 设定窗口的大小(长 * 宽)
    window.geometry('500x300')  # 这里的乘是小x
    window.resizable(0, 0)

    """第一个界面，模板选择"""
    """认证范围选择"""
    domain_L = Label(window, text='认证范围：')
    domain = ttk.Combobox(window)
    domain['value'] = (
        '通用生产', '通用生产和销售', '组装生产（无三废）', '组装生产（无三废）和销售', '家具生产', '通用销售', '软件',
        '施工',
        '通用服务', '物流服务', '检测服务')
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
    l = tk.Label(window, bg='yellow', text='empty')

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
        l.config(text=str(departselected))

    departC1 = tk.Checkbutton(window, text='行政部门', variable=departV1, onvalue=1, offvalue=0, command=depart_select)
    departC2 = tk.Checkbutton(window, text='采购部门', variable=departV2, onvalue=1, offvalue=0, command=depart_select)
    departC3 = tk.Checkbutton(window, text='生产部门', variable=departV3, onvalue=1, offvalue=0, command=depart_select)
    departC4 = tk.Checkbutton(window, text='质检部门', variable=departV4, onvalue=1, offvalue=0, command=depart_select)
    departC5 = tk.Checkbutton(window, text='销售部门', variable=departV5, onvalue=1, offvalue=0, command=depart_select)
    departC6 = tk.Checkbutton(window, text='财务部门', variable=departV6, onvalue=1, offvalue=0, command=depart_select)

    '''认证项目选择'''
    project_L = Label(window, text='认证项目')

    projectselected = []
    projectV1 = tk.IntVar(master=window)
    projectV2 = tk.IntVar(master=window)
    projectV3 = tk.IntVar(master=window)

    def project_select():
        global projectselected
        projectselected = []
        if projectV1.get() == 1:
            projectselected.append('Q')
        if projectV2.get() == 1:
            projectselected.append('E')
        if projectV3.get() == 1:
            projectselected.append('S')

    projectC1 = tk.Checkbutton(window, text='质量管理体系', variable=projectV1, onvalue=1, offvalue=0,
                               command=project_select)
    projectC2 = tk.Checkbutton(window, text='环境管理体系', variable=projectV2, onvalue=1, offvalue=0,
                               command=project_select)
    projectC3 = tk.Checkbutton(window, text='职业健康安全管理体系', variable=projectV3, onvalue=1, offvalue=0,
                               command=project_select)

    '''设计开发选择'''
    design_L = Label(window, text='设计开发')

    designV = tk.IntVar(master=window)

    def design_select():
        l.config(text=str(designV.get()))

    designC1 = tk.Radiobutton(window, text="有", variable=designV, value=1, command=design_select)
    designC2 = tk.Radiobutton(window, text="无", variable=designV, value=0, command=design_select)

    def pageJump():
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
        template_id += '-'
        template_id += 'Y' if designV.get() == 1 else 'N'
        print(template_id)
        info_dic = {}
        info_dic['template_id'] = template_id
        # Q界面
        if 'Q' in projectselected and len(projectselected) == 1:
            InforWindow_1(info_dic)
            return
            # E/QE 界面
        if 'E' in projectselected and len(projectselected) == 1 or 'S' not in projectselected and len(
                projectselected) == 2:
            InforWindow_2(info_dic)
            return
        # S/QS/ES/QES界面
        if 'S' in projectselected and len(projectselected) == 1 or 'E' not in projectselected and len(
                projectselected) == 2 \
                or 'Q' not in projectselected and len(projectselected) == 2 or len(projectselected) == 3:
            InforWindow_3(info_dic)
            return

    '''跳转按钮'''
    btn_login = tk.Button(window, text='确认信息无误，进入信息采集阶段。', command=lambda: [pageJump()])

    '''place布局'''
    domain_L.place(relx=0.22, rely=0.05)
    domain.place(relx=0.36, rely=0.05)

    Label(window, text=str('~-' * 30)).place(relx=0.05, rely=0.125)  # 分隔符

    depart_L.place(relx=0.42, rely=0.20)
    departC1.place(relx=0.15, rely=0.27)
    departC2.place(relx=0.4, rely=0.27)
    departC3.place(relx=0.65, rely=0.27)
    departC4.place(relx=0.15, rely=0.34)
    departC5.place(relx=0.4, rely=0.34)
    departC6.place(relx=0.65, rely=0.34)

    Label(window, text=str('~-' * 30)).place(relx=0.05, rely=0.415)  # 分隔符

    project_L.place(relx=0.42, rely=0.49)
    projectC1.place(relx=0.09, rely=0.58)
    projectC2.place(relx=0.33, rely=0.58)
    projectC3.place(relx=0.57, rely=0.58)

    Label(window, text=str('~-' * 30)).place(relx=0.05, rely=0.655)  # 分隔符

    design_L.place(relx=0.42, rely=0.73)
    designC1.place(relx=0.35, rely=0.82)
    designC2.place(relx=0.5, rely=0.82)

    btn_login.place(relx=0.30, rely=0.9)

    window.mainloop()


# 第二层界面
def InforWindow_1(info_dic):
    '''Q界面'''
    window = tk.Tk()

    # 给窗口的可视化起名字
    window.title('认证文件管理系统')
    window.config(background='Lavender')

    # 设定窗口的大小(长 * 宽)
    window.geometry('770x550')  # 这里的乘是小x
    window.resizable(0, 0)

    name_L = Label(window, text='企业名称：', bg='Lavender')
    name = Text(window, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

    code_L = Label(window, text='企业代码：', bg='Lavender')
    code = Text(window, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

    ver_L = Label(window, text='版本：', bg='Lavender')
    ver = Text(window, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
    ver.insert('0.0', 'A')

    times_L = Label(window, text='版次：', bg='Lavender')
    times = Text(window, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
    times.insert('0.0', '0')

    m_L = Label(window, text='管理者代表：', bg='Lavender')
    m = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    mx_L = Label(window, text='最高管理者：', bg='Lavender')
    mx = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    t_L = Label(window, text='手册发布实施日期：', bg='Lavender')
    t = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    jianjie_L = Label(window, text='公司简介：', bg='Lavender')
    jianjie = Text(window, height=2, width=97, relief=RAISED, highlightcolor='black', highlightthickness=1)

    fanwei_L = Label(window, text='认证范围：', bg='Lavender')
    fanwei = Text(window, height=1, width=97, relief=RAISED, highlightcolor='black', highlightthickness=1)

    waibaoV = tk.IntVar()

    def waibaobool():
        if waibaoV.get() == 0:
            wbguocheng.config(state=DISABLED)
        else:
            wbguocheng.config(state=NORMAL)

    waibaoC1 = tk.Radiobutton(window, text="公司有外包过程", variable=waibaoV, value=1, command=waibaobool,
                              bg='Lavender')
    waibaoC2 = tk.Radiobutton(window, text="公司无外包过程", variable=waibaoV, value=0, command=waibaobool,
                              bg='Lavender')
    wbguocheng_L = Label(window, text='外包过程表述：', bg='Lavender')
    wbguocheng = Text(window, height=2, width=74, relief=RAISED, highlightcolor='black', highlightthickness=1)
    wbguocheng.insert('0.0', '本公司外包过程为XX')

    tsguocheng_L = Label(window, text='特殊过程：', bg='Lavender')
    tsguocheng = Text(window, height=2, width=97, relief=RAISED, highlightcolor='black', highlightthickness=1)
    tsguocheng.insert('0.0', '无特殊过程/特殊过程为XX')

    zhijian_L = Label(window, text='质检部门：', bg='Lavender')
    zhijian = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    zjfuze_L = Label(window, text='质检负责人：', bg='Lavender')
    zjfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    zjbmcode_L = Label(window, text='质检部门代码：', bg='Lavender')
    zjbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xiaoshou_L = Label(window, text='销售部门：', bg='Lavender')
    xiaoshou = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xsfuze_L = Label(window, text='销售负责人：', bg='Lavender')
    xsfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xsbmcode_L = Label(window, text='销售部门代码：', bg='Lavender')
    xsbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    shengchan_L = Label(window, text='生产部门：', bg='Lavender')
    shengchan = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    scfuze_L = Label(window, text='生产负责人：', bg='Lavender')
    scfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    scbmcode_L = Label(window, text='生产部门代码：', bg='Lavender')
    scbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xingzheng_L = Label(window, text='行政部门：', bg='Lavender')
    xingzheng = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xzfuze_L = Label(window, text='行政负责人：', bg='Lavender')
    xzfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xzbmcode_L = Label(window, text='行政部门代码：', bg='Lavender')
    xzbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    caigou_L = Label(window, text='采购部门：', bg='Lavender')
    caigou = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    cgfuze_L = Label(window, text='采购负责人：', bg='Lavender')
    cgfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    cgbmcode_L = Label(window, text='采购部门代码：', bg='Lavender')
    cgbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    shangchanliuchng1_L = Label(window, text='生产工艺流程1：', bg='Lavender')
    shengchanliucheng1 = Text(window, height=1, width=91, relief=RAISED, highlightcolor='black', highlightthickness=1)
    shengchanliucheng1.insert('0.0', '若无该流程则跳过该项')

    shangchanliuchng2_L = Label(window, text='生产工艺流程2：', bg='Lavender')
    shengchanliucheng2 = Text(window, height=1, width=91, relief=RAISED, highlightcolor='black', highlightthickness=1)
    shengchanliucheng2.insert('0.0', '若无该流程则跳过该项')

    shangchanliuchng3_L = Label(window, text='生产工艺流程3：', bg='Lavender')
    shengchanliucheng3 = Text(window, height=1, width=91, relief=RAISED, highlightcolor='black', highlightthickness=1)
    shengchanliucheng3.insert('0.0', '若无该流程则跳过该项')

    def textGen():
        info_dic['__企业名称__'] = name.get(0.0, 20.0).strip()
        info_dic['__企业代码__'] = code.get(0.0, 20.0).strip()
        info_dic['__版本__'] = ver.get(0.0, 20.0).strip()
        info_dic['__版次__'] = '\'' + times.get(0.0, 20.0).strip() + '\''
        info_dic['__管理者代表__'] = m.get(0.0, 20.0).strip()
        info_dic['__最高管理者__'] = mx.get(0.0, 20.0).strip()
        info_dic['__手册发布实施日期__'] = t.get(0.0, 20.0).strip()
        info_dic['__公司简介__'] = jianjie.get(0.0, 20.0).strip()
        info_dic['__认证范围__'] = fanwei.get(0.0, 20.0).strip()
        if waibaoV.get() == 1:
            info_dic['__有无外包过程__'] = '有'
            info_dic['__外包过程表述__'] = wbguocheng.get(0.0, 20.0).strip()
        else:
            info_dic['__有无外包过程__'] = '无'
            info_dic['__外包过程表述__'] = ''
        info_dic['__特殊过程__'] = tsguocheng.get(0.0, 20.0).strip()
        info_dic['__质检部门__'] = zhijian.get(0.0, 20.0).strip()
        info_dic['__质检负责人__'] = zjfuze.get(0.0, 20.0).strip()
        info_dic['__质检部门代码__'] = zjbmcode.get(0.0, 20.0).strip()
        info_dic['__销售部门__'] = xiaoshou.get(0.0, 20.0).strip()
        info_dic['__销售负责人__'] = xsfuze.get(0.0, 20.0).strip()
        info_dic['__销售部门代码__'] = xsbmcode.get(0.0, 20.0).strip()
        info_dic['__生产部门__'] = shengchan.get(0.0, 20.0).strip()
        info_dic['__生产负责人__'] = scfuze.get(0.0, 20.0).strip()
        info_dic['__生产部门代码__'] = scbmcode.get(0.0, 20.0).strip()
        info_dic['__行政部门__'] = xingzheng.get(0.0, 20.0).strip()
        info_dic['__行政负责人__'] = xzfuze.get(0.0, 20.0).strip()
        info_dic['__行政部门代码__'] = xzbmcode.get(0.0, 20.0).strip()
        info_dic['__采购部门__'] = caigou.get(0.0, 20.0).strip()
        info_dic['__采购负责人__'] = cgfuze.get(0.0, 20.0).strip()
        info_dic['__采购部门代码__'] = cgbmcode.get(0.0, 20.0).strip()
        info_dic['__生产工艺流程1__'] = shengchanliucheng1.get(0.0, 20.0).strip()
        info_dic['__生产工艺流程2__'] = shengchanliucheng2.get(0.0, 20.0).strip()
        info_dic['__生产工艺流程3__'] = shengchanliucheng3.get(0.0, 20.0).strip()
        print(info_dic)
        window.destroy()
        informCollectWindow(info_dic)

    btn_gen = tk.Button(window, text='确认信息无误，进入下一采集阶段。', command=lambda: [textGen()])

    '''place布局'''
    name_L.place(x=5, y=5)  # 14 / token
    name.place(x=75, y=7)  # 5.6 / 1

    code_L.place(x=245, y=5)
    code.place(x=315, y=7)

    ver_L.place(x=485, y=5)
    ver.place(x=530, y=7)

    times_L.place(x=625, y=5)
    times.place(x=670, y=7)

    m_L.place(x=5, y=35)
    m.place(x=90, y=37)

    mx_L.place(x=245, y=35)
    mx.place(x=330, y=37)

    t_L.place(x=475, y=35)
    t.place(x=600, y=37)

    jianjie_L.place(x=5, y=70)
    jianjie.place(x=75, y=67)

    fanwei_L.place(x=5, y=110)
    fanwei.place(x=75, y=112)

    waibaoC1.place(x=5, y=140)
    waibaoC2.place(x=5, y=160)
    wbguocheng_L.place(x=135, y=150)
    wbguocheng.place(x=235, y=147)

    tsguocheng_L.place(x=5, y=195)
    tsguocheng.place(x=75, y=192)

    zhijian_L.place(x=6, y=235)
    zhijian.place(x=76, y=237)
    zjfuze_L.place(x=244, y=235)
    zjfuze.place(x=329, y=237)
    zjbmcode_L.place(x=497, y=235)
    zjbmcode.place(x=597, y=237)

    xiaoshou_L.place(x=6, y=265)
    xiaoshou.place(x=76, y=267)
    xsfuze_L.place(x=244, y=265)
    xsfuze.place(x=329, y=267)
    xsbmcode_L.place(x=497, y=265)
    xsbmcode.place(x=597, y=267)

    shengchan_L.place(x=6, y=295)
    shengchan.place(x=76, y=297)
    scfuze_L.place(x=244, y=295)
    scfuze.place(x=329, y=297)
    scbmcode_L.place(x=497, y=295)
    scbmcode.place(x=597, y=297)

    xingzheng_L.place(x=6, y=325)
    xingzheng.place(x=76, y=327)
    xzfuze_L.place(x=244, y=325)
    xzfuze.place(x=329, y=327)
    xzbmcode_L.place(x=497, y=325)
    xzbmcode.place(x=597, y=327)

    caigou_L.place(x=6, y=355)
    caigou.place(x=76, y=357)
    cgfuze_L.place(x=244, y=355)
    cgfuze.place(x=329, y=357)
    cgbmcode_L.place(x=497, y=355)
    cgbmcode.place(x=597, y=357)

    shangchanliuchng1_L.place(x=5, y=385)
    shengchanliucheng1.place(x=115, y=387)

    shangchanliuchng2_L.place(x=5, y=415)
    shengchanliucheng2.place(x=115, y=417)

    shangchanliuchng3_L.place(x=5, y=445)
    shengchanliucheng3.place(x=115, y=447)

    btn_gen.place(relx=0.35, rely=0.9)

    window.mainloop()


def InforWindow_2(info_dic):
    '''E/QE界面'''
    window = tk.Tk()

    # 给窗口的可视化起名字
    window.title('认证文件管理系统')
    window.config(background='Lavender')

    # 设定窗口的大小(长 * 宽)
    window.geometry('770x580')  # 这里的乘是小x
    window.resizable(0, 0)

    name_L = Label(window, text='企业名称：', bg='Lavender')
    name = Text(window, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

    code_L = Label(window, text='企业代码：', bg='Lavender')
    code = Text(window, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

    ver_L = Label(window, text='版本：', bg='Lavender')
    ver = Text(window, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
    ver.insert('0.0', 'A')

    times_L = Label(window, text='版次：', bg='Lavender')
    times = Text(window, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
    times.insert('0.0', '0')

    m_L = Label(window, text='管理者代表：', bg='Lavender')
    m = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    mx_L = Label(window, text='最高管理者：', bg='Lavender')
    mx = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    t_L = Label(window, text='手册发布实施日期：', bg='Lavender')
    t = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    jianjie_L = Label(window, text='公司简介：', bg='Lavender')
    jianjie = Text(window, height=2, width=97, relief=RAISED, highlightcolor='black', highlightthickness=1)

    fanwei_L = Label(window, text='认证范围：', bg='Lavender')
    fanwei = Text(window, height=1, width=97, relief=RAISED, highlightcolor='black', highlightthickness=1)

    waibaoV = tk.IntVar()

    def waibaobool():
        if waibaoV.get() == 0:
            wbguocheng.config(state=DISABLED)
        else:
            wbguocheng.config(state=NORMAL)

    waibaoC1 = tk.Radiobutton(window, text="公司有外包过程", variable=waibaoV, value=1, command=waibaobool,
                              bg='Lavender')
    waibaoC2 = tk.Radiobutton(window, text="公司无外包过程", variable=waibaoV, value=0, command=waibaobool,
                              bg='Lavender')
    wbguocheng_L = Label(window, text='外包过程表述：', bg='Lavender')
    wbguocheng = Text(window, height=2, width=74, relief=RAISED, highlightcolor='black', highlightthickness=1)
    wbguocheng.insert('0.0', '本公司外包过程为XX')

    tsguocheng_L = Label(window, text='特殊过程：', bg='Lavender')
    tsguocheng = Text(window, height=2, width=97, relief=RAISED, highlightcolor='black', highlightthickness=1)
    tsguocheng.insert('0.0', '无特殊过程/特殊过程为XX')

    zhijian_L = Label(window, text='质检部门：', bg='Lavender')
    zhijian = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    zjfuze_L = Label(window, text='质检负责人：', bg='Lavender')
    zjfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    zjbmcode_L = Label(window, text='质检部门代码：', bg='Lavender')
    zjbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xiaoshou_L = Label(window, text='销售部门：', bg='Lavender')
    xiaoshou = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xsfuze_L = Label(window, text='销售负责人：', bg='Lavender')
    xsfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xsbmcode_L = Label(window, text='销售部门代码：', bg='Lavender')
    xsbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    shengchan_L = Label(window, text='生产部门：', bg='Lavender')
    shengchan = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    scfuze_L = Label(window, text='生产负责人：', bg='Lavender')
    scfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    scbmcode_L = Label(window, text='生产部门代码：', bg='Lavender')
    scbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xingzheng_L = Label(window, text='行政部门：', bg='Lavender')
    xingzheng = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xzfuze_L = Label(window, text='行政负责人：', bg='Lavender')
    xzfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xzbmcode_L = Label(window, text='行政部门代码：', bg='Lavender')
    xzbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    caiwu_L = Label(window, text='财务部门：', bg='Lavender')
    caiwu = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    cwfuze_L = Label(window, text='财务负责人：', bg='Lavender')
    cwfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    cwbmcode_L = Label(window, text='财务部门代码：', bg='Lavender')
    cwbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    caigou_L = Label(window, text='采购部门：', bg='Lavender')
    caigou = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    cgfuze_L = Label(window, text='采购负责人：', bg='Lavender')
    cgfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    cgbmcode_L = Label(window, text='采购部门代码：', bg='Lavender')
    cgbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    shangchanliuchng1_L = Label(window, text='生产工艺流程1：', bg='Lavender')
    shengchanliucheng1 = Text(window, height=1, width=85, relief=RAISED, highlightcolor='black', highlightthickness=1)
    shengchanliucheng1.insert('0.0', '若无该流程则跳过该项')

    shangchanliuchng2_L = Label(window, text='生产工艺流程2：', bg='Lavender')
    shengchanliucheng2 = Text(window, height=1, width=85, relief=RAISED, highlightcolor='black', highlightthickness=1)
    shengchanliucheng2.insert('0.0', '若无该流程则跳过该项')

    shangchanliuchng3_L = Label(window, text='生产工艺流程3：', bg='Lavender')
    shengchanliucheng3 = Text(window, height=1, width=85, relief=RAISED, highlightcolor='black', highlightthickness=1)
    shengchanliucheng3.insert('0.0', '若无该流程则跳过该项')

    def textGen():
        info_dic['__企业名称__'] = name.get(0.0, 20.0).strip()
        info_dic['__企业代码__'] = code.get(0.0, 20.0).strip()
        info_dic['__版本__'] = ver.get(0.0, 20.0).strip()
        info_dic['__版次__'] = '\'' + times.get(0.0, 20.0).strip() + '\''
        info_dic['__管理者代表__'] = m.get(0.0, 20.0).strip()
        info_dic['__最高管理者__'] = mx.get(0.0, 20.0).strip()
        info_dic['__手册发布实施日期__'] = t.get(0.0, 20.0).strip()
        info_dic['__公司简介__'] = jianjie.get(0.0, 20.0).strip()
        info_dic['__认证范围__'] = fanwei.get(0.0, 20.0).strip()
        if waibaoV.get() == 1:
            info_dic['__有无外包过程__'] = '有'
            info_dic['__外包过程表述__'] = wbguocheng.get(0.0, 20.0).strip()
        else:
            info_dic['__有无外包过程__'] = '无'
            info_dic['__外包过程表述__'] = ''
        info_dic['__特殊过程__'] = tsguocheng.get(0.0, 20.0).strip()
        info_dic['__质检部门__'] = zhijian.get(0.0, 20.0).strip()
        info_dic['__质检负责人__'] = zjfuze.get(0.0, 20.0).strip()
        info_dic['__质检部门代码__'] = zjbmcode.get(0.0, 20.0).strip()
        info_dic['__销售部门__'] = xiaoshou.get(0.0, 20.0).strip()
        info_dic['__销售负责人__'] = xsfuze.get(0.0, 20.0).strip()
        info_dic['__销售部门代码__'] = xsbmcode.get(0.0, 20.0).strip()
        info_dic['__生产部门__'] = shengchan.get(0.0, 20.0).strip()
        info_dic['__生产负责人__'] = scfuze.get(0.0, 20.0).strip()
        info_dic['__生产部门代码__'] = scbmcode.get(0.0, 20.0).strip()
        info_dic['__行政部门__'] = xingzheng.get(0.0, 20.0).strip()
        info_dic['__行政负责人__'] = xzfuze.get(0.0, 20.0).strip()
        info_dic['__行政部门代码__'] = xzbmcode.get(0.0, 20.0).strip()
        info_dic['__财务部门__'] = caiwu.get(0.0, 20.0).strip()
        info_dic['__财务负责人__'] = cwfuze.get(0.0, 20.0).strip()
        info_dic['__财务部门代码__'] = cwbmcode.get(0.0, 20.0).strip()
        info_dic['__采购部门__'] = caigou.get(0.0, 20.0).strip()
        info_dic['__采购负责人__'] = cgfuze.get(0.0, 20.0).strip()
        info_dic['__采购部门代码__'] = cgbmcode.get(0.0, 20.0).strip()
        info_dic['__生产工艺流程1__'] = shengchanliucheng1.get(0.0, 20.0).strip()
        info_dic['__生产工艺流程2__'] = shengchanliucheng2.get(0.0, 20.0).strip()
        info_dic['__生产工艺流程3__'] = shengchanliucheng3.get(0.0, 20.0).strip()
        print(info_dic)
        window.destroy()
        informCollectWindow(info_dic)

    btn_gen = tk.Button(window, text='确认信息无误，进入下一采集阶段。', command=lambda: [textGen()])

    '''place布局'''
    name_L.place(x=5, y=5)  # 14 / token
    name.place(x=75, y=7)  # 5.6 / 1

    code_L.place(x=245, y=5)
    code.place(x=315, y=7)

    ver_L.place(x=485, y=5)
    ver.place(x=530, y=7)

    times_L.place(x=625, y=5)
    times.place(x=670, y=7)

    m_L.place(x=5, y=35)
    m.place(x=90, y=37)

    mx_L.place(x=245, y=35)
    mx.place(x=330, y=37)

    t_L.place(x=475, y=35)
    t.place(x=600, y=37)

    jianjie_L.place(x=5, y=70)
    jianjie.place(x=75, y=67)

    fanwei_L.place(x=5, y=110)
    fanwei.place(x=75, y=112)

    waibaoC1.place(x=5, y=140)
    waibaoC2.place(x=5, y=160)
    wbguocheng_L.place(x=135, y=150)
    wbguocheng.place(x=235, y=147)

    tsguocheng_L.place(x=5, y=195)
    tsguocheng.place(x=75, y=192)

    zhijian_L.place(x=6, y=235)
    zhijian.place(x=76, y=237)
    zjfuze_L.place(x=244, y=235)
    zjfuze.place(x=329, y=237)
    zjbmcode_L.place(x=497, y=235)
    zjbmcode.place(x=597, y=237)

    xiaoshou_L.place(x=6, y=265)
    xiaoshou.place(x=76, y=267)
    xsfuze_L.place(x=244, y=265)
    xsfuze.place(x=329, y=267)
    xsbmcode_L.place(x=497, y=265)
    xsbmcode.place(x=597, y=267)

    shengchan_L.place(x=6, y=295)
    shengchan.place(x=76, y=297)
    scfuze_L.place(x=244, y=295)
    scfuze.place(x=329, y=297)
    scbmcode_L.place(x=497, y=295)
    scbmcode.place(x=597, y=297)

    xingzheng_L.place(x=6, y=325)
    xingzheng.place(x=76, y=327)
    xzfuze_L.place(x=244, y=325)
    xzfuze.place(x=329, y=327)
    xzbmcode_L.place(x=497, y=325)
    xzbmcode.place(x=597, y=327)

    caiwu_L.place(x=6, y=355)
    caiwu.place(x=76, y=357)
    cwfuze_L.place(x=244, y=355)
    cwfuze.place(x=329, y=357)
    cwbmcode_L.place(x=497, y=355)
    cwbmcode.place(x=597, y=357)

    caigou_L.place(x=6, y=385)
    caigou.place(x=76, y=387)
    cgfuze_L.place(x=244, y=385)
    cgfuze.place(x=329, y=387)
    cgbmcode_L.place(x=497, y=385)
    cgbmcode.place(x=597, y=387)

    shangchanliuchng1_L.place(x=5, y=415)
    shengchanliucheng1.place(x=115, y=417)

    shangchanliuchng2_L.place(x=5, y=445)
    shengchanliucheng2.place(x=115, y=447)

    shangchanliuchng3_L.place(x=5, y=475)
    shengchanliucheng3.place(x=115, y=477)

    btn_gen.place(relx=0.35, rely=0.9)

    window.mainloop()


def InforWindow_3(info_dic):
    '''S/QS/ES/QES界面'''
    window = tk.Tk()

    # 给窗口的可视化起名字
    window.title('认证文件管理系统')
    window.config(background='Lavender')

    # 设定窗口的大小(长 * 宽)
    window.geometry('770x590')  # 这里的乘是小x
    window.resizable(0, 0)

    name_L = Label(window, text='企业名称：', bg='Lavender')
    name = Text(window, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

    code_L = Label(window, text='企业代码：', bg='Lavender')
    code = Text(window, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

    ver_L = Label(window, text='版本：', bg='Lavender')
    ver = Text(window, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
    ver.insert('0.0', 'A')

    times_L = Label(window, text='版次：', bg='Lavender')
    times = Text(window, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)
    times.insert('0.0', '0')

    m_L = Label(window, text='管理者代表：', bg='Lavender')
    m = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    mx_L = Label(window, text='最高管理者：', bg='Lavender')
    mx = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    t_L = Label(window, text='手册发布实施日期：', bg='Lavender')
    t = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    jianjie_L = Label(window, text='公司简介：', bg='Lavender')
    jianjie = Text(window, height=2, width=97, relief=RAISED, highlightcolor='black', highlightthickness=1)

    fanwei_L = Label(window, text='认证范围：', bg='Lavender')
    fanwei = Text(window, height=1, width=97, relief=RAISED, highlightcolor='black', highlightthickness=1)

    waibaoV = tk.IntVar()

    def waibaobool():
        if waibaoV.get() == 0:
            wbguocheng.config(state=DISABLED)
        else:
            wbguocheng.config(state=NORMAL)

    waibaoC1 = tk.Radiobutton(window, text="公司有外包过程", variable=waibaoV, value=1, command=waibaobool,
                              bg='Lavender')
    waibaoC2 = tk.Radiobutton(window, text="公司无外包过程", variable=waibaoV, value=0, command=waibaobool,
                              bg='Lavender')
    wbguocheng_L = Label(window, text='外包过程表述：', bg='Lavender')
    wbguocheng = Text(window, height=2, width=74, relief=RAISED, highlightcolor='black', highlightthickness=1)
    wbguocheng.insert('0.0', '本公司外包过程为XX')

    tsguocheng_L = Label(window, text='特殊过程：', bg='Lavender')
    tsguocheng = Text(window, height=2, width=97, relief=RAISED, highlightcolor='black', highlightthickness=1)
    tsguocheng.insert('0.0', '无特殊过程/特殊过程为XX')

    zhijian_L = Label(window, text='质检部门：', bg='Lavender')
    zhijian = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    zjfuze_L = Label(window, text='质检负责人：', bg='Lavender')
    zjfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    zjbmcode_L = Label(window, text='质检部门代码：', bg='Lavender')
    zjbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xiaoshou_L = Label(window, text='销售部门：', bg='Lavender')
    xiaoshou = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xsfuze_L = Label(window, text='销售负责人：', bg='Lavender')
    xsfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xsbmcode_L = Label(window, text='销售部门代码：', bg='Lavender')
    xsbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    shengchan_L = Label(window, text='生产部门：', bg='Lavender')
    shengchan = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    scfuze_L = Label(window, text='生产负责人：', bg='Lavender')
    scfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    scbmcode_L = Label(window, text='生产部门代码：', bg='Lavender')
    scbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xingzheng_L = Label(window, text='行政部门：', bg='Lavender')
    xingzheng = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xzfuze_L = Label(window, text='行政负责人：', bg='Lavender')
    xzfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    xzbmcode_L = Label(window, text='行政部门代码：', bg='Lavender')
    xzbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    caiwu_L = Label(window, text='财务部门：', bg='Lavender')
    caiwu = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    cwfuze_L = Label(window, text='财务负责人：', bg='Lavender')
    cwfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    cwbmcode_L = Label(window, text='财务部门代码：', bg='Lavender')
    cwbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    caigou_L = Label(window, text='采购部门：', bg='Lavender')
    caigou = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    cgfuze_L = Label(window, text='采购负责人：', bg='Lavender')
    cgfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    cgbmcode_L = Label(window, text='采购部门代码：', bg='Lavender')
    cgbmcode = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    anquanfuze_L = Label(window, text='安全负责人：', bg='Lavender')
    anquanfuze = Text(window, height=1, width=22, relief=RAISED, highlightcolor='black', highlightthickness=1)

    shangchanliuchng1_L = Label(window, text='生产工艺流程1：', bg='Lavender')
    shengchanliucheng1 = Text(window, height=1, width=85, relief=RAISED, highlightcolor='black', highlightthickness=1)
    shengchanliucheng1.insert('0.0', '若无该流程则跳过该项')

    shangchanliuchng2_L = Label(window, text='生产工艺流程2：', bg='Lavender')
    shengchanliucheng2 = Text(window, height=1, width=85, relief=RAISED, highlightcolor='black', highlightthickness=1)
    shengchanliucheng2.insert('0.0', '若无该流程则跳过该项')

    shangchanliuchng3_L = Label(window, text='生产工艺流程3：', bg='Lavender')
    shengchanliucheng3 = Text(window, height=1, width=85, relief=RAISED, highlightcolor='black', highlightthickness=1)
    shengchanliucheng3.insert('0.0', '若无该流程则跳过该项')

    def textGen():
        info_dic['__企业名称__'] = name.get(0.0, 20.0).strip()
        info_dic['__企业代码__'] = code.get(0.0, 20.0).strip()
        info_dic['__版本__'] = ver.get(0.0, 20.0).strip()
        info_dic['__版次__'] = '\'' + times.get(0.0, 20.0).strip() + '\''
        info_dic['__管理者代表__'] = m.get(0.0, 20.0).strip()
        info_dic['__最高管理者__'] = mx.get(0.0, 20.0).strip()
        info_dic['__手册发布实施日期__'] = t.get(0.0, 20.0).strip()
        info_dic['__公司简介__'] = jianjie.get(0.0, 20.0).strip()
        info_dic['__认证范围__'] = fanwei.get(0.0, 20.0).strip()
        if waibaoV.get() == 1:
            info_dic['__有无外包过程__'] = '有'
            info_dic['__外包过程表述__'] = wbguocheng.get(0.0, 20.0).strip()
        else:
            info_dic['__有无外包过程__'] = '无'
            info_dic['__外包过程表述__'] = ''
        info_dic['__特殊过程__'] = tsguocheng.get(0.0, 20.0).strip()
        info_dic['__质检部门__'] = zhijian.get(0.0, 20.0).strip()
        info_dic['__质检负责人__'] = zjfuze.get(0.0, 20.0).strip()
        info_dic['__质检部门代码__'] = zjbmcode.get(0.0, 20.0).strip()
        info_dic['__销售部门__'] = xiaoshou.get(0.0, 20.0).strip()
        info_dic['__销售负责人__'] = xsfuze.get(0.0, 20.0).strip()
        info_dic['__销售部门代码__'] = xsbmcode.get(0.0, 20.0).strip()
        info_dic['__生产部门__'] = shengchan.get(0.0, 20.0).strip()
        info_dic['__生产负责人__'] = scfuze.get(0.0, 20.0).strip()
        info_dic['__生产部门代码__'] = scbmcode.get(0.0, 20.0).strip()
        info_dic['__行政部门__'] = xingzheng.get(0.0, 20.0).strip()
        info_dic['__行政负责人__'] = xzfuze.get(0.0, 20.0).strip()
        info_dic['__行政部门代码__'] = xzbmcode.get(0.0, 20.0).strip()
        info_dic['__采购部门__'] = caigou.get(0.0, 20.0).strip()
        info_dic['__采购负责人__'] = cgfuze.get(0.0, 20.0).strip()
        info_dic['__采购部门代码__'] = cgbmcode.get(0.0, 20.0).strip()
        info_dic['__财务部门__'] = caiwu.get(0.0, 20.0).strip()
        info_dic['__财务负责人__'] = cwfuze.get(0.0, 20.0).strip()
        info_dic['__财务部门代码__'] = cwbmcode.get(0.0, 20.0).strip()
        info_dic['__安全负责人__'] = anquanfuze.get(0.0, 20.0).strip()
        info_dic['__生产工艺流程1__'] = shengchanliucheng1.get(0.0, 20.0).strip()
        info_dic['__生产工艺流程2__'] = shengchanliucheng2.get(0.0, 20.0).strip()
        info_dic['__生产工艺流程3__'] = shengchanliucheng3.get(0.0, 20.0).strip()
        print(info_dic)
        window.destroy()
        informCollectWindow(info_dic)

    btn_gen = tk.Button(window, text='确认信息无误，进入下一采集阶段。', command=lambda: [textGen()])

    '''place布局'''
    name_L.place(x=5, y=5)  # 14 / token
    name.place(x=75, y=7)  # 5.6 / 1

    code_L.place(x=245, y=5)
    code.place(x=315, y=7)

    ver_L.place(x=485, y=5)
    ver.place(x=530, y=7)

    times_L.place(x=625, y=5)
    times.place(x=670, y=7)

    m_L.place(x=5, y=35)
    m.place(x=90, y=37)

    mx_L.place(x=245, y=35)
    mx.place(x=330, y=37)

    t_L.place(x=475, y=35)
    t.place(x=600, y=37)

    jianjie_L.place(x=5, y=70)
    jianjie.place(x=75, y=67)

    fanwei_L.place(x=5, y=110)
    fanwei.place(x=75, y=112)

    waibaoC1.place(x=5, y=140)
    waibaoC2.place(x=5, y=160)
    wbguocheng_L.place(x=135, y=150)
    wbguocheng.place(x=235, y=147)

    tsguocheng_L.place(x=5, y=195)
    tsguocheng.place(x=75, y=192)

    zhijian_L.place(x=6, y=235)
    zhijian.place(x=76, y=237)
    zjfuze_L.place(x=244, y=235)
    zjfuze.place(x=329, y=237)
    zjbmcode_L.place(x=497, y=235)
    zjbmcode.place(x=597, y=237)

    xiaoshou_L.place(x=6, y=265)
    xiaoshou.place(x=76, y=267)
    xsfuze_L.place(x=244, y=265)
    xsfuze.place(x=329, y=267)
    xsbmcode_L.place(x=497, y=265)
    xsbmcode.place(x=597, y=267)

    shengchan_L.place(x=6, y=295)
    shengchan.place(x=76, y=297)
    scfuze_L.place(x=244, y=295)
    scfuze.place(x=329, y=297)
    scbmcode_L.place(x=497, y=295)
    scbmcode.place(x=597, y=297)

    xingzheng_L.place(x=6, y=325)
    xingzheng.place(x=76, y=327)
    xzfuze_L.place(x=244, y=325)
    xzfuze.place(x=329, y=327)
    xzbmcode_L.place(x=497, y=325)
    xzbmcode.place(x=597, y=327)

    caiwu_L.place(x=6, y=355)
    caiwu.place(x=76, y=357)
    cwfuze_L.place(x=244, y=355)
    cwfuze.place(x=329, y=357)
    cwbmcode_L.place(x=497, y=355)
    cwbmcode.place(x=597, y=357)

    caigou_L.place(x=6, y=385)
    caigou.place(x=76, y=387)
    cgfuze_L.place(x=244, y=385)
    cgfuze.place(x=329, y=387)
    cgbmcode_L.place(x=497, y=385)
    cgbmcode.place(x=597, y=387)

    anquanfuze_L.place(x=5, y=415)
    anquanfuze.place(x=90, y=417)

    shangchanliuchng1_L.place(x=5, y=445)
    shengchanliucheng1.place(x=115, y=447)

    shangchanliuchng2_L.place(x=5, y=475)
    shengchanliucheng2.place(x=115, y=477)

    shangchanliuchng3_L.place(x=5, y=505)
    shengchanliucheng3.place(x=115, y=507)

    btn_gen.place(relx=0.35, rely=0.92)

    window.mainloop()


# 第三层界面
def informCollectWindow(info_dic):
    window = tk.Tk()

    # 给窗口的可视化起名字
    window.title('认证文件管理系统')
    window.config(background='Lavender')

    window.geometry('1280x650')  # 这里的乘是小x

    jlnf_L = Label(window, text='记录年份：', bg='Lavender')
    jlnf = Text(window, width=22, heigh=1)
    jlnf.insert(0.0, '2022')

    ybjlrq_L = Label(window, text='一般记录日期：', bg='Lavender')
    ybjlrq = Text(window, width=22, heigh=1)
    ybjlrq.insert(0.0, '2022.1.4')

    peixun1 = Label(window, text='是否有1月培训：', bg='Lavender')
    peixun1V = tk.IntVar()
    peixun1C1 = tk.Radiobutton(window, text="是", variable=peixun1V, value=1, bg='Lavender')
    peixun1C2 = tk.Radiobutton(window, text="否", variable=peixun1V, value=0, bg='Lavender')

    peixun2 = Label(window, text='是否有2月培训：', bg='Lavender')
    peixun2V = tk.IntVar()
    peixun2C1 = tk.Radiobutton(window, text="是", variable=peixun2V, value=1, bg='Lavender')
    peixun2C2 = tk.Radiobutton(window, text="否", variable=peixun2V, value=0, bg='Lavender')

    peixun3 = Label(window, text='是否有3月培训：', bg='Lavender')
    peixun3V = tk.IntVar()
    peixun3C1 = tk.Radiobutton(window, text="是", variable=peixun3V, value=1, bg='Lavender')
    peixun3C2 = tk.Radiobutton(window, text="否", variable=peixun3V, value=0, bg='Lavender')

    peixun6 = Label(window, text='是否有6月培训：', bg='Lavender')
    peixun6V = tk.IntVar()
    peixun6C1 = tk.Radiobutton(window, text="是", variable=peixun6V, value=1, bg='Lavender')
    peixun6C2 = tk.Radiobutton(window, text="否", variable=peixun6V, value=0, bg='Lavender')

    peixun8 = Label(window, text='是否有8月培训：', bg='Lavender')
    peixun8V = tk.IntVar()
    peixun8C1 = tk.Radiobutton(window, text="是", variable=peixun8V, value=1, bg='Lavender')
    peixun8C2 = tk.Radiobutton(window, text="否", variable=peixun8V, value=0, bg='Lavender')

    peixun10 = Label(window, text='是否有10月培训：', bg='Lavender')
    peixun10V = tk.IntVar()
    peixun10C1 = tk.Radiobutton(window, text="是", variable=peixun10V, value=1, bg='Lavender')
    peixun10C2 = tk.Radiobutton(window, text="否", variable=peixun10V, value=0, bg='Lavender')

    peixun11 = Label(window, text='是否有11月培训：', bg='Lavender')
    peixun11V = tk.IntVar()
    peixun11C1 = tk.Radiobutton(window, text="是", variable=peixun11V, value=1, bg='Lavender')
    peixun11C2 = tk.Radiobutton(window, text="否", variable=peixun11V, value=0, bg='Lavender')

    peixun12 = Label(window, text='是否有12月培训：', bg='Lavender')
    peixun12V = tk.IntVar()
    peixun12C1 = tk.Radiobutton(window, text="是", variable=peixun12V, value=1, bg='Lavender')
    peixun12C2 = tk.Radiobutton(window, text="否", variable=peixun12V, value=0, bg='Lavender')

    peixun4 = Label(window, text='是否有4月培训：', bg='Lavender')
    peixun4V = tk.IntVar()
    peixun4C1 = tk.Radiobutton(window, text="是", variable=peixun4V, value=1, bg='Lavender')
    peixun4C2 = tk.Radiobutton(window, text="否", variable=peixun4V, value=0, bg='Lavender')

    peixun5 = Label(window, text='是否有5月培训：', bg='Lavender')
    peixun5V = tk.IntVar()
    peixun5C1 = tk.Radiobutton(window, text="是", variable=peixun5V, value=1, bg='Lavender')
    peixun5C2 = tk.Radiobutton(window, text="否", variable=peixun5V, value=0, bg='Lavender')

    peixun7 = Label(window, text='是否有7月培训：', bg='Lavender')
    peixun7V = tk.IntVar()
    peixun7C1 = tk.Radiobutton(window, text="是", variable=peixun7V, value=1, bg='Lavender')
    peixun7C2 = tk.Radiobutton(window, text="否", variable=peixun7V, value=0, bg='Lavender')

    peixun9 = Label(window, text='是否有9月培训：', bg='Lavender')
    peixun9V = tk.IntVar()
    peixun9C1 = tk.Radiobutton(window, text="是", variable=peixun8V, value=1, bg='Lavender')
    peixun9C2 = tk.Radiobutton(window, text="否", variable=peixun8V, value=0, bg='Lavender')

    nsypxrq_L = Label(window, text='内审员培训日期:', bg='Lavender')
    nsypxrq = Text(window, width=22, heigh=1)

    nsjhzdrq_L = Label(window, text='内审计划制定日期:', bg='Lavender')
    nsjhzdrq = Text(window, width=22, heigh=1)

    nsksrq_L = Label(window, text='内审开始日期:', bg='Lavender')
    nsksrq = Text(window, width=22, heigh=1)

    nsjsrq_L = Label(window, text='内审结束日期:', bg='Lavender')
    nsjsrq = Text(window, width=22, heigh=1)

    nszgwcrq_L = Label(window, text='内审整改完成日期:', bg='Lavender')
    nszgwcrq = Text(window, width=22, heigh=1)

    q713 = Label(window, text='是否为Q7.1.3条款不符合：', bg='Lavender')
    q713V = tk.IntVar()
    q713C1 = tk.Radiobutton(window, text="是", variable=q713V, value=1, bg='Lavender')
    q713C2 = tk.Radiobutton(window, text="否", variable=q713V, value=0, bg='Lavender')

    q851 = Label(window, text='是否为Q8.5.1条款不符合：', bg='Lavender')
    q851V = tk.IntVar()
    q851C1 = tk.Radiobutton(window, text="是", variable=q851V, value=1, bg='Lavender')
    q851C2 = tk.Radiobutton(window, text="否", variable=q851V, value=0, bg='Lavender')

    q62 = Label(window, text='是否为Q6.2条款不符合：', bg='Lavender')
    q62V = tk.IntVar()
    q62C1 = tk.Radiobutton(window, text="是", variable=q62V, value=1, bg='Lavender')
    q62C2 = tk.Radiobutton(window, text="否", variable=q62V, value=0, bg='Lavender')

    gpjhzdrq_L = Label(window, text='管评计划制定日期:', bg='Lavender')
    gpjhzdrq = Text(window, width=22, heigh=1)

    gprq_L = Label(window, text='管评日期:', bg='Lavender')
    gprq = Text(window, width=22, heigh=1)

    gpbgrq_L = Label(window, text='管评报告日期:', bg='Lavender')
    gpbgrq = Text(window, width=22, heigh=1)

    jqscjc = Label(window, text='是否为加强生产检查改进项：', bg='Lavender')
    jqscjcV = tk.IntVar()
    jqscjcC1 = tk.Radiobutton(window, text="是", variable=jqscjcV, value=1, bg='Lavender')
    jqscjcC2 = tk.Radiobutton(window, text="否", variable=jqscjcV, value=0, bg='Lavender')

    jqysjs = Label(window, text='是否为提高意识技术改进项：', bg='Lavender')
    jqysjsV = tk.IntVar()
    jqysjsC1 = tk.Radiobutton(window, text="是", variable=jqysjsV, value=1, bg='Lavender')
    jqysjsC2 = tk.Radiobutton(window, text="否", variable=jqysjsV, value=0, bg='Lavender')

    jqzp = Label(window, text='是否为加强招聘改进项：', bg='Lavender')
    jqzpV = tk.IntVar()
    jqzpC1 = tk.Radiobutton(window, text="是", variable=jqzpV, value=1, bg='Lavender')
    jqzpC2 = tk.Radiobutton(window, text="否", variable=jqzpV, value=0, bg='Lavender')

    gpgjwcsj_L = Label(window, text='管评改进项完成日期:', bg='Lavender')
    gpgjwcsj = Text(window, width=22, heigh=1)

    syndgprq_L = Label(window, text='上一年度管理评价日期:', bg='Lavender')
    syndgprq = Text(window, width=22, heigh=1)

    syndgpgjrq_L = Label(window, text='上一年度管评改进项完成日期:', bg='Lavender')
    syndgpgjrq = Text(window, width=22, heigh=1)

    syndjqscjc = Label(window, text='上一年度是否为加强生产检查改进项：', bg='Lavender')
    syndjqscjcV = tk.IntVar()
    syndjqscjcC1 = tk.Radiobutton(window, text="是", variable=syndjqscjcV, value=1, bg='Lavender')
    syndjqscjcC2 = tk.Radiobutton(window, text="否", variable=syndjqscjcV, value=0, bg='Lavender')

    syndjqysjs = Label(window, text='上一年度是否为提高意识技术改进项：', bg='Lavender')
    syndjqysjsV = tk.IntVar()
    syndjqysjsC1 = tk.Radiobutton(window, text="是", variable=syndjqysjsV, value=1, bg='Lavender')
    syndjqysjsC2 = tk.Radiobutton(window, text="否", variable=syndjqysjsV, value=0, bg='Lavender')

    syndjqzp = Label(window, text='上一年度是否为加强招聘改进项：', bg='Lavender')
    syndjqzpV = tk.IntVar()
    syndjqzpC1 = tk.Radiobutton(window, text="是", variable=syndjqzpV, value=1, bg='Lavender')
    syndjqzpC2 = tk.Radiobutton(window, text="否", variable=syndjqzpV, value=0, bg='Lavender')

    xxht_text = Text(window, width=120, heigh=4)
    xxhtwin_L = Label(window, text='销售合同信息：', bg='Lavender')
    btn_xxht = tk.Button(window, text='修改合同信息。', command=lambda: xxhtWindow())
    xxht_info = [xxht_text.get(0.0, 40.0)]

    myddcrq_L = Label(window, text='满意度调查日期:', bg='Lavender')
    myddcrq = Text(window, width=22, heigh=1)

    myddcsl_L = Label(window, text='满意度调查数量:', bg='Lavender')
    myddcsl = Text(window, width=22, heigh=1)

    myddcpj_L = Label(window, text='平均满意度', bg='Lavender')
    myddcpj = Text(window, width=22, heigh=1)

    myddc1_L = Label(window, text='销售合同1满意度', bg='Lavender')
    myddc1 = Text(window, width=22, heigh=1)

    myddc2_L = Label(window, text='销售合同2满意度', bg='Lavender')
    myddc2 = Text(window, width=22, heigh=1)

    myddc3_L = Label(window, text='销售合同3满意度', bg='Lavender')
    myddc3 = Text(window, width=22, heigh=1)

    myddc4_L = Label(window, text='销售合同4满意度', bg='Lavender')
    myddc4 = Text(window, width=22, heigh=1)

    myddc5_L = Label(window, text='销售合同5满意度', bg='Lavender')
    myddc5 = Text(window, width=22, heigh=1)

    myddc6_L = Label(window, text='销售合同6满意度', bg='Lavender')
    myddc6 = Text(window, width=22, heigh=1)

    myddc7_L = Label(window, text='销售合同7满意度', bg='Lavender')
    myddc7 = Text(window, width=22, heigh=1)

    myddc8_L = Label(window, text='销售合同8满意度', bg='Lavender')
    myddc8 = Text(window, width=22, heigh=1)

    gf_text = Text(window, width=120, heigh=4)
    gfwin_L = Label(window, text='已有供方信息：', bg='Lavender')
    btn_gf = tk.Button(window, text='修改供方信息。', command=lambda: gfWindow())
    gf_info = [gf_text.get(0.0, 40.0)]

    cgcp_text = Text(window, width=120, heigh=4)
    cgcpwin_L = Label(window, text='采购产品信息：', bg='Lavender')
    btn_cgcp = tk.Button(window, text='修改采购信息。', command=lambda: cgcpWindow())
    cgcp_info = [gf_text.get(0.0, 40.0)]

    # def doc_gen():
    #     dictionary = GetDictionary("tagList.yml")
    #     work_dir = os.path.abspath('.') # 工作路径

    #     for old, new in dictionary.items():
    #         print(old + "->" + new)
    #     ReplaceAll(os.path.abspath(os.curdir) , work_dir, dictionary)
    def next_stage():
        template_id = info_dic['template_id']
        rzfw, _, rzxm, _ = template_id.split('-')
        if (rzfw == 'SC' or rzfw == 'ZZ' or rzfw == 'JJSC') and (rzxm == 'QS' or rzxm == 'QES'):
            window.destroy()
            window4_1(info_dic)
        elif (rzfw == 'SC' or rzfw == 'ZZ' or rzfw == 'JJSC') and (rzxm == 'Q' or rzxm == 'QE'):
            window.destroy()
            window4_2(info_dic)
        elif (rzfw == 'SC' or rzfw == 'ZZ' or rzfw == 'JJSC') and (rzxm == 'S' or rzxm == 'ES'):
            window.destroy()
            window4_4(info_dic)
        else:
            #
            window.destroy()

    # 封装第三层页面radio_button处理结果逻辑
    def addRadioRes(bool_str, radio_res):
        if radio_res.get() == 1:
            info_dic['__{}__'.format(bool_str)] = '是'
        else:
            info_dic['__{}__'.format(bool_str)] = '否'

    def add_item_to_info_dict(common_str, key_list, text_str):
        """
        处理第三个页面中的三个多行文本框
        """
        row_list = text_str.split('\n')
        if len(row_list) == 0:
            return
        item_list = [row.split(',') for row in row_list]
        for row in range(len(row_list)):
            for item in range(len(item_list[0])):
                key_str = '__{}{}{}__'.format(common_str, row, key_list[item])
                if item_list[row][item] == '':
                    info_dic[key_str] = '无'
                else:
                    info_dic[key_str] = item_list[row][item]

    # 第三层界面处理结果生成字典
    def textGen():
        info_dic['__记录年份__'] = jlnf.get(0.0, 20.0).strip()
        info_dic['__一般记录日期__'] = ybjlrq.get(0.0, 20.0).strip()
        addRadioRes('是否有1月培训', peixun1V)
        addRadioRes('是否有2月培训', peixun2V)
        addRadioRes('是否有3月培训', peixun3V)
        addRadioRes('是否有4月培训', peixun4V)
        addRadioRes('是否有5月培训', peixun5V)
        addRadioRes('是否有6月培训', peixun6V)
        addRadioRes('是否有7月培训', peixun7V)
        addRadioRes('是否有8月培训', peixun8V)
        addRadioRes('是否有9月培训', peixun9V)
        addRadioRes('是否有10月培训', peixun10V)
        addRadioRes('是否有11月培训', peixun11V)
        addRadioRes('是否有12月培训', peixun12V)
        info_dic['__内审员培训日期__'] = nsypxrq.get(0.0, 20.0).strip()
        info_dic['__内审计划制定日期__'] = nsjhzdrq.get(0.0, 20.0).strip()
        info_dic['__内审开始日期__'] = nsksrq.get(0.0, 20.0).strip()
        info_dic['__内审结束日期__'] = nsjsrq.get(0.0, 20.0).strip()
        info_dic['__内审整改完成日期__'] = nszgwcrq.get(0.0, 20.0).strip()
        addRadioRes('是否为Q7.1.3条款不符合', q713V)
        addRadioRes('是否为Q8.5.1条款不符合', q851V)
        addRadioRes('是否为Q6.2条款不符合', q62V)
        info_dic['__管评计划制定日期__'] = gpjhzdrq.get(0.0, 20.0).strip()
        info_dic['__管评日期__'] = gprq.get(0.0, 20.0).strip()
        info_dic['__管评报告日期__'] = gpbgrq.get(0.0, 20.0).strip()
        addRadioRes('__是否为加强生产检查改进项__', jqscjcV)
        addRadioRes('__是否为提高意识技术改进项__', jqysjsV)
        addRadioRes('__是否为加强招聘改进项__', jqzpV)
        info_dic['__管评改进项完成日期__'] = gpgjwcsj.get(0.0, 20.0).strip()
        info_dic['__上一年度管理评价日期__'] = syndgprq.get(0.0, 20.0).strip()
        info_dic['__上一年度管评改进项完成日期__'] = syndgpgjrq.get(0.0, 20.0).strip()
        addRadioRes('__上一年度是否为加强生产检查改进项__', syndjqscjcV)
        addRadioRes('__上一年度是否为提高意识技术改进项__', syndjqysjsV)
        addRadioRes('__上一年度是否为加强招聘改进项__', syndjqzpV)
        add_item_to_info_dict('销售合同', ['产品', '客户', '签订日期', '编号', '评审时间'],
                              xxht_text.get(0.0, 40.0).strip())
        info_dic['__满意度调查日期__'] = myddcrq.get(0.0, 20.0).strip()
        info_dic['__满意度调查数量__'] = myddcsl.get(0.0, 20.0).strip()
        info_dic['__平均满意度__'] = myddcpj.get(0.0, 20.0).strip()
        info_dic['__销售合同1满意度__'] = myddc1.get(0.0, 20.0).strip()
        info_dic['__销售合同2满意度__'] = myddc2.get(0.0, 20.0).strip()
        info_dic['__销售合同3满意度__'] = myddc3.get(0.0, 20.0).strip()
        info_dic['__销售合同4满意度__'] = myddc4.get(0.0, 20.0).strip()
        info_dic['__销售合同5满意度__'] = myddc5.get(0.0, 20.0).strip()
        info_dic['__销售合同6满意度__'] = myddc6.get(0.0, 20.0).strip()
        info_dic['__销售合同7满意度__'] = myddc7.get(0.0, 20.0).strip()
        info_dic['__销售合同8满意度__'] = myddc8.get(0.0, 20.0).strip()
        add_item_to_info_dict('供方', ['名称', '地址', '所有产品'], gf_text.get(0.0, 40.0).strip())
        add_item_to_info_dict('采购',
                              ['产品', '产品规格型号', '产品供方', '产品数量方', '产品时间', '产品到货时间'],
                              gf_text.get(0.0, 40.0).strip())
        next_stage()

    btn_gen = tk.Button(window, text='信息确认完成，进入下一阶段。', command=textGen)

    def xxhtWindow():
        info_window = tk.Tk()
        info_window.title('销售合同添加')
        info_window.config(background='Lavender')

        info_window.geometry('1280x590')  # 这里的乘是小x
        elem_list = []

        def rendering():
            for row, lin_list in enumerate(elem_list, start=1):
                for col, elem in enumerate(lin_list):
                    elem.grid(row=row, column=col)

        def xxhtDel(i):
            for j in range(i, len(elem_list) - 1):
                elem_list[j][0].config(text='销售合同{}产品：'.format(j + 1))
                elem_list[j][1].delete(0.0, "end")
                elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                elem_list[j][2].config(text='销售合同{}客户：'.format(j + 1))
                elem_list[j][3].delete(0.0, "end")
                elem_list[j][3].insert(0.0, elem_list[j + 1][3].get(0.0, 2.0).strip())
                elem_list[j][4].config(text='销售合同{}签订日期：'.format(j + 1))
                elem_list[j][5].delete(0.0, "end")
                elem_list[j][5].insert(0.0, elem_list[j + 1][5].get(0.0, 2.0).strip())
                elem_list[j][6].config(text='销售合同{}编号：'.format(j + 1))
                elem_list[j][7].delete(0.0, "end")
                elem_list[j][7].insert(0.0, elem_list[j + 1][7].get(0.0, 2.0).strip())
                elem_list[j][8].config(text='销售合同{}评审时间：'.format(j + 1))
                elem_list[j][9].delete(0.0, "end")
                elem_list[j][9].insert(0.0, elem_list[j + 1][9].get(0.0, 2.0).strip())
            for j in range(len(elem_list[-1])):
                elem_list[-1][j].destroy()
            del elem_list[-1]
            rendering()

        def xxhtAdd(window, xxht_i, infos):
            line_list = []
            xxhtcp_L = Label(window, text='销售合同{}产品：'.format(xxht_i), bg='Lavender')
            xxhtcp = Text(window, height=1, width=18, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                xxhtcp.insert(0.0, infos[0])
            line_list.append(xxhtcp_L)
            line_list.append(xxhtcp)

            xxhtkh_L = Label(window, text='销售合同{}客户：'.format(xxht_i), bg='Lavender')
            xxhtkh = Text(window, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                xxhtkh.insert(0.0, infos[1])
            line_list.append(xxhtkh_L)
            line_list.append(xxhtkh)

            xxhtqd_L = Label(window, text='销售合同{}签订日期：'.format(xxht_i), bg='Lavender')
            xxhtqd = Text(window, height=1, width=10, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                xxhtqd.insert(0.0, infos[2])
            line_list.append(xxhtqd_L)
            line_list.append(xxhtqd)

            xxhtbh_L = Label(window, text='销售合同{}编号：'.format(xxht_i), bg='Lavender')
            xxhtbh = Text(window, height=1, width=8, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                xxhtbh.insert(0.0, infos[3])
            line_list.append(xxhtbh_L)
            line_list.append(xxhtbh)

            xxhtps_L = Label(window, text='销售合同{}评审时间：'.format(xxht_i), bg='Lavender')
            xxhtps = Text(window, height=1, width=10, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                xxhtps.insert(0.0, infos[4])
            line_list.append(xxhtps_L)
            line_list.append(xxhtps)

            btn_del = Button(info_window, text='删除该合同信息', command=lambda: xxhtDel(xxht_i - 1))
            line_list.append(btn_del)

            elem_list.append(line_list)

            rendering()

        def xxhtDone():
            infos = ''
            for row, lin_list in enumerate(elem_list):
                for col, elem in enumerate(lin_list):
                    if col % 2 == 0:
                        continue
                    infos += elem.get(0.0, 2.0).strip()
                    infos += ','
                infos = infos[:-1]
                infos += '\n'
            xxht_info[0] = infos
            xxht_text.insert(0.0, infos)
            info_window.destroy()

        infos = xxht_info[0].split('\n')
        for i, info in enumerate(infos, start=1):
            if info == '':
                continue
            xxhtAdd(info_window, i, info.split(','))

        btn_gen = tk.Button(info_window, text='新增合同信息。',
                            command=lambda: xxhtAdd(info_window, len(elem_list) + 1, []))
        btn_done = tk.Button(info_window, text='信息确认完成。', command=lambda: xxhtDone())

        btn_gen.grid(row=0, column=0, columnspan=5)
        btn_done.grid(row=0, column=6, columnspan=5)

        info_window.mainloop()

    def gfWindow():
        info_window = tk.Tk()
        info_window.title('供方信息添加')
        info_window.config(background='Lavender')

        info_window.geometry('1280x590')  # 这里的乘是小x
        elem_list = []

        def rendering():
            for row, lin_list in enumerate(elem_list, start=1):
                for col, elem in enumerate(lin_list):
                    elem.grid(row=row, column=col)

        def gfDel(i):
            for j in range(i, len(elem_list) - 1):
                elem_list[j][0].config(text='供方{}名称：'.format(j + 1))
                elem_list[j][1].delete(0.0, "end")
                elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                elem_list[j][2].config(text='供方{}地址：'.format(j + 1))
                elem_list[j][3].delete(0.0, "end")
                elem_list[j][3].insert(0.0, elem_list[j + 1][3].get(0.0, 2.0).strip())
                elem_list[j][4].config(text='供方{}所有产品：'.format(j + 1))
                elem_list[j][5].delete(0.0, "end")
                elem_list[j][5].insert(0.0, elem_list[j + 1][5].get(0.0, 2.0).strip())
            for j in range(len(elem_list[-1])):
                elem_list[-1][j].destroy()
            del elem_list[-1]
            rendering()

        def gfAdd(window, gf_i, infos):
            line_list = []
            gfcp_L = Label(window, text='供方{}名称：'.format(gf_i), bg='Lavender')
            gfcp = Text(window, height=1, width=18, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                gfcp.insert(0.0, infos[0])
            line_list.append(gfcp_L)
            line_list.append(gfcp)

            gfkh_L = Label(window, text='供方{}地址：'.format(gf_i), bg='Lavender')
            gfkh = Text(window, height=1, width=30, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                gfkh.insert(0.0, infos[1])
            line_list.append(gfkh_L)
            line_list.append(gfkh)

            gfqd_L = Label(window, text='供方{}所有产品：'.format(gf_i), bg='Lavender')
            gfqd = Text(window, height=1, width=60, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                gfqd.insert(0.0, infos[2])
            line_list.append(gfqd_L)
            line_list.append(gfqd)

            btn_del = Button(info_window, text='删除该供方信息', command=lambda: gfDel(gf_i - 1))
            line_list.append(btn_del)

            elem_list.append(line_list)

            rendering()

        def gfDone():
            infos = ''
            for row, lin_list in enumerate(elem_list):
                for col, elem in enumerate(lin_list):
                    if col % 2 == 0:
                        continue
                    infos += elem.get(0.0, 2.0).strip()
                    infos += ','
                infos = infos[:-1]
                infos += '\n'
            gf_info[0] = infos
            gf_text.insert(0.0, infos)
            info_window.destroy()

        infos = gf_info[0].split('\n')
        for i, info in enumerate(infos, start=1):
            if info == '':
                continue
            gfAdd(info_window, i, info.split(','))

        btn_gen = tk.Button(info_window, text='新增供方信息。',
                            command=lambda: gfAdd(info_window, len(elem_list) + 1, []))
        btn_done = tk.Button(info_window, text='信息确认完成。', command=lambda: gfDone())

        btn_gen.grid(row=0, column=0, columnspan=5)
        btn_done.grid(row=0, column=6, columnspan=5)

        info_window.mainloop()

    def cgcpWindow():
        info_window = tk.Tk()
        info_window.title('采购产品添加')
        info_window.config(background='Lavender')

        info_window.geometry('1280x590')  # 这里的乘是小x
        elem_list = []

        def rendering():
            for row, lin_list in enumerate(elem_list, start=1):
                for col, elem in enumerate(lin_list):
                    elem.grid(row=row, column=col)

        def init(infos):
            for i, info in enumerate(infos, start=1):
                if info == '':
                    continue
                cgcpAdd(info_window, i, info.split(','))

        def cgcpDel(i):
            for j in range(i, len(elem_list) - 1):
                elem_list[j][0].config(text='采购{}产品：'.format(j + 1))
                elem_list[j][1].delete(0.0, "end")
                elem_list[j][1].insert(0.0, elem_list[j + 1][1].get(0.0, 2.0).strip())
                elem_list[j][2].config(text='采购{}产品规格型号：'.format(j + 1))
                elem_list[j][3].delete(0.0, "end")
                elem_list[j][3].insert(0.0, elem_list[j + 1][3].get(0.0, 2.0).strip())
                elem_list[j][4].config(text='采购{}产品供方：'.format(j + 1))
                elem_list[j][5].delete(0.0, "end")
                elem_list[j][5].insert(0.0, elem_list[j + 1][5].get(0.0, 2.0).strip())
                elem_list[j][6].config(text='采购{}产品数量：'.format(j + 1))
                elem_list[j][7].delete(0.0, "end")
                elem_list[j][7].insert(0.0, elem_list[j + 1][7].get(0.0, 2.0).strip())
                elem_list[j][8].config(text='采购{}时间：'.format(j + 1))
                elem_list[j][9].delete(0.0, "end")
                elem_list[j][9].insert(0.0, elem_list[j + 1][9].get(0.0, 2.0).strip())
                elem_list[j][10].config(text='采购{}产品到货时间：'.format(j + 1))
                elem_list[j][11].delete(0.0, "end")
                elem_list[j][11].insert(0.0, elem_list[j + 1][11].get(0.0, 2.0).strip())
                # elem_list[j][12].destroy()
                # del elem_list[j][12]
                # elem_list[j].append(Button(info_window, text='删除该采购信息{}'.format(j), command=lambda:cgcpDel(j)))
            for j in range(len(elem_list[-1])):
                elem_list[-1][j].destroy()
            del elem_list[-1]
            rendering()

        def cgcpAdd(window, cgcp_i, infos):
            line_list = []
            cgcpcp_L = Label(window, text='采购{}产品：'.format(cgcp_i), bg='Lavender')
            cgcpcp = Text(window, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                cgcpcp.insert(0.0, infos[0])
            line_list.append(cgcpcp_L)
            line_list.append(cgcpcp)

            cgcpkh_L = Label(window, text='采购{}产品规格型号：'.format(cgcp_i), bg='Lavender')
            cgcpkh = Text(window, height=1, width=8, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                cgcpkh.insert(0.0, infos[1])
            line_list.append(cgcpkh_L)
            line_list.append(cgcpkh)

            cgcpqd_L = Label(window, text='采购{}产品供方：'.format(cgcp_i), bg='Lavender')
            cgcpqd = Text(window, height=1, width=15, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                cgcpqd.insert(0.0, infos[2])
            line_list.append(cgcpqd_L)
            line_list.append(cgcpqd)

            cgcpsl_L = Label(window, text='采购{}产品数量：'.format(cgcp_i), bg='Lavender')
            cgcpsl = Text(window, height=1, width=8, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                cgcpqd.insert(0.0, infos[3])
            line_list.append(cgcpsl_L)
            line_list.append(cgcpsl)

            cgcpsj_L = Label(window, text='采购{}时间：'.format(cgcp_i), bg='Lavender')
            cgcpsj = Text(window, height=1, width=10, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                cgcpqd.insert(0.0, infos[4])
            line_list.append(cgcpsj_L)
            line_list.append(cgcpsj)

            cgcpdhsl_L = Label(window, text='采购{}产品到货时间：'.format(cgcp_i), bg='Lavender')
            cgcpdhsl = Text(window, height=1, width=10, relief=RAISED, highlightcolor='black', highlightthickness=1)
            if infos != []:
                cgcpqd.insert(0.0, infos[5])
            line_list.append(cgcpdhsl_L)
            line_list.append(cgcpdhsl)

            btn_del = Button(info_window, text='删除该采购信息', command=lambda: [cgcpDel(cgcp_i - 1)])
            # cgcpcp_L.destroy(), cgcpcp.destroy(), cgcpkh_L.destroy(),
            # cgcpkh.destroy(), cgcpqd_L.destroy(), cgcpqd.destroy(),
            # cgcpsl_L.destroy(), cgcpsl.destroy(), cgcpsj_L.destroy(),
            # cgcpsj.destroy(), cgcpdhsl_L.destroy(), cgcpdhsl.destroy(),
            line_list.append(btn_del)

            elem_list.append(line_list)

            rendering()

        def cgcpDone():
            infos = ''
            for row, lin_list in enumerate(elem_list):
                for col, elem in enumerate(lin_list):
                    if col % 2 == 0:
                        continue
                    infos += elem.get(0.0, 2.0).strip()
                    infos += ','
                infos = infos[:-1]
                infos += '\n'
            cgcp_info[0] = infos
            cgcp_text.insert(0.0, infos)
            info_window.destroy()

        infos = cgcp_info[0].split('\n')
        init(infos)

        btn_gen = tk.Button(info_window, text='新增采购信息。',
                            command=lambda: cgcpAdd(info_window, len(elem_list) + 1, []))
        btn_done = tk.Button(info_window, text='信息确认完成。', command=lambda: cgcpDone())

        btn_gen.grid(row=0, column=0, columnspan=5)
        btn_done.grid(row=0, column=6, columnspan=5)

        info_window.mainloop()

    jlnf_L.grid(row=0, column=0)
    jlnf.grid(row=0, column=1, columnspan=2)

    ybjlrq_L.grid(row=0, column=3)
    ybjlrq.grid(row=0, column=4, columnspan=2)

    peixun1.grid(row=1, column=0)
    peixun1C1.grid(row=1, column=1)
    peixun1C2.grid(row=1, column=2)

    peixun2.grid(row=1, column=3)
    peixun2C1.grid(row=1, column=4)
    peixun2C2.grid(row=1, column=5)

    peixun3.grid(row=1, column=6)
    peixun3C1.grid(row=1, column=7)
    peixun3C2.grid(row=1, column=8)

    peixun4.grid(row=2, column=0)
    peixun4C1.grid(row=2, column=1)
    peixun4C2.grid(row=2, column=2)

    peixun5.grid(row=2, column=3)
    peixun5C1.grid(row=2, column=4)
    peixun5C2.grid(row=2, column=5)

    peixun6.grid(row=2, column=6)
    peixun6C1.grid(row=2, column=7)
    peixun6C2.grid(row=2, column=8)

    peixun7.grid(row=3, column=0)
    peixun7C1.grid(row=3, column=1)
    peixun7C2.grid(row=3, column=2)

    peixun8.grid(row=3, column=3)
    peixun8C1.grid(row=3, column=4)
    peixun8C2.grid(row=3, column=5)

    peixun9.grid(row=3, column=6)
    peixun9C1.grid(row=3, column=7)
    peixun9C2.grid(row=3, column=8)

    peixun10.grid(row=4, column=0)
    peixun10C1.grid(row=4, column=1)
    peixun10C2.grid(row=4, column=2)

    peixun11.grid(row=4, column=3)
    peixun11C1.grid(row=4, column=4)
    peixun11C2.grid(row=4, column=5)

    peixun12.grid(row=4, column=6)
    peixun12C1.grid(row=4, column=7)
    peixun12C2.grid(row=4, column=8)

    nsypxrq_L.grid(row=5, column=0)
    nsypxrq.grid(row=5, column=1, columnspan=2)

    nsjhzdrq_L.grid(row=5, column=3)
    nsjhzdrq.grid(row=5, column=4, columnspan=2)

    nsksrq_L.grid(row=6, column=0)
    nsksrq.grid(row=6, column=1, columnspan=2)

    nsjsrq_L.grid(row=6, column=3)
    nsjsrq.grid(row=6, column=4, columnspan=2)

    nszgwcrq_L.grid(row=6, column=6)
    nszgwcrq.grid(row=6, column=7, columnspan=2)

    q713.grid(row=7, column=0)
    q713C1.grid(row=7, column=1)
    q713C2.grid(row=7, column=2)

    q851.grid(row=7, column=3)
    q851C1.grid(row=7, column=4)
    q851C2.grid(row=7, column=5)

    q62.grid(row=7, column=6)
    q62C1.grid(row=7, column=7)
    q62C2.grid(row=7, column=8)

    gpjhzdrq_L.grid(row=8, column=0)
    gpjhzdrq.grid(row=8, column=1, columnspan=2)

    gprq_L.grid(row=8, column=3)
    gprq.grid(row=8, column=4, columnspan=2)

    gpbgrq_L.grid(row=8, column=6)
    gpbgrq.grid(row=8, column=7, columnspan=2)

    jqscjc.grid(row=9, column=0)
    jqscjcC1.grid(row=9, column=1)
    jqscjcC2.grid(row=9, column=2)

    jqysjs.grid(row=9, column=3)
    jqysjsC1.grid(row=9, column=4)
    jqysjsC2.grid(row=9, column=5)

    jqzp.grid(row=9, column=6)
    jqzpC1.grid(row=9, column=7)
    jqzpC2.grid(row=9, column=8)

    gpgjwcsj_L.grid(row=10, column=0)
    gpgjwcsj.grid(row=10, column=1, columnspan=2)

    syndgprq_L.grid(row=10, column=3)
    syndgprq.grid(row=10, column=4, columnspan=2)

    syndgpgjrq_L.grid(row=10, column=6)
    syndgpgjrq.grid(row=10, column=7, columnspan=2)

    syndjqscjc.grid(row=11, column=0)
    syndjqscjcC1.grid(row=11, column=1)
    syndjqscjcC2.grid(row=11, column=2)

    syndjqysjs.grid(row=11, column=3)
    syndjqysjsC1.grid(row=11, column=4)
    syndjqysjsC2.grid(row=11, column=5)

    syndjqzp.grid(row=11, column=6)
    syndjqzpC1.grid(row=11, column=7)
    syndjqzpC2.grid(row=11, column=8)

    xxhtwin_L.grid(row=12, column=0, rowspan=2, sticky='s')
    btn_xxht.grid(row=14, column=0, rowspan=2, sticky='n')
    xxht_text.grid(row=12, column=1, rowspan=4, columnspan=8, pady=(5, 10))

    myddcrq_L.grid(row=16, column=0)
    myddcrq.grid(row=16, column=1, columnspan=2)

    myddcsl_L.grid(row=16, column=3)
    myddcsl.grid(row=16, column=4, columnspan=2)

    myddcpj_L.grid(row=16, column=6)
    myddcpj.grid(row=16, column=7, columnspan=2)

    myddc1_L.grid(row=17, column=0)
    myddc1.grid(row=17, column=1, columnspan=2)

    myddc2_L.grid(row=17, column=3)
    myddc2.grid(row=17, column=4, columnspan=2)

    myddc3_L.grid(row=17, column=6)
    myddc3.grid(row=17, column=7, columnspan=2)

    myddc4_L.grid(row=18, column=0)
    myddc4.grid(row=18, column=1, columnspan=2)

    myddc5_L.grid(row=18, column=3)
    myddc5.grid(row=18, column=4, columnspan=2)

    myddc6_L.grid(row=18, column=6)
    myddc6.grid(row=18, column=7, columnspan=2)

    myddc7_L.grid(row=19, column=0)
    myddc7.grid(row=19, column=1, columnspan=2)

    myddc8_L.grid(row=19, column=3)
    myddc8.grid(row=19, column=4, columnspan=2)

    gfwin_L.grid(row=20, column=0, rowspan=2, sticky='s')
    btn_gf.grid(row=22, column=0, rowspan=2, sticky='n')
    gf_text.grid(row=20, column=1, rowspan=4, columnspan=8, pady=(5, 10))

    cgcpwin_L.grid(row=24, column=0, rowspan=2, sticky='s')
    btn_cgcp.grid(row=26, column=0, rowspan=2, sticky='n')
    cgcp_text.grid(row=24, column=1, rowspan=4, columnspan=8, pady=(5, 10))

    btn_gen.grid(row=29, column=4)

    window.mainloop()


# 第四层界面
class window4_1():
    # 适用于认证范围为SC/ZZ/JJSC且认证项目为QS/QES'
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

        for F in (cpgxPage, cpczPage, cpxxPage, qtxxPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(cpgxPage)
        window.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处

    # def put_var_list_into_map(self, edit_text, key):
    #     if isinstance(key, list):

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
        self.add_cp_info_to_dict(self.frames[cpgxPage].cpgx1_text.get(0.0, 20.0).strip(), 1, "工序")
        self.add_cp_info_to_dict(self.frames[cpgxPage].cpgx2_text.get(0.0, 20.0).strip(), 2, "工序")
        self.add_cp_info_to_dict(self.frames[cpgxPage].cpgx3_text.get(0.0, 20.0).strip(), 3, "工序")
        self.add_cp_info_to_dict(self.frames[cpgxPage].cpgx4_text.get(0.0, 20.0).strip(), 4, "工序")
        self.add_cp_info_to_dict(self.frames[cpgxPage].cpgx5_text.get(0.0, 20.0).strip(), 5, "工序")

        # 将修改五个产品的操作工的信息添加到字典里
        self.add_cp_info_to_dict(self.frames[cpczPage].cpgx1_text.get(0.0, 20.0).strip(), 1, "操作工")
        self.add_cp_info_to_dict(self.frames[cpczPage].cpgx2_text.get(0.0, 20.0).strip(), 2, "操作工")
        self.add_cp_info_to_dict(self.frames[cpczPage].cpgx3_text.get(0.0, 20.0).strip(), 3, "操作工")
        self.add_cp_info_to_dict(self.frames[cpczPage].cpgx4_text.get(0.0, 20.0).strip(), 4, "操作工")
        self.add_cp_info_to_dict(self.frames[cpczPage].cpgx5_text.get(0.0, 20.0).strip(), 5, "操作工")

        # 将修改五个产品的操作信息的信息添加到字典里
        self.add_cpxx_to_dict(self.frames[cpxxPage].cpgx1_text.get(0.0, 20.0).strip(), 1)
        self.add_cpxx_to_dict(self.frames[cpxxPage].cpgx2_text.get(0.0, 20.0).strip(), 2)
        self.add_cpxx_to_dict(self.frames[cpxxPage].cpgx3_text.get(0.0, 20.0).strip(), 3)
        self.add_cpxx_to_dict(self.frames[cpxxPage].cpgx4_text.get(0.0, 20.0).strip(), 4)
        self.add_cpxx_to_dict(self.frames[cpxxPage].cpgx5_text.get(0.0, 20.0).strip(), 5)

        # 第四个界面信息收集
        f_qtxx = self.frames[qtxxPage]
        self.add_item_to_dict(f_qtxx.jyy1, '检验员1')
        self.add_item_to_dict(f_qtxx.scbry1, '生产部人员1')
        self.add_item_to_dict(f_qtxx.scbry2, '生产部人员2')
        self.add_item_to_dict(f_qtxx.scbry3, '生产部人员3')
        self.add_radio_res_to_dict(f_qtxx.tsgcjbV, '特殊过程搅拌', f_qtxx.tsgcjb, '特殊过程搅拌搅拌工')
        self.add_radio_res_to_dict(f_qtxx.tsgcbmjshV, '特殊过程薄膜金属化', f_qtxx.tsgcbmjsh,
                                   '特殊过程薄膜金属化操作工')
        self.add_radio_res_to_dict(f_qtxx.tsgchjV, '特殊过程焊接', f_qtxx.tsgchj, '特殊过程焊接操作工')
        self.add_radio_res_to_dict(f_qtxx.tsgchhV, '特殊过程混合', f_qtxx.tsgchh, '特殊过程混合操作工')
        self.add_radio_res_to_dict(f_qtxx.tsgcjcV, '特殊过程挤出', f_qtxx.tsgcjc, '特殊过程挤出操作工')
        self.add_item_to_dict(f_qtxx.sjaqjyspxr1, '三级安全教育受培训人1')
        self.add_item_to_dict(f_qtxx.sjaqjyspxr2, '三级安全教育受培训人2')
        self.add_item_to_dict(f_qtxx.sjaqjyspxr3, '三级安全教育受培训人3')
        self.add_item_to_dict(f_qtxx.sjaqjyrq1, '三级安全教育第一天日期')
        self.add_item_to_dict(f_qtxx.sjaqjyrq2, '三级安全教育第二天日期')
        self.add_item_to_dict(f_qtxx.sjaqjyrq3, '三级安全教育第三天日期')
        self.add_item_to_dict(f_qtxx.sjaqjybzpxr3, '三级安全教育班组培训人')
        if f_qtxx.kyjV.get() == 0:
            self.info_dic['__是否有空压机__'] = '否'
        else:
            self.info_dic['__是否有空压机__'] = '是'

        print(self.info_dic)
        gen_yaml(self.info_dic)


class cpgxPage(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: [root.show_frame(cpgxPage)])
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        self.cpgx1_text = Text(self, width=120, heigh=4, state=DISABLED)
        self.cpgx1win_L = Label(self, text='产品1工序：', bg='Lavender')
        self.btn_cpgx1 = tk.Button(self, text='修改产品1工序。', command=lambda: cpgx1self())  # 解析
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

        cpgx2_text = Text(self, width=120, heigh=4)
        cpgx2win_L = Label(self, text='产品2工序：', bg='Lavender')
        btn_cpgx2 = tk.Button(self, text='修改产品2工序。', command=lambda: cpgx2self())
        cpgx2_info = [cpgx2_text.get(0.0, 40.0)]

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
                cpgx2_text.insert(0.0, infos)
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

        cpgx3_text = Text(self, width=120, heigh=4)
        cpgx3win_L = Label(self, text='产品3工序：', bg='Lavender')
        btn_cpgx3 = tk.Button(self, text='修改产品3工序。', command=lambda: cpgx3self())
        cpgx3_info = [cpgx3_text.get(0.0, 40.0)]

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
                cpgx3_text.insert(0.0, infos)
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

        cpgx4_text = Text(self, width=120, heigh=4)
        cpgx4win_L = Label(self, text='产品4工序：', bg='Lavender')
        btn_cpgx4 = tk.Button(self, text='修改产品4工序。', command=lambda: cpgx4self())
        cpgx4_info = [cpgx4_text.get(0.0, 40.0)]

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
                cpgx4_text.insert(0.0, infos)
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

        cpgx5_text = Text(self, width=120, heigh=4)
        cpgx5win_L = Label(self, text='产品5工序：', bg='Lavender')
        btn_cpgx5 = tk.Button(self, text='修改产品5工序。', command=lambda: cpgx5self())
        cpgx5_info = [cpgx5_text.get(0.0, 40.0)]

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
                cpgx5_text.insert(0.0, infos)
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

        cpgx2win_L.grid(row=5, column=0, rowspan=2)
        btn_cpgx2.grid(row=7, column=0, rowspan=2)
        cpgx2_text.grid(row=5, column=1, rowspan=4, pady=5, columnspan=4)

        cpgx3win_L.grid(row=9, column=0, rowspan=2)
        btn_cpgx3.grid(row=11, column=0, rowspan=2)
        cpgx3_text.grid(row=9, column=1, rowspan=4, pady=5, columnspan=4)

        cpgx4win_L.grid(row=13, column=0, rowspan=2)
        btn_cpgx4.grid(row=15, column=0, rowspan=2)
        cpgx4_text.grid(row=13, column=1, rowspan=4, pady=5, columnspan=4)

        cpgx5win_L.grid(row=17, column=0, rowspan=2)
        btn_cpgx5.grid(row=19, column=0, rowspan=2)
        cpgx5_text.grid(row=17, column=1, rowspan=4, pady=5, columnspan=4)


class cpczPage(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: [root.show_frame(cpgxPage)])
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
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

        cpgx2_text = Text(self, width=120, heigh=4)
        cpgx2win_L = Label(self, text='产品2操作工：', bg='Lavender')
        btn_cpgx2 = tk.Button(self, text='修改产品2操作工。', command=lambda: cpgx2self())
        cpgx2_info = [cpgx2_text.get(0.0, 40.0)]

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
                cpgx2_text.insert(0.0, infos)
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

        cpgx3_text = Text(self, width=120, heigh=4)
        cpgx3win_L = Label(self, text='产品3操作工：', bg='Lavender')
        btn_cpgx3 = tk.Button(self, text='修改产品3操作工。', command=lambda: cpgx3self())
        cpgx3_info = [cpgx3_text.get(0.0, 40.0)]

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
                cpgx3_text.insert(0.0, infos)
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

        cpgx4_text = Text(self, width=120, heigh=4)
        cpgx4win_L = Label(self, text='产品4操作工：', bg='Lavender')
        btn_cpgx4 = tk.Button(self, text='修改产品4操作工。', command=lambda: cpgx4self())
        cpgx4_info = [cpgx4_text.get(0.0, 40.0)]

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
                cpgx4_text.insert(0.0, infos)
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

        cpgx5_text = Text(self, width=120, heigh=4)
        cpgx5win_L = Label(self, text='产品5操作工：', bg='Lavender')
        btn_cpgx5 = tk.Button(self, text='修改产品5操作工。', command=lambda: cpgx5self())
        cpgx5_info = [cpgx5_text.get(0.0, 40.0)]

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
                cpgx5_text.insert(0.0, infos)
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

        cpgx2win_L.grid(row=5, column=0, rowspan=2)
        btn_cpgx2.grid(row=7, column=0, rowspan=2)
        cpgx2_text.grid(row=5, column=1, rowspan=4, pady=5, columnspan=4)

        cpgx3win_L.grid(row=9, column=0, rowspan=2)
        btn_cpgx3.grid(row=11, column=0, rowspan=2)
        cpgx3_text.grid(row=9, column=1, rowspan=4, pady=5, columnspan=4)

        cpgx4win_L.grid(row=13, column=0, rowspan=2)
        btn_cpgx4.grid(row=15, column=0, rowspan=2)
        cpgx4_text.grid(row=13, column=1, rowspan=4, pady=5, columnspan=4)

        cpgx5win_L.grid(row=17, column=0, rowspan=2)
        btn_cpgx5.grid(row=19, column=0, rowspan=2)
        cpgx5_text.grid(row=17, column=1, rowspan=4, pady=5, columnspan=4)


class cpxxPage(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: [root.show_frame(cpgxPage)])
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
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

        cpgx2_text = Text(self, width=120, heigh=4)
        cpgx2win_L = Label(self, text='产品2信息：', bg='Lavender')
        btn_cpgx2 = tk.Button(self, text='修改产品2信息。', command=lambda: cpgx2self())

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

            def cpgx1Add(self, cpgx1_i, infos):
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

        cpgx3_text = Text(self, width=120, heigh=4)
        cpgx3win_L = Label(self, text='产品3信息：', bg='Lavender')
        btn_cpgx3 = tk.Button(self, text='修改产品3信息。', command=lambda: cpgx3self())
        cpgx3_info = [cpgx3_text.get(0.0, 40.0)]

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

        cpgx4_text = Text(self, width=120, heigh=4)
        cpgx4win_L = Label(self, text='产品4信息：', bg='Lavender')
        btn_cpgx4 = tk.Button(self, text='修改产品4信息。', command=lambda: cpgx4self())
        cpgx4_info = [cpgx4_text.get(0.0, 40.0)]

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

        cpgx5_text = Text(self, width=120, heigh=4)
        cpgx5win_L = Label(self, text='产品5信息：', bg='Lavender')
        btn_cpgx5 = tk.Button(self, text='修改产品5信息。', command=lambda: cpgx5self())
        cpgx5_info = [cpgx5_text.get(0.0, 40.0)]

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

        cpgx2win_L.grid(row=5, column=0, rowspan=2)
        btn_cpgx2.grid(row=7, column=0, rowspan=2)
        cpgx2_text.grid(row=5, column=1, rowspan=4, pady=5, columnspan=4)

        cpgx3win_L.grid(row=9, column=0, rowspan=2)
        btn_cpgx3.grid(row=11, column=0, rowspan=2)
        cpgx3_text.grid(row=9, column=1, rowspan=4, pady=5, columnspan=4)

        cpgx4win_L.grid(row=13, column=0, rowspan=2)
        btn_cpgx4.grid(row=15, column=0, rowspan=2)
        cpgx4_text.grid(row=13, column=1, rowspan=4, pady=5, columnspan=4)

        cpgx5win_L.grid(row=17, column=0, rowspan=2)
        btn_cpgx5.grid(row=19, column=0, rowspan=2)
        cpgx5_text.grid(row=17, column=1, rowspan=4, pady=5, columnspan=4)


class qtxxPage(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        super().__init__(parent)
        self.config(bg='Lavender')
        btncpgx = tk.Button(self, text='修改产品工序', command=lambda: root.show_frame(cpgxPage))
        btncpxx = tk.Button(self, text='修改产品信息', command=lambda: root.show_frame(cpxxPage))
        btncpcz = tk.Button(self, text='修改产品操作工', command=lambda: root.show_frame(cpczPage))
        btnqtxx = tk.Button(self, text='修改其他信息', command=lambda: root.show_frame(qtxxPage))
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        jyy1_L = Label(self, text='检验员1：', bg='Lavender')
        jyy1 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        scbry1_L = Label(self, text='生产部人员1：', bg='Lavender')
        scbry1 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        scbry2_L = Label(self, text='生产部人员2：', bg='Lavender')
        scbry2 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        scbry3_L = Label(self, text='生产部人员3：', bg='Lavender')
        scbry3 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        tsgcjbV = tk.IntVar(master=self)

        def tsgcjbbool():
            if tsgcjbV.get() == 0:
                tsgcjb.config(state=DISABLED)
            else:
                tsgcjb.config(state=NORMAL)

        tsgcjbC1 = tk.Radiobutton(self, text="有搅拌过程", variable=tsgcjbV, value=1, command=tsgcjbbool, bg='Lavender')
        tsgcjbC2 = tk.Radiobutton(self, text="无搅拌过程", variable=tsgcjbV, value=0, command=tsgcjbbool, bg='Lavender')
        tsgcjb_L = Label(self, text='特殊过程搅拌搅拌工：', bg='Lavender')
        tsgcjb = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgcjbbool()

        tsgcbmjshV = tk.IntVar(master=self)

        def tsgcbmjshbool():
            if tsgcbmjshV.get() == 0:
                tsgcbmjsh.config(state=DISABLED)
            else:
                tsgcbmjsh.config(state=NORMAL)

        tsgcbmjshC1 = tk.Radiobutton(self, text="有薄膜金属化过程", variable=tsgcbmjshV, value=1, command=tsgcbmjshbool,
                                     bg='Lavender')
        tsgcbmjshC2 = tk.Radiobutton(self, text="无薄膜金属化过程", variable=tsgcbmjshV, value=0, command=tsgcbmjshbool,
                                     bg='Lavender')
        tsgcbmjsh_L = Label(self, text='特殊过程薄膜金属化操作工：', bg='Lavender')
        tsgcbmjsh = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgcbmjshbool()

        tsgchjV = tk.IntVar(master=self)

        def tsgchjbool():
            if tsgchjV.get() == 0:
                tsgchj.config(state=DISABLED)
            else:
                tsgchj.config(state=NORMAL)

        tsgchjC1 = tk.Radiobutton(self, text="有焊接过程", variable=tsgchjV, value=1, command=tsgchjbool, bg='Lavender')
        tsgchjC2 = tk.Radiobutton(self, text="无焊接过程", variable=tsgchjV, value=0, command=tsgchjbool, bg='Lavender')
        tsgchj_L = Label(self, text='特殊过程焊接操作工：', bg='Lavender')
        tsgchj = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgchjbool()

        tsgchhV = tk.IntVar(master=self)

        def tsgchhbool():
            if tsgchhV.get() == 0:
                tsgchh.config(state=DISABLED)
            else:
                tsgchh.config(state=NORMAL)

        tsgchhC1 = tk.Radiobutton(self, text="有混合过程", variable=tsgchhV, value=1, command=tsgchhbool, bg='Lavender')
        tsgchhC2 = tk.Radiobutton(self, text="无混合过程", variable=tsgchhV, value=0, command=tsgchhbool, bg='Lavender')
        tsgchh_L = Label(self, text='特殊过程混合操作工：', bg='Lavender')
        tsgchh = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgchhbool()

        tsgcjcV = tk.IntVar(master=self)

        def tsgcjcbool():
            if tsgcjcV.get() == 0:
                tsgcjc.config(state=DISABLED)
            else:
                tsgcjc.config(state=NORMAL)

        tsgcjcC1 = tk.Radiobutton(self, text="有挤出过程", variable=tsgcjcV, value=1, command=tsgcjcbool, bg='Lavender')
        tsgcjcC2 = tk.Radiobutton(self, text="无挤出过程", variable=tsgcjcV, value=0, command=tsgcjcbool, bg='Lavender')
        tsgcjc_L = Label(self, text='特殊过程挤出操作工：', bg='Lavender')
        tsgcjc = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgcjcbool()

        sjaqjyspxr1_L = Label(self, text='三级安全教育受培训人1：', bg='Lavender')
        sjaqjyspxr1 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyspxr2_L = Label(self, text='三级安全教育受培训人2：', bg='Lavender')
        sjaqjyspxr2 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyrq1_L = Label(self, text='三级安全教育第一天日期：', bg='Lavender')
        sjaqjyrq1 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyrq2_L = Label(self, text='三级安全教育第二天日期：', bg='Lavender')
        sjaqjyrq2 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyrq3_L = Label(self, text='三级安全教育第三天日期：', bg='Lavender')
        sjaqjyrq3 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjybzpxr3_L = Label(self, text='三级安全教育班组培训人：', bg='Lavender')
        sjaqjybzpxr3 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        kyjV = tk.IntVar(master=self)
        kyjC1 = tk.Radiobutton(self, text="有空压机", variable=kyjV, value=1, bg='Lavender')
        kyjC2 = tk.Radiobutton(self, text="无空压机", variable=kyjV, value=0, bg='Lavender')

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btncpcz.grid(row=0, column=2)
        btnqtxx.grid(row=0, column=3)
        btngen.grid(row=0, column=4)

        jyy1_L.grid(row=1, column=0)
        jyy1.grid(row=1, column=1)

        scbry1_L.grid(row=2, column=0)
        scbry1.grid(row=2, column=1)
        scbry2_L.grid(row=2, column=2)
        scbry2.grid(row=2, column=3)
        scbry3_L.grid(row=2, column=4)
        scbry3.grid(row=2, column=5)

        tsgcjbC1.grid(row=3, column=0)
        tsgcjbC2.grid(row=3, column=1)
        tsgcjb_L.grid(row=3, column=2)
        tsgcjb.grid(row=3, column=3, columnspan=4)

        tsgcbmjshC1.grid(row=4, column=0)
        tsgcbmjshC2.grid(row=4, column=1)
        tsgcbmjsh_L.grid(row=4, column=2)
        tsgcbmjsh.grid(row=4, column=3, columnspan=4)

        tsgchjC1.grid(row=5, column=0)
        tsgchjC2.grid(row=5, column=1)
        tsgchj_L.grid(row=5, column=2)
        tsgchj.grid(row=5, column=3, columnspan=4)

        tsgchhC1.grid(row=6, column=0)
        tsgchhC2.grid(row=6, column=1)
        tsgchh_L.grid(row=6, column=2)
        tsgchh.grid(row=6, column=3, columnspan=4)

        tsgcjcC1.grid(row=7, column=0)
        tsgcjcC2.grid(row=7, column=1)
        tsgcjc_L.grid(row=7, column=2)
        tsgcjc.grid(row=7, column=3, columnspan=4)

        sjaqjyspxr1_L.grid(row=8, column=0)
        sjaqjyspxr1.grid(row=8, column=1)
        sjaqjyspxr2_L.grid(row=8, column=2)
        sjaqjyspxr2.grid(row=8, column=3)

        sjaqjyrq1_L.grid(row=9, column=0)
        sjaqjyrq1.grid(row=9, column=1)
        sjaqjyrq2_L.grid(row=9, column=2)
        sjaqjyrq2.grid(row=9, column=3)
        sjaqjyrq3_L.grid(row=9, column=4)
        sjaqjyrq3.grid(row=9, column=5)

        sjaqjybzpxr3_L.grid(row=10, column=0)
        sjaqjybzpxr3.grid(row=10, column=1)

        kyjC1.grid(row=10, column=2)
        kyjC2.grid(row=10, column=3)


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
        f_qtxx = self.frames[qtxxPage]
        self.add_item_to_dict(f_qtxx.jyy1, '检验员1')
        self.add_item_to_dict(f_qtxx.scbry1, '生产部人员1')
        self.add_item_to_dict(f_qtxx.scbry2, '生产部人员2')
        self.add_item_to_dict(f_qtxx.scbry3, '生产部人员3')
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

        print(self.info_dic)
        gen_yaml(self.info_dic)


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
        cpgx2_info = [cpgx2_text.get(0.0, 40.0)]

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
        cpgx5_info = [cpgx5_text.get(0.0, 40.0)]

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
        cpgx5_info = [cpgx5_text.get(0.0, 40.0)]

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
        jyy1 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        scbry1_L = Label(self, text='生产部人员1：', bg='Lavender')
        scbry1 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        scbry2_L = Label(self, text='生产部人员2：', bg='Lavender')
        scbry2 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        scbry3_L = Label(self, text='生产部人员3：', bg='Lavender')
        scbry3 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        tsgcjbV = tk.IntVar(master=self)

        def tsgcjbbool():
            if tsgcjbV.get() == 0:
                tsgcjb.config(state=DISABLED)
            else:
                tsgcjb.config(state=NORMAL)

        tsgcjbC1 = tk.Radiobutton(self, text="有搅拌过程", variable=tsgcjbV, value=1, command=tsgcjbbool, bg='Lavender')
        tsgcjbC2 = tk.Radiobutton(self, text="无搅拌过程", variable=tsgcjbV, value=0, command=tsgcjbbool, bg='Lavender')
        tsgcjb_L = Label(self, text='特殊过程搅拌搅拌工：', bg='Lavender')
        tsgcjb = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgcjbbool()

        tsgcbmjshV = tk.IntVar(master=self)

        def tsgcbmjshbool():
            if tsgcbmjshV.get() == 0:
                tsgcbmjsh.config(state=DISABLED)
            else:
                tsgcbmjsh.config(state=NORMAL)

        tsgcbmjshC1 = tk.Radiobutton(self, text="有薄膜金属化过程", variable=tsgcbmjshV, value=1, command=tsgcbmjshbool,
                                     bg='Lavender')
        tsgcbmjshC2 = tk.Radiobutton(self, text="无薄膜金属化过程", variable=tsgcbmjshV, value=0, command=tsgcbmjshbool,
                                     bg='Lavender')
        tsgcbmjsh_L = Label(self, text='特殊过程薄膜金属化操作工：', bg='Lavender')
        tsgcbmjsh = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgcbmjshbool()

        tsgchjV = tk.IntVar(master=self)

        def tsgchjbool():
            if tsgchjV.get() == 0:
                tsgchj.config(state=DISABLED)
            else:
                tsgchj.config(state=NORMAL)

        tsgchjC1 = tk.Radiobutton(self, text="有焊接过程", variable=tsgchjV, value=1, command=tsgchjbool, bg='Lavender')
        tsgchjC2 = tk.Radiobutton(self, text="无焊接过程", variable=tsgchjV, value=0, command=tsgchjbool, bg='Lavender')
        tsgchj_L = Label(self, text='特殊过程焊接操作工：', bg='Lavender')
        tsgchj = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgchjbool()

        tsgchhV = tk.IntVar(master=self)

        def tsgchhbool():
            if tsgchhV.get() == 0:
                tsgchh.config(state=DISABLED)
            else:
                tsgchh.config(state=NORMAL)

        tsgchhC1 = tk.Radiobutton(self, text="有混合过程", variable=tsgchhV, value=1, command=tsgchhbool, bg='Lavender')
        tsgchhC2 = tk.Radiobutton(self, text="无混合过程", variable=tsgchhV, value=0, command=tsgchhbool, bg='Lavender')
        tsgchh_L = Label(self, text='特殊过程混合操作工：', bg='Lavender')
        tsgchh = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgchhbool()

        tsgcjcV = tk.IntVar(master=self)

        def tsgcjcbool():
            if tsgcjcV.get() == 0:
                tsgcjc.config(state=DISABLED)
            else:
                tsgcjc.config(state=NORMAL)

        tsgcjcC1 = tk.Radiobutton(self, text="有挤出过程", variable=tsgcjcV, value=1, command=tsgcjcbool, bg='Lavender')
        tsgcjcC2 = tk.Radiobutton(self, text="无挤出过程", variable=tsgcjcV, value=0, command=tsgcjcbool, bg='Lavender')
        tsgcjc_L = Label(self, text='特殊过程挤出操作工：', bg='Lavender')
        tsgcjc = Text(self, height=1, width=40, relief=RAISED, highlightcolor='black', highlightthickness=1)
        tsgcjcbool()

        kyjV = tk.IntVar(master=self)
        kyjC1 = tk.Radiobutton(self, text="有空压机", variable=kyjV, value=1, bg='Lavender')
        kyjC2 = tk.Radiobutton(self, text="无空压机", variable=kyjV, value=0, bg='Lavender')

        btncpgx.grid(row=0, column=0)
        btncpxx.grid(row=0, column=1)
        btncpcz.grid(row=0, column=2)
        btnqtxx.grid(row=0, column=3)
        btngen.grid(row=0, column=4)

        jyy1_L.grid(row=1, column=0)
        jyy1.grid(row=1, column=1)

        scbry1_L.grid(row=2, column=0)
        scbry1.grid(row=2, column=1)
        scbry2_L.grid(row=2, column=2)
        scbry2.grid(row=2, column=3)
        scbry3_L.grid(row=2, column=4)
        scbry3.grid(row=2, column=5)

        tsgcjbC1.grid(row=3, column=0)
        tsgcjbC2.grid(row=3, column=1)
        tsgcjb_L.grid(row=3, column=2)
        tsgcjb.grid(row=3, column=3, columnspan=4)

        tsgcbmjshC1.grid(row=4, column=0)
        tsgcbmjshC2.grid(row=4, column=1)
        tsgcbmjsh_L.grid(row=4, column=2)
        tsgcbmjsh.grid(row=4, column=3, columnspan=4)

        tsgchjC1.grid(row=5, column=0)
        tsgchjC2.grid(row=5, column=1)
        tsgchj_L.grid(row=5, column=2)
        tsgchj.grid(row=5, column=3, columnspan=4)

        tsgchhC1.grid(row=6, column=0)
        tsgchhC2.grid(row=6, column=1)
        tsgchh_L.grid(row=6, column=2)
        tsgchh.grid(row=6, column=3, columnspan=4)

        tsgcjcC1.grid(row=7, column=0)
        tsgcjcC2.grid(row=7, column=1)
        tsgcjc_L.grid(row=7, column=2)
        tsgcjc.grid(row=7, column=3, columnspan=4)

        kyjC1.grid(row=10, column=2)
        kyjC2.grid(row=10, column=3)


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
        f_qtxx = self.frames[qtxxPage]
        self.add_item_to_dict(f_qtxx.sjaqjyspxr1, '三级安全教育受培训人1')
        self.add_item_to_dict(f_qtxx.sjaqjyspxr2, '三级安全教育受培训人2')
        self.add_item_to_dict(f_qtxx.sjaqjyspxr3, '三级安全教育受培训人3')
        self.add_item_to_dict(f_qtxx.sjaqjyrq1, '三级安全教育第一天日期')
        self.add_item_to_dict(f_qtxx.sjaqjyrq2, '三级安全教育第二天日期')
        self.add_item_to_dict(f_qtxx.sjaqjyrq3, '三级安全教育第三天日期')
        self.add_item_to_dict(f_qtxx.sjaqjybzpxr3, '三级安全教育班组培训人')
        if f_qtxx.kyjV.get() == 0:
            self.info_dic['__是否有空压机__'] = '否'
        else:
            self.info_dic['__是否有空压机__'] = '是'
        gen_yaml(self.info_dic)


class qtxxPage_4(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        super().__init__(parent)
        self.config(bg='Lavender')
        btngen = tk.Button(self, text='信息无误开始生成文档！', command=lambda: root.getinfo())

        sjaqjyspxr1_L = Label(self, text='三级安全教育受培训人1：', bg='Lavender')
        sjaqjyspxr1 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyspxr2_L = Label(self, text='三级安全教育受培训人2：', bg='Lavender')
        sjaqjyspxr2 = Text(self, height=1, width=25, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyrq1_L = Label(self, text='三级安全教育第一天日期：', bg='Lavender')
        sjaqjyrq1 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyrq2_L = Label(self, text='三级安全教育第二天日期：', bg='Lavender')
        sjaqjyrq2 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjyrq3_L = Label(self, text='三级安全教育第三天日期：', bg='Lavender')
        sjaqjyrq3 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        sjaqjybzpxr3_L = Label(self, text='三级安全教育班组培训人：', bg='Lavender')
        sjaqjybzpxr3 = Text(self, height=1, width=12, relief=RAISED, highlightcolor='black', highlightthickness=1)

        kyjV = tk.IntVar(master=self)
        kyjC1 = tk.Radiobutton(self, text="有空压机", variable=kyjV, value=1, bg='Lavender')
        kyjC2 = tk.Radiobutton(self, text="无空压机", variable=kyjV, value=0, bg='Lavender')

        btngen.grid(row=0, column=4)

        sjaqjyspxr1_L.grid(row=8, column=0)
        sjaqjyspxr1.grid(row=8, column=1)
        sjaqjyspxr2_L.grid(row=8, column=2)
        sjaqjyspxr2.grid(row=8, column=3)

        sjaqjyrq1_L.grid(row=9, column=0)
        sjaqjyrq1.grid(row=9, column=1)
        sjaqjyrq2_L.grid(row=9, column=2)
        sjaqjyrq2.grid(row=9, column=3)
        sjaqjyrq3_L.grid(row=9, column=4)
        sjaqjyrq3.grid(row=9, column=5)

        sjaqjybzpxr3_L.grid(row=10, column=0)
        sjaqjybzpxr3.grid(row=10, column=1)

        kyjC1.grid(row=10, column=2)
        kyjC2.grid(row=10, column=3)


def gen_yaml(info_dic):
    with open("test.yaml", "w") as f:
        yaml.safe_dump(data=info_dic, stream=f)


mainWindow()
