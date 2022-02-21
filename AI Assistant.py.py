import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
import random
from datetime import date,datetime
engine=pyttsx3.init()
engine.setProperty("rate", 180)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices [0].id)
recognizer=sr.Recognizer()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def run_alexa():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print('\n')
        print("Start Speaking!!")
        talk('listening.. ')
        recordedaudio=recognizer.listen(source)
    try:
        command=recognizer.recognize_google(recordedaudio,language='en-in')
        command = command.lower()
        if 'niklaus' in command :
            command = command.replace('Niclaus', '')
            print('you said'+command)
        else :
            print('you said : '+command)
        if 'hello' in command :
            print('Hello Mate! How are you?')
            talk('Hello Mate! How are you?')

        elif 'what is your name' in command :
            print("Did i forgot to introduce Myself ? ")
            print("I'm your virtual mate Niklaus")
            talk("Did i forgot to introduce Myself ?  I'm your virtual mate Niklaus")

        elif'what do you look like' in command :
            l1={"Awesome, I hope!!.","I’m coded in secrecy. So you can't see me how am i looking !!","I Am look like an simple English Language just the fact is you can't see me !!"}
            item1 = random.choice(tuple(l1))
            print(item1)
            talk(item1)

        elif 'your birthday' in command :
            l2={"i don't have a single birthday , i go through lots and lots of versions , which means i have 365 sorts of birthdays "," I try to live every day like it’s my birthdays. I get more cake that way.!!"," It’s hard to remember. I was very young at the time."}
            item2 = random.choice(tuple(l2))
            print(item2)
            talk(item2)

        elif 'who are you' in command :
            print('I am Niklaus your virtual mate')
            talk('I am Niklaus.. your virtual mate. how can i help you ??')

        elif 'can you do' in command :
            print('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
                open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google.How may i help you ??''')
            talk('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
                open different websites like insta gram, youtube,gmail, git hub, stack overflow and searches on google. How may i help you ??''')
        elif 'play' in command:
            song = command.replace('play', '')
            print('Playing' +song)
            talk('Playing' +song)
            pywhatkit.playonyt(song)

        elif 'date and time' in command :
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            # Textual month, day and year
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2, 'Current time is', time)
            talk('Today is : '+ d2)
            talk('and current time is '+ time)

        elif 'time and date' in command :
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            # Textual month, day and year
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2, 'Current time is', time)
            talk( 'Current time is '+ time)
            talk('and Today is : '+ d2)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('The current time is' +time)
            talk("The current time is")
            talk(time)

        elif 'date' in command:
            today = date.today()
            print("Today's date:", today)
                # Textual month, day and year
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2)
            talk('The todays date is')
            talk(d2)

        elif 'tell me about' in command:
            name = command.replace('tell me about' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            talk(info)

        elif 'wikipedia' in command:
            name = command.replace('wikipedia' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            talk(info)

        elif 'what is' in command:
            name = command.replace('what is ' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            talk(info)

        elif 'who is ' in command:
            name = command.replace('who is' , '')
            info = wikipedia.summary(name, 1)
            print(info)
            talk(info)

        elif 'what is ' in command :
            search = 'https://www.google.com/search?q='+command
            print(' Here is what i found on the internet..')
            talk('searching... Here is what i found on the internet..')
            webbrowser.open(search)

        elif 'joke' in command:
            _joke = pyjokes.get_joke()
            print(_joke)
            talk(_joke)

        elif 'search' in command :
            search = 'https://www.google.com/search?q='+command
            talk('searching... ')
            webbrowser.open(search)

        elif "my location" in command:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            talk("You must be somewhere near here, as per Google maps")

        elif 'locate ' in command :
            talk('locating ...')
            loc = command.replace('locate', '')

            if 'on map' in loc :
                loc= loc.replace('on map',' ')
                url = 'https://google.nl/maps/place/'+loc+'/&amp;'
                webbrowser.get().open(url)
            print('Here is the location of '+loc)
            talk('Here is the location of '+loc)

        elif 'on map' in command :
            talk('locating ...')
            loc = command.split(" ")
            print(loc[1])
            url = 'https://google.nl/maps/place/'+loc[1] +'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc[1])
            talk('Here is the location of '+loc[1])

        elif 'location of' in command :
            talk('locating ...')
            loc = command.replace('find location of', '')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            talk('Here is the location of '+loc)

        elif 'where is ' in command :
            talk('locating ...')
            loc = command.replace('where is', '')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            talk('Here is the location of '+loc)

        elif 'bootcamps' in command :
            search = 'http://tathastu.twowaits.in/index.html#courses'
            talk('opening boot camps')
            webbrowser.open(search)

        elif 'boot camps' in command :
            search = 'http://tathastu.twowaits.in/index.html#courses'
            talk('opening boot camps')
            webbrowser.open(search)

        elif 'python bootcamp' in command :
            search = 'http://tathastu.twowaits.in/kickstart_python.html'
            talk('showing pythonboot camp')
            webbrowser.open(search)

        elif 'data science bootcamp' in command :
            search = 'http://tathastu.twowaits.in/kickstart_data_science.html'
            talk('showing data science and ml bootcamp')
            webbrowser.open(search)

        elif 'open google' in command :
            print('opening google ...')
            talk('opening google..')
            webbrowser.open_new('https://www.google.co.in/')

        elif 'gmail' in command :
            print('opening gmail ...')
            talk('opening gmail..')
            webbrowser.open_new('https://mail.google.com/')

        elif 'open youtube' in command :
            print('opening you tube ...')
            talk('opening you tube..')
            webbrowser.open_new('https://www.youtube.com/')

        elif 'open instagram' in command :
            print('opening instagram ...')
            talk('opening insta gram...')
            webbrowser.open_new('https://www.instagram.com/')

        elif 'open stack overflow' in command :
            print('opening stackoverflow ...')
            talk('opening stack overflow...')
            webbrowser.open_new('https://stackoverflow.com/')

        elif 'open github' in command :
            print('opening git hub ...')
            talk('opening git hub...')
            webbrowser.open_new('https://github.com/')

        elif 'bye' in command:
            print('good bye, have a nice day !!')
            talk('good bye, have a nice day !!')
            sys.exit()

        elif 'thank you' in command :
            print("your welcome")
            talk('your welcome')

        elif 'stop' in command:
            print('good bye, have a nice day !!')
            talk('good bye, have a nice day !!')
            sys.exit()

        elif 'tata' in command:
            print('good bye, have a nice day !!')
            talk('good bye, have a nice day !!')
            sys.exit()

        else:
            print(' Here is what i found on the internet..')
            talk('Here is what i found on the internet..')
            search = 'https://www.google.com/search?q='+command
            webbrowser.open(search)

    except Exception as ex:
        print(ex)
print('wait for a second...!!')
talk('wait for a second...!!')
print('\n')
print("I am Niklaus.. your virtual mate. how can i help you ??")
talk ("hello I am Niklaus.. your virtual mate. how can i help you ?? ")
while True:
     run_alexa()