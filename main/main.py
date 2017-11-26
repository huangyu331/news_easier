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
import time


class MainGUI(tk.Tk):

    def open(self):
        pw = PopupDialog(self)
        self.wait_window(pw)
        return

    def site_manage(self):
        pw = PopupSiteManageDialog(self)
        self.wait_window(pw)
        return

    def refresh_config(self):
        pw = RefreshConfigDialog(self)
        self.wait_window(pw)
        return

    def popup_new_contents(self):
        pw = ShowNewSitesDialog(self)
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

    def start_refresh_all(self, auto=None):
        self.new_list = []
        try:
            result = newsCrawl(self)
        except Exception as e:
            print('error:', e)
            showerror(title='错误❌', message='网络不给力，请重试或尝试单个刷新')
            raise Exception()
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
                        else:
                            new_dict[key1]['updated_at'] = \
                                str(datetime.datetime.now().replace(microsecond=0))
                            self.new_list.append(new_dict[key1])
                    self.data_source[key] = new_dict
            try:
                json.dump(result, open('data.json', 'w'))
                self.on_click_listbox(1)
            except Exception as e:
                print('error:', e)
                showerror(title='错误❌', message='未知异常，请联系开发人员')
                raise Exception()
            else:
                if auto:
                    if self.new_list:
                        self.popup_new_contents()
                else:
                    showinfo(title='提示✅', message='更新成功！')

    def refresh_all(self):
        self.progress.set(0)
        t = threading.Thread(target=self.start_refresh_all)
        t.start()

    def auto_refresh_all(self):
        while True:
            try:
                data = json.load(open('refresh_time.json', 'r'))
            except Exception as e:
                print('error:', e)
            else:
                time_refresh = data.get('time', 0)
                if time_refresh:
                    time_refresh = int(time_refresh) * 60
                    self.progress.set(0)
                    try:
                        self.start_refresh_all(True)
                    except Exception:
                        pass
                    time.sleep(time_refresh)

    def search(self):
        keyword = self.keywordEntry.get()
        index = self.listbox.curselection()
        if index:
            key = self.listbox.get(index[0])
            values_dict = self.data_source.get(key, [])
            values_list = []
            keys = values_dict.keys()
            for key in keys:
                title = values_dict[key]['title']
                if keyword in title:
                    values_list.append(values_dict[key])
            self.new_tree(values_list)

    def __init__(self):
        super().__init__()
        # self.iconbitmap('calculator.ico')
        self.title('news easier')
        self.geometry('+100+100')
        self.minsize(400, 400)
        mainFrame = Frame(self)
        dataFrame = Frame(mainFrame)
        listFrame = Frame(mainFrame)
        lb = Label(dataFrame, text='数据源', pady=10, padx=50)
        lb.pack(side=TOP, anchor=W)
        self.data_source = self.get_data_source()
        self.data_source_keys = self.data_source.keys()
        scrolly = Scrollbar(dataFrame)
        scrolly.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(dataFrame, selectmode=BROWSE, width=20,
                               height=30, yscrollcommand=scrolly.set)
        for value in self.data_source_keys:
            self.listbox.insert(END, value)
        self.listbox.bind('<ButtonRelease-1>', self.on_click_listbox)
        self.listbox.pack(side=LEFT)
        scrolly.config(command=self.listbox.yview)
        dataFrame.pack(side=LEFT, anchor=N, padx=41)
        list_search_frame = Frame(listFrame)
        list_show_frame = Frame(listFrame)
        Label(list_search_frame, text='关键字:', pady=10).pack(side=LEFT)
        self.keywordEntry = Entry(list_search_frame)
        self.keywordEntry.pack(side=LEFT)
        Button(list_search_frame, text='搜索', command=self.search, padx=20).pack(side=LEFT, padx=50)
        # Label(list_show_frame, text='数据列表', pady=10).grid(row=1, column=0)
        self.tree = ttk.Treeview(list_show_frame, show='headings', selectmode='extended',
                                 columns=('col1', 'col2', 'col3'), height=28)
        self.tree.column('col1', width=400, anchor='center')
        self.tree.column('col2', width=200, anchor='center')
        self.tree.column('col3', width=200, anchor='center')
        self.tree.heading('col1', text='标题')
        self.tree.heading('col2', text='发布时间')
        self.tree.heading('col3', text='更新时间')
        ysb = ttk.Scrollbar(list_show_frame, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(list_show_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.tag_configure('clicked', background='LightGrey')
        self.tree.grid(row=2, column=0)
        ysb.grid(row=2, column=1, sticky='ns')
        xsb.grid(row=3, column=0, sticky='ew')
        self.tree.bind("<Double-1>", self.onDBClick)
        list_search_frame.pack(side=TOP)
        list_show_frame.pack(side=BOTTOM)
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
        file.add_command(label='收藏管理', command=self.site_manage, underline=0)
        file.add_separator()
        file.add_command(label='刷新设置', command=self.refresh_config, underline=0)
        file.add_separator()
        file.add_command(label='退出', command=sys.exit, underline=0)
        top.add_cascade(label='文件', menu=file, underline=0)
        # help_menu = Menu(top, tearoff=0, font=("黑体", 12, "bold"))
        # help_menu.add_command(label='帮助')
        # top.add_cascade(label='帮助', menu=help_menu)
        t = threading.Thread(target=self.auto_refresh_all)
        t.start()
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


class RefreshConfigDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('自动刷新设置')
        self.parent = parent
        mainFrame = Frame(self)
        mainFrame.pack(fill="x")
        timeFrame = Frame(mainFrame)
        Label(timeFrame, text='时间(分)：', width=8).pack(side=LEFT)
        timeFrame.pack(pady=20)
        default_value = IntVar()
        self.refresh_time_entry = Entry(timeFrame, width=10, textvariable=default_value)
        self.refresh_time_entry.pack(side=LEFT)
        buttonFrame = Frame(mainFrame)
        Button(buttonFrame, text="确定", command=self.ok).pack(side=LEFT, padx=5)
        Button(buttonFrame, text="取消", command=self.cancel).pack(side=LEFT, padx=5)
        buttonFrame.pack(padx=100)

    def ok(self):
        refresh_time = self.refresh_time_entry.get()
        if refresh_time:
            data = json.load(open('refresh_time.json'))
            data['time'] = refresh_time
            json.dump(data, open('refresh_time.json', 'w'))
        self.destroy()

    def cancel(self):
        self.destroy()


class ShowNewSitesDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('最新更新内容')
        self.new_list = parent.new_list
        mainFrame = Frame(self)
        mainFrame.pack(fill="x")
        scrolly = Scrollbar(mainFrame)
        scrolly.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(mainFrame, selectmode=BROWSE, width=100,
                               height=20, yscrollcommand=scrolly.set)

        for value in self.new_list:
            self.listbox.insert(END, value.get('title', ''))
        self.listbox.bind('<ButtonRelease-1>', self.on_click_listbox)
        self.listbox.pack(side=LEFT, padx=10, pady=10)
        scrolly.config(command=self.listbox.yview)

    def on_click_listbox(self, event):
        index = self.listbox.curselection()
        if index:
            key = self.listbox.get(index[0])
            for item in self.new_list:
                print('item:', item)
                if item['title'] == key:
                    webbrowser.open(item['url'])
                    break

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