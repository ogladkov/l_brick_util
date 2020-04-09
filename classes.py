import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Wall:
    '''
    Makes wall with pattern and dataframe
    '''
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.wall = np.zeros((self.rows * self.cols))

    def fill(self, brick_probs):
        # Fills dataframe with random values of bricks according to limits avoiding repeating bricks in a row
        prev_brick_color = 0

        for x in range(self.wall.shape[0]):
            brick = Brick(prev_brick_color, brick_probs)
            self.wall[x] = brick.color
            prev_brick_color = brick.color

        self.wall = self.wall.reshape((self.rows, self.cols))
        self.df = pd.DataFrame(self.wall)

        for x in range(self.wall.shape[0]):
            if x % 2 == 0:
                self.df.iloc[x] = self.df.iloc[x].shift(-1)

        self.df.fillna(0, inplace=True)
        self.df = self.df.astype('int')

    def fill_print(self):
        # Makes a picture
        self.print_shape = np.zeros((self.cols * 4 * self.rows))

        for x in range(self.print_shape.shape[0]):
            self.print_shape[x] = self.wall.ravel()[x // 4]

        self.print_shape = self.print_shape.reshape(self.rows, self.cols * 4)

        # Shift every second row
        df = pd.DataFrame(self.print_shape)
        for x in range(self.print_shape.shape[0]):
            if x % 2 == 0:
                df.iloc[x] = df.iloc[x].shift(2)
                df.iloc[x, 0:2] = df.iloc[x, -2:].values

        plt.rcParams['figure.figsize'] = 18, 10
        plt.imshow(self.print_shape, cmap='OrRd_r')
        plt.show()


class Brick:
    def __init__(self, prev_brick_color, brick_probs):
        self.brick_probs = brick_probs
        self.colors_set = list(range(1, len(self.brick_probs)+1))
        self.color = np.random.choice(self.colors_set, p=self.brick_probs)

def make_limits(brick_qty):
    '''
    Makes limits from bricks quantities
    '''
    brick_qty = brick_qty.replace(' ', '').split(',')
    brick_qty = [float(x) for x in brick_qty]
    brick_probs = [x / sum(brick_qty) for x in brick_qty]
    return brick_probs