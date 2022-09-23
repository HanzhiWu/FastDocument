from temp_storage import *


class EditText:
    def __init__(self, root, title):
        super().__init__()
        self.frame = Frame(root, padx=2)  # container
        self.title = title
        self.label = Label(self.frame, text='{}：'.format(title), bg='Lavender')
        self.label.grid(row=0, column=0)
        self.text = Text(self.frame, height=1, width=70, relief=RAISED, highlightcolor='black',
                         highlightthickness=1)
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
        info_dic['__{}__'.format(key)] = self.get_text()

    def temp_save(self):
        save_input_into_dic(self.title, self.text)


class GroupButtonWithText:
    def __init__(self, root, title, pos_opt, neg_opt, text_title):
        super().__init__()
        self.frame = Frame(root)  # container
        self.titleV = tk.IntVar()
        self.title = title
        self.text_title = text_title
        self.pos_btn = tk.Radiobutton(self.frame, text=pos_opt, variable=self.titleV, value=1,
                                      command=self.btnbool,
                                      bg='Lavender')
        self.neg_btn = tk.Radiobutton(self.frame, text=neg_opt, variable=self.titleV, value=0, command=self.btnbool,
                                      bg='Lavender')
        self.text = EditText(self.frame, text_title)
        # 设置长宽
        self.text.text_setting(height=2, width=74)
        insert_val_into_input(self.text_title, self.text)
        insert_radio_res_to_button(self.title, self.titleV)

        self.pos_btn.grid(row=0, column=0)
        self.neg_btn.grid(row=1, column=0)
        self.text.frame.grid(row=0, column=1, rowspan=2)

    def btnbool(self):
        if self.titleV.get() == 0:
            self.text.text.config(state=DISABLED)
        else:
            self.text.text.config(state=NORMAL)

    def save_value_into_info_dic(self, info_dic):
        if self.titleV.get() == 1:
            info_dic["__{}__".format(self.title)] = '是'
        else:
            info_dic["__{}__".format(self.title)] = '否'
        info_dic[self.text_title] = self.text.get_text()

    def temp_save(self):
        save_radio_res_to_dic(self.title, self.titleV.get())
        self.text.temp_save()

    def set_position(self, row, column, columnspan=1, rowspan=1):
        self.frame.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)


root = Tk()
app = GroupButtonWithText(root, "吴瀚之", "yes", "no", "what")
app.frame.grid(row=0, column=0)
app1 = GroupButtonWithText(root, "吴瀚之", "yes", "no", "what")
app1.frame.grid(row=0, column=1)

root.mainloop()
