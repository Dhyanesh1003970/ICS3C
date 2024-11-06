def wc(TdegC, windKPH):
  wTemp=0
  
  wTemp = 13.12+0.6215*TdegC
  wTemp = wTemp - 11.37*windKPH**0.16
  wTemp = wTemp+0.3965*TdegC*windKPH**0.16
  
  if(0 >= wTemp> -10 ):
    print('Low risk')
  elif(-10>=wTemp>-28):
    print('Moderate risk of hypothermia')
  elif(-28>=wTemp>-40):
    print('High risk of frostbite')
  elif(-40>=wTemp>-48):
    print('Severe risk of frostbite: exposed skin freezes in 5-10 minutes')
  elif(-48>=wTemp>-55):
    print('Severe risk of frostbite: exposed skin freezes in 2-5 minutes')
  else:
    print('Extreme risk: exposed skin freezes in under 2 minutes')
  
  return wTemp
  
  
T = -5.0
W = 10.0


print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
print()

T = -20.0
W = 20.0



print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))
print()

T = -45.0
W = 40.0

print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc(T, W), T, W))

print()
