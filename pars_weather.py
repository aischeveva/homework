
# coding: utf-8

# In[30]:

import urllib.request
import re
req = urllib.request.Request('https://yandex.ru/pogoda/moscow')
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')
    regTemp = re.compile('<div class="current-weather__thermometer current-weather__thermometer_type_now">.*?</div>')
    regCloud = re.compile('<span class="current-weather__comment">.*?</span>')
    regEx = re.compile('<.*?>', flags = re.DOTALL)
    temp = regTemp.findall(html)
    cloud = regCloud.findall(html)
    cloud = regEx.sub("", cloud[0])
    temp = regEx.sub("", temp[0])
    print(cloud + ', ' + temp)
    
    regSunr = re.compile('<span class="current-weather__info-label">Восход: </span>.*?<', flags = re.DOTALL)
    sunr = regSunr.findall(html)
    sunr = regEx.sub("", sunr[0])
    sunr = re.sub("<", "", sunr)
    print(sunr)
    
    regSund = re.compile('<span class="current-weather__info-label current-weather__info-label_type_sunset">Закат: </span>.*?<', flags = re.DOTALL)
    sund = regSund.findall(html)
    print(sund)


# In[ ]:



