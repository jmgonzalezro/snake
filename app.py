from random import random
import tkinter as tk


window = tk.Tk()

window_dimensions = [800, 800]
window.geometry(str(window_dimensions[0]) + 'x' + str(window_dimensions[1]))
window.resizable(0, 0)
window.after_cancel


class Screen:
    # size
    # walls
    # possible_obstacles created as random non walkable walls
    #   this is possible with random creation and not repeating
    #   the last movement, (right right, down)
    pass


class input:
    # this can be created as just funcs
    pass


class Snake:
    # body
    # head
    # movement
    pass


class Booster:
    # size
    # power_up
    pass


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack
