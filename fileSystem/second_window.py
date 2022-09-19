import tkinter as tk
from tkinter import *




# 第二层界面
from fileSystem.third_window import informCollectWindow


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
            info_dic['__外包过程表述__'] = ' '
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
            info_dic['__外包过程表述__'] = ' '
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
            info_dic['__外包过程表述__'] = ' '
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