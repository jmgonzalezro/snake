from random import random
import sys
import tkinter as tk

window = tk.Tk()

window_dimensions = [800, 800]
window.geometry(str(window_dimensions[0]) + "x" + str(window_dimensions[1]))
window.resizable(0, 0)
window.after_cancel

window.title("Snake over 9000 turbo'")

window.protocol("WM_DELETE_WINDOW", sys.exit)

frames_per_second = 12

game_canvas = tk.Canvas(window,
                        width=window_dimensions[0],
                        height=window_dimensions[1],
                        bd=0,
                        highlightthickness=0)

game_canvas.pack()

game_scale = 25
game_dimensions = [window_dimensions[0] / game_scale,
                   window_dimensions[1] / game_scale]


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
    # spawn position
    # body
    # head
    # movement
    pass


def create_booster():
    # spawn position
    spawn_position = [random.randit(0, window_dimensions[0]-1), 
                      random.randint(0, window_dimensions[1]-1)]
    # need to check if it's spawning in the actual snake
    # size
    # power_up
    return spawn_position


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack
