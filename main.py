import subprocess
import sys
import math
import os

if __name__ != "__main__":
	print("call me directly!!")
	sys.exit(1)

COMMAND = "./target/release/mandelbrot_rs"
ASPECT_RATIO=1.5 # DEFAULT [1.5]
SHRINK_RATIO = 0.99 # DEFAULT [0.99]
FILESIZE_HEIGHT=10000 # DEFAULT [10000]
START_X = -2.3 # DEFAULT [-1.2]
START_Y = 1.02 # DEFAULT [0.35]

DEFAULT_WIDTH = 3.1000299996765301 # DEFAULT [0.2]
DEFAULT_HEIGHT = 2.0000816899999 # DEFAULT [0.15]


def processor(file_name, size, upper_left, lower_right):
	#print("py -> ", [COMMAND, file_name + ".png", size, upper_left, lower_right])
	#subprocess.Popen([COMMAND, file_name + ".png", size, upper_left, lower_right]) # 非同期実行
	subprocess.run([COMMAND, file_name + ".png", size, upper_left, lower_right]) # 同期実行
	return

height = DEFAULT_HEIGHT

name = input("enter name...").strip()
os.makedirs("./seeds/{}".format(name), exist_ok=True) 

for i in range(0, 3600):
	height =  DEFAULT_HEIGHT * SHRINK_RATIO ** i
	cSize_x = height * ASPECT_RATIO # 横幅
	cSize_y = height # 縦幅
	new_start_x = START_X + ((DEFAULT_WIDTH - cSize_x) / 2) # 左上のx座標
	new_start_y = START_Y - ((DEFAULT_HEIGHT - cSize_y) / 2) # 左上のy座標
	file_name = "./seeds/{}/{}".format(name, str(file_name).zfill(8))
	size = "{0}x{1}".format(math.floor(FILESIZE_HEIGHT * ASPECT_RATIO), math.floor(FILESIZE_HEIGHT))
	upper_left = "{0},{1}".format(new_start_x, new_start_y)
	lower_right = "{0},{1}".format(new_start_x + cSize_x, new_start_y - cSize_y)
	processor(file_name, size, upper_left, lower_right)

# /home/mandelbrot.rs/target/release/mandelbrot_rs image.png 40000x30000 -1.20,0.35 -1.0,0.20 &