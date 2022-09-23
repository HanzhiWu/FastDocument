from fileSystem.third_window import informCollectWindow
from fileSystem.widgets import EditText, GroupButtonWithText
from temp_storage import *


def InforWindow_1(info_dic):
    """Q界面"""
    window = tk.Tk()

    # 给窗口的可视化起名字
    window.title('认证文件管理系统')
    window.config(background='Lavender')
    widget_list = []
    # 设定窗口的大小(长 * 宽)
    window.geometry('770x550')  # 这里的乘是小x
    window.resizable(0, 0)

    name = EditText(window, '企业名称')
    name.text_setting(height=1, width=25)
    widget_list.append(name)

    code = EditText(window, '企业代码')
    code.text_setting(height=1, width=25)
    widget_list.append(code)

    ver = EditText(window, '版本')
    ver.text_setting(height=1, width=12)
    ver.text.insert('0.0', 'A')
    widget_list.append(ver)

    times = EditText(window, '版次')
    times.text_setting(height=1, width=12)
    ver.text.insert('0.0', '0')
    widget_list.append(times)

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
                                 text_title='外包过程表述')
    waibao.text.text.insert('0.0', '本公司外包过程为XX')
    widget_list.append(waibao)

    tsguocheng = EditText(window, '特殊过程')
    tsguocheng.text_setting(height=2, width=97)
    tsguocheng.text.insert('0.0', '无特殊过程/特殊过程为XX')
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

    shangchanliuchng1 = EditText(window, '生产工艺流程1')
    shangchanliuchng1.text_setting(height=1, width=91)
    shangchanliuchng1.text.insert('0.0', '若无该流程则跳过该项')
    widget_list.append(shangchanliuchng1)

    shangchanliuchng2 = EditText(window, '生产工艺流程2')
    shangchanliuchng2.text_setting(height=1, width=91)
    shangchanliuchng2.text.insert('0.0', '若无该流程则跳过该项')
    widget_list.append(shangchanliuchng2)

    shangchanliuchng3 = EditText(window, '生产工艺流程3')
    shangchanliuchng3.text_setting(height=1, width=91)
    shangchanliuchng3.text.insert('0.0', '若无该流程则跳过该项')
    widget_list.append(shangchanliuchng3)
    btn_gen = tk.Button(window, text='确认信息无误，进入下一采集阶段。', command=lambda: [text_gen()])
    btn_save = tk.Button(window, text='缓存信息。', command=lambda: [temp_save_to_local()])

    def text_gen():
        for widget in widget_list:
            widget.save_value_into_info_dic(info_dic)
            widget.temp_save()
        informCollectWindow(info_dic)

    def temp_save_to_local():
        for widget in widget_list:
            widget.temp_save()
        gen_temp_storage()


def InforWindow_2(info_dic):
    """E/QE界面"""

    window = tk.Tk()

    # 给窗口的可视化起名字
    window.title('认证文件管理系统')
    window.config(background='Lavender')
    widget_list = []
    # 设定窗口的大小(长 * 宽)
    window.geometry('770x580')  # 这里的乘是小x
    window.resizable(0, 0)

    name = EditText(window, '企业名称')
    name.text_setting(height=1, width=25)
    widget_list.append(name)

    code = EditText(window, '企业代码')
    code.text_setting(height=1, width=25)
    widget_list.append(code)

    ver = EditText(window, '版本')
    ver.text_setting(height=1, width=12)
    ver.text.insert('0.0', 'A')
    widget_list.append(ver)

    times = EditText(window, '版次')
    times.text_setting(height=1, width=12)
    ver.text.insert('0.0', '0')
    widget_list.append(times)

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
                                 text_title='外包过程表述')
    waibao.text.text.insert('0.0', '本公司外包过程为XX')
    widget_list.append(waibao)

    tsguocheng = EditText(window, '特殊过程')
    tsguocheng.text_setting(height=2, width=97)
    tsguocheng.text.insert('0.0', '无特殊过程/特殊过程为XX')
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

    shangchanliuchng1 = EditText(window, '生产工艺流程1')
    shangchanliuchng1.text_setting(height=1, width=91)
    shangchanliuchng1.text.insert('0.0', '若无该流程则跳过该项')
    widget_list.append(shangchanliuchng1)

    shangchanliuchng2 = EditText(window, '生产工艺流程2')
    shangchanliuchng2.text_setting(height=1, width=91)
    shangchanliuchng2.text.insert('0.0', '若无该流程则跳过该项')
    widget_list.append(shangchanliuchng2)

    shangchanliuchng3 = EditText(window, '生产工艺流程3')
    shangchanliuchng3.text_setting(height=1, width=91)
    shangchanliuchng3.text.insert('0.0', '若无该流程则跳过该项')
    widget_list.append(shangchanliuchng3)
    btn_gen = tk.Button(window, text='确认信息无误，进入下一采集阶段。', command=lambda: [text_gen()])
    btn_save = tk.Button(window, text='缓存信息。', command=lambda: [temp_save_to_local()])

    def text_gen():
        for widget in widget_list:
            widget.save_value_into_info_dic(info_dic)
            widget.temp_save()
        informCollectWindow(info_dic)

    def temp_save_to_local():
        for widget in widget_list:
            widget.temp_save()
        gen_temp_storage()
