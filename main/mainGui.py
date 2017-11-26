#coding:utf-8
#author__ = 'Huang Yu'

import tkinter
from math import e
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import win32com
from win32com.client import Dispatch, constants
root = Tk()
root.iconbitmap('calculator.ico')
root.title('凯信机械 Hicredit NipCAL V1.0')
# root.geometry('300x300+300+300')
# root.option_add("*Font", ("宋体", 15, "bold"))


mainFrame = Frame(root)
topTitleFrame = Frame(mainFrame)
titleFrame = Frame(mainFrame)
titleLineFrame = Frame(mainFrame)
topFrame = Frame(mainFrame)
#topLineFrame是topFrame下面用于显示虚线的frame
topLineFrame = Frame(mainFrame)
leftFrame = Frame(mainFrame)
rightFrame = Frame(mainFrame)
midFrame = Frame(mainFrame)

# topTitleLab = Label(topTitleFrame, width=50, text='凯信机械   Hicredit NipCAL  V1.0', font=("黑体", 17, "bold"))
# topTitleLab.pack()

#用户名输入框
userNameOutFrame = Frame(titleFrame)
userNameEnFrame = Frame(userNameOutFrame)
userNameEnLab = Label(userNameEnFrame,width = 31,text = '     User Name',font=("黑体", 12, "normal"))
userNameEnLab.pack(side=LEFT)
userNameFrame = Frame(userNameOutFrame)
noneLabel1 = Label(userNameFrame,width = 18)
noneLabel1.pack(side = LEFT)
userNameLab = Label(userNameFrame,width = 10,text = '用户名:',font=("黑体", 12, "normal"))
userNameEnt = Entry(userNameFrame, width =10, borderwidth = 4,insertwidth = 1,relief = 'sunken',font=("宋体", 15, "normal"))
userNameLab.pack(side = LEFT)
userNameEnt.pack()
userNameFrame.pack(side=BOTTOM)
userNameEnFrame.pack(side=TOP)
userNameOutFrame.pack(side=LEFT)

#编号输入
noOutFrame = Frame(titleFrame)
noEnFrame = Frame(noOutFrame)
noEnLab = Label(noEnFrame,width = 16,text = 'No.',font=("黑体", 12, "normal"))
noEnLab.pack(side=LEFT)
noFrame = Frame(noOutFrame)
noLabel1 = Label(noFrame,width = 16)
noLabel1.pack(side = LEFT)
noLab = Label(noFrame,width = 10,text = '编号:',font=("黑体", 12, "normal"))
noEnt = Entry(noFrame, width =10, borderwidth = 4,insertwidth = 1,relief = 'sunken',font=("宋体", 15, "normal"))
noLab.pack(side = LEFT)
noEnt.pack()
noFrame.pack(side=BOTTOM)
noEnFrame.pack(side=TOP)
noOutFrame.pack(side=LEFT)

#日期输入
dateOutFrame = Frame(titleFrame)
dateEnFrame = Frame(dateOutFrame)
dateEnLab = Label(dateEnFrame,width = 16,text = 'Date',font=("黑体", 12, "normal"))
dateEnLab.pack(side=LEFT)
dateFrame = Frame(dateOutFrame)
dateLabel1 = Label(dateFrame,width = 15)
dateLabel1.pack(side = LEFT)
dateLab = Label(dateFrame,width = 10,text = '日期:',font=("黑体", 12, "normal"))
dateEnt = Entry(dateFrame, width =10, borderwidth = 4,insertwidth = 1,relief = 'sunken',font=("宋体", 15, "normal"))
dateLab.pack(side = LEFT)
dateEnt.pack()
dateFrame.pack(side=BOTTOM)
dateEnFrame.pack(side=TOP)
dateOutFrame.pack(side=LEFT)

#编号输入
projectOutFrame = Frame(titleFrame)
projectEnFrame = Frame(projectOutFrame)
projectEnLab = Label(projectEnFrame,width = 16,text = 'Project',font=("黑体", 12, "normal"))
projectEnLab.pack(side=LEFT)
projectFrame = Frame(projectOutFrame)
projectLabel1 = Label(projectFrame,width = 17)
projectLabel1.pack(side = LEFT)
projectLab = Label(projectFrame,width = 10,text = '项目名称:',font=("黑体", 12, "normal"))
projectEnt = Entry(projectFrame, width =10, borderwidth = 4,insertwidth = 1,relief = 'sunken',font=("宋体", 15, "normal"))
projectLab.pack(side = LEFT)
projectEnt.pack()
projectFrame.pack(side=BOTTOM)
projectEnFrame.pack(side=TOP)
projectOutFrame.pack(side=LEFT)

#显示包胶性质、机器参数与运算结果下面的虚线
titleLineLab = Label(titleLineFrame,text = '-----------------------------------------------------'
                                    '-------------------------------------------------------------------------------',
                font=("宋体", 15, "normal"))
titleLineLab.pack()

#为topFrame左边留出空间
noneLabel = Label(topFrame,width=13)
noneLabel.pack(side=LEFT)

#包胶性质标签
coverPropertyOutFrame = Frame(topFrame)
coverPropertytopFrame = Frame(coverPropertyOutFrame)
coverPropertybottomFrame = Frame(coverPropertyOutFrame)
noEnLab = Label(coverPropertytopFrame, width=5)
noEnLab.pack(side=LEFT)
coverPropertyELab = Label(coverPropertytopFrame,width = 14,text = ' Cover property',font=("黑体", 13, "normal"))
coverPropertyLab = Label(coverPropertybottomFrame,width = 16,text = '包胶性质',font=("黑体", 13, "normal"))
coverPropertyLab.pack(side=LEFT)
coverPropertyELab.pack(side=LEFT)
coverPropertytopFrame.pack(side=TOP)
coverPropertybottomFrame.pack(side=BOTTOM)
coverPropertyOutFrame.pack(side=LEFT)

noneLabel1 = Label(topFrame,width = 28)
noneLabel1.pack(side = LEFT)

#机器参数标签
machineParameterOutFrame = Frame(topFrame)
machineParameterTopFrame = Frame(machineParameterOutFrame)
machineParameterBottomFrame = Frame(machineParameterOutFrame)
noneLabel1 = Label(machineParameterTopFrame,width = 9)
noneLabel1.pack(side = LEFT)
machineParameterELab = Label(machineParameterTopFrame,width = 20,text = '  Machine parameters',font=("黑体", 13, "normal"))
machineParameterLab = Label(machineParameterBottomFrame,width = 16,text = '机器参数',font=("黑体", 13, "normal"))
machineParameterBottomFrame.pack(side=BOTTOM)
machineParameterTopFrame.pack(side=TOP)
machineParameterLab.pack(side=LEFT)
machineParameterELab.pack(side=LEFT)
machineParameterOutFrame.pack(side=LEFT)

noneLabel1 = Label(topFrame,width = 30)
noneLabel1.pack(side = LEFT)

#运算结果标签
runResultFrame = Frame(topFrame)
runResultELab = Label(runResultFrame,width = 16,text = '  Run result',font=("黑体", 13, "normal"))
runResultLab = Label(runResultFrame,width = 16,text = '运算结果',font=("黑体", 13, "normal"))
runResultLab.pack(side=BOTTOM)
runResultELab.pack(side=TOP)
runResultFrame.pack(side=RIGHT)

#显示包胶性质、机器参数与运算结果下面的虚线
lineLab = Label(topLineFrame,text = '-----------------------------------------------------'
                                    '-------------------------------------------------------------------------------',
                font=("宋体", 15, "normal"))
lineLab.pack()

#包胶材料标签
CoverSelectOutFrame = Frame(leftFrame)
CoverSelectTopFrame = Frame(CoverSelectOutFrame)
CoverSelectBottomFrame = Frame(CoverSelectOutFrame)
noneLabel1 = Label(CoverSelectTopFrame, width=6)
noneLabel1.pack(side=LEFT)
CoverSelectELab = Label(CoverSelectTopFrame,width = 16,text = 'Cover select',font=("宋体", 13, "normal"))
CoverSelectLab = Label(CoverSelectBottomFrame,width = 16,text = '   包胶材料:',font=("宋体", 13, "normal"))
overSelectEnt = Entry(CoverSelectBottomFrame, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
noneLab1 = Label(CoverSelectBottomFrame, width=12)
noneLab1.pack(side=LEFT)
noneLab = Label(CoverSelectOutFrame,width = 12, text = '',font=("宋体", 22, "normal"))
noneLab.pack(side=BOTTOM)
CoverSelectTopFrame.pack(side=TOP)
CoverSelectELab.pack(side=TOP)
CoverSelectBottomFrame.pack(side=BOTTOM)
CoverSelectLab.pack(side=LEFT)
overSelectEnt.pack()
CoverSelectOutFrame.pack()

#材料编号标签
materialNoOutFrame = Frame(leftFrame)
materialNoTopFrame = Frame(materialNoOutFrame)
materialNoBottomFrame = Frame(materialNoOutFrame)
noneLabel1 = Label(materialNoTopFrame, width=6)
noneLabel1.pack(side=LEFT)
noneLabel2 = Label(materialNoBottomFrame, width=12)
noneLabel2.pack(side=LEFT)
materialNoLab = Label(materialNoBottomFrame,width = 16,text = '   材料编号:',font=("宋体", 13, "normal"))
materialNoEnt = Entry(materialNoBottomFrame, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
materialENoLab = Label(materialNoTopFrame,width = 16,text = 'Material No.',font=("宋体", 13, "normal"))
noneLab = Label(materialNoOutFrame,width = 16,text = '',font=("宋体", 20, "normal"))
noneLab.pack(side=BOTTOM)
materialNoLab.pack(side=LEFT)
materialNoEnt.pack()
materialENoLab.pack(side=LEFT)
materialNoTopFrame.pack(side=TOP)
materialNoBottomFrame.pack(side=BOTTOM)
materialNoOutFrame.pack()

#硬度输入框
hardnessOutFrame = Frame(leftFrame)
hardnessEnFrame = Frame(hardnessOutFrame)
noneLab = Label(hardnessEnFrame, width=6)
noneLab.pack(side=LEFT)
hardnessEnLab = Label(hardnessEnFrame,width = 16,text = ' Hardness(P&J)',font=("宋体", 13, "normal"))
hardnessEnLab.pack(side=LEFT)
hardnessFrame = Frame(hardnessOutFrame)
noneLabel1 = Label(hardnessFrame, width=12)
noneLabel1.pack(side = LEFT)
hardnessLab = Label(hardnessFrame,width = 16,text = '硬度:',font=("宋体", 13, "normal"))
hardnessEnt = Entry(hardnessFrame, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
hardnessLab.pack(side = LEFT)
hardnessEnt.pack()
hardnessFrame.pack(side=BOTTOM)
hardnessEnFrame.pack(side=TOP)
hardnessOutFrame.pack()

#包胶辊外径输入框
coverOutDiamOFrame = Frame(midFrame)
coverOutDiamEnFrame = Frame(coverOutDiamOFrame)
coverOutDiamEnLab = Label(coverOutDiamEnFrame,width = 26,text = ' Cover outer dia(mm)',font=("宋体", 13, "normal"))
coverOutDiamEnLab.pack(side=LEFT)
coverOutDiamEnFrame.pack(side=TOP)
coverOutDiamFrame = Frame(coverOutDiamOFrame)
noneLabel1 = Label(coverOutDiamFrame,width = 5)
noneLabel1.pack(side = LEFT)
coverOutDiamLab = Label(coverOutDiamFrame,width = 16,text = '包胶辊外径:',font=("宋体", 13, "normal"))
coverOutDiamEnt = Entry(coverOutDiamFrame, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
noneLabel = Label(coverOutDiamOFrame)
coverOutDiamLab.pack(side = LEFT)
coverOutDiamEnt.pack()
coverOutDiamFrame.pack(side = TOP)
noneLabel.pack(side = BOTTOM)
coverOutDiamOFrame.pack()

#辊子外径输入框
coreOuterDiamOFrame = Frame(midFrame)
coreOuterDiamEnFrame = Frame(coreOuterDiamOFrame)
coreOuterDiamEnLab = Label(coreOuterDiamEnFrame,width = 20,text = ' Core  outer dia(mm)',font=("宋体", 13, "normal"))
coreOuterDiamEnLab.pack(side=LEFT)
coreOuterDiamEnFrame.pack(side=TOP)
coreOuterDiamFrame = Frame(coreOuterDiamOFrame)
noneLabel1 = Label(coreOuterDiamFrame,width = 5)
noneLabel1.pack(side = LEFT)
coreOuterDiamLab = Label(coreOuterDiamFrame,width = 16,text = '辊子外径:  ',font=("宋体", 13, "normal"))
coreOuterDiamEnt = Entry(coreOuterDiamFrame, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
noneLabel = Label(coreOuterDiamOFrame)
coreOuterDiamLab.pack(side = LEFT)
coreOuterDiamEnt.pack()
coreOuterDiamFrame.pack(side=TOP)
noneLabel.pack(side = BOTTOM)
coreOuterDiamOFrame.pack()

#相邻辊外径输入框
matingRollOuterDiamOFrame = Frame(midFrame)
matingRollOuterDiamEnFrame = Frame(matingRollOuterDiamOFrame)
noneLabel1 = Label(matingRollOuterDiamEnFrame,width = 8)
noneLabel1.pack(side = LEFT)
matingRollOuterDiamEnLab = Label(matingRollOuterDiamEnFrame,width = 26,text = ' Mating roll outer dia(mm)',font=("宋体", 13, "normal"))
matingRollOuterDiamEnLab.pack()
matingRollOuterDiamEnFrame.pack(side = TOP)
matingRollOuterDiamFrame = Frame(matingRollOuterDiamOFrame)
noneLabel1 = Label(matingRollOuterDiamFrame,width = 5)
noneLabel1.pack(side = LEFT)
matingRollOuterDiamLab = Label(matingRollOuterDiamFrame,width = 16,text = '相邻辊外径:',font=("宋体", 13, "normal"))
matingRollOuterDiamEnt = Entry(matingRollOuterDiamFrame, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
noneLabel = Label(matingRollOuterDiamOFrame)
noneLabel.pack(side = BOTTOM)
matingRollOuterDiamLab.pack(side = LEFT)
matingRollOuterDiamEnt.pack()
matingRollOuterDiamFrame.pack(side = TOP)
matingRollOuterDiamOFrame.pack()

#荷载面宽输入框
loadedFaceLengthOFrame = Frame(midFrame)
loadedFaceLengthEnFrame = Frame(loadedFaceLengthOFrame)
noneLabel1 = Label(loadedFaceLengthEnFrame,width = 4)
noneLabel1.pack(side = LEFT)
loadedFaceLengthEnLab = Label(loadedFaceLengthEnFrame,width = 26,text = ' Loaded face length(mm)',font=("宋体", 13, "normal"))
loadedFaceLengthEnLab.pack()
loadedFaceLengthEnFrame.pack(side=TOP)
loadedFaceLengthFrame = Frame(loadedFaceLengthOFrame)
noneLabel1 = Label(loadedFaceLengthFrame,width = 5)
noneLabel1.pack(side = LEFT)
loadedFaceLengthLab = Label(loadedFaceLengthFrame,width = 16,text = '荷载面宽:  ',font=("宋体", 13, "normal"))
loadedFaceLengthEnt = Entry(loadedFaceLengthFrame, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
noneLabel = Label(loadedFaceLengthOFrame)
noneLabel.pack(side=BOTTOM)
loadedFaceLengthLab.pack(side = LEFT)
loadedFaceLengthEnt.pack()
loadedFaceLengthFrame.pack(side=TOP)
loadedFaceLengthOFrame.pack()

#线载荷确定按钮对应函数
def lineLoadConfirm():
    lineLoadValue = lineLoadEnt.get()
    if lineLoadValue:
        lineLoadVar.set(lineLoadValue)
    else:
        pass

#线载荷输入框
lineLoadOFrame = Frame(midFrame)
lineLoadFrame = Frame(lineLoadOFrame)
noneLabel1 = Label(lineLoadFrame,width = 3)
noneLabel1.pack(side = LEFT)
lineLoadLabel = Label(lineLoadFrame,width=8,text = '  线载荷:',font=("宋体", 13, "normal"))
lineLoadLabel.pack(side=LEFT,anchor = S)
lineLoadVar = DoubleVar()
lineLoadScale = Scale(
    lineLoadFrame,length = 140,label = 'Line load(KN/m)',font=("宋体", 13, "normal"),
    variable = lineLoadVar,highlightcolor = 'yellow',sliderlength = 10,troughcolor = 'green',
    from_=0, to=100, resolution = 0.01, orient='horizontal',width = 25,
    showvalue = YES)
lineLoadScale.pack(side = LEFT)
lineLoadBottomFrame = Frame(lineLoadFrame)
lineLoadEnt = Entry(lineLoadBottomFrame, width =7, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
btn1 = Button(lineLoadBottomFrame, text = '确定', font=("宋体", 13, "normal"), command = lineLoadConfirm)
noneLabel = Label(lineLoadOFrame)
noneLabel.pack(side=BOTTOM)
lineLoadBottomFrame.pack(side = BOTTOM,anchor = SE)
lineLoadEnt.pack(side = LEFT)
btn1.pack(side = RIGHT)
lineLoadFrame.pack(side = TOP)
lineLoadOFrame.pack()

#速度确定按钮对应函数
def speedConfirm():
    speedValue = speedEnt.get()
    if speedValue:
        speedVar.set(speedValue)
    else:
        pass

#速度输入框
speedOFrame = Frame(midFrame)
speedFrame = Frame(speedOFrame)
noneLabel1 = Label(speedFrame,width = 3)
noneLabel1.pack(side = LEFT)
speedLabel = Label(speedFrame,width =8,text = '车速:',font=("宋体", 13, "normal"))
speedLabel.pack(side=LEFT,anchor = S)
speedVar = DoubleVar()
speedScale = Scale(
    speedFrame,length = 140,label = 'Speed(m/min)',font=("宋体", 13, "normal"),
    variable = speedVar, sliderlength = 10,troughcolor = 'green',
    from_=0, to=1000, resolution = 0.01, orient='horizontal',width = 25,
    showvalue = YES)
speedScale.pack(side = LEFT)
speedBottomFrame = Frame(speedFrame)
speedEnt = Entry(speedBottomFrame, width =7, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
btnSpeed = Button(speedBottomFrame, text = '确定', font=("宋体", 13, "normal"), command = speedConfirm)
noneLabel = Label(speedOFrame)
noneLabel.pack(side = BOTTOM)
speedBottomFrame.pack(side = BOTTOM,anchor = SE)
speedEnt.pack(side = LEFT)
btnSpeed.pack(side = RIGHT)
speedFrame.pack(side = TOP)
speedOFrame.pack()

#压区宽度
nipWidthEntValue = DoubleVar()
nipWidthOFrame = Frame(rightFrame)
nipWidthFrame = Frame(nipWidthOFrame)
nipWidthLabel = Label(nipWidthFrame,width =20,text = '压区宽度:',font=("宋体", 13, "normal"))
nipWidthLabel.pack(side=LEFT,anchor = S)
nipWidthVar = DoubleVar()
nipWidthScale = Scale(
    nipWidthFrame,length = 150,label = 'Nip width(mm)',font=("宋体", 13, "normal"),
    variable = nipWidthVar, sliderlength = 10,troughcolor = 'green',
    from_=0, to=1000, resolution = 0.01, orient='horizontal',width = 25,
    showvalue = YES)
nipWidthScale.pack(side = LEFT)
nipWidthBottomFrame = Frame(nipWidthFrame)
nipWidthEnt = Entry(nipWidthBottomFrame, textvariable=nipWidthEntValue, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
noneLabel = Label(nipWidthOFrame)
noneLabel.pack(side = BOTTOM)
nipWidthBottomFrame.pack(side = BOTTOM,anchor = SE)
nipWidthEnt.pack()
nipWidthFrame.pack(side = TOP)
nipWidthOFrame.pack()

#峰值应力
peakStressEntValue = DoubleVar()
peakStressOFrame = Frame(rightFrame)
peakStressFrame = Frame(peakStressOFrame)
peakStressLabel = Label(peakStressFrame,width =20,text = '峰值应力:',font=("宋体", 13, "normal"))
peakStressLabel.pack(side=LEFT,anchor = S)
peakStressVar = DoubleVar()
peakStressScale = Scale(
    peakStressFrame,length = 150,label = 'Peak Stress(MPa)',font=("宋体", 13, "normal"),
    variable = peakStressVar, sliderlength = 10,troughcolor = 'green',
    from_=0, to=1000, resolution = 0.001, orient='horizontal',width = 25,
    showvalue = YES)
peakStressScale.pack(side = LEFT)
peakStressBottomFrame = Frame(peakStressFrame)
peakStressEnt = Entry(peakStressBottomFrame, textvariable=peakStressEntValue, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
noneLabel = Label(peakStressOFrame)
noneLabel.pack(side = BOTTOM)
peakStressBottomFrame.pack(side = BOTTOM,anchor = SE)
peakStressEnt.pack()
peakStressFrame.pack(side = TOP)
peakStressOFrame.pack()

#压区保压时间
nipDwellTimeEntValue = DoubleVar()
nipDwellTimeOFrame = Frame(rightFrame)
nipDwellTimeFrame = Frame(nipDwellTimeOFrame)
nipDwellTimeLabel = Label(nipDwellTimeFrame,width =20,text = '    压区保压时间:',font=("宋体", 13, "normal"))
nipDwellTimeLabel.pack(side=LEFT,anchor = S)
nipDwellTimeVar = DoubleVar()
nipDwellTimeScale = Scale(
    nipDwellTimeFrame,length = 150,label = 'Nip Dwell Time(ms)',font=("宋体", 13, "normal"),
    variable = nipDwellTimeVar, sliderlength = 10,troughcolor = 'green',
    from_=0, to=1000, resolution = 0.01, orient='horizontal',width = 25,
    showvalue = YES)
nipDwellTimeScale.pack(side = LEFT)
nipDwellTimeBottomFrame = Frame(nipDwellTimeFrame)
nipDwellTimeEnt = Entry(nipDwellTimeBottomFrame, textvariable=nipDwellTimeEntValue,width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
noneLabel = Label(nipDwellTimeOFrame)
noneLabel.pack(side = BOTTOM)
nipDwellTimeBottomFrame.pack(side = BOTTOM,anchor = SE)
nipDwellTimeEnt.pack()
nipDwellTimeFrame.pack(side = TOP)
nipDwellTimeOFrame.pack()

#压区冲击
nipImpulesEntValue=DoubleVar()
nipImpulesOFrame = Frame(rightFrame)
nipImpulesFrame = Frame(nipImpulesOFrame)
nipImpulesLabel = Label(nipImpulesFrame,width =20,text = '压区冲击:',font=("宋体", 13, "normal"))
nipImpulesLabel.pack(side=LEFT,anchor = S)
nipImpulesVar = DoubleVar()
nipImpulesScale = Scale(
    nipImpulesFrame,length = 150,label = 'Nip Impules(KPa-sec)',font=("宋体", 14, "normal"),
    variable = nipImpulesVar, sliderlength = 10,troughcolor = 'green',
    from_=0, to=1000, resolution = 0.01, orient='horizontal',width = 25,
    showvalue = YES)
nipImpulesScale.pack(side = LEFT)
nipImpulesBottomFrame = Frame(nipImpulesFrame)
nipImpulesEnt = Entry(nipImpulesBottomFrame,textvariable=nipImpulesEntValue, width =10, borderwidth = 7,insertwidth = 1,relief = 'sunken',font=("宋体", 13, "normal"))
noneLabel = Label(nipImpulesOFrame)
noneLabel.pack(side = BOTTOM)
nipImpulesBottomFrame.pack(side = BOTTOM,anchor = SE)
nipImpulesEnt.pack()
nipImpulesFrame.pack(side = TOP)
nipImpulesOFrame.pack()

#打印报告函数
def print1():
    file = asksaveasfilename(title=u'请选择报告生成的路径', filetypes=[('DOC', '*.doc')])
    if file:
        print(file)
        wordApp = Dispatch('Word.application')
        wordApp.Visible = 0
        wordApp.DisplayAlerts = 0
        doc = wordApp.Documents.Add()
        doc.PageSetup.PaperSize = 7
        sel = wordApp.Selection
        sel2 = wordApp.Selection
        sel.Font.Name = '黑体'
        sel.Font.Bold = True
        sel.Font.Size = 20
        sel.Font.Italic = False
        sel.ParagraphFormat.LineSpacing = 2*12
        sel.ParagraphFormat.Alignment = 1
        sel.TypeText("凯信机械   ")
        sel.Font.Size = 17
        sel.Font.Italic = True
        sel.TypeText('Hicredit NipCAL  V1.0')
        sel.TypeParagraph()

        sel2.Font.Name = '黑体'
        sel2.Font.Bold = False
        sel2.Font.Size = 12
        sel2.Font.Italic = False
        sel2.ParagraphFormat.LineSpacing = 1*12
        sel2.ParagraphFormat.Alignment = 0
        sel2.TypeText(u'用户名:%s    编号:%s    项目名称:%s    日期:%s             ' % (userNameEnt.get(), noEnt.get(), projectEnt.get(), dateEnt.get()))
        sel2.TypeParagraph()
        sel2.TypeText(u'-----------------------------------------------------------------')
        sel2.TypeParagraph()
        sel.Font.Size = 12
        sel.Font.Italic = False
        sel.Font.Bold = False
        sel.ParagraphFormat.LineSpacing = 1*12
        sel.ParagraphFormat.Alignment = 0
        # sel.TypeText("Cover Property       Machine parameters         Run Result ")
        # sel.TypeParagraph()
        # sel2.Font.Italic = False
        # sel2.TypeText('包胶性质             机器参数                   运算结果')
        headList = ['Cover Property\n包胶性质\n', 'Machine parameters\n机器参数\n', 'Run Result\n运算结果\n']
        # sel2.TypeParagraph()
        # sel2.TypeText(u'-----------------------------------------------------------------')
        # sel2.TypeParagraph()
        # textList = [['Cover select           Cover outer dia(mm)           Nip width(mm)',        '包胶材料:%s          包胶辊外径:%7.3f            压区宽度:%.3f' % (overSelectEnt.get(), float(coverOutDiamEnt.get() or 0), float(nipWidthEntValue.get() or 0))],
        #             ['Material No.           Core outer dia(mm)            Peak Stress(MPa)',     '材料编号:%s          辊子外径:%7.3f              峰值应力:%.3f' % (materialNoEnt.get(), float(coreOuterDiamEnt.get() or 0), float(peakStressEntValue.get() or 0))],
        #             ['Hardness(P&J)          Mating roll outer dia(mm)     Nip Dwell Time(ms)  ', '硬度:%7.3f           相邻辊外径:%7.3f            压区保压时间:%.3f' % (float(hardnessEnt.get() or 0), float(matingRollOuterDiamEnt.get() or 0), float(nipDwellTimeEntValue.get() or 0) )],
        #             ['                       Loaded face length(mm)        Nip Impules(KPa-sec)', '                       荷载面宽:%7.3f              压区冲击:%.3f' % (float(loadedFaceLengthEnt.get() or 0), float(nipImpulesEntValue.get() or 0))],
        #             ['                       Line Load(KN/m)                                   ',     '                       线载荷:%7.3f                     ' % float(lineLoadEnt.get() or 0)],
        #             ['                       Speed(m/min)                                      ',     '                       车速:%7.3f                       ' % float(speedEnt.get() or 0)]]
        textList = [['Cover select           Cover outer dia(mm)           Nip width(mm)',        '包胶材料:%s          包胶辊外径:%7.3f            压区宽度:%.3f' % (overSelectEnt.get(), float(coverOutDiamEnt.get() or 0), float(nipWidthEntValue.get() or 0))],
                    ['Material No.           Core outer dia(mm)            Peak Stress(MPa)',     '材料编号:%s          辊子外径:%7.3f              峰值应力:%.3f' % (materialNoEnt.get(), float(coreOuterDiamEnt.get() or 0), float(peakStressEntValue.get() or 0))],
                    ['Hardness(P&J)          Mating roll outer dia(mm)     Nip Dwell Time(ms)  ', '硬度:%7.3f           相邻辊外径:%7.3f            压区保压时间:%.3f' % (float(hardnessEnt.get() or 0), float(matingRollOuterDiamEnt.get() or 0), float(nipDwellTimeEntValue.get() or 0))],
                    ['                       Loaded face length(mm)        Nip Impules(KPa-sec)', '                       荷载面宽:%7.3f              压区冲击:%.3f' % (float(loadedFaceLengthEnt.get() or 0), float(nipImpulesEntValue.get() or 0))],
                    ['                       Line Load(KN/m)                                   ',     '                       线载荷:%7.3f                     ' % float(lineLoadEnt.get() or 0)],
                    ['                       Speed(m/min)                                      ',     '                       车速:%7.3f                       ' % float(speedEnt.get() or 0)]]
        textList = [['Cover select \n包胶材料:%s \n\nMaterial No. \n材料编号:%s\n\nHardness(P&J) ' % (overSelectEnt.get(), materialNoEnt.get())],
                    ['Cover outer dia(mm)\n包胶辊外径:%7.3f\n\nCore outer dia(mm)\n辊子外径:%7.3f\n\nMating roll outer dia(mm)\n相邻辊外径:%7.3f\n\nLoaded face length(mm)\n荷载面宽:%7.3f\n\nLine Load(KN/m)\n线载荷:%7.3f\n\nSpeed(m/min)\n车速:%7.3f\n\n\n\n' %
                     (float(coverOutDiamEnt.get() or 0), float(coreOuterDiamEnt.get() or 0), float(matingRollOuterDiamEnt.get() or 0), float(loadedFaceLengthEnt.get() or 0), float(lineLoadEnt.get() or 0), float(speedEnt.get() or 0))],
                    ['Nip width(mm)\n压区宽度:%.3f\n\nPeak Stress(MPa)\n峰值应力:%.3f\n\nNip Dwell Time(ms)\n压区保压时间:%.3f\n\nNip Impules(KPa-sec)\n压区冲击:%.3f' %
                     (float(nipWidthEntValue.get() or 0), float(peakStressEntValue.get() or 0), float(nipDwellTimeEntValue.get() or 0), float(nipImpulesEntValue.get() or 0))]]
        tab = doc.Tables.Add(sel.Range, 2, 3)		# 增加一个2行3列的表格
        tab.Style = "网格型"							# 显示表格边框
        tab.Columns(1).SetWidth(5*28.35, 1)			# 调整第1列宽度，1cm=28.35pt
        tab.Columns(2).SetWidth(5*28.35, 0)			# 调整第2列宽度
        tab.Columns(3).SetWidth(5*28.35, 0)
        tab.Rows.Alignment = 1                  		# 表格对齐,0=左对齐,1=居中,2=右对齐
        tab.Cell(1, 1).Range.Text = headList[0]
        tab.Cell(1, 2).Range.Text = headList[1]
        tab.Cell(1, 3).Range.Text = headList[2]
        tab.Cell(2, 1).Range.Text = textList[0][0]				# 填充内容，注意Excel中使用wSheet.Cells(i,j)
        tab.Cell(2, 2).Range.Text = textList[1][0]
        tab.Cell(2, 3).Range.Text = textList[2][0]
        # sel.Font.Name = '宋体'
        # sel.Font.Bold = False
        # sel2.Font.Name = '黑体'
        # sel.Font.Size = 11
        # sel2.Font.Bold = False
        # for listItem in textList:
        #     sel.TypeText(listItem[0])
        #     sel.TypeParagraph()
        #     sel2.TypeText(listItem[1])
        #     sel2.TypeParagraph()
        #     sel2.TypeParagraph()
        if file.endswith('.doc'):
            filename = file
        else:
            filename = file+'.doc'
        try:
            doc.SaveAs(filename)
        except Exception as e:
            showerror(title=u'失败', message=e)
        else:
            showinfo(title=u'成功', message=u'报告已成功生成！')
            doc.Close(-1)


top = Menu(root)
root.config(menu=top)
file = Menu(top, tearoff=0, font=("宋体", 13, "bold"))
file.add_command(label='打印报告', command=print1, underline=0)
file.add_separator()
file.add_command(label='退出', command=sys.exit, underline=0)
top.add_cascade(label = '文件', menu=file, underline=0)



#提交计算函数
def submit():
    try:
        H = float(hardnessEnt.get())
    except Exception:
        hardnessEnt.focus_force()
        showerror(title='提示',message='请确保硬度值的正确性!')
    else:
        try:
            coverOutDiam = float(coverOutDiamEnt.get())
        except Exception:
            coverOutDiamEnt.focus()
            showerror(title='提示',message='请确保包胶辊外径值的正确性')
        else:
            try:
                coreD = float(coreOuterDiamEnt.get())
            except Exception:
                coreOuterDiamEnt.focus()
                showerror(title='提示',message='请确保辊子外径值的正确性')
            else:
                try:
                    matingRollOuterDiam = float(matingRollOuterDiamEnt.get())
                except Exception:
                    matingRollOuterDiamEnt.focus()
                    showerror(title='提示',message='请确保相邻辊外径值的正确性')
                else:
                    try:
                        loadedFaceLength = float(loadedFaceLengthEnt.get())
                    except Exception:
                        lineLoadEnt.focus()
                        showerror(title='提示',message='请确保荷载面宽的正确性')
                    else:
                        try:
                            lineLoad = float(lineLoadEnt.get())
                        except Exception:
                            lineLoadEnt.focus()
                            showerror(title='提示',message='请确保线载荷值的正确性')
                        else:
                            try:
                                speedValue = float(speedEnt.get())
                            except Exception:
                                speedEnt.focus()
                                showerror(title='提示',message='请确保车速值的正确性')
                            else:
                                try:
                                    E = float('%.3f'%(pow(H,-1.0466)*pow(e, 12.509)))

                                    #胶辊公制直径值化为英制
                                    D1 = float('%.3f'%(coverOutDiam/25.4))

                                    #相邻辊公制直径值化为英制
                                    D2 = float('%.3f'%(matingRollOuterDiam/25.4))

                                    #线压公制化为英制
                                    L = float('%.3f'%(lineLoad / 0.175))

                                    #计算包胶厚度 T化为英制
                                    T=float('%.3f'%((coverOutDiam-coreD)/(2*25.4)))

                                    #计算直径指数MM
                                    MM = float('%.3f'%(pow(D1,0.3281)/pow(e,0.2719)))

                                    #压区宽度计算式
                                    b = float('%.3f'%(pow(((4*L*T*D1*D2)/(E*(D1+D2))),1/MM)*25.4))

                                    #峰值应力计算式
                                    PeakValue = float('%.3f'%((lineLoad/b)*1.34))

                                    #保压时间计算
                                    dwellTime = float('%.3f'%((b*60)/speedValue))

                                    #压区脉冲计算
                                    nipImpules = float('%.3f'%(60*lineLoad/speedValue))

                                    #压区冲击
                                    nipImpulesVar.set(nipImpules)
                                    nipImpulesEntValue.set(nipImpules)

                                    #压区保压时间
                                    nipDwellTimeEntValue.set(dwellTime)
                                    nipDwellTimeVar.set(dwellTime)

                                    #压区宽度
                                    nipWidthEntValue.set(b)
                                    nipWidthVar.set(b)

                                    #峰值应力
                                    peakStressEntValue.set(PeakValue)
                                    peakStressVar.set(PeakValue)
                                except Exception:
                                    showinfo(title='提示',message='请检查数值输入的有效性！')

btnSubmit = Button(root, text = '提交计算', font=("宋体", 10, "normal"), command = submit)
btnSubmit.config(bg='grey', fg='black', cursor='hand2', relief = RAISED, bd=10)
btnSubmit.pack(side = BOTTOM)
noneLabel = Label(mainFrame,width = 15)
noneLabel1 = Label(mainFrame,width = 13)
topTitleFrame.pack(side=TOP)
titleFrame.pack(side=TOP,anchor=W)
titleLineFrame.pack(side=TOP,anchor=W)
topFrame.pack(side=TOP,anchor=W)
topLineFrame.pack(side=TOP)
leftFrame.pack(side=LEFT,anchor=N)
noneLabel.pack(side=LEFT)
midFrame.pack(side=LEFT)
noneLabel1.pack(side=LEFT)
rightFrame.pack(side=RIGHT,anchor=N)
mainFrame.pack()
root.mainloop()

