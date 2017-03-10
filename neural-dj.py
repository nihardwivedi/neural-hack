from pydub import AudioSegment

sound1 = AudioSegment.from_mp3("h.mp3")
sound2 = AudioSegment.from_mp3("i.mp3")

# len() and slicing are in milliseconds
halfway_point = len(sound1) / 2
first_half = sound1[halfway_point:]
halfway_point = len(sound2) / 2
second_half = sound2[halfway_point:]
# Concatenation is just adding
res = first_half + second_half

# writing mp3 files is a one liner
res.export("res.mp3", format="mp3")