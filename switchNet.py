from utils import *
import json
import argparse



def switch():
	parser = argparse.ArgumentParser()
	parser.add_argument('index',type=int)
	args = parser.parse_args()
	index = args.index

	mdic = json.load(open('config.txt', 'r'))
	account = mdic[index]

	cmd_command("control.exe /name Microsoft.NetworkAndSharingCenter")
	# NetworkAndSharingCenter window
	time.sleep(0.5)
	window = get_foreground_window()
	rec = get_window_rect(window)

	execAndWaitPop(mouse_click,rec.left+644,rec.top+257)


	#properties
	execAndWaitPop(key_press,'alt','p')

	#identity verification
	key_press('ctrl','tab')

	#other settings
	execAndWaitPop(key_press,'alt','d')

	#replace credential
	execAndWaitPop(key_press,'alt','c')

	key_input(account[0])
	key_press('tab')
	key_input(account[1])
	time.sleep(1)

	execAndWaitPop(key_press,'enter')
	execAndWaitPop(key_press,'enter')
	execAndWaitPop(key_press,'enter')
	execAndWaitPop(key_press,'esc')
	execAndWaitPop(key_press,'alt','F4')

if __name__ == '__main__':
	switch()