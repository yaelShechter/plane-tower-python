import itertools

indices = [-1, 0, 1]


def both_zero(x, y):
    return x == 0 and y == 0


class Grid:
    def __init__(self, size, checker_size):
        self.size = size
        self.checker_size = checker_size

    def on_grid(self, plane, index_1, index_2):
        x, y = plane.get_position()
        return 0 <= x + index_1 < self.size and 0 <= y + index_2 < self.size

    def pos_collide(self, plane_1, plane_2, index_1, index_2):
        x_1, y_1 = plane_1.get_position()
        x_2, y_2 = plane_2.get_position()
        return x_1 + (index_1 * self.checker_size) == x_2 and y_1 + (index_2 * self.checker_size) == y_2

    def find_good_checker(self, plane, planes_list):
        for other_plane in planes_list:
            if plane is not other_plane:
                for index_1, index_2 in itertools.product(indices, indices):
                    if not both_zero(index_1, index_2) and \
                            self.on_grid(plane, index_1, index_2) and \
                            not self.pos_collide(plane, other_plane, index_1, index_2):
                        return index_1, index_2

    def is_dangerous(self, plane, planes_list):
        for other_plane in planes_list:
            if plane is not other_plane:
                for index_1, index_2 in zip(indices, indices):
                    if self.on_grid(plane, index_1, index_2) and \
                            self.pos_collide(plane, other_plane, index_1, index_2):
                        return True
        return False
