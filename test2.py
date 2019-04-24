import ctypes

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
dwCursorPosition = COORD()
dwCursorPosition.X = 5
dwCursorPosition.Y = 2
ctypes.windll.kernel32.SetConsoleCursorPosition(std_out_handle,dwCursorPosition)
i=1
while True:
    print(i)
    i += 1
    ctypes.windll.kernel32.SetConsoleCursorPosition(std_out_handle,dwCursorPosition)
exit()

