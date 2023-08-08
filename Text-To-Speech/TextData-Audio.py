from gtts import gTTS

import os

text = "LOL this is really funny"

output = gTTS(text=text,lang='en',slow=False)

output.save('output.mp3')

#To play whatever mp3 file you have made, either open it using os.system("start output.mp3"for windows) 
#os.system("afplay output.mp3"for MacOs) 

