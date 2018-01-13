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
import http.client


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

    def color_config(self):
        pw = ColorConfigDialog(self)
        self.wait_window(pw)
        return

    def popup_new_contents(self):
        if hasattr(self, 'pw'):
            try:
                self.pw.update_content()
            except Exception:
                self.pw = ShowNewSitesDialog(self)
                self.wait_window(self.pw)
                return
        else:
            self.pw = ShowNewSitesDialog(self)
            self.wait_window(self.pw)
            return

    @property
    def get_all_key_url(self):
        data_source = self.data_source
        all_key_url = dict()
        for list_key in data_source:
            for key in data_source[list_key]:
                if key != 'ratio':
                    all_key_url[key] = data_source[list_key][key]['url']
        return all_key_url

    def onDBClick(self, event=None):
        if self.tree.selection():
            data_source_key = self.current_listbox_selected
            item = self.tree.selection()[0]
            values = self.tree.item(item, "values")
            title = values[0]
            data = self.data_source.get(data_source_key)
            url = self.get_all_key_url[title]
            webbrowser.open(url)
            try:
                data[title]['tag'] = 'clicked'
            except Exception as e:
                pass
            else:
                values_list = []
                keys = data.keys()
                for key in keys:
                    value = data[key]
                    if isinstance(value, dict):
                        values_list.append(value)
                values_list.sort(key=lambda x: x['published_at'], reverse=True)
                self.new_tree(values_list)
                readed_num = 0
                if data.get('ratio', None):
                    total = len(data) - 1
                else:
                    total = len(data)
                for item in data:
                    value = data[item]
                    if isinstance(value, dict):
                        if value.get('tag', None):
                            readed_num += 1
                unread_num = total - readed_num
                ratio = '[{}/{}]'.format(unread_num, readed_num)
                data['ratio'] = ratio
                self.data_source[data_source_key] = data
                json.dump(self.data_source, open('data.json', 'w'))
                self.refresh_listbox()
                json.dump(self.data_source, open('data.json', 'w'))

    def new_tree(self, values_list):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        i = 1
        for value in values_list:
            if value.get('tag', None):
                self.tree.insert('', i, values=(value.get('title', ''),
                                                value.get('published_at', '').strip().strip('()').strip('[]'),
                                                value.get('updated_at', '')),
                                 tags=value.get('tag'))
            else:
                self.tree.insert('', i, values=(value.get('title', ''),
                                                value.get('published_at', '').strip().strip('()').strip('[]'),
                                                value.get('updated_at', '')),)
            i += 1

    def on_click_listbox(self, event):
        index = self.listbox.curselection()
        key = None
        if index:
            key = self.listbox.get(index[0]).split(' ')[0]
            self.current_listbox_selected = key
            key = self.current_listbox_selected
            if key:
                data_source = self.get_data_source()
                values_dict = data_source.get(key, {})
                values_list = []
                if values_dict:
                    keys = values_dict.keys()
                    for key in keys:
                        value = values_dict[key]
                        if isinstance(value, dict):
                            values_list.append(value)
                    values_list.sort(key=lambda x: x['published_at'], reverse=True)
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
        self.new_list = []
        self.progress.set(0)
        if self.current_listbox_selected:
            value = self.current_listbox_selected
            current_key = value.split(' ')[0]
            try:
                result = newsCrawl(self, [value])
            except Exception as e:
                time.sleep(5)
                self.start_refresh_selected()
            else:
                keys = result.keys()
                for key in keys:
                    if result[key]:
                        prev_dict = self.data_source[key]
                        new_dict = result[key]
                        new_dict_keys = new_dict.keys()
                        if len(new_dict) < len(prev_dict)-1:
                            for key1 in new_dict_keys:
                                if prev_dict.get(key1):
                                    prev_dict[key1]['updated_at'] = \
                                        str(datetime.datetime.now().replace(microsecond=0))
                                else:
                                    new_dict[key1]['updated_at'] = \
                                        str(datetime.datetime.now().replace(microsecond=0))
                                    new_dict[key1]['ref'] = key
                                    self.new_list.append(new_dict[key1])
                            new_dict.update(prev_dict)
                        else:
                            for key1 in new_dict_keys:
                                if prev_dict.get(key1):
                                    new_dict[key1] = prev_dict[key1]
                                    new_dict[key1]['updated_at'] = \
                                        str(datetime.datetime.now().replace(microsecond=0))
                                else:
                                    new_dict[key1]['updated_at'] = \
                                        str(datetime.datetime.now().replace(microsecond=0))
                                    new_dict[key1]["ref"] = key
                                    self.new_list.append(new_dict[key1])
                        readed_num = 0
                        if new_dict.get('ratio', None):
                            total = len(new_dict) - 1
                        else:
                            total = len(new_dict)
                        for item in new_dict:
                            value = new_dict[item]
                            if isinstance(value, dict) and value.get('tag', None):
                                readed_num += 1
                        unread_num = total - readed_num
                        ratio = '[{}/{}]'.format(unread_num, readed_num)
                        self.data_source[key] = new_dict
                        self.data_source[key]['ratio'] = ratio
                    else:
                        if key == current_key:
                            self.data_source[key] = {}
                try:
                    json.dump(self.data_source, open('data.json', 'w'))
                except Exception as e:
                    pass
                else:
                    self.on_click_listbox(1)
                    self.refresh_listbox()
                    if self.new_list:
                        self.popup_new_contents()

    def start_refresh_all(self, auto=None):
        self.new_list = []
        try:
            result = newsCrawl(self)
        except Exception as e:
            time.sleep(5)
            self.start_refresh_all(auto=auto)
        else:
            keys = result.keys()
            for key in keys:
                if result[key]:
                    prev_dict = self.data_source[key]
                    new_dict = result[key]
                    new_dict_keys = new_dict.keys()
                    if len(new_dict) < len(prev_dict):
                        for key1 in new_dict_keys:
                            if prev_dict.get(key1, None):
                                prev_dict[key1]['updated_at'] = \
                                    str(datetime.datetime.now().replace(microsecond=0))
                            else:
                                new_dict[key1]['updated_at'] = \
                                    str(datetime.datetime.now().replace(microsecond=0))
                                new_dict[key1]["ref"] = key
                                self.new_list.append(new_dict[key1])
                        new_dict.update(prev_dict)
                    else:
                        for key1 in new_dict_keys:
                            if prev_dict.get(key1, None):
                                new_dict[key1] = prev_dict[key1]
                                new_dict[key1]['updated_at'] = \
                                    str(datetime.datetime.now().replace(microsecond=0))
                            else:
                                new_dict[key1]['updated_at'] = \
                                    str(datetime.datetime.now().replace(microsecond=0))
                                new_dict[key1]["ref"] = key
                                self.new_list.append(new_dict[key1])

                    readed_num = 0
                    if new_dict.get('ratio', None):
                        total = len(new_dict) - 1
                    else:
                        total = len(new_dict)
                    for item in new_dict:
                        value = new_dict[item]
                        if isinstance(value, dict) and value.get('tag', None):
                            readed_num += 1
                    unread_num = total - readed_num
                    ratio = '[{}/{}]'.format(unread_num, readed_num)
                    self.data_source[key] = new_dict
                    self.data_source[key]['ratio'] = ratio
            try:
                json.dump(self.data_source, open('data.json', 'w'))
                self.on_click_listbox(1)
            except Exception as e:
                pass
            else:
                self.refresh_listbox()
                if self.new_list:
                    self.popup_new_contents()

    def refresh_all(self):
        self.progress.set(0)
        t = threading.Thread(target=self.start_refresh_all)
        t.start()

    def auto_refresh_all(self):
        while True:
            try:
                data = json.load(open('refresh_time.json', 'r'))
            except Exception as e:
                pass
            else:
                time_refresh = data.get('time', 0)
                if time_refresh:
                    time_refresh = int(time_refresh) * 60
                    self.progress.set(0)
                    try:
                        t = threading.Thread(target=self.start_refresh_all, args=(True,))
                        # self.start_refresh_all(True)
                        t.start()
                    except Exception:
                        pass
                    time.sleep(time_refresh)

    def search(self, event=None):
        keyword = self.keywordEntry.get()
        data_source_keys = self.data_source.keys()
        keys_list = []
        total_values_dict = dict()
        for key in data_source_keys:
            values_dict = self.data_source.get(key, [])
            total_values_dict.update(values_dict)
            keys = values_dict.keys()
            keys_list += keys
        values_list = []
        for key in keys_list:
            if isinstance(total_values_dict[key], dict):
                title = total_values_dict[key]['title']
                if keyword in title:
                    values_list.append(total_values_dict[key])
        values_list.sort(key=lambda x: x['published_at'], reverse=True)
        self.new_tree(values_list)

    def rightKey(self, event):
        try:
            self.menubar.post(event.x_root, event.y_root)
        except:
            pass

    def mark_read(self, event=None):
        if self.tree.selection():
            data_source_key = self.current_listbox_selected
            items = self.tree.selection()
            data = self.data_source.get(data_source_key)
            try:
                for item in items:
                    values = self.tree.item(item, "values")
                    title = values[0]
                    data[title]['tag'] = 'clicked'
            except:
                pass
            else:
                values_list = []
                keys = data.keys()
                for key in keys:
                    value = data[key]
                    if isinstance(value, dict):
                        values_list.append(data[key])
                values_list.sort(key=lambda x: x['published_at'], reverse=True)
                self.new_tree(values_list)

                readed_num = 0
                if data.get('ratio', None):
                    total = len(data) - 1
                else:
                    total = len(data)
                for item in data:
                    value = data[item]
                    if isinstance(value, dict):
                        if value.get('tag', None):
                            readed_num += 1
                unread_num = total - readed_num
                ratio = '[{}/{}]'.format(unread_num, readed_num)
                data['ratio'] = ratio
                self.data_source[data_source_key] = data
                json.dump(self.data_source, open('data.json', 'w'))
                self.refresh_listbox()

    def refresh_listbox(self):
        index = self.listbox.curselection()
        data_source = self.get_data_source()
        self.data_source_keys = data_source.keys()
        self.listbox.delete(0, END)
        for key in self.data_source_keys:
            value = self.data_source[key]
            ratio = value.get('ratio', '')
            new_key = key + '   ' + ratio
            self.listbox.insert(END, new_key)
        if index:
            self.listbox.select_set(index)

    def __init__(self):
        super().__init__()
        self.iconbitmap('lo.ico')
        self.title('news easier')
        self.geometry('+100+100')
        self.minsize(400, 400)
        self.font_color = 'white'
        self.current_listbox_selected = None
        self.mainFrame = Frame(self, bg=self.font_color)
        self.dataFrame = Frame(self.mainFrame, bg=self.font_color)
        self.listFrame = Frame(self.mainFrame, bg=self.font_color)
        self.data_source_label = Label(self.dataFrame, text='数据源', pady=10, padx=50, bg=self.font_color)
        self.data_source_label.pack(side=TOP, anchor=W)
        self.data_source = self.get_data_source()
        self.data_source_keys = self.data_source.keys()
        scrolly = Scrollbar(self.dataFrame)
        scrolly.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.dataFrame, selectmode=BROWSE, width=25,
                               height=30, yscrollcommand=scrolly.set, bg=self.font_color)
        for key in self.data_source_keys:
            value = self.data_source[key]
            ratio = value.get('ratio', '')
            new_key = key + '   ' + ratio
            self.listbox.insert(END, new_key)
        self.listbox.bind('<ButtonRelease-1>', self.on_click_listbox)
        self.listbox.pack(side=LEFT)
        scrolly.config(command=self.listbox.yview)
        self.dataFrame.pack(side=LEFT, anchor=N, padx=41)
        self.list_search_frame = Frame(self.listFrame, bg=self.font_color)
        list_show_frame = Frame(self.listFrame)
        self.keyword_label = Label(self.list_search_frame, text='关键字:', pady=10, bg=self.font_color)
        self.keyword_label.pack(side=LEFT)
        self.keywordEntry = Entry(self.list_search_frame)
        self.keywordEntry.bind('<Return>', self.search)
        self.keywordEntry.pack(side=LEFT)
        a = Button(self.list_search_frame, text='搜索', command=self.search, padx=20, bg=self.font_color)
        a.pack(side=LEFT, padx=50)
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
        self.tree.bind("<Button-3>", self.rightKey)
        self.tree.bind("<Shift-A>", self.mark_read)
        self.menubar = Menu(self.tree, tearoff=False)
        self.menubar.add_command(label='打开', command=self.onDBClick)
        self.menubar.add_command(label='标记已读', command=self.mark_read)

        self.list_search_frame.pack(side=TOP)
        list_show_frame.pack(side=BOTTOM)
        self.listFrame.pack(side=RIGHT)
        self.refreshFrame = Frame(self.dataFrame, bg=self.font_color)
        Button(self.refreshFrame, text="刷新选中", command=self.refresh, bg=self.font_color).pack(padx=10, pady=20)
        Button(self.refreshFrame, text="刷新全部", command=self.refresh_all, bg=self.font_color).pack(padx=10, pady=20)
        self.progress_frame = Frame(self.refreshFrame, bg=self.font_color)
        self.progress_label = Label(self.progress_frame, text='进度条:', width=8, bg=self.font_color)
        self.progress_label.pack(side=LEFT)
        self.progress = Scale(self.progress_frame, from_=0, to=100, resolution=1,
                              orient=HORIZONTAL, troughcolor='green', bg=self.font_color)
        self.progress.pack(side=LEFT)
        self.progress_frame.pack(padx=10, pady=20)
        self.refreshFrame.pack(side=LEFT)

        self.mainFrame.pack()
        top = Menu(self, font=("黑体", 10, "bold"))
        self.config(menu=top)
        file = Menu(top, tearoff=0, font=("黑体", 10, "bold"))
        file.add_command(label='添加收藏', command=self.open, underline=0)
        file.add_command(label='收藏管理', command=self.site_manage, underline=0)
        file.add_separator()
        file.add_command(label='刷新设置', command=self.refresh_config, underline=0)
        file.add_command(label='颜色设置', command=self.color_config, underline=0)
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
            data['time'] = float(refresh_time)
            json.dump(data, open('refresh_time.json', 'w'))
        self.destroy()

    def cancel(self):
        self.destroy()


class ColorConfigDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('背景颜色设置')
        self.parent = parent
        self.color = 'yellow'
        mainFrame = Frame(self)
        mainFrame.pack(fill="x")
        colorFrame = Frame(mainFrame)
        Label(colorFrame, text='背景颜色：', width=8).pack(side=LEFT)
        colorFrame.pack(pady=20)
        self.color_var = tk.StringVar()
        numberChosen = ttk.Combobox(colorFrame, width=12, textvariable=self.color_var)
        numberChosen['values'] = ('白色', '黄色', '红色', '蓝色', '棕色', '海洋绿', '紫色')  # 设置下拉列表的值
        numberChosen.pack(pady=20)  # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(0)
        buttonFrame = Frame(mainFrame)
        Button(buttonFrame, text="确定", command=self.ok).pack(side=LEFT, padx=5)
        Button(buttonFrame, text="取消", command=self.cancel).pack(side=LEFT, padx=5)
        buttonFrame.pack(padx=100)

    def ok(self):
        map = {'白色': 'white', '黄色': 'yellow', '红色': 'red',
               '蓝色': 'blue', '棕色': 'Brown', '海洋绿': 'SeaGreen', '紫色': 'Purple'}
        color = self.color_var.get()
        en_color = map[color]
        self.parent.mainFrame.configure(bg=en_color)
        self.parent.dataFrame.configure(bg=en_color)
        self.parent.listFrame.configure(bg=en_color)
        self.parent.data_source_label.configure(bg=en_color)
        self.parent.listbox.configure(bg=en_color)
        self.parent.list_search_frame.configure(bg=en_color)
        self.parent.keyword_label.configure(bg=en_color)
        self.parent.refreshFrame.configure(bg=en_color)
        self.parent.progress_frame.configure(bg=en_color)
        self.parent.progress.configure(bg=en_color)
        self.parent.progress_label.configure(bg=en_color)
        self.destroy()

    def cancel(self):
        self.destroy()


class ShowNewSitesDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('最新更新内容')
        self.parent = parent
        self.new_list = parent.new_list
        self.current_listbox_selected = None
        mainFrame = Frame(self)
        mainFrame.pack(fill="x")
        scrolly = Scrollbar(mainFrame)
        scrolly.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(mainFrame, selectmode=BROWSE, width=100,
                               height=20, yscrollcommand=scrolly.set)
        for value in self.new_list:
            title = value.get('title', '')
            ref = value.get('ref', '')
            insert = title + '                    ' + ref
            self.listbox.insert(END, insert)
        self.listbox.bind('<Double-1>', self.on_click_listbox)
        self.listbox.pack(side=LEFT, padx=10, pady=10)
        scrolly.config(command=self.listbox.yview)

    def on_click_listbox(self, event):
        index = self.listbox.curselection()
        if index:
            self.current_listbox_selected = self.listbox.get(index[0])
            if self.current_listbox_selected:
                for item in self.new_list:
                    selected = self.current_listbox_selected.split("                    ")[0]
                    if item['title'] == selected:
                        webbrowser.open(item['url'])
                        break

    def update_content(self):
        for value in self.parent.new_list:
            if value not in self.new_list:
                title = value.get('title', '')
                ref = value.get('ref', '')
                insert = title + '          ' + ref
                self.listbox.insert(END, insert)
                self.new_list.append(value)

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
        key = self.site_Manage_listbox.get(index[0])
        for site in site_data_list:
            value = site.get(key, None)
            if value:
                webbrowser.open(value)
                break


def get_webservertime(host):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", "/")
    r = conn.getresponse()
    ts = r.getheader('date')
    if not ts:
        return None
    else:
        ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
        ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
        return (ttime.tm_year, ttime.tm_mon, ttime.tm_mday)

def start():
    date = get_webservertime('www.baidu.com')
    if date is None:
        MainGUI()
    else:
        if date[0] <= 2017:
            if date[1] <= 12:
                if date[2] <= 31:
                    MainGUI()
        elif date[0] == 2018:
            if date[1] <= 1:
                if date[2] <= 30:
                    MainGUI()