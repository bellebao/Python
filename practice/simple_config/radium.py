from ConfigParser import ConfigParser

CONFIGFILE = "python.txt"

config = ConfigParser()
config.read(CONFIGFILE)

print (config.get('messages','greeting'))

radius = float(input(config.get('messages', 'question')+''))

PI = float(config.getfloat('numbers', 'pi') )
area = PI*radius**2
print (config.get('messages', 'result_message'))

print (area )



