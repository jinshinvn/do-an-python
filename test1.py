from matplotlib import pyplot as plt
def cvPicPlot(str):
    print(str)
    plt.plot()
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = [10, 20, 30, 40, 50, 60, 10, 20, 30, 11, 11, 12]
    plt.plot(x, y, color = "red"); #put ; to remove [<matplotlib.lines.Line2D at 0x17859473280>]
    plt.xlabel('MONTH')
    plt.ylabel('USD')
    plt.tight_layout()
    # plt.savefig('plot.png')
    plt.title('Doanh thu theo tháng tính bằng USD')
cvPicPlot("Xin chào")