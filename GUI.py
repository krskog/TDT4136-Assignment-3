from PIL import Image

some_colors = {
    'r': '#cd853f',
    'g': '#7fff00',
    'f': '#006400',
    'm': '#8b8989',
    'w': '#0000ff',
    'A': '#ff0000',
    'B': '#00ff00',
    '#': '#8b8989',
    '.': '#ffffff'
}

BLACK = '#000000'
GREEN = '#40FF00'
RED = '#FF0000'

TILE_SIDE = 32


def square(x, y):
    return (y * TILE_SIDE + 1,
            x * TILE_SIDE + 1,
            (y + 1) * TILE_SIDE - 1,
            (x + 1) * TILE_SIDE - 1)


def big_dot(x, y):
    return (y * TILE_SIDE + (TILE_SIDE / 2 - 3),
            x * TILE_SIDE + (TILE_SIDE / 2 - 3),
            y * TILE_SIDE + (TILE_SIDE / 2 + 3),
            x * TILE_SIDE + (TILE_SIDE / 2 + 3))


def small_dot(x, y):
    return (y * TILE_SIDE + (TILE_SIDE / 2 - 2),
            x * TILE_SIDE + (TILE_SIDE / 2 - 2),
            y * TILE_SIDE + (TILE_SIDE / 2 + 2),
            x * TILE_SIDE + (TILE_SIDE / 2 + 2))


def draw_map(board, file_path, path=None, open_nodes=None, closed_nodes=None):
    image = Image.new("RGB", (board.width * TILE_SIDE, board.height * TILE_SIDE))

    for x, row in enumerate(board.lines):
        for y, tile in enumerate(row):
            image.paste(some_colors[tile], square(x, y))

    for node in open_nodes:
        image.paste(RED, small_dot(node.x, node.y))

    for node in closed_nodes:
        image.paste(GREEN, small_dot(node.x, node.y))

    for node in path:
        image.paste(BLACK, big_dot(node.x, node.y))

    image.save(file_path)