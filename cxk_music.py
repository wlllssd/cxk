import ctypes
import time
import math
import os, os.path,shutil
import pyaudio
import wave
import sys
import threading

CHUNK = 1024

# cxk舞蹈界面
def cxk_dance():
	# 控制cmd输出位置
	class COORD(ctypes.Structure):
		_fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

	STD_OUTPUT_HANDLE= -11
	std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	dwCursorPosition = COORD()
	dwCursorPosition.X = 0
	dwCursorPosition.Y = 0
	ctypes.windll.kernel32.SetConsoleCursorPosition(std_out_handle,dwCursorPosition)

	# 读取文件地址
	txtPath = os.getcwd()+'\\data_txt'
	txtLists = os.listdir(txtPath)

	# 将文件加载到py中
	total = []
	i = 0
	for txt in txtLists:
		# 为了对应BGM的时间，删除其中一些帧
		i += 1
		if i % 10 == 0:
			continue
		onepic = []
		with open(txtPath+'\\'+txt,'r',encoding='utf-8') as t:
			lines = t.readlines()
			for line in lines:
				onepic.append(line)
		total.append(onepic)

	# 输出模块
	os.system('cls')
	for pic in total:
		time.sleep(0.004)
		for line in pic:
			print(line,end='')
		print()
		time.sleep(0.1)
		ctypes.windll.kernel32.SetConsoleCursorPosition(std_out_handle,dwCursorPosition)

# cxk背景音乐
def cxk_music():
	# 音乐播放模块
	audioPath = os.getcwd()+'\\audio\\bgm.wav'
	wf = wave.open(audioPath, 'rb')
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True)
	data = wf.readframes(CHUNK)
	while data:
		stream.write(data)
		data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()
	p.terminate()
	

# 多线程执行
t1 = threading.Thread(target=cxk_dance)
t2 = threading.Thread(target=cxk_music)

t1.start()
t2.start()
t1.join()
t2.join()

# 结束程序
time.sleep(2)
os.system('cls')
exit()

