import requests
import json
import time

print("Please wait while we load all city's database...")

time.sleep(2)

def other():
  inf1 = "http://apidev.accuweather.com/locations/v1/search?q="
  inf2 = str(input("Please enter your city name: "))
  inf3 = "&apikey=hoArfRosT1215"
  inf = inf1 + inf2 + inf3
  infreq = requests.get(inf).json()
  citykey = infreq[0]['Key']

  cond1 = "http://apidev.accuweather.com/currentconditions/v1/"
  cond2 = str(citykey)
  cond3 = ".json?language=en&apikey=hoArfRosT1215"
  cond = cond1 + cond2 + cond3
  data = requests.get(cond).json()

  timea = "Local time: "
  timem = data[0]['LocalObservationDateTime']
  weata = "Weather Condition: "
  weatm = data[0]['WeatherText']
  raina = "Chance of rain: "
  rainm = data[0]['HasPrecipitation']
  if rainm == False:
    rainn = 'No'
  elif rainm == True:
    rainn = 'Yes'
  tempa = "Temperature: "
  tempc = str(data[0]['Temperature']['Metric']['Value'])
  tempf = str(data[0]['Temperature']['Imperial']['Value'])

  time = timea + timem
  weather = weata + weatm
  rain = raina + rainn
  temp = tempa + tempc +' C' + ' or ' + tempf + ' F'

  alldata = [time, weather, rain, temp]

  for x in alldata:
    print(x)

  print(" ")

  other()

def default():
  res = requests.get('https://ipinfo.io/json')
  dt = res.json()
  decity = dt['region']
  
  inf1 = "http://apidev.accuweather.com/locations/v1/search?q="
  inf2 = decity
  inf3 = "&apikey=hoArfRosT1215"
  inf = inf1 + inf2 + inf3
  infreq = requests.get(inf).json()
  citykey = infreq[0]['Key']

  cond1 = "http://apidev.accuweather.com/currentconditions/v1/"
  cond2 = str(citykey)
  cond3 = ".json?language=en&apikey=hoArfRosT1215"
  cond = cond1 + cond2 + cond3
  data = requests.get(cond).json()

  timea = "Local time: "
  timem = data[0]['LocalObservationDateTime']
  weata = "Weather Condition: "
  weatm = data[0]['WeatherText']
  raina = "Chance of rain: "
  rainm = data[0]['HasPrecipitation']
  if rainm == False:
    rainn = 'No'
  elif rainm == True:
    rainn = 'Yes'
  tempa = "Temperature: "
  tempc = str(data[0]['Temperature']['Metric']['Value'])
  tempf = str(data[0]['Temperature']['Imperial']['Value'])
  dc = "Your location: "
  dc2 = inf2

  time = timea + timem
  weather = weata + weatm
  rain = raina + rainn
  temp = tempa + tempc +' C' + ' or ' + tempf + ' F'
  defcity = dc + dc2

  alldata = [defcity, time, weather, rain, temp]

  for x in alldata:
    print(x)

  print(" ")

default()
other()