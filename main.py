from tkinter import Tk
from tkinter import Label
from tkinter import Canvas
from tkinter import Button
from tksheet import Sheet
from pynput import keyboard
from PIL import ImageTk, Image
import json
import threading
import time

winClosed = False
tblWidth = 825
tblHeight = 425
appWidth = 1200
appHeight = 768
appIco = ''
navWidth = appWidth/4
heightLineNav = appHeight/3
lblNavX = navWidth/5*2+10

def updateDb():
    print('update db')
    return

def startAutoSave():
    global thrd1
    thrd1 = threading.Thread(target = autosave, args = ())
    thrd1.start()
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


def genNav():
    
    lftNavDiv = Canvas(
        dashbrd,
        width = navWidth,
        height = appHeight,
        background = 'white'
    )

    lftNavDiv.create_rectangle(
        0, 0, navWidth, appHeight,
        outline = "black",
        fill = 'white'
    )

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
        return lftNavDiv.create_polygon(points, **kwargs, smooth=True)
    def drawRec():
        x = [ 
            
        ]
        y = [i for i in range(310, 500, 50)]
        print(y)

        my_rectangle1 = round_rectangle(50, 260, 260, 310, radius=1, fill="blue")
        my_rectangle2 = round_rectangle(50, 320, 260, 370, radius=1, fill="blue")
        my_rectangle3 = round_rectangle(50, 380, 260, 430, radius=1, fill="blue")
        my_rectangle4 = round_rectangle(50, 380, 260, 430, radius=1, fill="blue")
        my_rectangle5 = round_rectangle(50, 380, 260, 430, radius=1, fill="blue")
        my_rectangle6 = round_rectangle(50, 380, 260, 430, radius=1, fill="blue")
        my_rectangle7 = round_rectangle(50, 380, 260, 430, radius=1, fill="blue")
        my_rectangle8 = round_rectangle(50, 380, 260, 430, radius=1, fill="blue")
    drawRec()

    brand = Label(
        dashbrd,
        text = 'Khách sạn SGU',
        font = ('Chirp', 14),
        foreground = 'black',
        bg = 'white'
    )
    lftNavDiv.create_line(20, heightLineNav, navWidth-20, heightLineNav, fill = 'white', width = 3)
    lbl1 = Label(
        text = 'Phiếu thuê',
        bg = 'white',
        font = ('Chirp', 14)
    )
    lbl2 = Label(
        text = 'Hóa đơn',
        bg = 'white',
        font = ('Chirp', 14)
    )
    lbl3 = Label(
        text = 'Phòng',
        bg = 'white',
        font = ('Chirp', 14)
    )
    lbl4 = Label(
        text = 'Nhân viên',
        bg = 'white',
        font = ('Chirp', 14)
    )
    lbl5 = Label(
        text = 'Khách hàng' ,
        bg = 'white',
        font = ('Chirp', 14)
    )
    lbl6 = Label(
        text = 'Dịch vụ',
        bg = 'white',
        font = ('Chirp', 14)
    )
    lbl7 = Label(
        text = 'Kho hàng',
        bg = 'white',
        font = ('Chirp', 14)
    )
    lbl8 = Label(
        text = 'Thống kê',
        bg = 'white',
        font = ('Chirp', 14)
    )

    brand.place(x=10, y=10)

    LblPlacing = [30]
    for i in range(1,8):
        LblPlacing.append(LblPlacing[i-1]+50)

    lbl1.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[0])
    lbl2.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[1])
    lbl3.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[2])
    lbl4.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[3])
    lbl5.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[4])
    lbl6.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[5])
    lbl7.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[6])
    lbl8.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[7])

    lftNavDiv.place(x=0, y=0) 

def genTopBanner():
    global topimg
    rawtopimg = Image.open('./img/hotel.jpg')
    rawtopimg = rawtopimg.resize((600, 200), Image.Resampling.LANCZOS)
    topimg = ImageTk.PhotoImage(rawtopimg)
    lblTopImg = Label(dashbrd, image = topimg)
    lblTopImg.place(x = 0, y = 0, relx = .25, rely = .25)

def genRight():
    
    # initialize json
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
        ['P001','H001' 'Coca-cola lon', '1000', 'NCC001', '', 'NV01', 500000, '10/3/2022', ''],
        ['P002','H002' 'Pepsi lon', '1000', 'NCC002', '', 'NV01', 500000, '11/3/2022', ''],
        ['P003','H003' 'Bia Sài Gòn', '1000', 'NCC003', '', 'NV01', 500000, '12/3/2022', ''],
        ['P004','H004' 'Trái cây', '20', 'NCC004', '', 'NV01', 100000, '14/3/2022', ''],
        ['P005','H005' 'Khăn lạnh', '1000', 'NCC005', '', 'NV01', 100000, '19/3/2022', ''],
        ['P006','H006' 'Thực phẩm', '20', 'NCC006', '', 'NV02', 200000, '21/3/2022', ''],
        ['P007','H007' 'Pepsi lon', '1000', 'NCC002', '', 'NV01', 500000, '25/3/2022', ''],
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
    dataTbl = json.dumps(dataRead['khachHang'], ensure_ascii=False)
    dataTblList = json.loads(dataTbl)

    nvHeader = ["ID", "Họ", "Tên", "Giới tính", "Năm sinh", "Quê quán", "Chức vụ", "Bộ phận", "Lương", "Thưởng"]


    global rSh
    rSh = Sheet(dashbrd, 
        show_table = True,
        width = tblWidth,
        height = tblHeight,
        show_header = True,
        row_height = 70,
        data = dataTblList,
        headers = list(nvHeader)
    )
    # rSh.set_cell_data(0, 0, value = 999, set_copy = True, redraw = False)
    rSh.set_all_cell_sizes_to_text(redraw = True)
    rSh.enable_bindings('all')
    rSh.place(x=340, y=200)

def genBotBut():
    botBut = Button(
        dashbrd,
        text = 'Save',
        bg = 'red'
    )
    botBut.place(x=1000, y=600)
    return



dashbrd = Tk()
# startAutoSave()
startKeyListener()
genDashUI()
genNav()
genTopBanner()
genRight()

genBotBut()
dashbrd.mainloop()
winClosed = True
listener.join()