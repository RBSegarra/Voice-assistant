
import speech_recognition as sr
import winsound
from gtts import gTTS
import os
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv

user_agent = os.environ.get("user-Agent")
load_dotenv()
apiKey = os.environ.get("google-token")
myText = 'Play what?'
newText = 'Now Playing '
title = ''
language = 'en'
youtube = build('youtube', 'v3', developerKey=apiKey)
r = sr.Recognizer()
frequency = 700  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
music_playing = False
idAccess = ''
text = ''
url = ''
cmd = ''


def musicplay():
    with sr.Microphone() as music_source:
        output = gTTS(text=myText, lang=language, slow=False)
        output.save('output.mp3')
        os.system('cmd /c output.mp3')
        winsound.Beep(frequency, duration)
        audio = r.listen(music_source)
        text = r.recognize_google(audio)
        request = youtube.search().list(part="snippet", maxResults=1, q=text)
        response = request.execute()
        itemAccess = response['items']
        for itemData in itemAccess:
            idAccess = itemData['id']
            titleAccess = itemData['snippet']
            title = titleAccess['title']
        print('Here is your link:  https://www.youtube.com/watch?v={}'.format(idAccess['videoId']))
        url = 'https://www.youtube.com/watch?v={}'.format(idAccess['videoId'])
        os.system('cmd /c del song.webm')
        cmd = "youtube-dl -f bestaudio -o song.webm {}".format(url)
        os.system('cmd /c {}'.format(cmd))
        now_playing = newText + title
        output = gTTS(text=now_playing, lang=language, slow=False)

        output.save('output2.mp3')
        now_playing = True
        os.system('cmd /c output2.mp3')
        os.system('cmd /c song.webm')


def main():
    with sr.Microphone() as source:
        print('Say Anything: ')
        winsound.Beep(frequency, duration)
        audio = r.listen(source)
        voice_text = ""
        try:
            voice_text = r.recognize_google(audio)
        except:
            print('Sorry could not recognize your voice')
    if voice_text == "play":
        musicplay()


def weather():
    tesxt = 't'
    # decide on api and code this section


# add some aychio functions here as well as well to pause or stop current song if current playing
while (True):
    main()



