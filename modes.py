# flake8: noqa F821
# pylint: disable=C0114,E0602,C0116


from movement import (
    move_to_home,
    zigzag_path,
    move_to
)
from maps import default, full_p
from drivers import prepare_ground


def default_mode(
    amount=1  # type: int
):
    # prepare path
    move_to_home()
    current_map = default[::-1]
    path = zigzag_path(get_world_size())

    # movement loop
    for _ in range(amount):
        for x, y in path:
            move_to(x, y)

            entity_type = current_map[y][x]
            prepare_ground(entity_type)
            plant(entity_type)


def full_pumpkin_mode(
    amount=1  # type: int
):
    # prepare path
    move_to_home()
    total_fields = get_world_size() * get_world_size()
    current_map = full_p[::-1]
    path = zigzag_path(get_world_size())
    ready_fields = 0

    # movement loop
    for _ in range(amount):

        # planting loop
        while ready_fields < total_fields:

            # reset counter after iteration
            ready_fields = 0

            for x, y in path:
                move_to(x, y)
                entity_type = current_map[y][x]

                if get_entity_type() != Entities.Pumpkin:
                    harvest()

                prepare_ground(entity_type)
                plant(entity_type)

                if can_harvest():
                    ready_fields = ready_fields + 1
        print("Ready")

        # harvesting loop
        for x, y in path:
            move_to(x, y)
            harvest()
