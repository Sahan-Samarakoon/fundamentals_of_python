import sys
def moon_weight():
    print('Please enter your current Earth weight')
    earth_weight = int(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year') 
    increment = int(sys.stdin.readline())
    print('Please enter the number of years')
    years = int(sys.stdin.readline())
    for i in range(1, years + 1):
        moon = earth_weight * 0.165
        earth_weight = earth_weight + increment
        print("Year %s:%s" % (i, moon))

moon_weight()


















