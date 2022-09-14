#==============================================
# Importing Files
#==============================================
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
#==============================================
# Define functions
#==============================================
def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text = mytext, lang = language, slow = False)
    myobj.save(filename)
#==============================================
#Combine all Audio Segments
#==============================================
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined
#==============================================
# Generating audio clips
#==============================================
def generateSkeleton():
    audio = AudioSegment.from_mp3('Mumbai local.mp3')
    
    # 1 - Time Hours

    # 2 - Generate baj kar
    start = 119500
    finish = 120100
    audioProcessed = audio[start:finish]
    audioProcessed.export("2_hindi.mp3",format="mp3")

    # 3 - Time Minutes

    # 4 - Generate minute ki
    start = 120300
    finish = 121050
    audioProcessed = audio[start:finish]
    audioProcessed.export("4_hindi.mp3",format="mp3")

    # 5 - Destination

    # 6 - Generate jaane wali
    start = 121550
    finish = 122300
    audioProcessed = audio[start:finish]
    audioProcessed.export("6_hindi.mp3",format="mp3")

    # 7 - Wagon Numbers

    # 8 - Generate dibbo ki
    start = 123000
    finish = 123500
    audioProcessed = audio[start:finish]
    audioProcessed.export("8_hindi.mp3",format="mp3")

    # 9 - Local Type

    # 10 - Generate local thodi hi samay mai platform kramank
    start = 124000
    finish = 126500
    audioProcessed = audio[start:finish]
    audioProcessed.export("10_hindi.mp3",format="mp3")

    # 11 - Platform No.

    # 12 - Generate par aa rahi hai
    start = 127000
    finish = 128030
    audioProcessed = audio[start:finish]
    audioProcessed.export("12_hindi.mp3",format="mp3")

#==============================================
#Generate Announcement
#==============================================
def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 1 - Time Hours
        textToSpeech(item['Hours'], '1_hindi.mp3')

        # 3 - Time Minutes
        textToSpeech(item['Minutes'], '3_hindi.mp3')
        
        # 5 - Destination
        textToSpeech(item['Destination'], '5_hindi.mp3')
        
        # 7 - Coach Numbers
        textToSpeech(item['Carts'], '7_hindi.mp3')
        
        # 9 - Local Type
        textToSpeech(item['Local Type'], '9_hindi.mp3')

        # 11 - Platform No.
        textToSpeech(item['Platform No.'], '11_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,13)]

        announcement = mergeAudios(audios)

        announcement.export(f'announcement_{index+1}.mp3',format = 'mp3')
#==============================================
#Main Function
#==============================================
if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Annoucement...")
    generateAnnouncement("announce_hindi.xlsx")