def get_logic():
    logic = input("enter either d = distance  or t = temperature")
    return logic

def get_dist():
    dist = input("enter your distance unite 'using km=kilometre or m=miles'")
    return dist

def get_temp():
    temp = input("enter your temperature unite 'using only c=celsius or f=fehrenheit': \n")
    return temp

def dist_conv(dist):
    if dist == 'km':
        kilometre = int(input("enter your distance in kilometre: "))
        return (kilometre * 0.621371)
    elif dist == 'm':
        miles = int(input("enter your distance in miles: "))
        return (miles * 1.60934)
    else:
       print("enter either km = kilometre or m = miles")

def temp_conv(temp):
    if temp == 'c':
        celsius = int(input("enter your temp in celsius: "))
        return (celsius * (9/5)+32)
    elif temp == 'f':
        fehren = int(input("enter your temp in fehrenheit: "))
        return ((fehren - 32) * (5/9))
    else:
       print("enter either c = celsius or f = fehrenheit")

def main():
    temperature = get_temp()
    converted = temp_conv(temperature)
    print("your converted value is:",converted)
main()
