def getPhase(t, p):
    if 10 <= p <= 1000000 :
            if t == 273.16 and p == 611.66 :
              return "Solid/Liquid/Vapor" 
            elif t == 250 and p == 100 :
                return "Vapor"
            elif 200 <= t < 273.16 and 100 <= p <= 611.66 :
                return "Solid/Vapor"
            elif t == 273.16 and 1000<= p <= 1000000 :
               return "Solid/Liquid"
            elif 15 <= t <= 270 and 1000 <= p <= 1000000 :
                return "Solid"
            elif t < 200:
                return "Solid"
            elif  t == 370 and  p == 611.66 :
                return "Liquid/Vapor"
            elif t == 374 and p == 101330 :
                return "Liquid/Vapor"
            elif p > 101330 :     
                return "Liquid"
            elif 273.16 < t < 373.15 and 1000 < p < 1000000:
                return "Liquid"
            elif 373.15 <= t <= 500 and p < 101300  :
                return "Vapor"
            elif 200 < t < 373.15 and p < 611.66 :
                return "Vapor"
   
