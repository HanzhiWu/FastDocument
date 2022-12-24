import threading
import tkinter
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from forth_page_1 import window4_1
from forth_page_2 import window4_2
from forth_page_4 import window4_4
import deal_with_file as df
from temp_storage import *
from widgets import EditText, AddText, GroupButton


# 第三层界面
def informCollectWindow(info_dic, re=False, old2new=None):
    window = tk.Tk()

    # 给窗口的可视化起名字
    if re:
        window.title('监督复评模式')
    else:
        window.title('初审模式')
    window.config(background='Lavender')
    widget_list = []

    window.geometry('1280x700')  # 这里的乘是小x

    peixun1 = GroupButton(window, '是否有1月培训', '是', '否', defalutl_pos='')
    peixun2 = GroupButton(window, '是否有2月培训', '是', '否', defalutl_pos='')
    peixun3 = GroupButton(window, '是否有3月培训', '是', '否', defalutl_pos='')
    peixun4 = GroupButton(window, '是否有4月培训', '是', '否', defalutl_pos='')
    peixun5 = GroupButton(window, '是否有5月培训', '是', '否', defalutl_pos='')
    peixun6 = GroupButton(window, '是否有6月培训', '是', '否', defalutl_pos='')
    peixun7 = GroupButton(window, '是否有7月培训', '是', '否', defalutl_pos='')
    peixun8 = GroupButton(window, '是否有8月培训', '是', '否', defalutl_pos='')
    peixun9 = GroupButton(window, '是否有9月培训', '是', '否', defalutl_pos='')
    peixun10 = GroupButton(window, '是否有10月培训', '是', '否', defalutl_pos='')
    peixun11 = GroupButton(window, '是否有11月培训', '是', '否', defalutl_pos='')
    peixun12 = GroupButton(window, '是否有12月培训', '是', '否', defalutl_pos='')

    widget_list.append(peixun1)
    widget_list.append(peixun2)
    widget_list.append(peixun3)
    widget_list.append(peixun4)
    widget_list.append(peixun5)
    widget_list.append(peixun6)
    widget_list.append(peixun7)
    widget_list.append(peixun8)
    widget_list.append(peixun9)
    widget_list.append(peixun10)
    widget_list.append(peixun11)
    widget_list.append(peixun12)

    nsypxrq = EditText(window, '内审员培训日期')
    nsypxrq.text_setting(width=22, height=1)
    widget_list.append(nsypxrq)

    nsjhzdrq = EditText(window, '内审计划制定日期')
    nsjhzdrq.text_setting(width=22, height=1)
    widget_list.append(nsjhzdrq)

    nsksrq = EditText(window, '内审开始日期')
    nsksrq.text_setting(width=22, height=1)
    widget_list.append(nsksrq)

    nsjsrq = EditText(window, '内审结束日期')
    nsjsrq.text_setting(width=22, height=1)
    widget_list.append(nsjsrq)

    nszgwcrq = EditText(window, '内审整改完成日期')
    nszgwcrq.text_setting(width=22, height=1)
    widget_list.append(nszgwcrq)

    q713 = GroupButton(window, '是否为Q7.1.3条款不符合', '是', '否')
    widget_list.append(q713)

    q851 = GroupButton(window, '是否为Q8.5.1条款不符合', "是", "否")
    widget_list.append(q851)

    q62 = GroupButton(window, '是否为Q6.2条款不符合', "是", "否")
    widget_list.append(q62)

    gpjhzdrq = EditText(window, '管评计划制定日期')
    gpjhzdrq.text_setting(width=22, height=1)
    widget_list.append(gpjhzdrq)

    gprq = EditText(window, '管评日期')
    gprq.text_setting(width=22, height=1)
    widget_list.append(gprq)

    gpbgrq = EditText(window, '管评报告日期')
    gpbgrq.text_setting(width=22, height=1)
    widget_list.append(gpbgrq)

    jqscjc = GroupButton(window, '是否为加强生产检查改进项', '是', '否')
    widget_list.append(jqscjc)

    jqysjs = GroupButton(window, '是否为提高意识技术改进项', "是", "否")
    widget_list.append(jqysjs)

    jqzp = GroupButton(window, '是否为加强招聘改进项', "是", "否")
    widget_list.append(jqzp)

    gpgjwcsj = EditText(window, '管评改进项完成日期')
    gpgjwcsj.text_setting(width=22, height=1)
    widget_list.append(gpgjwcsj)

    syndgprq = EditText(window, '上一年度管理评审日期')
    syndgprq.text_setting(width=22, height=1)
    widget_list.append(syndgprq)

    syndgpgjrq = EditText(window, '上一年度管评改进项完成日期')
    syndgpgjrq.text_setting(width=22, height=1)
    widget_list.append(syndgpgjrq)

    syndjqscjc = GroupButton(window, '上一年度是否为加强生产检查改进项', "是", "否")
    widget_list.append(syndjqscjc)

    syndjqysjs = GroupButton(window, '上一年度是否为提高意识技术改进项', "是", "否")
    widget_list.append(syndjqysjs)

    syndjqzp = GroupButton(window, '上一年度是否为加强招聘改进项', "是", "否")
    widget_list.append(syndjqzp)

    xxht = AddText(window, '销售合同信息', '销售合同', '修改合同信息', [18, 15, 10, 8, 10],
                   ['产品', '客户', '签订日期', '编号', '评审时间'])
    widget_list.append(xxht)

    myddcrq = EditText(window, '满意度调查日期')
    myddcrq.text_setting(width=22, height=1)
    widget_list.append(myddcrq)

    myddcsl = EditText(window, '满意度调查数量')
    myddcsl.text_setting(width=22, height=1)
    widget_list.append(myddcsl)

    myddcpj = EditText(window, '平均满意度', False)
    myddcpj.text_setting(width=22, height=1)
    widget_list.append(myddcpj)

    myddc1 = EditText(window, '销售合同1满意度', '95')
    myddc1.text_setting(width=22, height=1)
    widget_list.append(myddc1)

    myddc2 = EditText(window, '销售合同2满意度')
    myddc2.text_setting(width=22, height=1)
    widget_list.append(myddc2)

    myddc3 = EditText(window, '销售合同3满意度')
    myddc3.text_setting(width=22, height=1)
    widget_list.append(myddc3)

    myddc4 = EditText(window, '销售合同4满意度')
    myddc4.text_setting(width=22, height=1)
    widget_list.append(myddc4)

    myddc5 = EditText(window, '销售合同5满意度')
    myddc5.text_setting(width=22, height=1)
    widget_list.append(myddc5)

    myddc6 = EditText(window, '销售合同6满意度')
    myddc6.text_setting(width=22, height=1)
    widget_list.append(myddc6)

    myddc7 = EditText(window, '销售合同7满意度')
    myddc7.text_setting(width=22, height=1)
    widget_list.append(myddc7)

    myddc8 = EditText(window, '销售合同8满意度')
    myddc8.text_setting(width=22, height=1)
    widget_list.append(myddc8)

    gf = AddText(window, '已有供方信息', '供方', '修改供方信息', [18, 30, 60], ['名称', '地址', '所有产品'])
    widget_list.append(gf)

    cgcp = AddText(window, '采购产品信息', '采购', '修改采购信息', [15, 8, 15, 8, 10, 10],
                   ['产品', '产品规格型号', '产品供方', '产品数量', '时间', '产品到货时间'])
    widget_list.append(cgcp)

    def next_stage(info_dict):
        template_id = info_dic['template_id']
        rzfw, _, rzxm, _ = template_id.split('-')
        if (rzfw == 'SC' or rzfw == 'ZZ' or rzfw == 'JJSC') and (rzxm == 'QS' or rzxm == 'QES'):
            window4_1(info_dic, re=re, old2new=old2new)
        elif (rzfw == 'SC' or rzfw == 'ZZ' or rzfw == 'JJSC') and (rzxm == 'Q' or rzxm == 'QE'):
            window4_2(info_dic, re=re, old2new=old2new)
        elif (rzfw == 'SC' or rzfw == 'ZZ' or rzfw == 'JJSC') and (rzxm == 'S' or rzxm == 'ES'):
            window4_4(info_dic, re=re, old2new=old2new)
        else:
            threading.Thread(target=generate_storage_file(info_dict)).start()

    def generate_storage_file(info_dict):
        print(info_dict)
        # 函数上层已对字典进行缓存直接存到本地即可
        gen_temp_storage()
        print('生成缓存文件完成')
        df.replace_process(info_dict, re=re, old2new=old2new)
        showinfo(title="提示",
                 message="文档输出完成!")

    # 第三层界面处理结果生成字典
    def text_gen():
        for widget in widget_list:
            widget.save_value_into_info_dic(info_dic)
            widget.temp_save()
        next_stage(info_dic)

    def temp_save_to_local():
        for widget in widget_list:
            widget.temp_save()
        gen_temp_storage()
        tkinter.messagebox.showinfo("success", "生成缓存文件成功")

    btn_gen = tk.Button(window, text='信息确认完成，进入下一阶段。', command=text_gen)
    btn_save = tk.Button(window, text='缓存信息。', command=lambda: [temp_save_to_local()])

    peixun1.set_position(row=1, column=0, columnspan=3)
    peixun2.set_position(row=1, column=3, columnspan=3)
    peixun3.set_position(row=1, column=6, columnspan=3)
    peixun4.set_position(row=2, column=0, columnspan=3)
    peixun5.set_position(row=2, column=3, columnspan=3)
    peixun6.set_position(row=2, column=6, columnspan=3)
    peixun7.set_position(row=3, column=0, columnspan=3)
    peixun8.set_position(row=3, column=3, columnspan=3)
    peixun9.set_position(row=3, column=6, columnspan=3)
    peixun10.set_position(row=4, column=0, columnspan=3)
    peixun11.set_position(row=4, column=3, columnspan=3)
    peixun12.set_position(row=4, column=6, columnspan=3)
    nsypxrq.set_position(row=5, column=1, columnspan=3)
    nsjhzdrq.set_position(row=5, column=4, columnspan=3)
    nsksrq.set_position(row=6, column=1, columnspan=3)
    nsjsrq.set_position(row=6, column=4, columnspan=3)
    nszgwcrq.set_position(row=6, column=7, columnspan=3)
    q713.set_position(row=7, column=0, columnspan=3)
    q851.set_position(row=7, column=3, columnspan=3)
    q62.set_position(row=7, column=6, columnspan=3)
    gpjhzdrq.set_position(row=8, column=1, columnspan=3)
    gprq.set_position(row=8, column=4, columnspan=3)
    gpbgrq.set_position(row=8, column=7, columnspan=3)
    jqscjc.set_position(row=9, column=0, columnspan=3)
    jqysjs.set_position(row=9, column=3, columnspan=3)
    jqzp.set_position(row=9, column=6, columnspan=3)
    gpgjwcsj.set_position(row=10, column=1, columnspan=3)
    syndgprq.set_position(row=10, column=4, columnspan=3)
    syndgpgjrq.set_position(row=10, column=7, columnspan=3)
    syndjqscjc.set_position(row=11, column=0, columnspan=3)
    syndjqysjs.set_position(row=11, column=3, columnspan=3)
    syndjqzp.set_position(row=11, column=6, columnspan=3)
    xxht.set_position(row=12, column=0, columnspan=9, rowspan=4)
    myddcrq.set_position(row=16, column=1, columnspan=3)
    myddcsl.set_position(row=16, column=4, columnspan=3)
    myddcpj.set_position(row=16, column=7, columnspan=3)
    myddc1.set_position(row=17, column=1, columnspan=3)
    myddc2.set_position(row=17, column=4, columnspan=3)
    myddc3.set_position(row=17, column=7, columnspan=3)
    myddc4.set_position(row=18, column=1, columnspan=3)
    myddc5.set_position(row=18, column=4, columnspan=3)
    myddc6.set_position(row=18, column=7, columnspan=3)
    myddc7.set_position(row=19, column=1, columnspan=3)
    myddc8.set_position(row=19, column=4, columnspan=3)
    gf.set_position(row=20, column=0, rowspan=4, columnspan=9)
    cgcp.set_position(row=24, column=0, rowspan=4, columnspan=9)

    btn_gen.grid(row=29, column=3)
    btn_save.grid(row=29, column=7)

    window.mainloop()
