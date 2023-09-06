# Leap Year

def isLeapYear(Year):
  if(Year%4==0 and Year%100!=0)or Year%400==0:
     return True
  else:
    return False
Year=int(input ("Enter a Year :"))
if isLeapYear(Year):
  print('{} is a Leap Year.'.format(Year))
else:
  print('{} is not a Leap Year.'.format(Year))