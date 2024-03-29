from datetime import datetime 

a = '12:30'

s_format = '%H:%M'
dt = datetime.datetime.strptime(a, s_format)

print(type(dt))


        



