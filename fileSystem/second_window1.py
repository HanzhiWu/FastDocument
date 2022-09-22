from fileSystem.third_window import informCollectWindow
from fileSystem.widgets import EditText, GroupButtonWithText
from temp_storage import *


def InforWindow_1(info_dic):
    """Q界面"""
    window = tk.Tk()

    # 给窗口的可视化起名字
    window.title('认证文件管理系统')
    window.config(background='Lavender')

    # 设定窗口的大小(长 * 宽)
    window.geometry('770x550')  # 这里的乘是小x
    window.resizable(0, 0)

    name = EditText(window, '企业名称')
    name.text_setting(height=1, width=25)

    code = EditText(window, '企业代码')
    code.text_setting(height=1, width=25)

    ver = EditText(window, '版本')
    ver.text_setting(height=1, width=12)
    ver.text.insert('0.0', '0')

    m = EditText(window, '管理者代表')
    m.text_setting(height=1, width=22)

    mx = EditText(window, '最高管理者')
    mx.text_setting(height=1, width=22)

    t = EditText(window, '最高管理者')
    t.text_setting(height=1, width=22)

    jianjie = EditText(window, '公司简介')
    jianjie.text_setting(height=2, width=97)

    fanwei = EditText(window, '认证范围')
    fanwei.text_setting(height=1, width=97)

    waibao = GroupButtonWithText(window, title='公司有无外包过程', pos_opt='公司有外包过程', neg_opt='公司无外包过程',
                                 text_title='外包过程表述')
    waibao.text.text.insert('0.0', '本公司外包过程为XX')

    wbguocheng = EditText(window, '特殊过程')
    wbguocheng.text_setting(height=2, width=97)
    wbguocheng.text.insert('0.0', '无特殊过程/特殊过程为XX')

    zhijian = EditText(window, '质检部门')
    zhijian.text_setting(height=1, width=22)

    zjfuze = EditText(window, '质检负责人')
    zjfuze.text_setting(height=1, width=22)

    zjbmcode = EditText(window, '质检部门代码')
    zjbmcode.text_setting(height=1, width=22)

    zhijian = EditText(window, '销售部门')
    zhijian.text_setting(height=1, width=22)

    zjfuze = EditText(window, '销售负责人')
    zjfuze.text_setting(height=1, width=22)

    zjbmcode = EditText(window, '销售部门代码')
    zjbmcode.text_setting(height=1, width=22)

    zhijian = EditText(window, '生产部门')
    zhijian.text_setting(height=1, width=22)

    zjfuze = EditText(window, '生产负责人')
    zjfuze.text_setting(height=1, width=22)

    zjbmcode = EditText(window, '生产部门代码')
    zjbmcode.text_setting(height=1, width=22)

    zhijian = EditText(window, '行政部门')
    zhijian.text_setting(height=1, width=22)

    zjfuze = EditText(window, '行政负责人')
    zjfuze.text_setting(height=1, width=22)

    zjbmcode = EditText(window, '行政部门代码')
    zjbmcode.text_setting(height=1, width=22)

    zhijian = EditText(window, '采购部门')
    zhijian.text_setting(height=1, width=22)

    zjfuze = EditText(window, '采购负责人')
    zjfuze.text_setting(height=1, width=22)

    zjbmcode = EditText(window, '采购部门代码')
    zjbmcode.text_setting(height=1, width=22)


