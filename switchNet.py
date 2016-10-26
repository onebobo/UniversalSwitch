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

	#cmd_command("control.exe /name Microsoft.NetworkAndSharingCenter")
	# NetworkAndSharingCenter window
	#window = get_foreground_window()
	#rec = get_window_rect(window)
	#exec_and_wait_pop(mouse_click,rec.left+644,rec.top+257)
	exec_and_wait_pop(cmd_command,'ncpa.cpl')
	time.sleep(0.1)

	key_press('right_arrow')
	key_press('left_arrow')
	exec_and_wait_pop(key_press,'ctrl','enter')

	#properties
	exec_and_wait_pop(key_press,'alt','p')

	#identity verification
	key_press('ctrl','tab')

	#other settings
	exec_and_wait_pop(key_press,'alt','d')

	#replace credential
	exec_and_wait_pop(key_press,'alt','c')

	key_input(account[0])
	key_press('tab')
	key_input(account[1])
	time.sleep(1)

	exec_and_wait_pop(key_press,'enter')
	exec_and_wait_pop(key_press,'enter')
	exec_and_wait_pop(key_press,'enter')
	exec_and_wait_pop(key_press,'esc')
	exec_and_wait_pop(key_press,'alt','F4')

if __name__ == '__main__':
	switch()