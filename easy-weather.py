from tkinter import*
import urllib.request, urllib.parse, urllib.error
import json
from pprint import pprint

class Application(Frame):

    

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
       
    def createWidgets(self):

        self.master.title('Easy Weather')   
        
        self.label = Label(text = 'Easy Weather', font = 'Helvetica 30', bg = 'white', fg = 'blue')
        self.label.grid(row=0, columnspan=3)

        self.enterzip = Label(text = 'Enter your zipcode and press GO: ', font = 'Helvetica 15')
        self.enterzip.grid(row=1, column=0)
        
        self.zipentry = Entry()
        self.zipentry.grid(row=1, column=1)

        self.GO = Button(text = 'GO', font = 'Helvetica 13', command=self.get_weather)
        self.GO.grid(row=1, column=2) 

        

    def get_weather(self):
        zip = self.zipentry.get()
        url = 'http://api.openweathermap.org/data/2.5/weather?zip='
        apikey = 'us&appid=07130d9bce616a013a718eeb25ede6dd&units=imperial'
        fullurl = (url + zip + apikey)
        uh = urllib.request.urlopen(fullurl)

        data = uh.read().decode()
        js = json.loads(data)
        pprint(js)
        description = js['weather'][0]['description']
        wind = js['wind']['speed']
        wind = str(wind)+' mph'
        location = js['name']
        temperature = js['main']['temp']
        temperature = str(temperature)+' degrees'
        print('Temperature: ', temperature, 'location: ', location)
        print(description)
        
        self.descriptionlabel = Label(text = 'Description: ')
        self.descriptionlabel.grid(row = 3, column=0)

        self.description = Label(text = description)
        self.description.grid(row = 3, column = 1)
        
        self.locationlabel = Label(text = 'Location: ')
        self.locationlabel.grid(row = 2, column = 0)

        self.location = Label(text = location)
        self.location.grid(row = 2, column = 1)

        self.temperaturelabel = Label(text = 'Temperature: ')
        self.temperaturelabel.grid(row = 4, column = 0)

        self.temperature = Label(text = temperature)
        self.temperature.grid(row = 4, column = 1)
        
        self.windspeedlabel = Label(text = 'Windspeed: ')
        self.windspeedlabel.grid(row = 5, column = 0)

        self.windspeed = Label(text = wind)
        self.windspeed.grid(row = 5, column = 1)

root=Tk()
app = Application(master=root)
app.mainloop()
