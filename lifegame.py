#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as ani

class LifeGame:

    def __init__(self, rows: int, cols: int) -> None:
        self.cells = np.zeros(shape=(rows+2, cols+2), dtype=int)
        self.cells[1:-1, 1:-1] = np.random.choice(a=[0, 1], size=(rows, cols))

    def life_cycle(self) -> None:
        new_cells = self.cells.copy()
        for row in range(1, self.cells.shape[0]-1):
            for col in range(1, self.cells.shape[1]-1):
                local_cells = self.cells[row-1:row+2, col-1:col+2]
                if self.cells[row, col] == 1:
                    n = np.count_nonzero(local_cells) - 1
                    if n == 2 or n == 3:
                        new_cells[row, col] = 1
                    else:
                        new_cells[row, col] = 0
                else:
                    n = np.count_nonzero(local_cells)
                    if n == 3:
                        new_cells[row, col] = 1
                    else:
                        new_cells[row, col] = 0
        self.cells = new_cells

    def _update(self, frame: int) -> None:
        self.life_cycle()
        plt.title(frame)
        plt.imshow(self.cells, cmap='binary')

    def show(self, n: int) -> None:
        fig = plt.figure()
        anime = ani.FuncAnimation(fig, func=self._update, frames=n, interval=300, repeat=False)
        plt.show()
        plt.close()

if __name__ == '__main__':
    lg = LifeGame(100, 100)
    lg.show(200)
