import sys
import time

import Adafruit_MPR121.MPR121 as MPR121

highbar = MPR121.MPR121()
lowbar  = MPR121.MPR121()

#	sensor initialization
# high bar
if highbar.begin(address=0x5A): # default wiring
	print("# high bar sensor initialized #")
else:
	print("## error initializing high bar sensor, shutting down ##")
	sys.exit(1)
# low bar
if lowbar.begin(address=0x5B): # connect ADDR to 3 volts
	print("# low bar sensor initialized #")
else:
	print("## error initializing low bar sensor, shutting down ##")
	sys.exit(1)

highSaveBit = highbar.touched()
lowSaveBit  = lowbar.touched()

while True:
	changedPressedPins  = []
	changedReleasedPins = []
	highFetchBit = highbar.touched()
	lowFetchBit  = lowbar.touched()
	for i in range(12):
		scanBit = 1 << i
		if highFetchBit & scanBit and not highSaveBit & scanBit:
			changedPressedPins.append(i)
			print("- {0} high bar sensor pressed".format(i))
		if not highFetchBit & scanBit and highSaveBit & scanBit:
			changedReleasedPins.append(i)
			print("- {0} high bar sensor released".format(i))
	for i in range(12):
		scanBit = 1 << i
		lowbarOffset = i + 12
		if lowFetchBit & scanBit and not lowSaveBit & scanBit:
			changedPressedPins.append(lowbarOffset)
			print("- {0} high bar sensor pressed".format(lowbarOffset))
		if not lowFetchBit & scanBit and lowSaveBit & scanBit:
			changedReleasedPins.append(lowbarOffset)
			print("- {0} high bar sensor released".format(lowbarOffset))
	lowSaveBit  = lowFetchBit
	highSaveBit = highFetchBit
	print("# changed pins #")
	print(str(changedPressedPins) + " pressed pins")
	print(str(changedReleasedPins) + " released pins")
	time.sleep(0.001)
    