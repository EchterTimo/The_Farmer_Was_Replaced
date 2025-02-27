# flake8: noqa F821
# pylint: disable=C0114,E0602,C0116


def move_to(
    x,  # type: int
    y  # type: int
):
    # x pos
    while get_pos_x() < x:
        move(East)
    while get_pos_x() > x:
        move(West)

    # y pos
    while get_pos_y() < y:
        move(North)
    while get_pos_y() > y:
        move(South)


def move_to_home():
    move_to(0, 0)


def zigzag_path(
    size  # type: int
):
    path = []  # type: list[tuple[int, int]]
    for x in range(size):
        if x % 2 == 0:
            # Downward movement
            for y in range(size):
                path.append((x, y))
        else:
            # Upward movement
            for y in range(size - 1, -1, -1):
                path.append((x, y))
    return path
