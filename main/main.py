from tkinter import *
import webbrowser
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText, Scrollbar
import json
import tkinter as tk
from crawler import *


class MainGUI(tk.Tk):

    def open(self):
        pw = PopupDialog(self)
        self.wait_window(pw)  # 这一句很重要！！！
        return

    def site_manage(self):
        pw = PopupSiteManageDialog(self)
        self.wait_window(pw)  # 这一句很重要！！！
        return

    def onDBClick(self, event):
        if self.tree.selection():
            index = self.listbox.curselection()
            data_source_key = self.listbox.get(index[0])
            item = self.tree.selection()[0]
            values = self.tree.item(item, "values")
            title = values[0]
            data = self.data_source.get(data_source_key)
            url = data[title]['url']
            webbrowser.open(url)
            data[title]['tag'] = 'clicked'
            values_list = []
            keys = data.keys()
            for key in keys:
                values_list.append(data[key])
            self.new_tree(values_list)
            json.dump(self.data_source, open('data.json', 'w'))

    def new_tree(self, values_list):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        i = 1
        for value in values_list:
            if value.get('tag'):
                self.tree.insert('', i, values=(value.get('title', ''),
                                                value.get('published_at', ''),
                                                value.get('updated_at', '')),
                                 tags=value.get('tag'))
            else:
                self.tree.insert('', i, values=(value.get('title', ''),
                                                value.get('published_at', ''),
                                                value.get('updated_at', '')))
            i += 1

    def on_click_listbox(self, event):
        index = self.listbox.curselection()
        key = self.listbox.get(index[0])
        values_dict = self.data_source.get(key, [])
        values_list = []
        keys = values_dict.keys()
        for key in keys:
            values_list.append(values_dict[key])
        self.new_tree(values_list)

    def add_data_source(self, item):
        self.data_source.append(item)

    def get_data_source(self):
        data = json.load(open('data.json'))
        return data

    def __init__(self):
        super().__init__()
        # self.iconbitmap('calculator.ico')
        self.title('news easier')
        self.geometry('+100+100')
        self.minsize(400, 400)
        mainFrame = Frame(self)
        dataFrame = Frame(mainFrame)
        listFrame = Frame(mainFrame)
        lb = Label(dataFrame, text='数据源', pady=10)
        lb.pack(side=TOP)
        self.data_source = self.get_data_source()
        self.data_source_keys = self.data_source.keys()
        scrolly = Scrollbar(dataFrame)
        scrolly.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(dataFrame, selectmode=BROWSE, width=20,
                               height=22, yscrollcommand=scrolly.set)
        for value in self.data_source_keys:
            self.listbox.insert(END, value)
        self.listbox.bind('<ButtonRelease-1>', self.on_click_listbox)
        self.listbox.pack(side=LEFT)
        scrolly.config(command=self.listbox.yview)
        dataFrame.pack(side=LEFT, anchor=N, padx=41)
        Label(listFrame, text='数据列表', pady=10).grid(row=0, column=0)

        self.tree = ttk.Treeview(listFrame, show='headings', selectmode='extended',
                                 columns=('col1', 'col2', 'col3'), height=20)
        self.tree.column('col1', width=400, anchor='center')
        self.tree.column('col2', width=200, anchor='center')
        self.tree.column('col3', width=200, anchor='center')
        self.tree.heading('col1', text='标题')
        self.tree.heading('col2', text='发布时间')
        self.tree.heading('col3', text='更新时间')
        ysb = ttk.Scrollbar(listFrame, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(listFrame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.tag_configure('clicked', background='LightGrey')
        self.tree.grid(row=1, column=0)
        ysb.grid(row=1, column=1, sticky='ns')
        xsb.grid(row=2, column=0, sticky='ew')
        self.tree.bind("<Double-1>", self.onDBClick)
        listFrame.pack()
        mainFrame.pack()
        top = Menu(self, font=("黑体", 15, "bold"))
        self.config(menu=top)
        file = Menu(top, tearoff=0, font=("黑体", 15, "bold"))
        file.add_command(label='添加网址', command=self.open, underline=0)
        file.add_separator()
        file.add_command(label='站点管理', command=self.site_manage, underline=0)
        file.add_command(label='退出', command=sys.exit, underline=0)
        top.add_cascade(label='文件', menu=file, underline=0)
        help_menu = Menu(top, tearoff=0, font=("黑体", 15, "bold"))
        help_menu.add_command(label='帮助')
        top.add_cascade(label='帮助', menu=help_menu)
        self.mainloop()


class PopupDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('添加新网址')
        self.parent = parent
        mainFrame = Frame(self)
        mainFrame.pack(fill="x")
        categoryFrame = Frame(mainFrame)
        Label(categoryFrame, text='网站名称：', width=8).pack(side=LEFT)
        categoryFrame.pack(pady=20)
        self.site_name_entry = Entry(categoryFrame, width=20)
        # self.site_name_text = Text(categoryFrame, height=2)
        self.site_name_entry.pack(side=LEFT)
        urlFrame = Frame(mainFrame)
        urlFrame.pack(pady=20)
        Label(urlFrame, text='网址：', width=8).pack(side=LEFT)
        self.site_url = tk.StringVar()
        Entry(urlFrame, textvariable=self.site_url, width=20).pack(side=LEFT)
        buttonFrame = Frame(mainFrame)
        Button(buttonFrame, text="确定", command=self.ok).pack(side=LEFT)
        Button(buttonFrame, text="取消", command=self.cancel).pack(side=LEFT)
        buttonFrame.pack(padx=100)

    def ok(self):
        name = self.site_name_entry.get()
        url = self.site_url.get()
        site_data = json.load(open('site_manage.json'))
        site_data['site'].append({name: url})
        json.dump(site_data, open('site_manage.json', 'w'))
        self.destroy()

    def cancel(self):
        self.destroy()


class PopupSiteManageDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('站点管理')
        self.parent = parent
        mainFrame = Frame(self)
        mainFrame.pack(fill="x")
        scrolly = Scrollbar(mainFrame)
        scrolly.pack(side=RIGHT, fill=Y)
        data = json.load(open('site_manage.json'))
        site_data_list = data['site']
        self.site_Manage_listbox = Listbox(mainFrame, selectmode=BROWSE, width=20,
                                           height=22, yscrollcommand=scrolly.set)
        for data in site_data_list:
            self.site_Manage_listbox.insert(END, list(data.keys())[0])
        self.site_Manage_listbox.bind('<ButtonRelease-1>', self.on_click_listbox)
        self.site_Manage_listbox.pack(side=LEFT)
        scrolly.config(command=self.site_Manage_listbox.yview)

    def on_click_listbox(self, event):
        data = json.load(open('site_manage.json'))
        site_data_list = data['site']
        index = self.site_Manage_listbox.curselection()
        key = self.site_Manage_listbox.get(index[0])
        for site in site_data_list:
            value = site.get(key, None)
            if value:
                webbrowser.open(value)
            break



if __name__ == '__main__':
    main = MainGUI()

