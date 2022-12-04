'''
Author: vxfla 1849062059@qq.com
Date: 2022-09-30 14:29:16
LastEditors: vxfla 1849062059@qq.com
LastEditTime: 2022-12-04 16:58:38
FilePath: /FastDocument/fileSystem/temp_storage.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import datetime
import os 

temp_dic = {}
is_auto_restore = False
save_dic = {}
'''
1. 存储时，当前页面的所有填写过的内容存入缓存文件中，最后存储的就是temp_dic的所有内容
2. 在每个页面跳转下一个页面的时候，需要调用一下当前页面的存储函数，缓存当前页面的文本框中所有的内容
2. 读取时,将临时文件中的key经过处理存入temp_dic
3. 在页面的每个页面的每个控件进行检查，如果有就进行注入
'''
from tempfile import tempdir
import yaml


# 将选取的文件处理成为temp_dic 将自动填入的开关打开
def read_file_to_temp_list(temp_file):
    global is_auto_restore
    is_auto_restore = True
    """
    将读取到的文件生成yml
    """
    global temp_dic
    with open(temp_file, 'r', encoding='utf8') as y:
        temp_dic = yaml.safe_load(y.read())

    return temp_dic


def gen_temp_storage():
    global is_auto_restore
    is_auto_restore = False
    """
    将已有的temp_dic生成yml存到对应的文件夹下
    """
    global temp_dic
    year = temp_dic['记录年份'] if '记录年份' in temp_dic else datetime.datetime.now().strftime("%Y")
    name = temp_dic['企业名称'] if '企业名称' in temp_dic else '未命名企业'
    proj = temp_dic['template_id'].split('-')[2] if 'template_id' in temp_dic else 'unknown'
    li = [year, name, proj, '信息存档.txt']
    filename = '-'.join(li)
    filepath = os.path.join('save', filename[:-4])
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    for path in ['01管理手册', '02程序文件', '03三层文件', '04记录资料', '05内审管评']:
        if not os.path.exists(os.path.join(filepath, path)):
            os.makedirs(os.path.join(filepath, path))

    with open(os.path.join(filepath, filename), 'w', encoding='utf-8') as f:
        yaml.dump(data=temp_dic, stream=f, allow_unicode=True)


# 文本框的自动注入
def insert_val_into_input(text_label, text_input):
    if not is_auto_restore or not text_label in temp_dic.keys():
        return
    else:
        text_input.delete(0.0, 'end')
        text_input.insert(0.0, temp_dic[text_label])


# 文本框存储
def save_input_into_dic(text_label, text_input):
    text = text_input.get(0.0, 20.0).strip()
    if text != '':
        temp_dic[text_label] = text_input.get(0.0, 20.0).strip()


def save_radio_res_to_dic(label_text, radio_res):
    key = label_text
    if radio_res == 0:
        temp_dic[key] = '否'
    else:
        temp_dic[key] = '是'


def insert_radio_res_to_button(label_text, value, btns):
    if is_auto_restore and label_text in temp_dic:
        if temp_dic[label_text] == '是':
            value.set(1)
            btns[0].select()
        else:
            value.set(0)
            btns[1].select()


def clear_temp_storage():
    global temp_dic
    temp_dic = {}


def add_item_temp_storage(key, val):
    global temp_dic
    temp_dic[key] = val
