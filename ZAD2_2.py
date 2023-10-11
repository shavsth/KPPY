temperature = float(input("Podaj temperaturę w stopniach Celsjusza: "))

if temperature <= -10:
    print("{} stopni to niezwykle zimna pogoda.".format(temperature))
elif -10 < temperature <= 0:
    print("{} stopni to zimna pogoda.".format(temperature))
elif 0 < temperature <= 10:
    print("{} stopni to chłodna pogoda.".format(temperature))
else:
    print("{} stopni to ciepła pogoda.".format(temperature))
