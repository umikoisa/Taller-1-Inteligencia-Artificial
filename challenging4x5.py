'''
1. The report of the cigar-shaped UFO was submitted 2 days before the report of the horseshoe-shaped UFO.
2. Dan Delgado's report was either the report from Zearing or the sighting of the diamond-shaped UFO.
3. Of the report from Jackson and Cindy Chan's sighting, one involved the horseshoe-shaped UFO and the other was received on August 5.
4. The sighting of the diamond-shaped UFO wasn't from Newark.
5. Gil Gates's report wasn't from Zearing.
6. The sighting of the teardrop-shaped UFO wasn't from Zearing.
7. The sighting of the cigar-shaped UFO was submitted 1 day after the sighting from Zearing.
8. The sighting of the cigar-shaped UFO was from Visalia.
9. The report from Jackson was submitted sometime before Dan Delgado's sighting.
10. Flora Flynn's sighting was received on August 7.
'''
'''
dominios
dates
    August 4
    -August 5
    August 6
    August 7
    August 8
witnesses
    iva ingram*
    -cindy chan
    -gil gates
    -flora flynn
    -dan delgado
towns
    -zearing
    -visalia
    -newark
    -jackson
    yarnmout*
shapes
    egg*
    -cigar
    -teardrop
    -horseshoe
    -diamond
    -nombrados*sinNombrar
'''
import time
from logicpuzzles import *
from logicpuzzles import differents as diff
#dates,witnesses,towns,shaped
case1=(4,var(),var(),var())
case2=(5,var(),var(),var())
case3=(6,var(),var(),var())
case4=(7,var(),var(),var())
case5=(8,var(),var(),var())
cases=(case1,case2,case3,case4,case5)
def problemsolver(cases):
    return lall(
        #1. The report of the cigar-shaped UFO was submitted 2 days before the report of the horseshoe-shaped UFO.
        left_of(cases,(var(),var(),var(),"cigar"),(var(),var(),var(),"horseshoe"),2),
        #2. Dan Delgado's report was either the report from Zearing or the sighting of the diamond-shaped UFO.
        lany(membero((var(),"dan delgado","zearing" ,var()), cases), membero((var(),"dan delgado", var(),"diamond"), cases)),
        #3. Of the report from Jackson and Cindy Chan's sighting, one involved the horseshoe-shaped UFO and the other was received on August 5.
        conde((membero((var(),var(),"jackson","horseshoe"),cases),eq((5,"cindy chan",var(),var()),case2)),(membero((var(),"cindy",var(),"horseshoe"),cases),eq((5,var(),"jackson",var()),case2))),
        #7. The sighting of the cigar-shaped UFO was submitted 1 day after the sighting from Zearing.
        right_of(cases,(var(),var(),var(),"cigar"),(var(),var(),"zearing",var()),1),
        #8. The sighting of the cigar-shaped UFO was from Visalia.
        membero((var(),var(),"visalia","cigar"),cases),
        #9. The report from Jackson was submitted sometime before Dan Delgado's sighting.
        somewhat_left_of(cases,(var(),var(),"jackson",var()),(var(),"dan delgado",var(),var())),
        #10. Flora Flynn's sighting was received on August 7.
        eq((7,"flora flynn",var(),var()),case4),
        #dominios que nesecitan ser integrados aparte
        membero((var(),"gil gates",var(),var()),cases),
        membero((var(),var(),"newark",var()),cases),
        membero((var(),var(),var(),"teardrop"),cases),
        membero((var(),var(),var(),"diamond"),cases),
        #dominio no mencionado
        membero((var(),var(),var(),"egg"),cases),
        membero((var(),var(),"yarnmout",var()),cases),
        membero((var(),"iva ingram",var(),var()),cases)


    )
seg_ini=time.time()
solutions=run(1,cases,problemsolver(cases),
        nmembero(cases, ("zearing", "diamond"), (2,3)),
        #4. The sighting of the diamond-shaped UFO wasn't from Newark.
        nmembero(cases, ("newark", "diamond"), (2,3)),
        #5. Gil Gates's report wasn't from Zearing.
        nmembero(cases,("gil gates","zearing"),(1,2)),
        #6. The sighting of the teardrop-shaped UFO wasn't from Zearing.
        nmembero(cases,("zearing","teardrop"),(2,3))
        )
print (solutions)
print (time.time()-seg_ini)
