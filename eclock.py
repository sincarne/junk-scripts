#!/usr/bin/python
# coding=utf-8
 
import datetime

now = datetime.datetime.now()
hour = now.hour
minutes = now.minute

hourClock = ['🕐','🕑','🕒','🕓','🕔','🕕','🕖','🕗','🕘','🕙','🕚','🕛']
hourAndAHalfClock = ['🕜','🕝','🕞','🕟','🕠','🕡','🕢','🕣','🕤','🕥','🕦','🕧']

if hour > 12:
  hour = hour - 12;

if minutes < 15:
  output = hourClock[hour]
elif minutes < 45:
  output = hourAndAHalfClock[hour]
else:
  output = hourClock[hour + 1]

print output
