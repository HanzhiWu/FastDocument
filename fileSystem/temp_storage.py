temp_dic = {}
is_auto_restore = False
save_dic = {}
'''
1. 存储时，当前页面的所有填写过的内容存入缓存文件中，最后存储的就是temp_dic的所有内容
2. 在每个页面跳转下一个页面的时候，需要调用一下当前页面的存储函数，缓存当前页面的文本框中所有的内容
2. 读取时,将临时文件中的key经过处理存入temp_dic
3. 在页面的每个页面的每个控件进行检查，如果有就进行注入
'''


# 将选取的文件处理成为temp_dic 将自动填入的开关打开
def read_file_to_temp_list(temp_file):
    global is_auto_restore
    is_auto_restore = True
    """
    将读取到的文件生成yml
    """
    return temp_dic


def gen_temp_storage():
    global is_auto_restore
    is_auto_restore = False
    """
    将已有的temp_dic生成yml存到对应的文件夹下
    """


# 文本框的自动注入
def insert_val_into_input(text_label, text_input):
    if not is_auto_restore or text_label in temp_dic.keys():
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
        temp_dic[key] = '是'
    else:
        temp_dic[key] = '否'


def insert_radio_res_to_button(label_text, buttonV):
    if is_auto_restore and temp_dic[label_text] is not None:
        if temp_dic[label_text] == '是':
            buttonV.set(1)
        else:
            buttonV.set(0)
