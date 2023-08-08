#This particular program is good for creating audio book 

from gtts import gTTS

import os
text = open("zen_of_python.txt","r").read()

# You can adjust your  language as you deemed fit, but also chane your text as well
language = 'en'

output = gTTS(text=text,lang=language,slow=False)

output.save('fileoutput.mp3')

os.system("afplay fileoutput.mp3") #I used MacOS