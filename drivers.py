# flake8: noqa F821
# pylint: disable=C0114,E0602,C0116


def prepare_ground(
    entity  # type: Entities
):
    if entity == Entities.Tree:
        if get_ground_type() != Grounds.Grassland:
            till()

        use_item(Items.Fertilizer)

    elif entity == Entities.Grass:
        if get_ground_type() != Grounds.Grassland:
            till()

    elif entity == Entities.Bush:
        if get_ground_type() != Grounds.Grassland:
            till()

    elif entity == Entities.Pumpkin:
        if get_ground_type() != Grounds.Soil:
            till()

    elif entity == Entities.Carrot:
        if get_ground_type() != Grounds.Soil:
            till()

        if get_water() < 0.5:
            use_item(Items.Water)
