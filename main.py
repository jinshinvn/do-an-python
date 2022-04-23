from tkinter import Tk
from tkinter import Label
from tkinter import Canvas
from tksheet import Sheet

#ajshdjasd

tblWidth = 800
tblHeight = 400
appWidth = 1200
appHeight = 768
appIco = ''
navWidth = appWidth/4
heightLineNav = appHeight/3
lblNavX = navWidth/5*2+10



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
        background = 'blue'
    )

    lftNavDiv.create_rectangle(
        0, 0, navWidth, appHeight,
        outline = "grey",
        fill = 'grey'
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
    my_rectangle = round_rectangle(50, 50, 150, 100, radius=20, fill="blue")

    brand = Label(
        dashbrd,
        text = 'Khách sạn SGU',
        font = ('Roboto', 14),
        foreground = 'black',
        bg = 'white'
    )
    lftNavDiv.create_line(20, heightLineNav, navWidth-20, heightLineNav, fill = 'white', width = 3)
    lbl1 = Label(
        text = 'Phiếu thuê',
        font = ('Roboto', 14)
    )
    lbl2 = Label(
        text = 'Hóa đơn',
        font = ('Roboto', 14)
    )
    lbl3 = Label(
        text = 'Phòng',
        font = ('Roboto', 14)
    )
    lbl4 = Label(
        text = 'Nhân viên',
        font = ('Roboto', 14)
    )
    lbl5 = Label(
        text = 'Khách hàng' ,
        font = ('Roboto', 14)
    )
    lbl6 = Label(
        text = 'Dịch vụ',
        font = ('Roboto', 14)
    )
    lbl7 = Label(
        text = 'Kho hàng',
        font = ('Roboto', 14)
    )
    lbl8 = Label(
        text = 'Thống kê',
        font = ('Roboto', 14)
    )

    brand.place(x=10, y=10)

    LblPlacing = [30]
    for i in range(1,8):
        LblPlacing.append(LblPlacing[i-1]+42.5)

    lbl1.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[0])
    lbl2.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[1])
    lbl3.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[2])
    lbl4.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[3])
    lbl5.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[4])
    lbl6.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[5])
    lbl7.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[6])
    lbl8.place(x=navWidth/5*2, y=(appHeight-20)/3+LblPlacing[7])

    lftNavDiv.place(x=10, y=10) 

    # tblData = [
    #         [f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(5)] for r in range(3)
    #     ]

    tblData = [
        [2, 3, 4, 5, 6],
        [2, 4, 10]
    ]

    rSh = Sheet(dashbrd, 
        show_table = True,
        width = tblWidth,
        height = tblHeight,
        show_header = True,
        data = tblData
    )
    rSh.set_cell_data(0, 0, value = 999, set_copy = True, redraw = False)
    rSh.enable_bindings('all')
    
    rSh.place(x=200, y=50)


dashbrd = Tk()
genDashUI()
genNav()
dashbrd.mainloop()