from tkinter import *
import webbrowser
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText, Scrollbar
import json
import tkinter as tk
from crawler import *
import datetime
from tkinter.messagebox import *
import threading


class MainGUI(tk.Tk):

    def open(self):
        pw = PopupDialog(self)
        self.wait_window(pw)
        return

    def site_manage(self):
        pw = PopupSiteManageDialog(self)
        self.wait_window(pw)
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
            print('url:', url)
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
        if index:
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

    def refresh(self):
        t = threading.Thread(target=self.start_refresh_selected)
        t.start()

    def start_refresh_selected(self):
        self.progress.set(0)
        index_tuple = self.listbox.curselection()
        if index_tuple:
            index = index_tuple[0]
            value = self.listbox.get(index)
            try:
                result = newsCrawl(self, [value])
            except Exception as e:
                showerror(title='错误❌', message='网络异常，更新失败')
            else:
                keys = result.keys()
                for key in keys:
                    if result[key]:
                        prev_dict = self.data_source[key]
                        new_dict = result[key]
                        new_dict_keys = new_dict.keys()
                        for key1 in new_dict_keys:
                            if prev_dict.get(key1):
                                new_dict[key1] = prev_dict[key1]
                                new_dict[key1]['updated_at'] = \
                                    str(datetime.datetime.now().replace(microsecond=0))
                        self.data_source[key] = new_dict
                try:
                    json.dump(self.data_source, open('data.json', 'w'))
                    self.on_click_listbox(1)
                except Exception as e:
                    showerror(title='错误❌', message='未知异常，请联系开发人员')
                else:
                    showinfo(title='提示✅', message='更新成功！')

    def start_refresh_all(self):
        try:
            result = newsCrawl(self)
        except Exception as e:
            print('error:', e)
            showerror(title='错误❌', message='网络不给力，请尝试单个刷新')
        else:
            keys = result.keys()
            for key in keys:
                if result[key]:
                    prev_dict = self.data_source[key]
                    new_dict = result[key]
                    new_dict_keys = new_dict.keys()
                    for key1 in new_dict_keys:
                        if prev_dict.get(key1):
                            new_dict[key1] = prev_dict[key1]
                            new_dict[key1]['updated_at'] = \
                                str(datetime.datetime.now().replace(microsecond=0))
                    self.data_source[key] = new_dict
            try:
                json.dump(result, open('data.json', 'w'))
                self.on_click_listbox(1)
            except Exception as e:
                print('error:', e)
                showerror(title='错误❌', message='未知异常，请联系开发人员')
            else:
                showinfo(title='提示✅', message='更新成功！')

    def refresh_all(self):
        self.progress.set(0)
        t = threading.Thread(target=self.start_refresh_all)
        t.start()

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
                               height=32, yscrollcommand=scrolly.set)
        for value in self.data_source_keys:
            self.listbox.insert(END, value)
        self.listbox.bind('<ButtonRelease-1>', self.on_click_listbox)
        self.listbox.pack(side=LEFT)
        scrolly.config(command=self.listbox.yview)
        dataFrame.pack(side=LEFT, anchor=N, padx=41)
        Label(listFrame, text='数据列表', pady=10).grid(row=0, column=0)

        self.tree = ttk.Treeview(listFrame, show='headings', selectmode='extended',
                                 columns=('col1', 'col2', 'col3'), height=30)
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
        listFrame.pack(side=RIGHT)
        refreshFrame = Frame(dataFrame)
        Button(refreshFrame, text="刷新选中", command=self.refresh).pack(padx=10, pady=20)
        Button(refreshFrame, text="刷新全部", command=self.refresh_all).pack(padx=10, pady=20)
        progress_frame = Frame(refreshFrame)
        Label(progress_frame, text='进度条:', width=8).pack(side=LEFT)
        self.progress = Scale(progress_frame, from_=0, to=100, resolution=1,
                              orient=HORIZONTAL, troughcolor='green')
        self.progress.pack(side=LEFT)
        progress_frame.pack(padx=10, pady=20)
        refreshFrame.pack(side=LEFT)

        mainFrame.pack()
        top = Menu(self, font=("黑体", 12, "bold"))
        self.config(menu=top)
        file = Menu(top, tearoff=0, font=("黑体", 12, "bold"))
        file.add_command(label='添加收藏', command=self.open, underline=0)
        file.add_separator()
        file.add_command(label='收藏管理', command=self.site_manage, underline=0)
        file.add_command(label='退出', command=sys.exit, underline=0)
        top.add_cascade(label='文件', menu=file, underline=0)
        # help_menu = Menu(top, tearoff=0, font=("黑体", 12, "bold"))
        # help_menu.add_command(label='帮助')
        # top.add_cascade(label='帮助', menu=help_menu)
        self.mainloop()


class PopupDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('添加收藏')
        self.parent = parent
        mainFrame = Frame(self)
        mainFrame.pack(fill="x")
        categoryFrame = Frame(mainFrame)
        Label(categoryFrame, text='标签：', width=8).pack(side=LEFT)
        categoryFrame.pack(pady=20)
        self.site_name_entry = Entry(categoryFrame, width=20)
        self.site_name_entry.pack(side=LEFT)
        urlFrame = Frame(mainFrame)
        urlFrame.pack(pady=20)
        Label(urlFrame, text='网址：', width=8).pack(side=LEFT)
        self.site_url = tk.StringVar()
        Entry(urlFrame, textvariable=self.site_url, width=20).pack(side=LEFT)
        buttonFrame = Frame(mainFrame)
        Button(buttonFrame, text="确定", command=self.ok).pack(side=LEFT, padx=10)
        Button(buttonFrame, text="取消", command=self.cancel).pack(side=LEFT, padx=10)
        buttonFrame.pack(padx=100)

    def ok(self):
        name = self.site_name_entry.get()
        url = self.site_url.get()
        if name and url:
            site_data = json.load(open('site_manage.json'))
            site_data['site'].append({name: url})
            json.dump(site_data, open('site_manage.json', 'w'))
        self.destroy()

    def cancel(self):
        self.destroy()


class PopupSiteManageDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('收藏管理')
        self.parent = parent
        mainFrame = Frame(self)
        mainFrame.pack(fill="x")
        leftFrame = Frame(mainFrame)
        scrolly = Scrollbar(leftFrame)
        scrolly.pack(side=RIGHT, fill=Y)
        lb = Label(leftFrame, text='数据源', pady=10)
        lb.pack(side=TOP)
        data = json.load(open('site_manage.json'))
        site_data_list = data['site']
        self.site_Manage_listbox = Listbox(leftFrame, selectmode=MULTIPLE, width=30,
                                           height=22, yscrollcommand=scrolly.set)
        for data in site_data_list:
            self.site_Manage_listbox.insert(END, list(data.keys())[0])
        self.site_Manage_listbox.bind('<Double-Button-1>', self.on_click_listbox)
        self.site_Manage_listbox.pack(side=LEFT, padx=20, pady=10)
        scrolly.config(command=self.site_Manage_listbox.yview)
        leftFrame.pack(side=LEFT)
        rightFrame = Frame(mainFrame)
        Button(rightFrame, text="移除", command=self.remove).pack(side=LEFT, padx=20)
        rightFrame.pack(side=RIGHT)

    def remove(self):
        index_tuple = self.site_Manage_listbox.curselection()
        if index_tuple:
            data = json.load(open('site_manage.json'))
            site_data_list = data['site']
            index_list = list(index_tuple)
            index_list.sort(key=lambda x:-x)
            for index in index_list:
                del site_data_list[index]
                self.site_Manage_listbox.delete(index)
            data['site'] = site_data_list
            json.dump(data, open('site_manage.json', 'w'))

    def on_click_listbox(self, event):
        data = json.load(open('site_manage.json'))
        site_data_list = data['site']
        index = self.site_Manage_listbox.curselection()
        print(index)
        key = self.site_Manage_listbox.get(index[0])
        print(key)
        for site in site_data_list:
            print('site:', site)
            value = site.get(key, None)
            print('value:', value)
            if value:
                webbrowser.open(value)
                break