from temp_storage import *
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import deal_with_file as df


class EditText:
    def __init__(self, root, title, default=''):
        super().__init__()
        self.frame = Frame(root, padx=2)  # container
        self.title = title
        self.label = Label(self.frame, text='{}：'.format(title), bg='Lavender')
        self.label.grid(row=0, column=0)
        self.text = Text(self.frame, height=1, width=70, relief=RAISED, highlightcolor='black',
                         highlightthickness=1)
        self.default = default
        self.text.insert('0.0', self.default)
        insert_val_into_input(self.title, self.text)
        self.text.grid(row=0, column=1)

    def text_setting(self, height, width):
        self.text.config(height=height, width=width)

    def set_position(self, row, column, columnspan=1, rowspan=1):
        self.frame.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

    def get_label(self):
        return self.title

    def get_text(self):
        return self.text.get(0.0, 20.0).strip()

    def save_value_into_info_dic(self, info_dic, key=''):
        if key == '':
            key = self.title
        content = self.get_text()
        if content == self.default:
            content = ''
        info_dic['__{}__'.format(key)] = content

    def temp_save(self):
        save_input_into_dic(self.title, self.text)


class GroupButtonWithText:
    def __init__(self, root, title, pos_opt, neg_opt, text_title, text_default=''):
        super().__init__()
        self.frame = Frame(root)  # container
        self.titleV = tk.IntVar(self.frame)
        self.title = title
        self.text_title = text_title
        self.pos_btn = tk.Radiobutton(self.frame, text=pos_opt, variable=self.titleV, value=1,
                                      command=self.btnbool,
                                      bg='Lavender')
        self.neg_btn = tk.Radiobutton(self.frame, text=neg_opt, variable=self.titleV, value=0, command=self.btnbool,
                                      bg='Lavender')
        self.text = EditText(self.frame, text_title, text_default)
        # 设置长宽
        self.text.text_setting(height=2, width=74)
        insert_val_into_input(self.text_title, self.text.text)
        insert_radio_res_to_button(self.title, self.titleV, (self.pos_btn, self.neg_btn))

        self.pos_btn.grid(row=0, column=0)
        self.neg_btn.grid(row=1, column=0)
        self.text.frame.grid(row=0, column=1, rowspan=2)

    def btnbool(self):
        print(self.titleV.get())
        if self.titleV.get() == 0:
            self.text.text.config(state=DISABLED)
        else:
            self.text.text.config(state=NORMAL)

    def save_value_into_info_dic(self, info_dic):
        if self.titleV.get() == 1:
            info_dic["__{}__".format(self.title)] = '是'
        else:
            info_dic["__{}__".format(self.title)] = '否'
        self.text.save_value_into_info_dic(info_dic)

    def temp_save(self):
        save_radio_res_to_dic(self.title, self.titleV.get())
        self.text.temp_save()

    def set_position(self, row, column, columnspan=1, rowspan=1):
        self.frame.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)


class GroupButton:
    def __init__(self, root, title, pos_opt, neg_opt):
        super().__init__()
        self.frame = Frame(root)  # container
        self.titleV = tk.IntVar(self.frame)
        self.title = title
        self.label = Label(self.frame, text='{}：'.format(title), bg='Lavender')
        self.pos_btn = tk.Radiobutton(self.frame, text=pos_opt, variable=self.titleV, value=1,
                                      bg='Lavender')
        self.neg_btn = tk.Radiobutton(self.frame, text=neg_opt, variable=self.titleV, value=0,
                                      bg='Lavender')
        insert_radio_res_to_button(self.title, self.titleV, (self.pos_btn, self.neg_btn))
        self.label.grid(row=0, column=0, padx=2)
        self.pos_btn.grid(row=0, column=1, padx=2)
        self.neg_btn.grid(row=0, column=2, padx=2)

    def save_value_into_info_dic(self, info_dic):
        if self.titleV.get() == 1:
            info_dic["__{}__".format(self.title)] = '是'
        else:
            info_dic["__{}__".format(self.title)] = '否'

    def temp_save(self):
        save_radio_res_to_dic(self.title, self.titleV.get())

    def set_position(self, row, column, columnspan=1, rowspan=1):
        self.frame.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)


class AddText:
    def __init__(self, root, title, key_word, btn_title, width_list, item_key_list=None):
        super().__init__()
        """
        parameter:
        root 根窗口
        title 标签的标题
        key_word 组件的关键词
        btn_title 按钮标题
        width_list 新开的窗口中对应的每个文本框宽度
        item_key_list 对应新开每个文本框中的关键字 要和上面的宽度列表一一对应
        """
        if item_key_list is None:
            item_key_list = ['']
        self.title = title
        self.key_word = key_word
        self.item_key_list = item_key_list
        self.width_list = width_list  # 子页面中每个item条目宽度
        self.content = []  # 内容的二维数组

        self.frame = Frame(root, bg='Lavender')  # container
        self.label = Label(self.frame, text='{}：'.format(title), bg='Lavender')
        self.button = tk.Button(self.frame, text=btn_title, bg='Lavender', command=lambda: self.btn_window())
        self.element_list = []  # 控件中对应的控件，本质上是一个二维数组，与content一一对应
        self.text = Text(self.frame, width=120, heigh=4)
        insert_val_into_input(self.title, self.text)
        self.text.config(state=DISABLED)
        self.label.grid(row=0, column=0)
        self.button.grid(row=3, column=0)
        self.text.grid(row=0, column=1, columnspan=5, rowspan=4, padx=4)

    def btn_window(self):
        if len(self.item_key_list) < 1:
            return
        info_window = Toplevel()
        info_window.title('{}添加'.format(self.title))
        info_window.config(background='Lavender')
        info_window.geometry('1280x590')

        btn_gen = tk.Button(info_window, text='新增{}信息'.format(self.key_word),
                            command=lambda: self.add_item(info_window, len(self.element_list) + 1))
        btn_done = tk.Button(info_window, text='信息确认完成', command=lambda: self.done(info_window))
        btn_gen.grid(row=0, column=0, columnspan=3)
        btn_done.grid(row=0, column=3, columnspan=3)
        self.convert_text_to_content(self.text.get(0.0, 40.0).strip())
        self.element_list = []
        for i, item in enumerate(self.content):
            self.add_item(info_window, i + 1)

    def rendering(self):
        for row, row_item in enumerate(self.element_list, start=1):
            row_item[0].frame.grid(row=row, column=0)
            row_item[1].grid(row=row, column=1)

    def add_item(self, root, index):
        row_item = []
        window_item = self.WindowItem(root, index, self.key_word, self.width_list,
                                      self.content[index - 1] if index <= len(self.content) else [], self.item_key_list)
        row_item.append(window_item)
        btn_del = Button(root, text='删除{}信息'.format(self.key_word), command=lambda: self.delete_item(index))
        row_item.append(btn_del)
        self.element_list.append(row_item)
        self.rendering()

    def delete_item(self, i):
        index = i - 1
        self.element_list[index][0].destroy_all()
        self.element_list[index][1].destroy()
        self.element_list.pop(index)
        for row, element in enumerate(self.element_list):
            element[0].change_index(row + 1)
            element[1].config(command=lambda: self.delete_item(row + 1))
        self.rendering()

    def done(self, root):
        self.content = []
        info = ''
        for element in self.element_list:
            for word in element[0].get_content():
                info += '{},'.format(word)
            info = info[:-1]
            info += '\n'
        self.text.config(state=NORMAL)
        self.text.delete(0.0, 'end')
        self.text.insert(0.0, info)
        self.text.config(state=DISABLED)
        root.destroy()

    def get_label(self):
        return self.title

    def get_text(self):
        return self.text.get(0.0, 40.0).strip()

    def convert_text_to_content(self, text_content):
        if text_content == '':
            return
        row_list = text_content.split('\n')
        item_list = [row.split(',') for row in row_list]
        self.content = item_list

    def save_value_into_info_dic(self, info_dic):
        row_list = self.get_text().split('\n')
        item_list = [row.split(',') for row in row_list]
        for row in range(len(row_list)):
            for item in range(len(item_list[0])):
                key_str = '__{}{}{}__'.format(self.key_word, row, self.item_key_list[item])
                if item_list[row][item] == '':
                    info_dic[key_str] = '无'
                else:
                    info_dic[key_str] = item_list[row][item]

    def temp_save(self):
        save_input_into_dic(self.title, self.text)

    def set_position(self, row, column, columnspan=1, rowspan=1):
        self.frame.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, pady=4)

    class WindowItem:
        def __init__(self, root, index, key_word, width_list, content=None, item_key_list=None):
            super().__init__()
            if item_key_list is None:
                item_key_list = ['']
            if content is None:
                content = []
            self.index = index
            self.key_word = key_word
            self.item_key_list = item_key_list
            self.width_list = width_list  # 子页面中每个item条目宽度
            self.content = content  # 内容的一维数组
            self.element_list = []  # 控件的一维数组
            self.frame = Frame(root, bg='Lavender')  # container
            for i, key in enumerate(self.item_key_list):
                editText = EditText(self.frame, "{}{}{}".format(self.key_word, index, key))
                editText.text_setting(width=self.width_list[i], height=1)
                self.element_list.append(editText)
                if content:
                    editText.text.insert(0.0, self.content[i])
                editText.frame.grid(row=0, column=i)

        def get_content(self):
            self.content = []
            for element in self.element_list:
                self.content.append(element.get_text())
            return self.content

        def change_index(self, index):
            for i in range(len(self.element_list)):
                self.element_list[i].label.config(text="{}{}{}: ".format(self.key_word, index, self.item_key_list[i]))

        def destroy_all(self):
            for element in self.element_list:
                element.frame.destroy()
                element.text.destroy()
                element.label.destroy()


# root = Tk()
# root.config(background='Lavender')
# app = AddText(root, "吴瀚之", "合同", "修改", [8, 12], ['产品', '技术'])
# app.set_position(row=0, column=0)
# app1 = GroupButtonWithText(root, '吴瀚之帅不帅', '1', '0', 'title')
# app1.set_position(row=1, column=0)
# root.mainloop()
