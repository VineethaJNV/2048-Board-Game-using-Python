import tkinter
from tkinter import *
#from tkinter import Frame, Label, CENTER

import logics
import values as v

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title("2048")
        self.master.bind("<Key>", self.down_key)
        self.commands = {v.UP_KEY:logics.move_up, v.DOWN_KEY:logics.move_down,
                         v.LEFT_KEY:logics.move_left, v.RIGHT_KEY:logics.move_right}

        self.mat_cells = []
        self.init_mat()
        self.init_matrix()
        self.update_mat_cells()

        self.mainloop()

    def init_mat(self):
        background = Frame(self, bg = "blue",
                           width = v.AREA, height = v.AREA)
        '''background = Frame(self, bg = v.BG_COLOR,
                           width = v.AREA, height = v.AREA)'''
        background.grid()

        for i in range(v.MAT_LEN):
            mat_row = []
            for j in range(v.MAT_LEN):
                cell = Frame(background, bg = v.BG_COLOR_EMPTY_CELL,
                             width = v.AREA / v.MAT_LEN,
                             height = v.AREA / v.MAT_LEN)
                cell.grid(row = i, column = j, padx = v.MAT_PADDING,
                         pady = v.MAT_PADDING)
                x = Label(master = cell, text = "",
                          bg = v.BG_COLOR_EMPTY_CELL,
                          justify = CENTER, font = v.FONT, width = 5, height = 2)
                x.grid()
                mat_row.append(x)

            self.mat_cells.append(mat_row)

    def init_matrix(self):
        self.matrix = logics.start_game()
        logics.add_new_2(self.matrix)
        logics.add_new_2(self.matrix)

    def update_mat_cells(self):
        for i in range(v.MAT_LEN):
            for j in range(v.MAT_LEN):
                num = self.matrix[i][j]
                if num == 0:
                    self.mat_cells[i][j].configure(text = "", bg = v.BG_COLOR_EMPTY_CELL)
                else:
                    self.mat_cells[i][j].configure(text = str(num),
                        bg = v.BG_COLOR[num], fg = v.CELL_COLOR[num])
        self.update_idletasks()

    def down_key(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                logics.add_new_2(self.matrix)
                self.update_mat_cells()
                changed = False
                if logics.get_current_state(self.matrix) == "WON":
                    self.mat_cells[1][1].configure(
                        text = "You", bg = v.BG_COLOR_EMPTY_CELL)
                    self.mat_cells[1][2].configure(
                        text = "Won!", bg = v.BG_COLOR_EMPTY_CELL)
                if logics.get_current_state(self.matrix) == "LOST":
                    self.mat_cells[1][1].configure(
                        text = "You", bg = v.BG_COLOR_EMPTY_CELL)
                    self.mat_cells[1][2].configure(
                        text = "Lose!", bg = v.BG_COLOR_EMPTY_CELL)

game_mat = Game2048()
                    
                                                  
            
        
