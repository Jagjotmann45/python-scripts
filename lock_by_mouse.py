import pyautogui as pg
from time import sleep
import ctypes

lock_time = 9
var = 0
current1 = pg.position()

try:
	while 1:
		current2 = pg.position()
		if current1 == current2 and var == lock_time:
			ctypes.windll.user32.LockWorkStation()
		elif current1 != current2:
			current1 = pg.position()
			var = 0
		var += 1
		sleep(1)
except KeyboardInterrupt:
	print('Hope u locked it on time.')