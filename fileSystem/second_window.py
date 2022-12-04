import tkinter.messagebox
import threading
from third_window import informCollectWindow
from widgets import EditText, GroupButtonWithText
from temp_storage import *
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import deal_with_file as df


def InfoWindow_1(info_dic, re=False):
    """Q界面"""
    window = tk.Tk()

    # 给窗口的可视化起名字
    if re:
        window.title('监督复评模式')
    else:
        window.title('初审模式')
    window.config(background='Lavender')
    widget_list = []
    # 设定窗口的大小(长 * 宽)
    window.geometry('850x650')  # 这里的乘是小x
    window.resizable(0, 0)

    name = EditText(window, '企业名称')
    name.text_setting(height=1, width=25)
    widget_list.append(name)

    code = EditText(window, '企业代码')
    code.text_setting(height=1, width=25)
    widget_list.append(code)

    version_code = EditText(window, '版本号', default='A/0', replaceable=False)
    version_code.text_setting(height=1, width=12)
    widget_list.append(version_code)

    m = EditText(window, '管理者代表')
    m.text_setting(height=1, width=22)
    widget_list.append(m)

    mx = EditText(window, '最高管理者')
    mx.text_setting(height=1, width=22)
    widget_list.append(mx)

    t = EditText(window, '手册发布实施日期')
    t.text_setting(height=1, width=22)
    widget_list.append(t)

    jianjie = EditText(window, '公司简介')
    jianjie.text_setting(height=2, width=97)
    widget_list.append(jianjie)

    fanwei = EditText(window, '认证范围')
    fanwei.text_setting(height=1, width=97)
    widget_list.append(fanwei)

    waibao = GroupButtonWithText(window, title='公司有无外包过程', pos_opt='公司有外包过程', neg_opt='公司无外包过程',
                                 text_title='外包过程表述', text_default='本公司无外包过程')
    waibao.text.replaceable = False
    widget_list.append(waibao)

    tsguocheng = EditText(window, '特殊过程', default='特殊过程为XX', replaceable=False)
    tsguocheng.text_setting(height=2, width=97)
    widget_list.append(tsguocheng)

    zhijian = EditText(window, '质检部门')
    zhijian.text_setting(height=1, width=22)
    widget_list.append(zhijian)

    zjfuze = EditText(window, '质检负责人')
    zjfuze.text_setting(height=1, width=22)
    widget_list.append(zjfuze)

    zjbmcode = EditText(window, '质检部门代码')
    zjbmcode.text_setting(height=1, width=22)
    widget_list.append(zjbmcode)

    xiaoshou = EditText(window, '销售部门')
    xiaoshou.text_setting(height=1, width=22)
    widget_list.append(xiaoshou)

    xsfuze = EditText(window, '销售负责人')
    xsfuze.text_setting(height=1, width=22)
    widget_list.append(xsfuze)

    xsbmcode = EditText(window, '销售部门代码')
    xsbmcode.text_setting(height=1, width=22)
    widget_list.append(xsbmcode)

    shengchan = EditText(window, '生产部门')
    shengchan.text_setting(height=1, width=22)
    widget_list.append(shengchan)

    scfuze = EditText(window, '生产负责人')
    scfuze.text_setting(height=1, width=22)
    widget_list.append(scfuze)

    scbmcode = EditText(window, '生产部门代码')
    scbmcode.text_setting(height=1, width=22)
    widget_list.append(scbmcode)

    xingzheng = EditText(window, '行政部门')
    xingzheng.text_setting(height=1, width=22)
    widget_list.append(xingzheng)

    xzfuze = EditText(window, '行政负责人')
    xzfuze.text_setting(height=1, width=22)
    widget_list.append(xzfuze)

    xzbmcode = EditText(window, '行政部门代码')
    xzbmcode.text_setting(height=1, width=22)
    widget_list.append(xzbmcode)

    caigou = EditText(window, '采购部门')
    caigou.text_setting(height=1, width=22)
    widget_list.append(caigou)

    cgfuze = EditText(window, '采购负责人')
    cgfuze.text_setting(height=1, width=22)
    widget_list.append(cgfuze)

    cgbmcode = EditText(window, '采购部门代码')
    cgbmcode.text_setting(height=1, width=22)
    widget_list.append(cgbmcode)

    xscaigou = EditText(window, '销售采购部门')
    xscaigou.text_setting(height=1, width=22)
    widget_list.append(xscaigou)

    xscgfuze = EditText(window, '销售采购负责人')
    xscgfuze.text_setting(height=1, width=22)
    widget_list.append(xscgfuze)

    xscgbmcode = EditText(window, '销售采购部门代码')
    xscgbmcode.text_setting(height=1, width=22)
    widget_list.append(xscgbmcode)

    xzcaigou = EditText(window, '行政采购部门')
    xzcaigou.text_setting(height=1, width=22)
    widget_list.append(xzcaigou)

    xzcgfuze = EditText(window, '行政采购负责人')
    xzcgfuze.text_setting(height=1, width=22)
    widget_list.append(xzcgfuze)

    xzcgbmcode = EditText(window, '行政采购部门代码')
    xzcgbmcode.text_setting(height=1, width=22)
    widget_list.append(xzcgbmcode)

    shangchanliuchng1 = EditText(window, '生产工艺流程1', default='若无该流程则跳过该项')
    shangchanliuchng1.text_setting(height=1, width=91)
    widget_list.append(shangchanliuchng1)

    shangchanliuchng2 = EditText(window, '生产工艺流程2', default='若无该流程则跳过该项')
    shangchanliuchng2.text_setting(height=1, width=91)
    widget_list.append(shangchanliuchng2)

    shangchanliuchng3 = EditText(window, '生产工艺流程3', default='若无该流程则跳过该项')
    shangchanliuchng3.text_setting(height=1, width=91)
    widget_list.append(shangchanliuchng3)

    jlnf = EditText(window, '记录年份', '2022', replaceable=False)
    jlnf.text_setting(height=1, width=22)
    widget_list.append(jlnf)

    ybjlrq = EditText(window, '一般记录日期', '2022.1.4', replaceable=False)
    ybjlrq.text_setting(width=22, height=1)
    widget_list.append(ybjlrq)

    def text_gen():
        for widget in widget_list:
            widget.save_value_into_info_dic(info_dic)
            widget.temp_save()
        informCollectWindow(info_dic, re=re)

    def temp_save_to_local():
        for widget in widget_list:
            widget.temp_save()
        gen_temp_storage()
        tkinter.messagebox.showinfo("success", "生成缓存文件成功")
        print("成功")

    def gen_docx(info_dict):
        for widget in widget_list:
            widget.save_value_into_info_dic(info_dict)
        df.ReplaceProcess(info_dict, re=re, page2=True)
        showinfo(title="提示",
                 message="文档输出完成!")
        window.destroy()

    btn_gen = tk.Button(window, text='确认信息无误，进入下一采集阶段。', command=lambda: [text_gen()])
    btn_save = tk.Button(window, text='缓存信息。', command=lambda: [temp_save_to_local()])
    btn_gen_docx = tk.Button(window, text='输出上报材料',
                             command=lambda: threading.Thread(target=lambda: gen_docx(info_dic)).start())

    name.set_position(row=0, column=0)
    code.set_position(row=0, column=1)
    version_code.set_position(row=0, column=2, columnspan=2)
    m.set_position(row=1, column=0)
    mx.set_position(row=1, column=1)
    t.set_position(row=1, column=2, columnspan=2)
    jianjie.set_position(row=2, column=0, rowspan=2, columnspan=4)
    fanwei.set_position(row=4, column=0, rowspan=1, columnspan=4)
    waibao.set_position(row=6, column=0, rowspan=2, columnspan=4)
    tsguocheng.set_position(row=8, column=0, rowspan=2, columnspan=4)
    zhijian.set_position(row=10, column=0, columnspan=1)
    zjfuze.set_position(row=10, column=1, columnspan=1)
    zjbmcode.set_position(row=10, column=2, columnspan=2)
    xiaoshou.set_position(row=11, column=0, columnspan=1)
    xsfuze.set_position(row=11, column=1, columnspan=1)
    xsbmcode.set_position(row=11, column=2, columnspan=2)
    shengchan.set_position(row=12, column=0, columnspan=1)
    scfuze.set_position(row=12, column=1, columnspan=1)
    scbmcode.set_position(row=12, column=2, columnspan=2)
    xingzheng.set_position(row=13, column=0, columnspan=1)
    xzfuze.set_position(row=13, column=1, columnspan=1)
    xzbmcode.set_position(row=13, column=2, columnspan=2)
    caigou.set_position(row=14, column=0, columnspan=1)
    cgfuze.set_position(row=14, column=1, columnspan=1)
    cgbmcode.set_position(row=14, column=2, columnspan=2)
    xscaigou.set_position(row=15, column=0, columnspan=1)
    xscgfuze.set_position(row=15, column=1, columnspan=1)
    xscgbmcode.set_position(row=15, column=2, columnspan=2)
    xzcaigou.set_position(row=16, column=0, columnspan=1)
    xzcgfuze.set_position(row=16, column=1, columnspan=1)
    xzcgbmcode.set_position(row=16, column=2, columnspan=2)
    shangchanliuchng1.set_position(row=17, column=0, columnspan=4)
    shangchanliuchng2.set_position(row=18, column=0, columnspan=4)
    shangchanliuchng3.set_position(row=19, column=0, columnspan=4)
    jlnf.set_position(row=20, column=0, columnspan=2)
    ybjlrq.set_position(row=20, column=2, columnspan=2)
    btn_gen.grid(row=21, column=0, columnspan=2, pady=(30, 0))
    btn_save.grid(row=21, column=2, columnspan=1, pady=(30, 0))
    btn_gen_docx.grid(row=21, column=3, columnspan=1, pady=(30, 0))

    window.mainloop()


def InfoWindow_2(info_dic, re=False):
    """E/QE界面"""

    window = tk.Tk()

    # 给窗口的可视化起名字
    if re:
        window.title('监督复评模式')
    else:
        window.title('初审模式')
    window.config(background='Lavender')
    widget_list = []
    # 设定窗口的大小(长 * 宽)
    window.geometry('850x650')  # 这里的乘是小x
    window.resizable(0, 0)

    name = EditText(window, '企业名称')
    name.text_setting(height=1, width=25)
    widget_list.append(name)

    code = EditText(window, '企业代码')
    code.text_setting(height=1, width=25)
    widget_list.append(code)

    version_code = EditText(window, '版本号', default='A/0', replaceable=False)
    version_code.text_setting(height=1, width=12)
    widget_list.append(version_code)

    m = EditText(window, '管理者代表')
    m.text_setting(height=1, width=22)
    widget_list.append(m)

    mx = EditText(window, '最高管理者')
    mx.text_setting(height=1, width=22)
    widget_list.append(mx)

    t = EditText(window, '手册发布实施日期')
    t.text_setting(height=1, width=22)
    widget_list.append(t)

    jianjie = EditText(window, '公司简介')
    jianjie.text_setting(height=2, width=97)
    widget_list.append(jianjie)

    fanwei = EditText(window, '认证范围')
    fanwei.text_setting(height=1, width=97)
    widget_list.append(fanwei)

    waibao = GroupButtonWithText(window, title='公司有无外包过程', pos_opt='公司有外包过程', neg_opt='公司无外包过程',
                                 text_title='外包过程表述', text_default='本公司外包过程为XX')
    widget_list.append(waibao)

    tsguocheng = EditText(window, '特殊过程', default='特殊过程为XX', replaceable=False)
    tsguocheng.text_setting(height=2, width=97)
    widget_list.append(tsguocheng)

    zhijian = EditText(window, '质检部门')
    zhijian.text_setting(height=1, width=22)
    widget_list.append(zhijian)

    zjfuze = EditText(window, '质检负责人')
    zjfuze.text_setting(height=1, width=22)
    widget_list.append(zjfuze)

    zjbmcode = EditText(window, '质检部门代码')
    zjbmcode.text_setting(height=1, width=22)
    widget_list.append(zjbmcode)

    xiaoshou = EditText(window, '销售部门')
    xiaoshou.text_setting(height=1, width=22)
    widget_list.append(xiaoshou)

    xsfuze = EditText(window, '销售负责人')
    xsfuze.text_setting(height=1, width=22)
    widget_list.append(xsfuze)

    xsbmcode = EditText(window, '销售部门代码')
    xsbmcode.text_setting(height=1, width=22)
    widget_list.append(xsbmcode)

    shengchan = EditText(window, '生产部门')
    shengchan.text_setting(height=1, width=22)
    widget_list.append(shengchan)

    scfuze = EditText(window, '生产负责人')
    scfuze.text_setting(height=1, width=22)
    widget_list.append(scfuze)

    scbmcode = EditText(window, '生产部门代码')
    scbmcode.text_setting(height=1, width=22)
    widget_list.append(scbmcode)

    xingzheng = EditText(window, '行政部门')
    xingzheng.text_setting(height=1, width=22)
    widget_list.append(xingzheng)

    xzfuze = EditText(window, '行政负责人')
    xzfuze.text_setting(height=1, width=22)
    widget_list.append(xzfuze)

    xzbmcode = EditText(window, '行政部门代码')
    xzbmcode.text_setting(height=1, width=22)
    widget_list.append(xzbmcode)

    caiwu = EditText(window, '财务部门')
    caiwu.text_setting(height=1, width=22)
    widget_list.append(caiwu)

    cwfuze = EditText(window, '财务负责人')
    cwfuze.text_setting(height=1, width=22)
    widget_list.append(cwfuze)

    cwbmcode = EditText(window, '财务部门代码')
    cwbmcode.text_setting(height=1, width=22)
    widget_list.append(cwbmcode)

    caigou = EditText(window, '采购部门')
    caigou.text_setting(height=1, width=22)
    widget_list.append(caigou)

    cgfuze = EditText(window, '采购负责人')
    cgfuze.text_setting(height=1, width=22)
    widget_list.append(cgfuze)

    cgbmcode = EditText(window, '采购部门代码')
    cgbmcode.text_setting(height=1, width=22)
    widget_list.append(cgbmcode)

    xscaigou = EditText(window, '销售采购部门')
    xscaigou.text_setting(height=1, width=22)
    widget_list.append(xscaigou)

    xscgfuze = EditText(window, '销售采购负责人')
    xscgfuze.text_setting(height=1, width=22)
    widget_list.append(xscgfuze)

    xscgbmcode = EditText(window, '销售采购部门代码')
    xscgbmcode.text_setting(height=1, width=22)
    widget_list.append(xscgbmcode)

    xzcaigou = EditText(window, '行政采购部门')
    xzcaigou.text_setting(height=1, width=22)
    widget_list.append(xzcaigou)

    xzcgfuze = EditText(window, '行政采购负责人')
    xzcgfuze.text_setting(height=1, width=22)
    widget_list.append(xzcgfuze)

    xzcgbmcode = EditText(window, '行政采购部门代码')
    xzcgbmcode.text_setting(height=1, width=22)
    widget_list.append(xzcgbmcode)

    shangchanliuchng1 = EditText(window, '生产工艺流程1', default='若无该流程则跳过该项')
    shangchanliuchng1.text_setting(height=1, width=91)
    widget_list.append(shangchanliuchng1)

    shangchanliuchng2 = EditText(window, '生产工艺流程2', default='若无该流程则跳过该项')
    shangchanliuchng2.text_setting(height=1, width=91)
    widget_list.append(shangchanliuchng2)

    shangchanliuchng3 = EditText(window, '生产工艺流程3', default='若无该流程则跳过该项')
    shangchanliuchng3.text_setting(height=1, width=91)
    widget_list.append(shangchanliuchng3)

    jlnf = EditText(window, '记录年份', '2022', replaceable=False)
    jlnf.text_setting(height=1, width=22)
    widget_list.append(jlnf)

    ybjlrq = EditText(window, '一般记录日期', '2022.1.4', replaceable=False)
    ybjlrq.text_setting(width=22, height=1)
    widget_list.append(ybjlrq)

    def text_gen():
        for widget in widget_list:
            widget.save_value_into_info_dic(info_dic)
            widget.temp_save()
        informCollectWindow(info_dic, re=re)

    def temp_save_to_local():
        for widget in widget_list:
            widget.temp_save()
        gen_temp_storage()
        tkinter.messagebox.showinfo("success", "生成缓存文件成功")

    def gen_docx(info_dict):
        for widget in widget_list:
            widget.save_value_into_info_dic(info_dict)
        df.ReplaceProcess(info_dict, re=re, page2=True)
        showinfo(title="提示",
                 message="文档输出完成!")
        window.destroy()

    btn_gen = tk.Button(window, text='确认信息无误，进入下一采集阶段。', command=lambda: [text_gen()])
    btn_save = tk.Button(window, text='缓存信息。', command=lambda: [temp_save_to_local()])
    btn_gen_docx = tk.Button(window, text='输出上报材料',
                             command=lambda: threading.Thread(target=lambda: gen_docx(info_dic)).start())

    name.set_position(row=0, column=0)
    code.set_position(row=0, column=1)
    version_code.set_position(row=0, column=2, columnspan=2)
    m.set_position(row=1, column=0)
    mx.set_position(row=1, column=1)
    t.set_position(row=1, column=2, columnspan=2)
    jianjie.set_position(row=2, column=0, rowspan=2, columnspan=4)
    fanwei.set_position(row=4, column=0, rowspan=1, columnspan=4)
    waibao.set_position(row=6, column=0, rowspan=2, columnspan=4)
    tsguocheng.set_position(row=8, column=0, rowspan=2, columnspan=4)
    zhijian.set_position(row=10, column=0, columnspan=1)
    zjfuze.set_position(row=10, column=1, columnspan=1)
    zjbmcode.set_position(row=10, column=2, columnspan=2)
    xiaoshou.set_position(row=11, column=0, columnspan=1)
    xsfuze.set_position(row=11, column=1, columnspan=1)
    xsbmcode.set_position(row=11, column=2, columnspan=2)
    shengchan.set_position(row=12, column=0, columnspan=1)
    scfuze.set_position(row=12, column=1, columnspan=1)
    scbmcode.set_position(row=12, column=2, columnspan=2)
    xingzheng.set_position(row=13, column=0, columnspan=1)
    xzfuze.set_position(row=13, column=1, columnspan=1)
    xzbmcode.set_position(row=13, column=2, columnspan=2)
    caiwu.set_position(row=14, column=0, columnspan=1)
    cwfuze.set_position(row=14, column=1, columnspan=1)
    cwbmcode.set_position(row=14, column=2, columnspan=2)
    caigou.set_position(row=15, column=0, columnspan=1)
    cgfuze.set_position(row=15, column=1, columnspan=1)
    cgbmcode.set_position(row=15, column=2, columnspan=2)
    xscaigou.set_position(row=16, column=0, columnspan=1)
    xscgfuze.set_position(row=16, column=1, columnspan=1)
    xscgbmcode.set_position(row=16, column=2, columnspan=2)
    xzcaigou.set_position(row=17, column=0, columnspan=1)
    xzcgfuze.set_position(row=17, column=1, columnspan=1)
    xzcgbmcode.set_position(row=17, column=2, columnspan=2)
    shangchanliuchng1.set_position(row=18, column=0, columnspan=4)
    shangchanliuchng2.set_position(row=19, column=0, columnspan=4)
    shangchanliuchng3.set_position(row=20, column=0, columnspan=4)
    jlnf.set_position(row=21, column=0, columnspan=2)
    ybjlrq.set_position(row=21, column=2, columnspan=2)
    btn_gen.grid(row=22, column=0, columnspan=2, pady=(30, 0))
    btn_save.grid(row=22, column=2, columnspan=1, pady=(30, 0))
    btn_gen_docx.grid(row=22, column=3, columnspan=1, pady=(30, 0))

    window.mainloop()


def InfoWindow_3(info_dic, re=False):
    """S/QS/ES/QES界面"""

    window = tk.Tk()

    # 给窗口的可视化起名字
    if re:
        window.title('监督复评模式')
    else:
        window.title('初审模式')
    window.config(background='Lavender')
    widget_list = []
    # 设定窗口的大小(长 * 宽)
    window.geometry('850x650')  # 这里的乘是小x
    window.resizable(0, 0)

    name = EditText(window, '企业名称')
    name.text_setting(height=1, width=25)
    widget_list.append(name)

    code = EditText(window, '企业代码')
    code.text_setting(height=1, width=25)
    widget_list.append(code)

    version_code = EditText(window, '版本号', default='A/0', replaceable=False)
    version_code.text_setting(height=1, width=12)
    widget_list.append(version_code)

    m = EditText(window, '管理者代表')
    m.text_setting(height=1, width=22)
    widget_list.append(m)

    mx = EditText(window, '最高管理者')
    mx.text_setting(height=1, width=22)
    widget_list.append(mx)

    t = EditText(window, '手册发布实施日期')
    t.text_setting(height=1, width=22)
    widget_list.append(t)

    jianjie = EditText(window, '公司简介')
    jianjie.text_setting(height=2, width=97)
    widget_list.append(jianjie)

    fanwei = EditText(window, '认证范围')
    fanwei.text_setting(height=1, width=97)
    widget_list.append(fanwei)

    waibao = GroupButtonWithText(window, title='公司有无外包过程', pos_opt='公司有外包过程', neg_opt='公司无外包过程',
                                 text_title='外包过程表述', text_default='本公司外包过程为XX')
    widget_list.append(waibao)

    tsguocheng = EditText(window, '特殊过程', default='特殊过程为XX', replaceable=False)
    tsguocheng.text_setting(height=2, width=97)
    widget_list.append(tsguocheng)

    zhijian = EditText(window, '质检部门')
    zhijian.text_setting(height=1, width=22)
    widget_list.append(zhijian)

    zjfuze = EditText(window, '质检负责人')
    zjfuze.text_setting(height=1, width=22)
    widget_list.append(zjfuze)

    zjbmcode = EditText(window, '质检部门代码')
    zjbmcode.text_setting(height=1, width=22)
    widget_list.append(zjbmcode)

    xiaoshou = EditText(window, '销售部门')
    xiaoshou.text_setting(height=1, width=22)
    widget_list.append(xiaoshou)

    xsfuze = EditText(window, '销售负责人')
    xsfuze.text_setting(height=1, width=22)
    widget_list.append(xsfuze)

    xsbmcode = EditText(window, '销售部门代码')
    xsbmcode.text_setting(height=1, width=22)
    widget_list.append(xsbmcode)

    shengchan = EditText(window, '生产部门')
    shengchan.text_setting(height=1, width=22)
    widget_list.append(shengchan)

    scfuze = EditText(window, '生产负责人')
    scfuze.text_setting(height=1, width=22)
    widget_list.append(scfuze)

    scbmcode = EditText(window, '生产部门代码')
    scbmcode.text_setting(height=1, width=22)
    widget_list.append(scbmcode)

    xingzheng = EditText(window, '行政部门')
    xingzheng.text_setting(height=1, width=22)
    widget_list.append(xingzheng)

    xzfuze = EditText(window, '行政负责人')
    xzfuze.text_setting(height=1, width=22)
    widget_list.append(xzfuze)

    xzbmcode = EditText(window, '行政部门代码')
    xzbmcode.text_setting(height=1, width=22)
    widget_list.append(xzbmcode)

    caiwu = EditText(window, '财务部门')
    caiwu.text_setting(height=1, width=22)
    widget_list.append(caiwu)

    cwfuze = EditText(window, '财务负责人')
    cwfuze.text_setting(height=1, width=22)
    widget_list.append(cwfuze)

    cwbmcode = EditText(window, '财务部门代码')
    cwbmcode.text_setting(height=1, width=22)
    widget_list.append(cwbmcode)

    caigou = EditText(window, '采购部门')
    caigou.text_setting(height=1, width=22)
    widget_list.append(caigou)

    cgfuze = EditText(window, '采购负责人')
    cgfuze.text_setting(height=1, width=22)
    widget_list.append(cgfuze)

    cgbmcode = EditText(window, '采购部门代码')
    cgbmcode.text_setting(height=1, width=22)
    widget_list.append(cgbmcode)

    xscaigou = EditText(window, '销售采购部门')
    xscaigou.text_setting(height=1, width=22)
    widget_list.append(xscaigou)

    xscgfuze = EditText(window, '销售采购负责人')
    xscgfuze.text_setting(height=1, width=22)
    widget_list.append(xscgfuze)

    xscgbmcode = EditText(window, '销售采购部门代码')
    xscgbmcode.text_setting(height=1, width=22)
    widget_list.append(xscgbmcode)

    xzcaigou = EditText(window, '行政采购部门')
    xzcaigou.text_setting(height=1, width=22)
    widget_list.append(xzcaigou)

    xzcgfuze = EditText(window, '行政采购负责人')
    xzcgfuze.text_setting(height=1, width=22)
    widget_list.append(xzcgfuze)

    xzcgbmcode = EditText(window, '行政采购部门代码')
    xzcgbmcode.text_setting(height=1, width=22)
    widget_list.append(xzcgbmcode)

    anquanfuze = EditText(window, '安全负责人')
    anquanfuze.text_setting(height=1, width=22)
    widget_list.append(anquanfuze)

    shangchanliuchng1 = EditText(window, '生产工艺流程1', default='若无该流程则跳过该项')
    shangchanliuchng1.text_setting(height=1, width=91)
    widget_list.append(shangchanliuchng1)

    shangchanliuchng2 = EditText(window, '生产工艺流程2', default='若无该流程则跳过该项')
    shangchanliuchng2.text_setting(height=1, width=91)
    widget_list.append(shangchanliuchng2)

    shangchanliuchng3 = EditText(window, '生产工艺流程3', default='若无该流程则跳过该项')
    shangchanliuchng3.text_setting(height=1, width=91)
    widget_list.append(shangchanliuchng3)

    jlnf = EditText(window, '记录年份', '2022', replaceable=False)
    jlnf.text_setting(height=1, width=22)
    widget_list.append(jlnf)

    ybjlrq = EditText(window, '一般记录日期', '2022.1.4', replaceable=False)
    ybjlrq.text_setting(width=22, height=1)
    widget_list.append(ybjlrq)

    def text_gen():
        for widget in widget_list:
            widget.save_value_into_info_dic(info_dic)
            widget.temp_save()
        informCollectWindow(info_dic, re=re)

    def temp_save_to_local():
        for widget in widget_list:
            widget.temp_save()
        gen_temp_storage()
        tkinter.messagebox.showinfo("success", "生成缓存文件成功")

    def gen_docx(info_dict):
        for widget in widget_list:
            widget.save_value_into_info_dic(info_dict)
        df.ReplaceProcess(info_dict, re=re, page2=True)
        showinfo(title="提示",
                 message="文档输出完成!")
        window.destroy()

    btn_gen = tk.Button(window, text='确认信息无误，进入下一采集阶段。', command=lambda: [text_gen()])
    btn_save = tk.Button(window, text='缓存信息。', command=lambda: [temp_save_to_local()])
    btn_gen_docx = tk.Button(window, text='输出上报材料',
                             command=lambda: threading.Thread(target=lambda: gen_docx(info_dic)).start())

    name.set_position(row=0, column=0)
    code.set_position(row=0, column=1)
    version_code.set_position(row=0, column=2, columnspan=2)
    m.set_position(row=1, column=0)
    mx.set_position(row=1, column=1)
    t.set_position(row=1, column=2, columnspan=2)
    jianjie.set_position(row=2, column=0, rowspan=2, columnspan=4)
    fanwei.set_position(row=4, column=0, rowspan=1, columnspan=4)
    waibao.set_position(row=6, column=0, rowspan=2, columnspan=4)
    tsguocheng.set_position(row=8, column=0, rowspan=2, columnspan=4)
    zhijian.set_position(row=10, column=0, columnspan=1)
    zjfuze.set_position(row=10, column=1, columnspan=1)
    zjbmcode.set_position(row=10, column=2, columnspan=2)
    xiaoshou.set_position(row=11, column=0, columnspan=1)
    xsfuze.set_position(row=11, column=1, columnspan=1)
    xsbmcode.set_position(row=11, column=2, columnspan=2)
    shengchan.set_position(row=12, column=0, columnspan=1)
    scfuze.set_position(row=12, column=1, columnspan=1)
    scbmcode.set_position(row=12, column=2, columnspan=2)
    xingzheng.set_position(row=13, column=0, columnspan=1)
    xzfuze.set_position(row=13, column=1, columnspan=1)
    xzbmcode.set_position(row=13, column=2, columnspan=2)
    caiwu.set_position(row=14, column=0, columnspan=1)
    cwfuze.set_position(row=14, column=1, columnspan=1)
    cwbmcode.set_position(row=14, column=2, columnspan=2)
    caigou.set_position(row=15, column=0, columnspan=1)
    cgfuze.set_position(row=15, column=1, columnspan=1)
    cgbmcode.set_position(row=15, column=2, columnspan=2)
    xscaigou.set_position(row=16, column=0, columnspan=1)
    xscgfuze.set_position(row=16, column=1, columnspan=1)
    xscgbmcode.set_position(row=16, column=2, columnspan=2)
    xzcaigou.set_position(row=17, column=0, columnspan=1)
    xzcgfuze.set_position(row=17, column=1, columnspan=1)
    xzcgbmcode.set_position(row=17, column=2, columnspan=2)
    anquanfuze.set_position(row=18, column=0, columnspan=1)
    shangchanliuchng1.set_position(row=19, column=0, columnspan=4)
    shangchanliuchng2.set_position(row=20, column=0, columnspan=4)
    shangchanliuchng3.set_position(row=21, column=0, columnspan=4)
    jlnf.set_position(row=22, column=0, columnspan=2)
    ybjlrq.set_position(row=22, column=2, columnspan=2)
    btn_gen.grid(row=23, column=0, columnspan=2, pady=(30, 0))
    btn_save.grid(row=23, column=2, columnspan=1, pady=(30, 0))
    btn_gen_docx.grid(row=23, column=3, columnspan=1, pady=(30, 0))

    window.mainloop()

