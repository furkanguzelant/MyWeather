import requests
import json
import math
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("600x300")
root.title("MyWeather")
root.resizable(False, False)

background_image= PhotoImage(file = "bg.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
background_label.image = background_image

city_label = Label(root, text = "Enter city: ", font = "Helvetica 12")
city_entry = Entry(root, borderwidth=5, font = "Helvetica 12")

city_label.place(x = 150, y = 14)
city_entry.place(x = 250, y = 10, width=200, height = 30)

week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
setUnix = 1628899200
setDayIndex = 5

def findDay(unix):
    time_between = unix - setUnix
    day_num = math.floor(time_between / (3600 * 24))
    result = (setDayIndex + day_num) % 7
    return week[result]

def forecast(city = "Konya"):
    global clear
    global clear_label

    if city_entry.get() != "":
        city = city_entry.get()
    try:
        api_request = requests.get(
            "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&units=metric&appid=61659fdc59535b0384e2085bd606e5ff")
        api = json.loads(api_request.content)

        api_cur_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=61659fdc59535b0384e2085bd606e5ff")

        api_cur = json.loads(api_cur_request.content)

        print(api_cur)
        api_cur_weather = api_cur['weather'][0]
        api_cur_info = api_cur['main']

    except Exception as e:
        print(e)
        return False

    temp = []
    weatherCondition = []
    timestamps = []
    hours = []
    top = Toplevel()

    top.title("Weather report for " + city )
    top.geometry("800x750")

    Label(top, text = "4 day weather forecast for " + city, bd  = 1 , font = ("Helvetica", "16"))\
        .grid(row = 0, column = 1, columnspan = 3, sticky = "we")

    firstDay = findDay(api['list'][0]['dt'])
    firstDayIndex = week.index(firstDay)

    for hour in api['list']:
        temp.append(str(hour['main']['temp']) + " °C")
        weatherCondition.append(hour['weather'][0]['main'])
        timestamps.append(hour['dt_txt'][0: 10])
        hours.append(hour['dt_txt'][11 :])

    index_firstHour = hours.index("00:00:00")

    curWeatherIcon =  ImageTk.PhotoImage(Image.open('sunny.png'))
    background_image_top = 0

    if (api_cur_weather['main'] == "Clear"):
        curWeatherIcon = ImageTk.PhotoImage(Image.open('sunny.png'))
        background_image_top = PhotoImage(file="sunbg.png")
    elif (api_cur_weather['main'] == "Clouds"):
        curWeatherIcon = ImageTk.PhotoImage(Image.open('cloud_cur.png'))
        background_image_top = PhotoImage(file="cloud_bg.png")
    elif (api_cur_weather['main'] == "Rain"):
        curWeatherIcon = ImageTk.PhotoImage(Image.open('rain_cur.png'))
        background_image_top = PhotoImage(file="rain_bg.png")
    elif (api_cur_weather['main'] == "Snow"):
        curWeatherIcon = ImageTk.PhotoImage(Image.open('kar.png'))

    background_label_top = Label(top, image=background_image_top)
    background_label_top.place(x=0, y=0, relwidth=1, relheight=1, anchor="nw")
    background_label_top.image = background_image_top

    frame1 = LabelFrame(top, text = months[int(timestamps[index_firstHour][5:7]) - 1] + " " + timestamps[index_firstHour][8:10] + ", " +
                                    timestamps[0][0:4] + "  " + week[firstDayIndex], padx = 10, pady = 10, borderwidth = 5)
    frame2 = LabelFrame(top, text = months[int(timestamps[index_firstHour + 8][5:7]) - 1] + " " + timestamps[index_firstHour + 8][8:10] + ", " +
                                    timestamps[0][0:4] + "  " + week[(firstDayIndex + 1) % 7], padx = 10, pady = 10, borderwidth = 5)
    frame3 = LabelFrame(top, text = months[int(timestamps[index_firstHour + 16][5:7]) - 1] + " " + timestamps[index_firstHour + 16][8:10] + ", " +
                                    timestamps[0][0:4] + "  " + week[(firstDayIndex + 2) % 7], padx = 10, pady = 10, borderwidth = 5)
    frame4 = LabelFrame(top, text = months[int(timestamps[index_firstHour + 24][5:7]) - 1] + " " + timestamps[index_firstHour + 24][8:10] + ", " +
                                    timestamps[0][0:4] + "  " + week[(firstDayIndex + 3) % 7], padx = 10, pady = 10, borderwidth = 5)

    frame_cur = LabelFrame(top, text = "Current weather")
    labelWeather = Label(frame_cur, text = api_cur_weather['main'], font = ("Helvetica", "24"))
    labelTemp = Label(frame_cur, text= str(api_cur_info['temp']) + " °C", font=("Helvetica", "24"))


    cloud_label = Label(frame_cur, image = curWeatherIcon)
    cloud_label.image = curWeatherIcon
    cloud_label.grid(row = 0, column = 0)

    labelTemp.grid(row = 1, column = 0)
    labelWeather.grid(row = 2, column = 0)
    Label(frame_cur, text=str("   Humidity: " + str(api_cur_info['humidity'])) + " %", font=("Helvetica", "15")).grid(row = 0, column = 1)
    Label(frame_cur, text=str("   Feels like: " + str(api_cur_info['feels_like'])) + " °C", font=("Helvetica", "15")).grid(row=1, column=1)

    for i in range(index_firstHour, 40, 2):

        if i < index_firstHour + 8:
            frame = frame1
        elif i < index_firstHour + 16:
            frame = frame2
        elif i < index_firstHour + 24:
            frame = frame3
        elif i < index_firstHour + 32:
            frame = frame4
        else:
            break


        Label(frame, text="Time").grid(row=0, column=0)
        Label(frame, text="Weather").grid(row=0, column=1)
        Label(frame, text="Temperature").grid(row=0, column=2)

        time_label = Label(frame, text= hours[i], pady = 10, padx = 10)
        weather_label = Label(frame, text= weatherCondition[i],  pady = 10, padx = 10)
        temp_label = Label(frame, text = temp[i],  pady = 10, padx = 10)

        time_label.grid(row = i + 1, column = 0)
        weather_label.grid(row = i + 1, column = 1)
        temp_label.grid(row = i + 1, column = 2)

        if(weatherCondition[i] == "Clear"):
            clear = ImageTk.PhotoImage(Image.open('clear.png'))
            clear_label = Label(frame, image=clear)
            clear_label.image = clear
            clear_label.grid(row=i + 1, column=3)
        elif (weatherCondition[i] == "Clouds"):
            cloudy = ImageTk.PhotoImage(Image.open('cloudy2.png'))
            cloud_label = Label(frame, image=cloudy)
            cloud_label.image = cloudy
            cloud_label.grid(row=i + 1, column=3)
        elif (weatherCondition[i] == "Rain"):
            cloudy = ImageTk.PhotoImage(Image.open('rain.png'))
            cloud_label = Label(frame, image=cloudy)
            cloud_label.image = cloudy
            cloud_label.grid(row=i + 1, column=3)
        elif (weatherCondition[i] == "Snow"):
            cloudy = ImageTk.PhotoImage(Image.open('kar.png'))
            cloud_label = Label(frame, image=cloudy)
            cloud_label.image = cloudy
            cloud_label.grid(row=i + 1, column=3)

    frame1.grid(row = 2, column = 1, padx = 10, pady = 10)
    frame2.grid(row = 2, column = 2, padx = 10, pady = 10)
    frame3.grid(row = 3, column = 1, padx = 10, pady = 10)
    frame4.grid(row = 3, column = 2, padx = 10, pady = 10)

    frame_cur.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "we")

city_button = Button(root, text = "Check Weather", pady = 5, command = forecast, font = "Helvetica 10")
city_button.place(x = 250, y = 50)
root.mainloop()



