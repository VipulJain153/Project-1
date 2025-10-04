import os ,wikipedia,pyttsx3,speech_recognition as sr,webbrowser,datetime,pygame,openai
pygame.init()
SCREEN = pygame.display.set_mode((1280,720))
pygame.display.set_caption('JARVIS')
pygame.display.set_icon(pygame.image.load('icon.png'))
openai.api_key = "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"
with open('memory.txt', 'r+') as f:
    chatStr = f.read()
bgmusic=1
def TakeCommand():
    try:
        r = sr.Recognizer()
        r.pause_threshold = 0.6
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic)
            return r.recognize_google(r.listen(mic)).lower()
    except Exception as e:print(e);return 'error@44324324'
def ai(query):
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=query,
  temperature=2,
  max_tokens=2048,
  top_p=1,
  best_of=20,
  frequency_penalty=0,
  presence_penalty=0
)
    with open(datetime.datetime.now().strftime('Prompt %Y-%m-%d %H:%M:%S'),'w') as f:f.write(response)
def chat(query):
    global chatStr
    chatStr+=f'\n\nUser: {query}\n Jarvis: '
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=chatStr,
  temperature=2,
  max_tokens=2048,
  top_p=1,
  best_of=20,
  frequency_penalty=0,
  presence_penalty=0
)
    speak(response)
    chatStr+=response
    print(f'\nUser: {query}\n Jarvis: {response}')
def speak(word):
    engine = pyttsx3.init()
    engine.setProperty('rate',146)
    engine.setProperty('volume',100.0)
    engine.say(word)
    engine.runAndWait()
clock = pygame.time.Clock()
if __name__ == "__main__":
    speak('Hello, I am Jarvis Sir, How can I Serve You.')
    while True:
        SCREEN.blit(pygame.image.load('bg.jpg').convert_alpha(),(0,0))
        pygame.display.update()
        print('Listening...')
        query = TakeCommand()
        print(f"\n\nUser: {query}" if 'error@44324324' not in query else "")
        if 'error@44324324' in query:
            continue
        elif 'open' in query:
            if 'google' in query:
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            elif 'code' in query:
                os.startfile("C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif 'pycharm' in query:
                os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe")
            elif 'explorer' in query:
                os.system("explorer")
            elif 'youtube' in query:
                webbrowser.open('youtube.com')
            elif 'github' in query:
                webbrowser.open('github.com')
            elif 'stackoverflow' in query:
                webbrowser.open('stackoverflow.com')
            elif 'spotify' in query:
                webbrowser.open('open.spotify.com')
            elif 'chatgpt' in query:
                webbrowser.open('openai.com')
        elif 'wikipedia' in query:
            try:
                wiki = wikipedia.summary(query.replace('wikipedia', '').strip(),sentences=2)
                print('Jarvis: ',wiki)
                speak(wiki)
            except Exception as e:
                print("Jarvis: Not Found!")
                speak("Not Found!")
        elif 'time' in query:
            now = datetime.datetime.now().strftime("%H %S %p")
            print('Jarvis: ', now)
            speak(now)
        elif 'play music' in query:
            pygame.mixer.Sound('music.mp3').play()
        elif 'play background music' in query:
            bgmusic = pygame.mixer.Sound('music.mp3')
            bgmusic.play(loops=-1)
        elif 'stop music' in query:
            bgmusic.stop()
        elif 'search' in query:
            webbrowser.open(f"https://www.google.com/search?q={query.replace('search','').strip()}")
        elif 'watch' in query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query.replace('watch','').strip()}")
        elif 'using artificial intelligence' in query:
            ai(query.split('using artificial intelligence')[1])
        elif 'bye' in query or pygame.QUIT in [event.type for event in pygame.event.get()]:
            speak('Good Bye Sir.')
            with open("memory.txt","w") as f:
                f.write(chatStr)
            exit()
        elif 'reset chat' in query:
            chatStr = ""
        else:
            chat(query)
        clock.tick(60)