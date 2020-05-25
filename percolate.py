import numpy as np
from numpy import random


class Percolate:

    def __init__(self, row=3):
        self.ROW = row
        self.BLOCK_SIZE = self.ROW ** 2
        self.block = np.zeros(self.BLOCK_SIZE)
        self.adjaceny_list = dict()

    def find_neighbors(self, item_index):
        left = item_index - 1
        right = item_index + 1
        up = item_index - self.ROW
        down = item_index + self.ROW
        return (left, right, up, down)

    def create_connection(self, item, connection):
        """Adjaceny List:
        {0: [(0,1), (2,3)]
            1: []
        }
        """
        if self.adjaceny_list.get(item):
            self.adjaceny_list[item].add(connection)
        else:
            self.adjaceny_list[item] = set()
            self.adjaceny_list[item].add(connection)

    def find_path(self, top, bottom):
        block = [0, 0, 1, 0, 0, 1, 1, 0, 0]
        top = (2, 1)[0]
        bottom = (6, 1)[0]

    def open_block(self):
        choice = random.choice(self.block.size)
        print("Opening a block")
        updated_location = self.block[choice] = 1
        return (choice, updated_location)

    def does_it_percolate(self):
        # I need to make a virtual top element for both the top and bottom.
        # top_row = enumerate(self.block:ROW])
        # active_top = list(filter(lambda x: x[1] is 1, top_row))
        # bottom_row = enumerate(self.block:-ROW])
        # active_bottom = list(filter(lambda x: x[1] is 1, bottom_row))
        # yield False
        # yield False
        yield True

    def block_main(self):
        while self.does_it_percolate() is False:
            self.open_block(self.block)
            # print(my_set)
        return print(f"\nThis block percolates:\n{self.block}")
