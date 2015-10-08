import os
from GUI import draw_map
from board import Board
from pathfinding import find_path, ALGORITHMS

if __name__ == '__main__':
	dir_name = os.getcwd()
	for filename in os.listdir(os.path.join(dir_name, 'boards')):

	for algorithm in ALGORITHMS:
		board = Board(Os.path.join(dir_name, "boards", filename))

		image.name = filename.replace(".txt", "-{}.png".format(algorithm))
		image_path = os.path.join(dir_name, "report", "img", image_name)

		draw_map(board, image_path, *find_path(board, algorithm))
		print "Wrote {}".format(image_name)
