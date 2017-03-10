'''
Name of the Task : Neural DJ
KIITFEST ID : KF36723
Operating System : MacOS Sierra
Programming Language used: Python
External modules used (if any) : pydub
Additional instructions to use the program (if any) : pydub module should be installed and two audio files must exist already.
'''

from pydub import AudioSegment

sound1 = AudioSegment.from_mp3("h.mp3") #first audio file
sound2 = AudioSegment.from_mp3("i.mp3") #second audio file

# len() and slicing are in milliseconds
halfway_point = len(sound1) / 2
first_half = sound1[:halfway_point]

halfway_point = len(sound2) / 2
second_half = sound2[halfway_point:]

res = first_half + second_half
res.export("res.mp3", format="mp3")
