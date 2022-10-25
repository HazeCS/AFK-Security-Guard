import pyautogui, time
from discord_webhook import DiscordWebhook
from random import *
from pynput.keyboard import Key, Listener

pyautogui.FAILSAFE = False

wr, hr = pyautogui.size()
ww = randint(1, wr)
hh = randint(1, hr)
num = 1

whook = "WEBHOOK HERE"

print("BHU Security Guard Starting in 10 Seconds!\n	Move Mouse to Bottom Right of the Screen then Top Left to Exit BHU Security Guard!\n		And HIDE THE CONSOLE!!")

time.sleep(10)

webhook = DiscordWebhook(url=whook, content=f'```ini\n[ BHU Security Guard ]\n	Guard Started! Your PC will be safe!\n\n	Move Mouse to Bottom Right of the Screen then Top Left to Exit BHU Security Guard!```')
webhook.execute()

while True:
	w, h = pyautogui.position()
	time.sleep(0.3)
	wu, hu = pyautogui.position()
	if wu == w and hu == h:
		pass
	else:
		webhook = DiscordWebhook(url=whook, content=f'```ini\n[ BHU Security Guard ]\n	Mouse Moved! ({w}, {h} to {wu}, {hu})\n		Running Mouse Spam Defence!```')
		webhook.execute()
		while True:
			ww = randint(1, wr - 5)
			hh = randint(1, hr - 5)
			w, h = pyautogui.position()
			if w == wr - 1 and h == hr - 1:
				time.sleep(1)
				w, h = pyautogui.position()
				if w == 0 and h == 0:
					webhook = DiscordWebhook(url=whook, content=f'```ini\n[ BHU Security Guard ]\n	Security Guard Killed | Secret Mouse Position Key!```')
					webhook.execute()
					exit()
				else:
					pass
			pyautogui.moveTo(ww, hh)
			if num == 10000:
				num = 1
				webhook = DiscordWebhook(url=whook, content=f'```ini\n[ BHU Security Guard ]\n	Self Defence Ended Naturally!```')
				webhook.execute()
				break
			else:
				num += 1
