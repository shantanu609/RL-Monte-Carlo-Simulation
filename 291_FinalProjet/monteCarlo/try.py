import tkinter as tk
class A(tk.Tk):
    def __init__(self, x):
        super().__init__()
        self.x =x

    def update(self):
        pass


if __name__ == "__main__":
    a = A()
    a.update()
    