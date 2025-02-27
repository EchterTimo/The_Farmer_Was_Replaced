# flake8: noqa F821
# pylint: disable=C0114,E0602,C0116

# Synonyms
p = Entities.Pumpkin
b = Entities.Bush
c = Entities.Carrot


def Carrot_driver():
    if get_water() < 0.5:
        use_item(Items.Water)

    if get_ground_type() != Grounds.Soil:
        till()
    plant(Entities.Carrot)


field = [
    [p, p, b, b, b],
    [p, p, b, b, b],
    [c, c, c, c, c],
    [c, c, c, c, c],
]


while True:

    # movement
    if get_pos_y() == get_world_size()-1:
        move(East)
    move(North)

    if can_harvest():
        harvest()

    if get_pos_x() == 0:
        if get_ground_type() != Grounds.Soil:
            till()
        plant(p)

    elif get_pos_x() == 1:
        if get_ground_type() != Grounds.Soil:
            till()
        plant(p)

    elif get_pos_x() == 2:
        plant(Entities.Bush)

    elif get_pos_x() == 3:

        if num_items(Items.Carrot) > 1.000:
            plant(Entities.Bush)
        else:
            Carrot_driver()
