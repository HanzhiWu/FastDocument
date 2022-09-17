import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from fileSystem.forth_page_1 import window4_1
from fileSystem.forth_page_2 import window4_2
from fileSystem.forth_page_4 import window4_4
import deal_with_file as df


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

    syndgprq_L = Label(window, text='上一年度管理评审日期:', bg='Lavender')
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
    myddc1.insert(0.0, '95')

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
    def next_stage(info_dict):
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
            df.ReplaceProcess(info_dict)
            showinfo(title="提示",
                     message="文档输出完成!")
            window.destroy()

    # 封装第三层页面radio_button处理结果逻辑
    def addRadioRes(bool_str, radio_res):
        if radio_res.get() == 1:
            info_dic['__{}__'.format(bool_str)] = ' '
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
        addRadioRes('是否为加强生产检查改进项', jqscjcV)
        addRadioRes('是否为提高意识技术改进项', jqysjsV)
        addRadioRes('是否为加强招聘改进项', jqzpV)
        info_dic['__管评改进项完成日期__'] = gpgjwcsj.get(0.0, 20.0).strip()
        info_dic['__上一年度管理评审日期__'] = syndgprq.get(0.0, 20.0).strip()
        info_dic['__上一年度管评改进项完成日期__'] = syndgpgjrq.get(0.0, 20.0).strip()
        addRadioRes('上一年度是否为加强生产检查改进项', syndjqscjcV)
        addRadioRes('上一年度是否为提高意识技术改进项', syndjqysjsV)
        addRadioRes('上一年度是否为加强招聘改进项', syndjqzpV)
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
        next_stage(info_dic)

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
            xxht_text.delete(0.0, 'end')
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
            gf_text.delete(0.0, "end")
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
            cgcp_text.delete(0.0, "end")
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
