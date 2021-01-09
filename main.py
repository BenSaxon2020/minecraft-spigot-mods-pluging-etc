import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    print(hexKeyCode)
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
# while (True):
#     PressKey(0x11)
#     # time.sleep(0.5)
#     # ReleaseKey(0x11)
time.sleep(3)
i=0
row_length = 180
num_of_rows = 4
rows_compleate = 0
# while i<=8:
while rows_compleate<=num_of_rows:
    PressKey(0x4C)#Numper 5 on key pad down
    PressKey(0x11)# W key down
    time.sleep(0.2)#0.2 seconds per block (without buffs)
    ReleaseKey(0x4C)#Numper 5 on key pad 
    ReleaseKey(0x11)# W key up
    print(i)
    i=i+1
    if i==row_length:
        PressKey(0x1E)#A key down
        time.sleep(0.2)
        ReleaseKey(0x1E)#A key up
        i=0
        while i<=row_length:
            PressKey(0x4C)#Numper 5 on key pad down
            PressKey(0x1F)#S key down
            time.sleep(0.2)
            ReleaseKey(0x4C)#Numper 5 on key pad 
            ReleaseKey(0x1F)
            i=i+1
        PressKey(0x1E)
        time.sleep(0.45)
        ReleaseKey(0x1E)
        i=0
        rows_compleate=rows_compleate+1







# # PressKey(0x1E)
# # PressKey(0x39)
# # time.sleep(0.4)
# # ReleaseKey(0x1E)
# # ReleaseKey(0x39)
# # PressKey(0x1E)
# # time.sleep(0.1)
# # ReleaseKey(0x1E)

# PressKey(0x1E)
# time.sleep(0.4)
# ReleaseKey(0x1E)

