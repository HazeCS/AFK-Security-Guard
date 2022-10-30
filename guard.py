import pyautogui, time, argparse, platform
from discord_webhook import DiscordWebhook
from random import *
from pynput.keyboard import Key, Listener

parser = argparse.ArgumentParser(description='AFK Security Guard')
parser.add_argument('-brtl', required=False, action='store_true', help='Bottom Right to Top Left')
parser.add_argument('-brtr', required=False, action='store_true', help='Bottom Right to Top Right')
parser.add_argument('-bltl', required=False, action='store_true', help='Bottom Left to Top Left')
parser.add_argument('-bltr', required=False, action='store_true', help='Bottom Left to Top Right')
parser.add_argument('-brbl', required=False, action='store_true', help='Bottom Right to Bottom Left')
parser.add_argument('-blbr', required=False, action='store_true', help='Bottom Left to Bottom Right')
parser.add_argument('-trtl', required=False, action='store_true', help='Top Right to Top Left')
parser.add_argument('-tltr', required=False, action='store_true', help='Top Left to Top Right')
parser.add_argument('-trbl', required=False, action='store_true', help='Top Right to Bottom Left')
parser.add_argument('-trbr', required=False, action='store_true', help='Top Right to Bottom Right')
parser.add_argument('-tlbl', required=False, action='store_true', help='Top Left to Bottom Left')
parser.add_argument('-tlbr', required=False, action='store_true', help='Top Left to Bottom Right')
args = parser.parse_args()

pyautogui.FAILSAFE = False

wr, hr = pyautogui.size()
ww = randint(1, wr)
hh = randint(1, hr)
num = 1

sr = wr - 1
sl = wr - wr
st = hr - hr
sb = hr - 1

whook = "https://discordapp.com/api/webhooks/1034281360745037895/mmA6oViyhZK8St7yIRWAL7gVX0xSfxYPmcdjoDQe-xSLyv-9eoZevkjYpL-8vJtbx2vj"

clf = open("log.txt", "w")
clf.write('')
clf.close()

f = open('log.txt', 'a')

def exitn():
	webhook = DiscordWebhook(url=whook, content=f'```ini\n[ BHU Security Guard ]\n	Security Guard Killed | Secret Mouse Position Key!```')
	webhook.execute()
	f.write(f'[ BHU Security Guard ]\n	Security Guard Killed | Secret Mouse Position Key!\n\n')
	f.close()
	exit()

def fNoti(key):
	webhook = DiscordWebhook(url=whook, content=f'```ini\n[ BHU Security Guard ]\n  Security Guard Started |    \nSecret Mouse Position Key is {key}!```')
	webhook.execute()

def key(fw, fh, sw, sh):
	w, h = pyautogui.position()
	if w == fw and h == fh:
		time.sleep(1)
		w, h = pyautogui.position()
		if w == sw and h == sh:
			exitn()
		else:
			pass

if platform.system() == 'Windows':
	def msg():
		print('Starting in 5 seconds... Make sure to hide the console!')

if platform.system() == 'Linux':
	def msg():
		print('Starting in 5 seconds... Make sure to hide the terminal!')

if args.brtl:
	fNoti('Bottom Right to Top Left')
	def checkKey():
		key(sr, sb, sl, st)
			
if args.brtr:
	fNoti('Bottom Right to Top Right')
	def checkKey():
		key(sr, sb, sr, st)

if args.bltl:
	fNoti('Bottom Left to Top Left')
	def checkKey():
		key(sl, sb, sl, st)
			
if args.bltr:
	fNoti('Bottom Left to Top Right')
	def checkKey():
		key(sl, sb, sr, st)
			
if args.brbl:
	fNoti('Bottom Right to Bottom Left')
	def checkKey():
		key(sr, sb, sl, sb)
			
if args.blbr:
	fNoti('Bottom Left to Bottom Right')
	def checkKey():
		key(sl, sb, sr, sb)
			
if args.trtl:
	fNoti('Top Right to Top Left')
	def checkKey():
		key(sr, st, sl, st)
			
if args.tltr:
	fNoti('Top Left to Top Right')
	def checkKey():
		key(sl, st, sr, st)

if args.trbl:
	fNoti('Top Right to Bottom Left')
	def checkKey():
		key(sr, st, sl, sb)

if args.trbr:
	fNoti('Top Right to Bottom Right')
	def checkKey():
		key(sr, st, sr, sb)

if args.tlbl:
	fNoti('Top Left to Bottom Left')
	def checkKey():
		key(sl, st, sl, sb)

if args.tlbr:
	fNoti('Top Left to Bottom Right')
	def checkKey():
		key(sl, st, sr, sb)

class Main:
	msg()
	time.sleep(5)
	while True:
		w, h = pyautogui.position()
		time.sleep(0.3)
		wu, hu = pyautogui.position()
		if wu == w and hu == h:
			pass
		else:
			webhook = DiscordWebhook(url=whook, content=f'```ini\n[ BHU Security Guard ]\n	Mouse Moved! ({w}, {h} to {wu}, {hu})\n		Running Mouse Spam Defence!```')
			webhook.execute()
			f.write(f'[ BHU Security Guard ]\n	Mouse Moved! ({w}, {h} to {wu}, {hu})\n		Running Mouse Spam Defence!\n\n')
			while True:
				ww = randint(1, wr - 5)
				hh = randint(1, hr - 5)
				w, h = pyautogui.position()
				checkKey()
				pyautogui.moveTo(ww, hh)
				if num == 10000:
					num = 1
					webhook = DiscordWebhook(url=whook, content=f'```ini\n[ BHU Security Guard ]\n	Self Defence Ended Naturally!```')
					webhook.execute()
					f.write(f'[ BHU Security Guard ]\n Self Defence Ended Naturally!\n\n')
					break
				else:
					num += 1
