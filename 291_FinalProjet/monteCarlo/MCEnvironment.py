import time
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image

np.random.seed(1)
PhotoImage = ImageTk.PhotoImage
UNIT = 100  # pixels
HEIGHT = 8  # grid height
WIDTH = 8  # grid width


class Env(tk.Tk):
    def __init__(self):
        super(Env, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('monte carlo')
        self.geometry('{0}x{1}'.format(HEIGHT * UNIT, HEIGHT * UNIT))
        self.shapes = self.load_images()
        self.canvas = self._build_canvas()
        self.texts = []

    def _build_canvas(self):
        canvas = tk.Canvas(self, bg='white',
                                height=HEIGHT * UNIT,
                                width=WIDTH * UNIT)
        # create grids
        for c in range(0, WIDTH * UNIT, UNIT):  # 0~400 by 80
            x0, y0, x1, y1 = c, 0, c, HEIGHT * UNIT
            canvas.create_line(x0, y0, x1, y1)
        for r in range(0, HEIGHT * UNIT, UNIT):  # 0~400 by 80
            x0, y0, x1, y1 = 0, r, HEIGHT * UNIT, r
            canvas.create_line(x0, y0, x1, y1)

        # add img to canvas
        # self.rectangle = canvas.create_image(50, 50, image=self.shapes[0])
        # self.triangle1 = canvas.create_image(250, 150, image=self.shapes[1])
        # self.triangle2 = canvas.create_image(150, 250, image=self.shapes[1])
        # self.circle = canvas.create_image(250, 250, image=self.shapes[2])
        self.black_square1 = canvas.create_image(150, 50, image=self.shapes[1])
        self.black_square2 = canvas.create_image(550, 50, image=self.shapes[1])
        self.black_square3 = canvas.create_image(650, 50, image=self.shapes[1])
        self.black_square4 = canvas.create_image(250, 250, image=self.shapes[1])
        self.black_square5 = canvas.create_image(350, 250, image=self.shapes[1])
        self.black_square6 = canvas.create_image(450, 250, image=self.shapes[1])
        self.black_square7 = canvas.create_image(450, 350, image=self.shapes[1])
        self.black_square8 = canvas.create_image(650, 350, image=self.shapes[1])
        self.black_square9 = canvas.create_image(150, 450, image=self.shapes[1])
        self.black_square10 = canvas.create_image(250, 450, image=self.shapes[1])
        self.black_square11 = canvas.create_image(650, 450, image=self.shapes[1])
        self.black_square12 = canvas.create_image(250, 550, image=self.shapes[1])
        self.black_square13 = canvas.create_image(550, 550, image=self.shapes[1])
        self.black_square14 = canvas.create_image(550, 650, image=self.shapes[1])
        self.black_square15 = canvas.create_image(650, 650, image=self.shapes[1])
        self.black_square16 = canvas.create_image(350, 750, image=self.shapes[1])
        self.green_square = canvas.create_image(750, 50, image=self.shapes[2])

        self.red_square1 = canvas.create_image(50, 50, image=self.shapes[3])
        self.red_square2 = canvas.create_image(450, 50, image=self.shapes[3])
        self.red_square3 = canvas.create_image(250, 350, image=self.shapes[3])
        self.red_square4 = canvas.create_image(650, 550, image=self.shapes[3])

        self.yellow_square = canvas.create_image(50, 750, image=self.shapes[0])

        # pack all
        canvas.pack()

        return canvas

    def load_images(self):
        yellow_triange = PhotoImage(
            Image.open("../img/yellow_square.png").resize((65, 65)))
        black_square = PhotoImage(
            Image.open("../img/black_square.png").resize((65, 65)))
        green_square = PhotoImage(
            Image.open("../img/green_square.png").resize((65, 65)))
        red_square = PhotoImage(
            Image.open("../img/red_square.png").resize((65, 65)))
        return yellow_triange,black_square,green_square,red_square

        # rectangle = PhotoImage(
        #     Image.open("../img/rectangle.png").resize((65, 65)))
        # triangle = PhotoImage(
        #     Image.open("../img/triangle.png").resize((65, 65)))
        # circle = PhotoImage(
        #     Image.open("../img/circle.png").resize((65, 65)))
        #
        # return rectangle, triangle, circle

    @staticmethod
    def coords_to_state(coords):
        x = int((coords[0] - 50) / 100)
        y = int((coords[1] - 50) / 100)
        print("x,y in coords", x,y)
        return [x, y]

    def reset(self):
        self.update()
        time.sleep(0.5)
        x, y = self.canvas.coords(self.yellow_square)
        print("x,y",x,y)
        self.canvas.move(self.yellow_square, UNIT / 2 - x, UNIT / 2 - y)
        # return observation
        return self.coords_to_state(self.canvas.coords(self.yellow_square))

    def step(self, action):
        state = self.canvas.coords(self.yellow_square)
        base_action = np.array([0, 0])
        self.render()

        if action == 0:  # up
            if state[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:  # down
            if state[1] < (HEIGHT - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:  # left
            if state[0] > UNIT:
                base_action[0] -= UNIT
        elif action == 3:  # right
            if state[0] < (WIDTH - 1) * UNIT:
                base_action[0] += UNIT
        # move agent
        self.canvas.move(self.yellow_square, base_action[0], base_action[1])
        # move rectangle to top level of canvas
        self.canvas.tag_raise(self.yellow_square)

        next_state = self.canvas.coords(self.yellow_square)

        # reward function
        if next_state == self.canvas.coords(self.green_square):
            #Goal State, so R goal is +1
            reward = 1
            done = True
        elif next_state in [self.canvas.coords(self.black_square1),
                            self.canvas.coords(self.black_square2), self.canvas.coords(self.black_square3), self.canvas.coords(self.black_square4),
                            self.canvas.coords(self.black_square5), self.canvas.coords(self.black_square6), self.canvas.coords(self.black_square7),
                            self.canvas.coords(self.black_square8), self.canvas.coords(self.black_square9), self.canvas.coords(self.black_square10),
                            self.canvas.coords(self.black_square11), self.canvas.coords(self.black_square12), self.canvas.coords(self.black_square13),
                            self.canvas.coords(self.black_square14), self.canvas.coords(self.black_square15),
                            self.canvas.coords(self.black_square16),
                            ]:
            reward = 0
            done = False

        elif next_state in [self.canvas.coords(self.red_square1),self.canvas.coords(self.red_square2),
                            self.canvas.coords(self.red_square3),self.canvas.coords(self.red_square4)]:
            reward = -1
            done = True
        else:
            reward = 0.02
            done = False

        next_state = self.coords_to_state(next_state)

        return next_state, reward, done

    def render(self):
        time.sleep(0.03)
        self.update()