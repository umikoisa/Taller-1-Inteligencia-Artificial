'''
Backstory and Goal
Bernice is a ticketing agent for Global Airways, and she has several customers waiting for her to book their international flights. 
Match each traveler to his or her departure and arrival counties and determine what time their flight is scheduled to depart.

1. The traveler leaving at 5:30 pm is either the person going to Ireland or Florence.
2. Bridget is leaving 3 hours earlier than the person flying from Malta.
3. The traveler flying from Zambia is leaving 3 hours later than Florence.
4. The traveler leaving at 3:30 pm is either Inez or the traveler going to Finland.
5. Bridget isn't going to Guinea.
6. Of the person leaving at 4:30 pm and the traveler flying from Ukraine, one is going to Angola and the other is Claude.
7. The person going to Denmark is leaving earlier than Claude.
8. The person going to Denmark isn't flying from Romania.
9. The traveler going to Denmark is either the person flying from Zambia or the traveler leaving at 2:30 pm.
10. The traveler flying from South Africa is leaving earlier than Inez.
11. The traveler going to Angola is either the traveler flying from South Africa or the person leaving at 2:30 pm.
12. Of the person going to Ireland and the traveler flying from Taiwan, one is Katherine and the other is leaving at 3:30 pm.

estructura :(Times, Travelers, Departures, Arrivals)
solucion:
((2:30 pm, Bridget, Romania, Barbados),
(3:30 pm, Florence, Taiwan, Finland),
(4:30 pm, Gabriel, South Africa, Angola),
(5:30 pm, Katherine, Malta, Ireland),
(6:30 pm, Inez, Zambia, Denmark),
(7:30 pm, Claude, Ukraine, Guinea))

'''
from logicpuzzles import *
import time


viaje1=(230 , var(), var(), var())
viaje2=(330 , var(), var(), var())
viaje3=(430 , var(), var(), var())
viaje4=(530 , var(), var(), var())
viaje5=(630 , var(), var(), var())
viaje6=(730 , var(), var(), var())
viajes=(viaje1,viaje2,viaje3,viaje4,viaje5,viaje6)

def viajesolu(viajes):
    return lall(
    #1. The traveler leaving at 5:30 pm is either the person going to Ireland or Florence.
    lany(eq((530,var(),var(),'Ireland'),viaje4),eq((530,'Florence',var(),var()),viaje4)),
    #2. Bridget is leaving 3 hours earlier than the person flying from Malta.
    left_of(viajes,(var(),'Bridget',var(),var()),(var(),var(),'Malta',var()),3),
    #3. The traveler flying from Zambia is leaving 3 hours later than Florence.
    right_of(viajes,(var(),var(),'Zambia',var()),(var(),'Florence',var(),var()),3),
    #4. The traveler leaving at 3:30 pm is either Inez or the traveler going to Finland.
    lany(eq((330,'Inez',var(),var()),viaje2),eq((330,var(),var(),'Finland'),viaje2)),
    #5. Bridget isn't going to Guinea.

    #6. Of the person leaving at 4:30 pm and the traveler flying from Ukraine, one is going to Angola and the other is Claude.
    conde((eq((430,var(),var(),'Angola'),viaje3),membero((var(),'Claude','Ukraine',var()),viajes)),
          (eq((430,'Claude',var(),var()),viaje3),membero((var(),var(),'Ukraine','Angola'),viajes))),
    neq((430,'Claude','Ukraine','Angola'),viaje3),
    #7. The person going to Denmark is leaving earlier than Claude.
    somewhat_left_of(viajes,(var(),var(),var(),'Denmark'),(var(),'Claude',var(),var())),
    #8. The person going to Denmark isn't flying from Romania.

    #9. The traveler going to Denmark is either the person flying from Zambia or the traveler leaving at 2:30 pm.
    lany(membero((var(),var(),'Zambia','Denmark'),viajes),eq((230,var(),var(),'Denmark'),viaje1)),
    #10. The traveler flying from South Africa is leaving earlier than Inez.
    somewhat_left_of(viajes,(var(),var(),'South Africa',var()),(var(),'Inez',var(),var())),
    #11. The traveler going to Angola is either the traveler flying from South Africa or the person leaving at 2:30 pm.
    lany(membero((var(),var(),'South Africa','Angola'),viajes),eq((230,var(),var(),'Angola'),viaje1)),
    #12. Of the person going to Ireland and the traveler flying from Taiwan, one is Katherine and the other is leaving at 3:30 pm.
    conde((membero((var(),'Katherine',var(),'Ireland'),viajes),eq((330,var(),'Taiwan',var()),viaje2)),
          (eq((330,var(),var(),'Ireland'),viaje2),membero((var(),'Katherine','Taiwan',var()),viajes))),
    neq((330,'Katherine','Taiwan','Ireland'),viaje2),
    #datos no mencionados
    membero((var(),'Gabriel',var(),var()),viajes),
    membero((var(),var(),'Romania',var()),viajes),
    membero((var(),var(),var(),'Barbados'),viajes),
    membero((var(),var(),var(),'Guinea'),viajes)


    )
segundos=time.time()
local_time=(time.ctime(segundos))
solucion=run(0,viajes,viajesolu(viajes),
             lall(neq(('Bridget','Guinea'),(n,a)) for _,n,_,a in viajes),
             lall(neq(('Romania','Denmark'),(d,a)) for _,_,d,a in viajes)
             )
print(solucion)
print(local_time)
print(time.time()-segundos)