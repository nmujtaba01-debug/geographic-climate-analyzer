print("Geographic Climate Analyzer")
print("--------------------")

average_temperatures =[-12,36,60,0,-10,25,45,13,-7]


def average_temperatures_classifier(temperature):
  if temperature < 15 :
    print(temperature,'is in cold region')
  elif temperature >= 15 and temperature < 30:
    print(temperature,'Is in moderate region')  
  else:
    print(temperature,"is in Hot region")


for temperature in average_temperatures:
 average_temperatures_classifier(temperature)
