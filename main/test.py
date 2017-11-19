from tkinter import ttk
from tkinter import *

root = Tk()
main = Frame(root)
tree = ttk.Treeview(main, show='headings', selectmode='extended', columns=('col1', 'col2', 'col3'))
tree.column('col1', width=200, anchor='center')
tree.column('col2', width=100, anchor='center')
tree.column('col3', width=100, anchor='center')
tree.heading('col1', text='col1')
tree.heading('col2', text='col2')
tree.heading('col3', text='col3')
ysb = ttk.Scrollbar(main, orient='vertical', command=tree.yview)
xsb = ttk.Scrollbar(main, orient='horizontal', command=tree.xview)
tree.configure(yscroll=ysb.set, xscroll=xsb.set)

tree.grid(row=0, column=0)
ysb.grid(row=0, column=1, sticky='ns')
xsb.grid(row=1, column=0, sticky='ew')


def onDBClick(event):
    item = tree.selection()[0]
    print('item:', tree.item(item, 'values'))
    print("you clicked on ", tree.item(item, "values"))


for i in range(10):
    tree.insert('', i, values=('a' + str(i), 'b' + str(i), 'c' + str(i)))
tree.bind("<Double-1>", onDBClick)
main.pack()
root.mainloop()



# index = 0
        # for key in self.maps:
        #     default_value = StringVar()
        #     default_value.set(key)
        #     label = Entry(listFrame, bg='black', width=20, textvariable=default_value, state='readonly')
        #     label.grid(row=1, column=index)
        #     label.bind('<Button-3>', self.func1)
        #     index += 1
        # listFrame.pack(side=RIGHT, anchor=N, padx=41)