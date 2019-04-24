import ctypes
import os
import time
import time
import math
import os
import sys
import os, os.path,shutil

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
dwCursorPosition = COORD()
dwCursorPosition.X = 0
dwCursorPosition.Y = 0
ctypes.windll.kernel32.SetConsoleCursorPosition(std_out_handle,dwCursorPosition)


# print(os.getcwd())
txtPath = os.getcwd()+'\\data_txt'
# print(txtPath)
txtLists = os.listdir(txtPath)
# print(txtLists)

total = []
for txt in txtLists:
	onepic = []
	with open(txtPath+'\\'+txt,'r',encoding='utf-8') as t:
		lines = t.readlines()
		for line in lines:
			onepic.append(line)
	total.append(onepic)

os.system('cls')
for pic in total:
    for line in pic:
        print(line,end='')
    print()
    time.sleep(0.1)
    ctypes.windll.kernel32.SetConsoleCursorPosition(std_out_handle,dwCursorPosition)

time.sleep(2)
os.system('cls')
exit()


