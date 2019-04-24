# -*- coding: utf-8 -*-
import time
import math
import os
import sys
import os, os.path,shutil
print(os.getcwd())
txtPath = os.getcwd()+'\\data_txt'
print(txtPath)
txtLists = os.listdir(txtPath)
print(txtLists)

for txt in txtLists:
	with open(txtPath+'\\'+txt,'r',encoding='utf-8') as t:
		lines = t.readlines()
		for line in lines:
			print(line,end='')
		print()
	time.sleep(0.5)
	os.system('cls')