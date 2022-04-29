from tkinter import Tk
from tkinter import Label
from tkinter import Canvas
from tkinter import Button
from tkinter import messagebox
from tksheet import Sheet
from tkinter import ttk
from pynput import keyboard
from PIL import ImageTk, Image
import json
import threading
import time

isSaved = True
cfg_radius = 60
cfg_clr = 'white'
winClosed = False
tblWidth = 825
tblHeight = 425
appWidth = 1200
appHeight = 768
appIco = ''
navWidth = appWidth/4
heightLineNav = appHeight/3
lblNavX = navWidth/5*2+10

def genNav():
    
    lftNavDiv = Canvas(
        dashbrd,
        width = navWidth,
        height = appHeight,
        background = 'white'
    )
    a = [i for i in range(200, 1200, 60)]
    b = [i-10 for i in range(260, 1200, 60)]
    
    def genBut1(x, y, filename):
        global icoBut1
        rawIcoBut1 = Image.open('./img/'+filename)
        rawIcoBut1 = rawIcoBut1.resize((x, y), Image.Resampling.LANCZOS)
        icoBut1 = ImageTk.PhotoImage(rawIcoBut1)
        global lblIcoBut1
        lblIcoBut1 = Label(dashbrd, image = icoBut1, bg = cfg_clr)
    genBut1(200, 60, 'but.png')
    def mouEnBut1(e):
        lbl1['font'] = ('Chirp', 14, 'bold')
    def mouLeBut1(e):
        lbl1['font'] = ('Chirp', 14)

    def genBut2(x, y):
        global icoBut2
        rawIcoBut2 = Image.open('./img/but.png')
        rawIcoBut2 = rawIcoBut2.resize((x, y), Image.Resampling.LANCZOS)
        icoBut2 = ImageTk.PhotoImage(rawIcoBut2)
        global lblIcoBut2
        lblIcoBut2 = Label(dashbrd, image = icoBut2, bg = cfg_clr)
        return
    genBut2(200, 60)
    def mouEnBut2(e):
        lbl2['font'] = ('Chirp', 14, 'bold')
    def mouLeBut2(e):
        lbl2['font'] = ('Chirp', 14)

    def genBut3(x, y):
        global icoBut3
        rawIcoBut3 = Image.open('./img/but.png')
        rawIcoBut3 = rawIcoBut3.resize((x, y), Image.Resampling.LANCZOS)
        icoBut3 = ImageTk.PhotoImage(rawIcoBut3)
        global lblIcoBut3
        lblIcoBut3 = Label(dashbrd, image = icoBut3, bg = cfg_clr)
        return
    genBut3(200, 60)
    def mouEnBut3(e):
        lbl3['font'] = ('Chirp', 14, 'bold')
    def mouLeBut3(e):
        lbl3['font'] = ('Chirp', 14)

    def genBut4(x, y):
        global icoBut4
        rawIcoBut4 = Image.open('./img/but.png')
        rawIcoBut4 = rawIcoBut4.resize((x, y), Image.Resampling.LANCZOS)
        icoBut4 = ImageTk.PhotoImage(rawIcoBut4)
        global lblIcoBut4
        lblIcoBut4 = Label(dashbrd, image = icoBut4, bg = cfg_clr)
        return
    genBut4(200, 60)
    def mouEnBut4(e):
        lbl4['font'] = ('Chirp', 14, 'bold')
    def mouLeBut4(e):
        lbl4['font'] = ('Chirp', 14)

    def genBut5(x, y):
        global icoBut5
        rawIcoBut5 = Image.open('./img/but.png')
        rawIcoBut5 = rawIcoBut5.resize((x, y), Image.Resampling.LANCZOS)
        icoBut5 = ImageTk.PhotoImage(rawIcoBut5)
        global lblIcoBut5
        lblIcoBut5 = Label(dashbrd, image = icoBut5, bg = cfg_clr)
        return
    genBut5(200, 60)
    def mouEnBut5(e):
        lbl5['font'] = ('Chirp', 14, 'bold')
    def mouLeBut5(e):
        lbl5['font'] = ('Chirp', 14)

    def genBut6(x, y):
        global icoBut6
        rawIcoBut6 = Image.open('./img/but.png')
        rawIcoBut6 = rawIcoBut6.resize((x, y), Image.Resampling.LANCZOS)
        icoBut6 = ImageTk.PhotoImage(rawIcoBut6)
        global lblIcoBut6
        lblIcoBut6 = Label(dashbrd, image = icoBut6, bg = cfg_clr)
        return
    genBut6(200, 60)
    def mouEnBut6(e):
        lbl6['font'] = ('Chirp', 14, 'bold')
    def mouLeBut6(e):
        lbl6['font'] = ('Chirp', 14)

    def genBut7(x, y):
        global icoBut7
        rawIcoBut7 = Image.open('./img/but.png')
        rawIcoBut7 = rawIcoBut7.resize((x, y), Image.Resampling.LANCZOS)
        icoBut7 = ImageTk.PhotoImage(rawIcoBut7)
        global lblIcoBut7
        lblIcoBut7 = Label(dashbrd, image = icoBut7, bg = cfg_clr)
        return
    genBut7(200, 60)
    def mouEnBut7(e):
        lbl7['font'] = ('Chirp', 14, 'bold')
    def mouLeBut7(e):
        lbl7['font'] = ('Chirp', 14)

    def genBut8(x, y):
        global icoBut8
        rawIcoBut8 = Image.open('./img/but.png')
        rawIcoBut8 = rawIcoBut8.resize((x, y), Image.Resampling.LANCZOS)
        icoBut8 = ImageTk.PhotoImage(rawIcoBut8)
        global lblIcoBut8
        lblIcoBut8 = Label(dashbrd, image = icoBut8, bg = cfg_clr)
        return
    genBut8(200, 60)
    def mouEnBut8(e):
        lbl8['font'] = ('Chirp', 14, 'bold')
    def mouLeBut8(e):
        lbl8['font'] = ('Chirp', 14)

    brand = Label(
        dashbrd,
        text = 'GRAND HOTEL',
        font = ('Montserrat', 18),
        foreground = 'black',
        bg = 'white'
    )
    brand.place(x=60, y=10)

    def genLogo(x, y):
        global logo
        rawLogo = Image.open('./img/logo.jpg')
        rawLogo = rawLogo.resize((x, y), Image.Resampling.LANCZOS)
        logo = ImageTk.PhotoImage(rawLogo)
        global lblLogo
        lblLogo = Label(dashbrd, image = logo, bg = cfg_clr)
        return
    genLogo(120, 120)
    lblLogo.place(x = 90, y = 60)

    lbl1 = Label(cursor = 'hand2', text = 'Phiếu thuê',bg = cfg_clr,font = ('Chirp', 14))
    lbl2 = Label(cursor = 'hand2', text = 'Hóa đơn',bg = cfg_clr,font = ('Chirp', 14))
    lbl3 = Label(cursor = 'hand2', text = 'Phòng',bg = cfg_clr,font = ('Chirp', 14))
    lbl4 = Label(cursor = 'hand2', text = 'Nhân viên',bg = cfg_clr,font = ('Chirp', 14))
    lbl5 = Label(cursor = 'hand2', text = 'Khách hàng' ,bg = cfg_clr,font = ('Chirp', 14))
    lbl6 = Label(cursor = 'hand2', text = 'Dịch vụ', bg = cfg_clr, font = ('Chirp', 14))
    lbl7 = Label(cursor = 'hand2', text = 'Kho hàng',bg = cfg_clr,font = ('Chirp', 14))
    lbl8 = Label(cursor = 'hand2', text = 'Thống kê',bg = cfg_clr,font = ('Chirp', 14))
    lbl9 = Label(cursor = 'hand2', text = 'Phiếu thuê',bg = cfg_clr,font = ('Chirp', 14, 'bold'))
    lbl10 = Label(cursor = 'hand2', text = 'Hóa đơn',bg = cfg_clr,font = ('Chirp', 14, 'bold'))
    lbl11 = Label(cursor = 'hand2', text = 'Phòng',bg = cfg_clr,font = ('Chirp', 14, 'bold'))
    lbl12 = Label(cursor = 'hand2', text = 'Nhân viên',bg = cfg_clr,font = ('Chirp', 14, 'bold'))
    lbl13 = Label(cursor = 'hand2', text = 'Khách hàng' ,bg = cfg_clr,font = ('Chirp', 14, 'bold'))
    lbl14 = Label(cursor = 'hand2', text = 'Dịch vụ',bg = cfg_clr,font = ('Chirp', 14, 'bold'))
    lbl15 = Label(cursor = 'hand2', text = 'Kho hàng',bg = cfg_clr,font = ('Chirp', 14, 'bold'))
    lbl16 = Label(cursor = 'hand2', text = 'Thống kê',bg = cfg_clr,font = ('Chirp', 14, 'bold'))


    LblPlacing = [30]
    for i in range(1,8):
        LblPlacing.append(LblPlacing[i-1]+50)

    def lblIcoButHovering():
        lblIcoBut1.bind("<Enter>", mouEnBut1)
        lblIcoBut1.bind("<Leave>", mouLeBut1)
        lblIcoBut2.bind("<Enter>", mouEnBut2)
        lblIcoBut2.bind("<Leave>", mouLeBut2)
        lblIcoBut3.bind("<Enter>", mouEnBut3)
        lblIcoBut3.bind("<Leave>", mouLeBut3)
        lblIcoBut4.bind("<Enter>", mouEnBut4)
        lblIcoBut4.bind("<Leave>", mouLeBut4)
        lblIcoBut5.bind("<Enter>", mouEnBut5)
        lblIcoBut5.bind("<Leave>", mouLeBut5)
        lblIcoBut6.bind("<Enter>", mouEnBut6)
        lblIcoBut6.bind("<Leave>", mouLeBut6)
        lblIcoBut7.bind("<Enter>", mouEnBut7)
        lblIcoBut7.bind("<Leave>", mouLeBut7)
        lblIcoBut8.bind("<Enter>", mouEnBut8)
        lblIcoBut8.bind("<Leave>", mouLeBut8)
    lblIcoButHovering()

    def toggleLbl1(e):
        lbl9.place(x=125, y=a[0]+10)
        lbl10.place_forget()
        lbl11.place_forget()
        lbl12.place_forget()
        lbl13.place_forget()
        lbl14.place_forget()
        lbl15.place_forget()
        lbl16.place_forget()
    def toggleLbl2(e):
        lbl10.place(x=125, y=a[1]+10)
        lbl9.place_forget()
        lbl11.place_forget()
        lbl12.place_forget()
        lbl13.place_forget()
        lbl14.place_forget()
        lbl15.place_forget()
        lbl16.place_forget()
    def toggleLbl3(e):
        lbl11.place(x=125, y=a[2]+10)
        lbl9.place_forget()
        lbl10.place_forget()
        lbl12.place_forget()
        lbl13.place_forget()
        lbl14.place_forget()
        lbl15.place_forget()
        lbl16.place_forget()
    def toggleLbl4(e):
        lbl12.place(x=125, y=a[3]+10)
        lbl9.place_forget()
        lbl10.place_forget()
        lbl11.place_forget()
        lbl13.place_forget()
        lbl14.place_forget()
        lbl15.place_forget()
        lbl16.place_forget()
    def toggleLbl5(e):
        lbl13.place(x=125, y=a[4]+10)
        lbl9.place_forget()
        lbl10.place_forget()
        lbl11.place_forget()
        lbl12.place_forget()
        lbl14.place_forget()
        lbl15.place_forget()
        lbl16.place_forget()
    def toggleLbl6(e):
        lbl14.place(x=125, y=a[5]+10)
        lbl9.place_forget()
        lbl10.place_forget()
        lbl11.place_forget()
        lbl12.place_forget()
        lbl13.place_forget()
        lbl15.place_forget()
        lbl16.place_forget()
    def toggleLbl7(e):
        lbl15.place(x=125, y=a[6]+10)
        lbl9.place_forget()
        lbl10.place_forget()
        lbl11.place_forget()
        lbl12.place_forget()
        lbl13.place_forget()
        lbl14.place_forget()
        lbl16.place_forget()
    def toggleLbl8(e):
        lbl16.place(x=125, y=a[7]+10)
        lbl9.place_forget()
        lbl10.place_forget()
        lbl11.place_forget()
        lbl12.place_forget()
        lbl13.place_forget()
        lbl14.place_forget()
        lbl15.place_forget()

    lftNavDiv.place(x=0, y=0) 
        
    def genIco1(x, y):
        global icoimg1
        rawIcoImg1 = Image.open('./img/formIcon.png')
        rawIcoImg1 = rawIcoImg1.resize((x, y), Image.Resampling.LANCZOS)
        icoimg1 = ImageTk.PhotoImage(rawIcoImg1)
        global lblIcoImg1
        lblIcoImg1 = Label(dashbrd, image = icoimg1, bg = cfg_clr, cursor = 'hand2')
        return
    def genIco2(x, y):
        global icoimg2
        rawIcoImg2 = Image.open('./img/billIcon.png')
        rawIcoImg2 = rawIcoImg2.resize((x, y), Image.Resampling.LANCZOS)
        icoimg2 = ImageTk.PhotoImage(rawIcoImg2)
        global lblIcoImg2
        lblIcoImg2 = Label(dashbrd, image = icoimg2, bg = cfg_clr, cursor = 'hand2')
        return
    def genIco3(x, y):
        global icoimg3
        rawIcoImg3 = Image.open('./img/room.png')
        rawIcoImg3 = rawIcoImg3.resize((x, y), Image.Resampling.LANCZOS)
        icoimg3 = ImageTk.PhotoImage(rawIcoImg3)
        global lblIcoImg3
        lblIcoImg3 = Label(dashbrd, image = icoimg3, bg = cfg_clr, cursor = 'hand2')
        return
    def genIco4(x, y):
        global icoimg4
        rawIcoImg4 = Image.open('./img/staff.png')
        rawIcoImg4 = rawIcoImg4.resize((x, y), Image.Resampling.LANCZOS)
        icoimg4 = ImageTk.PhotoImage(rawIcoImg4)
        global lblIcoImg4
        lblIcoImg4 = Label(dashbrd, image = icoimg4, bg = cfg_clr, cursor = 'hand2')
        return
    def genIco5(x, y):
        global icoimg5
        rawIcoImg5 = Image.open('./img/cust.png')
        rawIcoImg5 = rawIcoImg5.resize((x, y), Image.Resampling.LANCZOS)
        icoimg5 = ImageTk.PhotoImage(rawIcoImg5)
        global lblIcoImg5
        lblIcoImg5 = Label(dashbrd, image = icoimg5, bg = cfg_clr, cursor = 'hand2')
        return
    def genIco6(x, y):
        global icoimg6
        rawIcoImg6 = Image.open('./img/serv.png')
        rawIcoImg6 = rawIcoImg6.resize((x, y), Image.Resampling.LANCZOS)
        icoimg6 = ImageTk.PhotoImage(rawIcoImg6)
        global lblIcoImg6
        lblIcoImg6 = Label(dashbrd, image = icoimg6, bg = cfg_clr, cursor = 'hand2')
        return
    def genIco7(x, y):
        global icoimg7
        rawIcoImg7 = Image.open('./img/ware.png')
        rawIcoImg7 = rawIcoImg7.resize((x, y), Image.Resampling.LANCZOS)
        icoimg7 = ImageTk.PhotoImage(rawIcoImg7)
        global lblIcoImg7
        lblIcoImg7 = Label(dashbrd, image = icoimg7, bg = cfg_clr, cursor = 'hand2')
        return
    def genIco8(x, y):
        global icoimg8
        rawIcoImg8 = Image.open('./img/stat.png')
        rawIcoImg8 = rawIcoImg8.resize((x, y), Image.Resampling.LANCZOS)
        icoimg8 = ImageTk.PhotoImage(rawIcoImg8)
        global lblIcoImg8
        lblIcoImg8 = Label(dashbrd, image = icoimg8, bg = cfg_clr, cursor = 'hand2')
        return

    def lblIcoButPlacing():
        lblIcoBut1.place(x = 60, y = 195)
        lblIcoBut2.place(x = 60, y = 257)
        lblIcoBut3.place(x = 60, y = 317)
        lblIcoBut4.place(x = 60, y = 377)
        lblIcoBut5.place(x = 60, y = 437)
        lblIcoBut6.place(x = 60, y = 497)
        lblIcoBut7.place(x = 60, y = 557)
        lblIcoBut8.place(x = 60, y = 617)
    lblIcoButPlacing()

    def lblPlacing():
        lbl1.place(x=125, y=a[0]+10)
        lbl2.place(x=125, y=a[1]+10)
        lbl3.place(x=125, y=a[2]+10)
        lbl4.place(x=125, y=a[3]+10)
        lbl5.place(x=125, y=a[4]+10)
        lbl6.place(x=125, y=a[5]+10)
        lbl7.place(x=125, y=a[6]+10)
        lbl8.place(x=125, y=a[7]+10)
    lblPlacing()

    def genIco():
        genIco1(25, 25)
        genIco2(25, 30)
        genIco3(25, 30)
        genIco4(30, 30)
        genIco5(30, 30)
        genIco6(30, 30)
        genIco7(30, 30)
        genIco8(30, 30)
    genIco()

    def showTbl():
        return

    def temp1(e): toggleLbl1, genRight('phieuThue')
    def temp2(e): toggleLbl1, genRight('phieuThanhToan')
    def temp3(e): toggleLbl1, genRight('phong')
    def temp4(e): toggleLbl1, genRight('nhanVien')
    def temp5(e): toggleLbl1, genRight('khachHang')
    def temp6(e): toggleLbl1, genRight('dichVu')
    def temp7(e): toggleLbl1, genRight('pNhapTbiAndFood')
    def temp8(e): toggleLbl1, genRight('nhanVien')

    def onclickEffectAndGuide():
        lbl1.bind("<Button-1>", temp1)
        lbl2.bind("<Button-1>", temp2)
        lbl3.bind("<Button-1>", temp3)
        lbl4.bind("<Button-1>", temp4)
        lbl5.bind("<Button-1>", temp5)
        lbl6.bind("<Button-1>", temp6)
        lbl7.bind("<Button-1>", temp7)
        lbl8.bind("<Button-1>", temp8)
        lblIcoBut1.bind("<Button-1>", temp1)
        lblIcoBut2.bind("<Button-1>", temp2)
        lblIcoBut3.bind("<Button-1>", temp3)
        lblIcoBut4.bind("<Button-1>", temp4)
        lblIcoBut5.bind("<Button-1>", temp5)
        lblIcoBut6.bind("<Button-1>", temp6)
        lblIcoBut7.bind("<Button-1>", temp7)
        lblIcoBut8.bind("<Button-1>", temp8)

        lblIcoImg1.bind("<Button-1>", temp1)
        lblIcoImg2.bind("<Button-1>", temp2)
        lblIcoImg3.bind("<Button-1>", temp3)
        lblIcoImg4.bind("<Button-1>", temp4)
        lblIcoImg5.bind("<Button-1>", temp5)
        lblIcoImg6.bind("<Button-1>", temp6)
        lblIcoImg7.bind("<Button-1>", temp7)
        lblIcoImg8.bind("<Button-1>", temp8)
    onclickEffectAndGuide()

    def hovering():
        lblIcoImg1.bind("<Enter>", mouEnBut1)
        lblIcoImg1.bind("<Leave>", mouLeBut1)
        lbl1.bind("<Enter>", mouEnBut1)
        lbl1.bind("<Leave>", mouLeBut1)
        lblIcoImg2.bind("<Enter>", mouEnBut2)
        lblIcoImg2.bind("<Leave>", mouLeBut2)
        lbl2.bind("<Enter>", mouEnBut2)
        lbl2.bind("<Leave>", mouLeBut2)
        lblIcoImg3.bind("<Enter>", mouEnBut3)
        lblIcoImg3.bind("<Leave>", mouLeBut3)
        lbl3.bind("<Enter>", mouEnBut3)
        lbl3.bind("<Leave>", mouLeBut3)
        lblIcoImg4.bind("<Enter>", mouEnBut4)
        lblIcoImg4.bind("<Leave>", mouLeBut4)
        lbl4.bind("<Enter>", mouEnBut4)
        lbl4.bind("<Leave>", mouLeBut4)
        lblIcoImg5.bind("<Enter>", mouEnBut5)
        lblIcoImg5.bind("<Leave>", mouLeBut5)
        lbl5.bind("<Enter>", mouEnBut5)
        lbl5.bind("<Leave>", mouLeBut5)
        lblIcoImg6.bind("<Enter>", mouEnBut6)
        lblIcoImg6.bind("<Leave>", mouLeBut6)
        lbl6.bind("<Enter>", mouEnBut6)
        lbl6.bind("<Leave>", mouLeBut6)
        lblIcoImg7.bind("<Enter>", mouEnBut7)
        lblIcoImg7.bind("<Leave>", mouLeBut7)
        lbl7.bind("<Enter>", mouEnBut7)
        lbl7.bind("<Leave>", mouLeBut7)
        lblIcoImg8.bind("<Enter>", mouEnBut8)
        lblIcoImg8.bind("<Leave>", mouLeBut8)
        lbl8.bind("<Enter>", mouEnBut8)
        lbl8.bind("<Leave>", mouLeBut8)
    hovering()

    def placing():
        lblIcoImg1.place(x = 90, y = a[0]+10)
        lblIcoImg2.place(x = 90, y = a[1]+10)
        lblIcoImg3.place(x = 90, y = a[2]+10)
        lblIcoImg4.place(x = 87.5, y = a[3]+7.5)
        lblIcoImg5.place(x = 87.5, y = a[4]+7.5)
        lblIcoImg6.place(x = 87.5, y = a[5]+7.5)
        lblIcoImg7.place(x = 87.5, y = a[6]+7.5)
        lblIcoImg8.place(x = 87.5, y = a[7]+7.5)
    placing()


def updateDb():
    print('update db')
    return

def startAutoSave():
    global thrd1
    thrd1 = threading.Thread(target = autosave, args = ())
    thrd1.start()
    return

def mouOnBut(k):
    if (k==1):
        print('render phieu')
    return

def autosave():
    print('auto saving...')
    time.sleep(2)
    if (winClosed):
        try:
            thrd1.join()
        except (RuntimeError):
            pass
        return
    else:
        autosave()

def startKeyListener():
    def on_press(key):
        if (winClosed):
            return False
        if key == keyboard.Key.enter:
            updateDb()
        try:
            k = key.char 
        except:
            k = key.name 
        
    global listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  

def genDashUI():
    dashbrd.title('Dashboard')
    dashbrd.iconbitmap(appIco)
    dashbrd.configure(bg='white')
    tmp = str(appWidth) + 'x' + str(appHeight) + '+' + str(60) + '+' + str(0)
    dashbrd.geometry(tmp)
    dashbrd.resizable(False, False)


def genTopBanner():
    global topimg
    rawtopimg = Image.open('./img/hotel.jpg')
    rawtopimg = rawtopimg.resize((600, 200), Image.Resampling.LANCZOS)
    topimg = ImageTk.PhotoImage(rawtopimg)
    lblTopImg = Label(dashbrd, image = topimg)
    lblTopImg.place(x = 0, y = 0, relx = .25, rely = .25)

def genRight(s):
    
    dataNv = [
        ['B001', 'Trịnh Quang', 'Hòa', 'Nam', 1979, 'TP.HCM', 'CEO', 'Hội đồng quản trị', None, None],
        ['B002', 'Kim Đức', 'Long', 'Nam', 1983, 'Quảng Nam', 'CTO', 'Hội đồng quản trị', None, None],
        ['B003', 'Huỳnh Nguyên', 'Khang', 'Nam', 1982, 'Bình Phước', 'CFO', 'Hội đồng quản trị', None, None],
        ['G001', 'Hoàng Hòa', 'Hợp', 'Nam', 1982, 'Bình Thuận', 'Nhân viên', 'Bảo vệ', 5000000, 800000],
        ['G002', 'Lưu Duy', 'Hiếu', 'Nam', 1991, 'Long An', 'Nhân viên', 'Bảo vệ', 5000000, 800000],
        ['G003', 'Hồ Văn', 'Thông', 'Nam', 1998, 'Gia Lai', 'Trưởng phòng', 'Bảo vệ', 6000000, 1000000],
        ['G004', 'Nguyễn Văn', 'Sinh', 'Nam', 1991, 'TP.HCM', 'Nhân viên', 'Bảo vệ', 5000000, 600000],
        ['E001', 'Châu Văn', 'Đạt', 'Nam', 1998, 'Quảng Nam', 'Trưởng phòng', 'Kế toán', 8000000, 600000],
        ['E002', 'Nguyễn Thị', 'Nga', 'Nữ', 1991, 'Long An', 'Nhân viên', 'Kế toán', 7000000, 600000],
        ['E003', 'Vũ Việt', 'Đông', 'Nam', 1982, 'Tiền Giang', 'Nhân viên', 'Kế toán', 7000000, 600000],
        ['C001', 'Đào Ngọc', 'Cẩm', 'Nữ', 1992, 'Bình Dương', 'Nhân viên', 'Vệ sinh', 4000000, 600000],
        ['C002', 'Huỳnh Thụy Phương', 'Khánh', 'Nữ', 1996, 'TP.HCM', 'Nhân viên', 'Vệ sinh', 4000000, 600000],
        ['F001', 'Nguyễn Văn Gia', 'Trí', 'Nam', 1992, 'Tiền Giang', 'Trưởng phòng', 'Quản trị nhân sự', 6000000, 600000],
        ['F002', 'Lưu Ngọc Hoài ', 'Trinh', 'Nữ', 1992, 'Bình Dương', 'Nhân viên', 'Quản trị nhân sự', 6000000, 600000],
        ['Z001', 'Đoàn Trần Văn ', 'Kha', 'Nam', 1996, 'Long An', 'Bếp trưởng', 'Bếp ăn', 4000000, 600000],
        ['Z002', 'David ', 'Joe', 'Nam', 1998, 'TP.HCM', 'Đầu bếp', 'Bếp ăn', 8700000, 900000],
        ['Z003', 'Phạm Toàn ', 'Thắng', 'Nam', 1998, 'TP.HCM', 'Đầu bếp', 'Bếp ăn', 4000000, 600000],
        ['M001', 'Phạm Quốc ', 'Khải', 'Nam', 1996, 'Tiền Giang', 'Tiếp tân', 'Lễ tân', 3000000, 600000],
        ['M002', 'Nguyễn Võ ', 'Lợi', 'Nam', 2000, 'Gia Lai', 'Tiếp tân', 'Lễ tân', 3000000, 600000],
        ['T001', 'Lưu Bích ', 'Thoa', 'Nữ', 1992, 'Quảng Nam', 'Nhân viên', 'massage', 7000000, 600000],
        ['T002', 'Trần Thục ', 'Quyên', 'Nữ', 2000, 'Tây Ninh', 'Nhân viên', 'massage', 7000000, 600000],
        ['K001', 'Hứa Vĩnh ', 'Đức', 'Nam', 1990, 'Bến Tre', 'Nhân viên', 'Kho vận', 7000000, 600000],
        ['K002', 'Trần Phùng ', 'Thọ', 'Nam', 1998, 'TP.HCM', 'Nhân viên', 'Kho vận', 7000000, 600000]
    
    ]
    dataKh = [
        ['KH001', 'Nguyễn Thế', 'Doanh', 'Nam', 1983, '286 Str. 3/2, Ward 12, Dist', 312509075, 'Việt Nam', '09753650117', 'user01@gmail.com' ],
        ['KH002', 'Úc Quốc', 'Hải', 'Nam', 1982, ' 95 Nguyen Hong Dao street, Tan Binh District', 312509076, 'Việt Nam', '09753650117', 'user02@gmail.com' ],
        ['KH003', 'Nguyễn Thiện', 'Ân', 'Nam', 1979, '49 Le Trung Nghia, Ward. 12, Tan Binh District', 312509075, 'Việt Nam', '09753650117', 'user03@gmail.com' ],
        ['KH004', 'Vương Đăng', 'Đạt', 'Nam', 1982, '128 Tran Quy Cap, Group 4, Ninh Hoa, Khanh Hoa', 312509075, 'Việt Nam', '09753650117', 'user04@gmail.com'],
        ['KH005', 'Trang Diệu', 'Nương', 'Nữ', 1991, 'Tan Quy Tay Ward, Sa Dec Township', 312509075, 'Việt Nam', '09753650117', 'user05@gmail.com' ],
        ['KH006', 'Nguyễn Chiêu', 'Dương', 'Nữ', 1998, '659 Xo Viet Nghe Tinh, Binh Thanh District', 312509075, 'Việt Nam', '09753650117', 'user06@gmail.com' ],
        ['KH007', 'Bùi Thúy', 'Vy', 'Nam', 1991, '39A/3 Kha Van Can Street, Hiep Binh Chanh Ward, Thu Duc District', 312509075, 'Việt Nam', '09753650117', 'user07@gmail.com' ],
    ]
    dataPhieuThue = [
        ['PTP0001', ['KH001'], 'M001', {'DV001':2, 'DV002':1}, '20/10/2021', '20/12/2021', False, '', 0, 0, 0]
    ]
    dataPhieuTT = [
        ['PTT0001', ['KH001'], 'M001', '<tên nv Auto điền>', 12, 0, .15, 0, '<ngày in auto đi>']
    ]
    phieuNhapTbAndFood = [
        ['P001','H001', 'Coca-cola lon', '1000', 'NCC001', 'Nhà cung cấp 1', 'NV01', 500000, '10/3/2022'],
        ['P002','H002', 'Pepsi lon', '1000', 'NCC002', 'Nhà cung cấp 2', 'NV01', 500000, '11/3/2022'],
        ['P003','H003', 'Bia Sài Gòn', '1000', 'NCC003', 'Nhà cung cấp 3', 'NV01', 500000, '12/3/2022'],
        ['P004','H004', 'Trái cây', '20', 'NCC004', 'Nhà cung cấp 4', 'NV01', 100000, '14/3/2022'],
        ['P005','H005', 'Khăn lạnh', '1000', 'NCC005', 'Nhà cung cấp 5', 'NV01', 100000, '19/3/2022'],
        ['P006','H006', 'Thực phẩm', '20', 'NCC006', 'Nhà cung cấp 6', 'NV02', 200000, '21/3/2022'],
        ['P007','H007', 'Pepsi lon', '1000', 'NCC002', 'Nhà cung cấp 7', 'NV01', 500000, '25/3/2022'],
    ]
    dataDv = [
        ['DV001', 'Xông hơi', 250000],
        ['DV002', 'Massage', 500000],
        ['DV003', 'Tắm hồ bơi', 200000],
        ['DV004', 'Giặt ủi', 50000],
        ['DV005', 'Ăn sáng', 500000],
        ['DV006', 'Ăn trưa', 250000],
        ['DV007', 'Ăn tối', 250000]
    ]
    dataPh = [
        ['A101', 'available', 'Phòng thường 1 giường','normal', ['1 giường', ' 1 tu lanh nho', '1 bo ban ghe', '1 may lanh', '2 den']],
        ['A102', 'available', 'Phòng thường 2 giường','normal', ['2 giường', '1 tu lanh nho', '1 bo ban ghe', '1 may lanh', '2 den']],
        ['B202', 'available', 'Phòng cao cấp 1 giường','elite', ['1 giường', '1 tu lanh lon', '2 bo ban ghe ', '1 may lanh', '4 den', '1 bon tam']],
        ['B201', 'available', 'Phòng thường 2 giường','elite', ['2 giường', '1 tu lanh lon', '2 bo ban ghe ', '1 may lanh', '4 den', '1 bon tam']],
        ['C301', 'available', 'Phòng thượng hạng 1 giường','vip', ['1 giường', '1 tu lanh lon', '3 bo ban ghe ', '2 may lanh', '6 den', '1 bon tam', 'dien thoai', 'quay bep  + minibar']],
        ['C303', 'occupied', 'Phòng thượng hạng 2 giường','vip', ['2 giường', '1 tu lanh lon', '3 bo ban ghe ', '2 may lanh', '6 den', '1 bon tam', 'dien thoai', 'quay bep  + minibar']],
        ['A103', 'maintaining', 'Phòng thườnng 1 giường','normal', ['1 giường', ' 1 tu lanh nho', '1 bo ban ghe', '1 may lanh', '2 den']],
    ]
    dct = {
        'nhanVien': dataNv,
        'khachHang': dataKh,
        'phieuThue': dataPhieuThue,
        'phieuThanhToan': dataPhieuTT,
        'pNhapTbiAndFood': phieuNhapTbAndFood,
        'phong': dataPh,
        'dichVu': dataDv
    }

    with open('./json/data.json', 'w', encoding='utf-8') as fi:
        json.dump(dct, fi, ensure_ascii=False, indent=4)

    with open('./json/data.json', 'r', encoding='utf-8') as fo:
        dataRead = json.loads(fo.read())
    
    # print(json.dumps(dataRead['khachHang'], ensure_ascii=False, indent = 4))
    dataTbl = json.dumps(dataRead[s], ensure_ascii=False)
    dataTblList = json.loads(dataTbl)

    nvHeader = ["ID", "Họ", "Tên", "Giới tính", "Năm sinh", "Quê quán", "Chức vụ", "Bộ phận", "Lương", "Thưởng"]
    khHeader = ['ID', 'Họ', 'Tên', 'Giới tính', 'Năm sinh', 'Địa chỉ', 'Số CMND/CDDD', 'Quốc tịch', 'Số điện thoại', 'Email']
    ptpHeader = ["ID Phiếu", "ID Khách hàng", "ID Nhân viên", "Danh sách dịch vụ", "Ngày ở", "Ngày đến", "Trả trước", "Ghi chú", "Tiền thuê", "Phí dịch vụ", "Tổng tiền"]
    pttHeader = ['ID Phiếu', 'ID dịch vụ', 'ID nhân viên', 'Tên nhân viên', 'Số ngày ở', 'Tổng tiền', 'VAT', 'Tiền phải trả', 'Ngày in' ]
    pnHeader = ['ID phiếu', 'ID Hàng hóa', 'Tên hàng hóa', 'Số lượng', 'ID nhà cung cấp', 'Tên nhà cung cấp', 'ID nhân viên', 'Phí vận chuyển', 'Ngày nhập']
    phongHeader = ['ID', 'Trạng thái', 'Mô tả', 'Kiểu phòng', 'Trang bị']
    dvHeader = ['ID', 'Tên dịch vụ', 'Chi phí']
    toRenderHeader = []
    if (s == 'nhanVien'):
        toRenderHeader = nvHeader
    elif (s == 'phieuThue'):
        toRenderHeader = ptpHeader
    elif (s == 'khachHang'):
        toRenderHeader = khHeader
    elif (s == 'phieuThanhToan'):
        toRenderHeader = pttHeader
        tmpnvTbl = json.loads(json.dumps(dataRead['nhanVien'], ensure_ascii=False))
        tmpDataTbl = dataTblList
        for r1 in tmpDataTbl:
            isFound = False
            for r2 in tmpnvTbl:
                if (r2[0] == r1[2]):
                    print(r1)
                    print(r2)
                    r1[3] = r2[1] + r2[2]
                    isFound = True
            if (not isFound):
                r1[3] = '<Not found>'
    elif (s == 'pNhapTbiAndFood'):
        toRenderHeader = pnHeader
    elif (s == 'dichVu'):
        toRenderHeader = dvHeader
    elif (s == 'phong'):
        toRenderHeader = phongHeader
    global rSh
    rSh = Sheet(dashbrd, 
        show_table = True,
        width = tblWidth,
        height = tblHeight,
        show_header = True,
        row_height = 70,
        data = dataTblList,
        headers = list(toRenderHeader)
    )
    # rSh.set_cell_data(0, 0, value = 999, set_copy = True, redraw = False)
    rSh.set_all_cell_sizes_to_text(redraw = True)
    rSh.enable_bindings('all')
    rSh.place(x=340, y=200)

def genBotBut():
    botBut = Button(
        dashbrd,
        font = ('Chirp', 14),
        text = 'Save ',
        bg = 'white',
        border = '1px solid black',
        height = 1,
        width = 10
    )
    addBut1 = Button(
        dashbrd,
        font = ('Chirp', 14),
        text = 'Add +',
        bg = 'white',
        border = '1px solid black',
        height = 1,
        width = 10
    )
    sortBut1 = ttk.Combobox(
        dashbrd,
        font = ('Chirp', 14),
        values = ['1', '2', '3', '4'],
        text = 'Filter',
        width = 10,
        cursor = 'hand2'
    )
    botBut.place(x=800, y=630)
    addBut1.place(x=800, y=130)
    sortBut1.place(x=850, y=200)
    return



dashbrd = Tk()
# startAutoSave()
# startKeyListener()
genDashUI()
genNav()
# genTopBanner()
genRight('nhanVien')
genBotBut()
dashbrd.mainloop()
winClosed = True
# listener.join()


