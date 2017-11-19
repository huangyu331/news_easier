#coding:utf-8
#author__ = 'Huang Yu'

import tkinter
from math import e
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
# from pyh import *


class MainGUI:
    def __init__(self):
        root = Tk()
        root.iconbitmap('calculator.ico')
        root.title('压区计算')
        #中春绿
        #MediumSpringGreen
        color = 'LawnGreen'
        minFrameY = 13
        # root.geometry('300x300+300+300')
        # root.option_add("*Font", ("宋体", 15, "bold"))
        mainFrame = Frame(root, bg=color)
        #第一行标题
        topTitleFrame = Frame(mainFrame, bg=color)
        #第二行标题
        titleFrame = Frame(mainFrame, bg=color)
        titleLineFrame = Frame(mainFrame, bg=color)
        #表格标题
        topFrame = Frame(mainFrame, bg=color)
        #topLineFrame是topFrame下面用于显示虚线的frame
        topLineFrame = Frame(mainFrame, bg=color)
        #包胶性质一栏的Frame
        leftFrame = Frame(mainFrame, bg=color)
        #运算结果一栏的Frame
        rightFrame = Frame(mainFrame, bg=color)
        #设备与包胶辊参数一栏的Frame
        midFrame = Frame(mainFrame, bg=color)
        #主标题
        topTitleLab = Label(topTitleFrame, width=25, text='Nip Compu 压区计算 V1.0', font=("黑体", 16, "bold italic"), bg=color)
        topTitleLab.pack(side=LEFT, fill=X, padx=180)
        #编号输入
        noFrame = Frame(topTitleFrame, bg=color)
        noLab = Label(noFrame, width=10, text='编号:', font=("黑体", 15, "normal"), bg=color)
        self.noEnt = Entry(noFrame, width=15, borderwidth=4, insertwidth=1, relief='sunken', font=("宋体", 15, "normal"))
        noLab.pack(side=LEFT)
        self.noEnt.pack()
        noFrame.pack(side=LEFT)
        
        #用户名输入框
        userNameFrame = Frame(titleFrame, bg=color)
        userNameLab = Label(userNameFrame, width=10, text='用户:', font=("黑体", 15, "normal"), bg=color)
        self.userNameEnt = Entry(userNameFrame, width=15, borderwidth=4, insertwidth=1, relief='sunken',
                            font=("宋体", 15, "normal"))
        userNameLab.pack(side=LEFT)
        self.userNameEnt.pack()
        userNameFrame.pack(fill=BOTH, side=LEFT, padx=50)

        #项目名称输入
        projectFrame = Frame(titleFrame, bg=color)
        projectLab = Label(projectFrame, width=10, text='项目名称:', font=("黑体", 15, "normal"), bg=color)
        self.projectEnt = Entry(projectFrame, width=15, borderwidth=4, insertwidth=1, relief='sunken',
                           font=("宋体", 15, "normal"))
        projectLab.pack(side=LEFT)
        self.projectEnt.pack()
        projectFrame.pack(fill=BOTH, side=LEFT, padx=100)
        

        #日期输入
        dateFrame = Frame(titleFrame, bg=color)
        dateLab = Label(dateFrame, width=10, text='日期:', font=("黑体", 15, "normal"), bg=color)
        self.dateEnt = Entry(dateFrame, width=15, borderwidth=4, insertwidth=1, relief='sunken', font=("宋体", 15, "normal"))
        dateLab.pack(side=LEFT)
        self.dateEnt.pack()
        dateFrame.pack(fill=BOTH, side=LEFT, padx=45)

        #显示包胶性质、机器参数与运算结果下面的虚线
        titleLineLab = Label(titleLineFrame, text = '  -----------------------------------------------------------------------------------------------------------------------------------',
                             font=("宋体", 15, "normal"), bg=color)
        titleLineLab.pack()


        #包胶性质标签
        coverPropertyFrame = Frame(topFrame, bg=color)
        coverPropertyLab = Label(coverPropertyFrame, width=16, text='包胶性质', font=("黑体", 13, "normal"), bg=color)
        coverPropertyLab.pack(side=LEFT)
        coverPropertyFrame.pack(side=LEFT, padx=120)

        #设备与包胶辊参数
        machineParameterFrame = Frame(topFrame, bg=color)
        machineParameterLab = Label(machineParameterFrame, width=16, text='设备与包胶辊参数', font=("黑体", 13, "normal"), bg=color)
        machineParameterLab.pack(side=LEFT)
        machineParameterFrame.pack(side=LEFT, padx=150)

        #运算结果标签
        runResultFrame = Frame(topFrame, bg=color)
        runResultLab = Label(runResultFrame, width=16, text='运算结果', font=("黑体", 13, "normal"), bg=color)
        runResultLab.pack(side=BOTTOM)
        runResultFrame.pack(side=LEFT, padx=100)

        #显示包胶性质、机器参数与运算结果下面的虚线
        lineLab = Label(topLineFrame, text='-----------------------------------------------------'
                                            '-------------------------------------------------------------------------------',
                        font=("宋体", 15, "normal"), bg=color)
        lineLab.pack()

        #材料名称
        CoverSelectFrame = Frame(leftFrame, bg=color)
        entryFrame = Frame(CoverSelectFrame, bg=color)
        entryFrame1 = Frame(entryFrame, bg=color)
        entryFrame2 = Frame(entryFrame, bg=color)
        entryFrame3 = Frame(entryFrame, bg=color)
        self.coverSelectEnt = Entry(entryFrame1, width =10, borderwidth=7, insertwidth=1, relief='sunken',
                                    font=("宋体", 13, "normal"))
        CoverSelectLab = Label(entryFrame1, width=16, text = '材料名称:', font=("宋体", 13, "normal"), bg=color)
        CoverSelectLab.pack(side=LEFT)
        self.coverSelectEnt.pack(side=RIGHT)
        self.coverSelectEnt1 = Entry(entryFrame2, width =10, borderwidth=7, insertwidth=1, relief='sunken',
                                     font=("宋体", 13, "normal"))
        CoverSelectLab = Label(entryFrame2, width=16, text = '', font=("宋体", 13, "normal"), bg=color)
        CoverSelectLab.pack(side=LEFT)
        self.coverSelectEnt1.pack(side=TOP)
        self.coverSelectEnt2 = Entry(entryFrame3, width =10, borderwidth=7, insertwidth=1, relief='sunken',
                                     font=("宋体", 13, "normal"))
        CoverSelectLab = Label(entryFrame3, width=16, text = '', font=("宋体", 13, "normal"), bg=color)
        CoverSelectLab.pack(side=LEFT)
        self.coverSelectEnt2.pack(side=TOP)
        entryFrame1.pack(fill=BOTH, pady=8)
        entryFrame2.pack(fill=BOTH, pady=8)
        entryFrame3.pack(fill=BOTH, pady=8)
        entryFrame.pack(fill=BOTH, side=RIGHT)
        CoverSelectFrame.pack()

        #材料编号标签
        materialNoFrame = Frame(leftFrame, bg=color)
        materialNoLab = Label(materialNoFrame, width=16, text='材料编号:', font=("宋体", 13, "normal"), bg=color)
        self.materialNoEnt = Entry(materialNoFrame, width=10, borderwidth=7, insertwidth=1, relief='sunken',
                              font=("宋体", 13, "normal"))
        materialNoLab.pack(side=LEFT)
        self.materialNoEnt.pack()
        materialNoFrame.pack(fill=BOTH, pady=50)

        #硬度输入框
        hardnessFrame = Frame(leftFrame, bg=color)
        hardnessLab = Label(hardnessFrame, width=16, text='材料硬度值(PJ):',font=("宋体", 13, "normal"), bg=color)
        self.hardnessEnt = Entry(hardnessFrame, width=10, borderwidth=7, insertwidth=1, relief='sunken',
                                 font=("宋体", 13, "normal"))
        hardnessLab.pack(side=LEFT)
        self.hardnessEnt.pack()
        hardnessFrame.pack(side=BOTTOM, fill=BOTH, pady=50)
        
        #包胶辊外径输入框
        coverOutDiamFrame = Frame(midFrame, bg=color)
        coverOutDiamLab = Label(coverOutDiamFrame, width=17, text='包胶辊外径(mm):', font=("宋体", 13, "normal"), bg=color)
        self.coverOutDiamEnt = Entry(coverOutDiamFrame, width=10, borderwidth=7, insertwidth=1, relief='sunken',
                                     font=("宋体", 13, "normal"))
        coverOutDiamLab.pack(side=LEFT)
        self.coverOutDiamEnt.pack()
        coverOutDiamFrame.pack(side=TOP, fill=BOTH, pady=minFrameY)

        #辊芯外径输入框
        coreOuterDiamFrame = Frame(midFrame, bg=color)
        coreOuterDiamLab = Label(coreOuterDiamFrame, width=17, text='辊芯外径(mm):  ', font=("宋体", 13, "normal"), bg=color)
        self.coreOuterDiamEnt = Entry(coreOuterDiamFrame, width=10, borderwidth=7, insertwidth=1, relief='sunken',
                                      font=("宋体", 13, "normal"))
        coreOuterDiamLab.pack(side = LEFT)
        self.coreOuterDiamEnt.pack()
        coreOuterDiamFrame.pack(side=TOP, fill=BOTH, pady=minFrameY)

        #辊芯内径输入框
        coreInnerDiamFrame = Frame(midFrame, bg=color)
        coreInnerDiamLab = Label(coreInnerDiamFrame, width=17, text='辊芯内径(mm):  ', font=("宋体", 13, "normal"), bg=color)
        self.coreInnerDiamEnt = Entry(coreInnerDiamFrame, width=10, borderwidth=7, insertwidth=1, relief='sunken',
                                      font=("宋体", 13, "normal"))
        coreInnerDiamLab.pack(side = LEFT)
        self.coreInnerDiamEnt.pack()
        coreInnerDiamFrame.pack(side=TOP, fill=BOTH, pady=minFrameY)
        
        #相邻辊外径输入框
        matingRollOuterDiamFrame = Frame(midFrame, bg=color)
        matingRollOuterDiamLab = Label(matingRollOuterDiamFrame, width=17, text='相邻辊外径(mm):', font=("宋体", 13, "normal"), bg=color)
        self.matingRollOuterDiamEnt = Entry(matingRollOuterDiamFrame, width=10, borderwidth=7, insertwidth=1,
                                            relief='sunken', font=("宋体", 13, "normal"))
        matingRollOuterDiamLab.pack(side=LEFT)
        self.matingRollOuterDiamEnt.pack()
        matingRollOuterDiamFrame.pack(side=TOP, fill=BOTH, pady=minFrameY)


        #线载荷输入框
        lineLoadFrame = Frame(midFrame, bg=color)
        lineLoadLabel = Label(lineLoadFrame, width=17, text='  线载荷(KN/m):', font=("宋体", 13, "normal"), bg=color)
        lineLoadLabel.pack(side=LEFT, anchor=S)
        self.lineLoadEnt = Entry(lineLoadFrame, width=10, borderwidth=7, insertwidth=1, relief='sunken',
                                 font=("宋体", 13, "normal"))
        self.lineLoadEnt.pack(side=LEFT)
        lineLoadFrame.pack(side=TOP, fill=BOTH, pady=minFrameY)

        #车速输入框
        speedFrame = Frame(midFrame, bg=color)
        speedLabel = Label(speedFrame, width=17, text='车速(m/min):', font=("宋体", 13, "normal"), bg=color)
        speedLabel.pack(side=LEFT, anchor=S)
        self.speedEnt = Entry(speedFrame, width=10, borderwidth=7, insertwidth=1, relief='sunken',
                              font=("宋体", 13, "normal"))
        self.speedEnt.pack(side=LEFT)
        speedFrame.pack(side=TOP, fill=BOTH, pady=minFrameY)

        #荷载面宽输入框
        wideLoadFrame = Frame(midFrame, bg=color)
        wideLoadLabel = Label(wideLoadFrame, width=17, text='荷载面宽(mm):', font=("宋体", 13, "normal"), bg=color)
        wideLoadLabel.pack(side=LEFT, anchor=S)
        self.wideLoadEnt = Entry(wideLoadFrame, width=10, borderwidth=7, insertwidth=1, relief='sunken',
                                 font=("宋体", 13, "normal"))
        self.wideLoadEnt.pack(side=LEFT)
        wideLoadFrame.pack(side=TOP, fill=BOTH, pady=minFrameY)

        #包胶辊表面温度输入框
        coverTemperatureFrame = Frame(midFrame, bg=color)
        coverTemperatureLabel = Label(coverTemperatureFrame, width=17, text='包胶辊表面温度(℃):', font=("宋体", 13, "normal"), bg=color)
        coverTemperatureLabel.pack(side=LEFT, anchor=S)
        self.coverTemperatureEnt = Entry(coverTemperatureFrame, width=10, borderwidth=7, insertwidth=1, relief='sunken',
                                         font=("宋体", 13, "normal"))
        self.coverTemperatureEnt.pack(side=LEFT)
        coverTemperatureFrame.pack(side=TOP, fill=BOTH, pady=minFrameY)
        
        #压区宽度
        self.nipWidthEntValue = DoubleVar()
        nipWidthFrame = Frame(rightFrame, bg=color)
        nipWidthLabel = Label(nipWidthFrame,width=13,text = '压区宽度:',font=("宋体", 13, "normal"), bg=color)
        nipWidthLabel.pack(side=LEFT,anchor = S)
        self.nipWidthEnt = Entry(nipWidthFrame, textvariable=self.nipWidthEntValue, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
        self.nipWidthEnt.pack()
        nipWidthFrame.pack(side=TOP, fill=BOTH, pady=30)

        #最大应力
        self.peakStressEntValue = DoubleVar()
        peakStressFrame = Frame(rightFrame, bg=color)
        peakStressLabel = Label(peakStressFrame,width=13,text = '最大应力:',font=("宋体", 13, "normal"), bg=color)
        peakStressLabel.pack(side=LEFT,anchor = S)
        self.peakStressEnt = Entry(peakStressFrame, textvariable=self.peakStressEntValue, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
        self.peakStressEnt.pack()
        peakStressFrame.pack(side=TOP, fill=BOTH, pady=30)

        #保压时间
        self.nipDwellTimeEntValue = DoubleVar()
        nipDwellTimeFrame = Frame(rightFrame, bg=color)
        nipDwellTimeLabel = Label(nipDwellTimeFrame,width=13,text = '保压时间:',font=("宋体", 13, "normal"), bg=color)
        nipDwellTimeLabel.pack(side=LEFT,anchor = S)
        self.nipDwellTimeEnt = Entry(nipDwellTimeFrame, textvariable=self.nipDwellTimeEntValue,width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
        self.nipDwellTimeEnt.pack()
        nipDwellTimeFrame.pack(side=TOP, fill=BOTH, pady=30)

        #压榨冲量值
        self.nipImpulesEntValue=DoubleVar()
        nipImpulesFrame = Frame(rightFrame, bg=color)
        nipImpulesLabel = Label(nipImpulesFrame,width=13,text = '压榨冲量值:',font=("宋体", 13, "normal"), bg=color)
        nipImpulesLabel.pack(side=LEFT,anchor = S)
        self.nipImpulesEnt = Entry(nipImpulesFrame, textvariable=self.nipImpulesEntValue, width=10, borderwidth=7,
                              insertwidth=1, relief='sunken', font=("宋体", 13, "normal"))
        self.nipImpulesEnt.pack()
        nipImpulesFrame.pack(side=TOP, fill=BOTH, pady=30)

        bottomFrame = Frame(mainFrame, bg=color)
        btnSubmit = Button(bottomFrame, text='计算', font=("宋体", 15, "normal"), command=self.submit)
        btnSubmit.config(bg='grey', fg='black', cursor='hand2', relief=RAISED, bd=10)
        btnSubmit.pack(side=LEFT)
        btnPrint = Button(bottomFrame, text='打印', font=("宋体", 15, "normal"), command=self.printHtml)
        btnPrint.config(bg='grey', fg='black', cursor='hand2', relief=RAISED, bd=10)
        btnPrint.pack(side=LEFT)
        bottomFrame.pack(side=BOTTOM, fill=BOTH, padx=550)
        topTitleFrame.pack(side=TOP, ipady=20, padx=210)
        titleFrame.pack(side=TOP, anchor=W)
        titleLineFrame.pack(side=TOP, anchor=W)
        topFrame.pack(side=TOP, anchor=W, fill=BOTH, ipadx=30)
        topLineFrame.pack(side=TOP)
        leftFrame.pack(side=LEFT, padx=10)
        midFrame.pack(side=LEFT, anchor=N, padx=140)
        rightFrame.pack(side=LEFT, anchor=N, padx=41)
        mainFrame.pack()
        root.mainloop()

    # 提交计算函数
    def submit(self):
        try:
            H = float(self.hardnessEnt.get())
        except Exception:
            self.hardnessEnt.focus()
            showerror(title='提示', message='请确保硬度值的正确性!')
        else:
            try:
                coverOutDiam = float(self.coverOutDiamEnt.get())
            except Exception:
                self.coverOutDiamEnt.focus()
                showerror(title='提示', message='请确保包胶辊外径值的正确性')
            else:
                try:
                    coreD = float(self.coreOuterDiamEnt.get())
                except Exception:
                    self.coreOuterDiamEnt.focus()
                    showerror(title='提示', message='请确保辊芯外径值的正确性')
                else:
                    try:
                        float(self.coreInnerDiamEnt.get())
                    except Exception:
                        self.coreInnerDiamEnt.focus()
                        showerror(title='提示', message='请确保辊芯内径值的正确性')
                    else:
                        try:
                            matingRollOuterDiam = float(self.matingRollOuterDiamEnt.get())
                        except Exception:
                            self.matingRollOuterDiamEnt.focus()
                            showerror(title='提示', message='请确保相邻辊外径值的正确性')
                        else:
                            try:
                                lineLoad = float(self.lineLoadEnt.get())
                            except Exception:
                                self.lineLoadEnt.focus()
                                showerror(title='提示', message='请确保线载荷值的正确性')
                            else:
                                try:
                                    speedValue = float(self.speedEnt.get())
                                except Exception:
                                    self.speedEnt.focus()
                                    showerror(title='提示', message='请确保车速值的正确性')
                                else:
                                    try:
                                        wideLoadValue = float(self.wideLoadEnt.get())
                                    except Exception:
                                        self.wideLoadEnt.focus()
                                        showerror(title='提示', message='请确保荷载面宽的正确性')
                                    else:
                                        try:
                                            E = float('%.3f' % (pow(H, -1.0466) * pow(e, 12.509)))

                                            # 胶辊公制直径值化为英制
                                            D1 = float('%.3f' % (coverOutDiam / 25.4))

                                            # 相邻辊公制直径值化为英制
                                            D2 = float('%.3f' % (matingRollOuterDiam / 25.4))

                                            # 线压公制化为英制
                                            L = float('%.3f' % (lineLoad / 0.175))

                                            # 计算包胶厚度 T化为英制
                                            T = float('%.3f' % ((coverOutDiam - coreD) / (2 * 25.4)))

                                            # 计算直径指数MM
                                            MM = float('%.3f' % (pow(D1, 0.3281) / pow(e, 0.2719)))

                                            # 压区宽度计算式
                                            b = float('%.3f' % (
                                            pow(((4 * L * T * D1 * D2) / (E * (D1 + D2))), 1 / MM) * 25.4))
                                            #包胶辊表面温度
                                            coverTemperatureEnt = self.coverTemperatureEnt.get()
                                            if coverTemperatureEnt:
                                                b = b+ (( 0.0125 * float(coverTemperatureEnt) + 0.75) - 1) / 2

                                            # 峰值应力计算式
                                            PeakValue = float('%.3f' % ((lineLoad / b) * 1.34))

                                            # 保压时间计算
                                            dwellTime = float('%.3f' % ((b * 60) / speedValue))

                                            # 压区脉冲计算
                                            nipImpules = float('%.3f' % (60 * lineLoad / speedValue))

                                            #压榨冲量值
                                            self.nipImpulesEntValue.set(nipImpules)

                                            # 压区保压时间
                                            #self.nipDwellTimeEntValue.set(dwellTime)
                                            #self.nipDwellTimeVar.set(dwellTime)
                                            self.nipDwellTimeEntValue.set(dwellTime)

                                            # 压区宽度
                                            self.nipWidthEntValue.set(b)

                                            # 峰值应力
                                            self.peakStressEntValue.set(PeakValue)
                                        except Exception as eW2:
                                            showinfo(title='提示', message='Error:%s' % eW2)

    # 打印html报告函数
    def printHtml(self):
        file = asksaveasfilename(title=u'请选择报告生成的路径', filetypes=[('html', '*.html')])
        if file:
            if file.endswith('.html') or file.endswith('.htm'):
                pass
            else:
                file = file + '.html'
            #编号
            noEnt = self.noEnt.get()
            #用户名
            userNameEnt = self.userNameEnt.get()
            #项目名称
            projectEnt = self.projectEnt.get()
            #日期
            dateEnt = self.dateEnt.get()
            #材料名称
            coverSelectEnt1 = self.coverSelectEnt.get()
            coverSelectEnt2 = self.coverSelectEnt1.get()
            coverSelectEnt3 = self.coverSelectEnt2.get()
            coverSelectEnt = coverSelectEnt1 + '<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + \
                             coverSelectEnt2 + '<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + coverSelectEnt3
            #材料编号
            materialNoEnt = self.materialNoEnt.get()
            #硬度值
            hardnessEnt = self.hardnessEnt.get()
            #包胶辊外径
            coverOutDiamEnt = self.coverOutDiamEnt.get()
            #芯辊外径
            coreOuterDiamEnt = self.coreOuterDiamEnt.get()
            #芯辊内径
            coreInnerDiamEnt = self.coreInnerDiamEnt.get()
            #相邻辊外径
            matingRollOuterDiamEnt = self.matingRollOuterDiamEnt.get()
            #线载荷
            lineLoadEnt = self.lineLoadEnt.get()
            #车速
            speedEnt = self.speedEnt.get()
            #荷载面宽
            wideLoadEnt = self.wideLoadEnt.get()
            #包胶辊表面温度
            coverTemperatureEnt = self.coverTemperatureEnt.get()
            #压区宽度
            nipWidthEnt = float(self.nipWidthEnt.get())
            #最大应力
            peakStressEnt = float(self.peakStressEnt.get())
            #保压时间
            nipDwellTimeEnt = float(self.nipDwellTimeEnt.get())
            #压榨冲量值
            nipImpulesEnt = float(self.nipImpulesEnt.get())
            page = PyH('压区计算')
            outDiv = page<<div(style='background-color:#7CFC00')
            divTitle = outDiv<<div()
            titleP = divTitle<<p(style='text-align:center')
            titleP<<span('<i>Nip Compu 压区计算 V1.0</i>', style='font-weight:bold; font-size:35px;')
            titleP<<span('编号:%s' % noEnt, style='font-size:30px; padding-left:150px')
            titleP1 = divTitle<<p()
            titleP1<<span('用户:%s' % userNameEnt, style='font-size:30px; padding-left:50px')
            titleP1<<span('项目名称:%s' % projectEnt, style='font-size:30px; padding-left:150px')
            titleP1<<span('日期:%s' % dateEnt, style='font-size:30px; padding-left:150px')
            divTable = outDiv<<div(style='font-size:27px; padding-left:50px; padding-top:10px;')
            table1 = divTable<<table(width='1200px')
            tr1 = table1<<tr()
            tr1<<th('包胶性质', align='left',height=71)
            tr1<<th('设备与包胶辊参数', align='left',height=71)
            tr1<<th('计算结果', align='left',height=71)
            tr2 = table1<<tr()
            tr2<<td('材料名称:%s <br/><br/><br/>材料编号:%s<br/><br/><br/>材料硬度值(PJ):%s' % (coverSelectEnt, materialNoEnt, hardnessEnt))
            tr2<<td('包胶辊外径(mm):%s<br/><br/>辊芯外径(mm)%s<br/><br/>辊芯内径(mm):%s<br/><br/>相邻辊外径(mm):%s<br/><br/>\
                    线载荷(KN/m):%s<br/><br/>车速(m/min):%s<br/><br/>荷载面宽(mm):%s<br/><br/>包胶辊表面温度(℃):%s' % (coverOutDiamEnt, coreOuterDiamEnt,
                                                                                  coreInnerDiamEnt, matingRollOuterDiamEnt,
                                                                                  lineLoadEnt, speedEnt, wideLoadEnt, coverTemperatureEnt
                                                                                  ))
            tr2<<td('压区宽度(mm):%.5f<br/><br/><br/>最大应力(MPa):%.5f<br/><br/><br/>保压时间(ms):%.5f<br/><br/><br/>压榨冲量值(KPa sec):%.5f' %
                    (nipWidthEnt, peakStressEnt, nipDwellTimeEnt, nipImpulesEnt))
            page.printOut(file)
            

if __name__ == '__main__':
    MainGUI()
