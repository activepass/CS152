def weatherAnnouncer(temp, clearSkies, windy):
    #try to combine these two statements into one if statement!
    tempClass = temperatureClassification(temp)
    if (tempClass == 'HOT'):
        if (windy and clearSkies) or (clearSkies and not windy):
            return 'Wear summer clothes today.'
        elif windy and not clearSkies:
            return "Wear summer clothes today, but bring a rain jacket just in case."
        elif not windy and not clearSkies:
            return "Wear summer clothes today, but bring an umbrella just in case."
        else:
            return "Something has Gone Wrong!"
    elif (tempClass == 'FAIR'):
        if clearSkies and not windy:
            return "Wear whatever you would like today."
        else:
            return "Wear a jacket today."
    elif (tempClass == 'COLD'):
        if not clearSkies and windy:
            return "Just stay inside today."
        else:
            return "Wear winter gear today."
    

def temperatureClassification(temp):
    if temp < 40:
        return "COLD"
    elif temp > 40 and temp < 75:
        return "FAIR"
    elif temp >= 75:
        return "HOT"


#if hot and clear and not windy: 'Wear summer clothes today. 
print('TESTING', weatherAnnouncer(77, True, False))
# if hot and not clear and windy: 'Wear summer clothes today, but bring a rain jacket just in case.'
print('TESTING', weatherAnnouncer(95, False, True))
# if hot and not clear and not windy: 'Wear summer clothes today, but bring an umbrella just in case.'
print('TESTING', weatherAnnouncer(95, False, False))

# if fair AND clear AND not windy: 'Wear whatever you would like today.'
print('TESTING', weatherAnnouncer(56, True, False))
# if fair AND otherwise: 'Wear a jacket today.'
print('TESTING', weatherAnnouncer(56, False, False))

# if cold AND windy AND PC: 'Just stay inside today.'
print('TESTING', weatherAnnouncer(22, False, True))
# if cold AND otherwise: 'Wear winter gear today.'
print('TESTING', weatherAnnouncer(2, True, True)) 
