from datetime import datetime

from .models import Monitor_video, Environment_monitor, Crop_maturity

temp = [12.3, 21.1, 18.4, 15.6]
light_intensity = [0,0,0,0]
CO_concentration = [0,0,0,0]
humidity = [0,0,0,0]
soil_humidity = [0,0,0,0]
precipitation = [0,0,0,0]

for i in range(3):
    test = Environment_monitor(temp = temp[i], light_intensity = light_intensity[i],\
         CO_concentration =  CO_concentration[i], humidity = humidity[i],\
         soil_humidity = soil_humidity[i], precipitation =  precipitation[i],\
         time = datetime.now()) 
    test.save()