from classes import Wall, Brick, make_limits


brick_qty = input('Quantity of every type of tile: ')
brick_probs = make_limits(brick_qty)

h_qty = int(input('Tiles quantuty horizontally: '))
v_qty = int(input('Tiles quantuty vertically: '))

wall = Wall(v_qty, h_qty)
wall.fill(brick_probs)
wall.fill_print()