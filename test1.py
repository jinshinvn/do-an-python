from tksheet import Sheet
import tkinter as tk


class demo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.sheet = Sheet(self.frame,
                           expand_sheet_if_paste_too_big = True,
                           empty_horizontal = 0,
                           empty_vertical = 0,
                           align = "w",
                           header_align = "c",
                           data = [[f"Row {r}, Column {c}\nnewline 1\nnewline 2" for c in range(6)] for r in range(21)],
                           headers = ["Dropdown Column", "Checkbox Column", "Center Aligned Column", "East Aligned Column", "", ""],
                           theme = "dark",
                           height = 520,
                           width = 930)
        self.sheet.enable_bindings()
        self.sheet.enable_bindings("edit_header")
        self.frame.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        colors = ("#509f56",
                  "#64a85b",
                  "#78b160",
                  "#8cba66",
                  "#a0c36c",
                  "#b4cc71",
                  "#c8d576",
                  "#dcde7c",
                  "#f0e782",
                  "#ffec87",
                  "#ffe182",
                  "#ffdc7d",
                  "#ffd77b",
                  "#ffc873",
                  "#ffb469",
                  "#fea05f",
                  "#fc8c55",
                  "#fb784b",
                  "#fa6441",
                  "#f85037")
        self.sheet.align_columns(columns = 2, align = "c")
        self.sheet.align_columns(columns = 3, align = "e")
        self.sheet.create_dropdown(r = "all",
                                   c = 0,
                                   values = ["Dropdown"] + [f"{i}" for i in range(15)])
        self.sheet.create_checkbox(r = "all", c = 1, checked = True, text = "Checkbox")
        self.sheet.create_header_dropdown(c = 0, values = ["Header Dropdown"] + [f"{i}" for i in range(15)])
        self.sheet.create_header_checkbox(c = 1, checked = True, text = "Header Checkbox")
        self.sheet.align_cells(5, 0, align = "c")
        self.sheet.highlight_cells(5, 0, bg = "gray50", fg = "blue")
        self.sheet.highlight_cells(17, canvas = "index", bg = "yellow", fg = "black")
        self.sheet.highlight_cells(12, 1, bg = "gray90", fg = "purple")
        for r in range(len(colors)):
            self.sheet.highlight_cells(row = r,
                                       column = 3,
                                       fg = colors[r])
            self.sheet.highlight_cells(row = r,
                                       column = 4,
                                       bg = colors[r],
                                       fg = "black")
            self.sheet.highlight_cells(row = r,
                                       column = 5,
                                       bg = colors[r],
                                       fg = "purple")
        self.sheet.highlight_cells(column = 5,
                                   canvas = "header",
                                   bg = "white",
                                   fg = "purple")
        #self.sheet.display_columns(indexes = [0, 1, 2], enable = True)
        self.sheet.set_all_column_widths()
        self.sheet.extra_bindings("all", self.all_extra_bindings)
        
    def all_extra_bindings(self, event = None):
        #print (event)
        pass

        
app = demo()
app.mainloop()