'''clues
1. Of the athlete who started from Encinitas and Geneva, one finished in 184 days and the other finished in 195 days.
2. The rower who traveled for 228 days started from Pismo Beach.
3. The athlete who traveled for 217 days didn't start out from Arcata.
4. Tracy, the rower who started from Ventura, the competitor who started from Avalon and the rower who traveled for 195 days were all different rowers.
5. Antonio started from Arcata.
6. Joey was either the rower who started from Ventura or the athlete who traveled for 184 days.
'''
'''solucion
Durations   Rowers      Start Points
184 days    -Geneva      Avalon
195 days    Nina        -Encinitas
206 days    -Antonio     Arcata
217 days    -Joey        Ventura
228 days    -Tracy       -Pismo Beach
'''
import time
from logicpuzzles import *
from logicpuzzles import differents as diff
case1=(184,var(),var())
case2=(195,var(),var())
case3=(206,var(),var())
case4=(217,var(),var())
case5=(228,var(),var())
cases=(case1,case2,case3,case4,case5)
def problemsolver(cases):
    return lall(
        #1. Of the athlete who started from Encinitas and Geneva, one finished in 184 days and the other finished in 195 days.
        conde((eq((184,"Geneva",var()),case1),(eq((195,var(),"Encinitas"),case2))),(eq((184,var(),"Encinitas"),case1),(eq((195,"Geneva",var()),case2)))),
        #2. The rower who traveled for 228 days started from Pismo Beach.
        eq((228,var(),"Pismo Beach"),case5),
        #3. The athlete who traveled for 217 days didn't start out from Arcata.
        neq((217,var(),"Arcata"),case4),
        #5. Antonio started from Arcata.
        membero((var(),"Antonio","Arcata"),cases),
        #6. Joey was either the rower who started from Ventura or the athlete who traveled for 184 days.
        lany(membero((var(),"Joey","Ventura"),cases),eq((184,"Joey",var()),case1)),

        membero((var(),"Tracy",var()),cases),
        membero((var(),var(),"Avalon"),cases),
        membero((var(),var(),"Ventura"),cases),
        membero((var(),"Nina",var()),cases)
    )
seg_init=time.time()
solution=run(0,cases,problemsolver(cases),
        #4. Tracy, the rower who started from Ventura, the competitor who started from Avalon and the rower who traveled for 195 days were all different rowers.
        diff(cases,((195,),("Tracy",),("Ventura","Avalon"))),
)
print(solution)
print(time.time()-seg_init)
