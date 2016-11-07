#!/usr/bin/python
# Jan Horbowicz
from math import floor
import matplotlib.pyplot as plt
file1=open('data09-2016.csv','r')
datetime,temperature=[],[]
line=file1.readline()
line=file1.readline()
#
# creating lists datetime[] and temperature[]
#
while len(line)!=0:
    line=file1.readline()
    if len(line)== 0:
        break
    data=int(line[8]+line[9]+line[3]+line[4]+line[0]+line[1])
    hrs,mnt,sec=float(line[11]+line[12]),float(line[14]+line[15]),float(line[17]+line[18])
    time = (hrs+mnt/60.+sec/3600.)/24
    datetime.append(data+time)		#datetime format YYMMDD.<part of day - 1 is whole day>
    if line[27]=='.':
        temp=float(line[26]+line[27]+line[28])
    else:
        temp=float(line[26]+line[27]+line[28]+line[29])
    temperature.append(temp)
file1.close()
#
# finding highest temperature
#
maxtemp,i=temperature[1],1
while i != len(temperature):
    if temperature[i] > maxtemp:
        maxtemp,max_i=temperature[i],i
    i+=1
print max_i, maxtemp, datetime[max_i]
#
# datetime conversion to more readable format
#
day_time=(datetime[max_i]-floor(datetime[max_i]))*24.
hrs=int(floor(day_time))
m1=(day_time-floor(day_time))*60.
mnt=int(floor(m1))
sec=int((m1-mnt)*60.) # we lost last second becasue of int()
year=int(floor(floor(datetime[max_i])/10000))
month=int(floor((floor(datetime[max_i])-10000*year)/100))
day=int(floor(datetime[max_i])-(10000*year+100*month))
print 'Maximum temperature was ', maxtemp,'Celcius degree, and it was on', day,'\b.',month,'\b.',year+2000, ' at time: ', hrs, ':', mnt, ':', sec
#
# creating a plot
#
plt.scatter(datetime,temperature)
plt.title('September Temperatures')
plt.xlabel('datetime')
plt.ylabel('temperature')
plt.show()
