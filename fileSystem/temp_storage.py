import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo

temp_dic = {}
is_auto_restore = False
save_dic = {}
'''
1. 存储时，将info_dic和当前页面的所有填写过的内容直接存入缓存文件中
2. 读取时,将临时文件中的key经过处理存入temp_dic
3. 在页面的每个页面的每个控件进行检查，如果有就进行注入
'''


# 将选取的文件处理成为temp_dic 将自动填入的开关打开
def read_file_to_temp_list(temp_file):
    is_auto_restore = True
    return temp_dic


# 将info_dic存入将要存储的save_dic
def save_info_dic_to_save_dic(info_dic):
    save_dic.update(info_dic)


# 文本框的自动注入
def insert_val_into_input(text_label, text_input):
    if not is_auto_restore or text_label["text"] in temp_dic.keys():
        return
    else:
        text_input.insert(temp_dic[text_label["text"]])


# 文本框存储
def save_input_into_dic(text_label, text_input):
    save_dic["__{}__".format(text_label["text"])] = text_input.get(0.0, 20.0).strip()


def save_radio_res_to_dic(radio_label, radio_res):
    key = "__{}__".format(radio_label["text"])
    if radio_res == 0:
        save_dic[key] = '是'
