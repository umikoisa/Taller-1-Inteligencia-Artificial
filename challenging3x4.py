"""https://logic.puzzlebaron.com/play.php?u2=715ad6e71c4d69817df08fc286e690f0"""
"""
1. The contestant who jumped 86.4 meters scored 7 more points than Robyn.
2. Of Olive and the jumper who jumped 96.3 meters, one scored 82 points and the other scored 103 points.
3. Madeline scored 7 more points than the skier who jumped 86.4 meters.
4. The jumper who jumped 95.0 meters was either Elaine or Robyn.
"""
"""solution
Points  Jumpers     Distances
82      -Olive       102.9 meters-
89      -Robyn       95.0 meters
96      Elaine      -86.4 meters
103     -Madeline    -96.3 meters
"""
import time
from logicpuzzles import *
from logicpuzzles import differents as diff
case1=(82,var(),var())
case2=(89,var(),var())
case3=(96,var(),var())
case4=(103,var(),var())
cases=(case1,case2,case3,case4)
def problemsolver(cases):
    return lall(
        #1. The contestant who jumped 86.4 meters scored 7 more points than Robyn.
        right_of(cases,(var(),var(),86.4),(var(),"Robyn",var()),1),
        #2. Of Olive and the jumper who jumped 96.3 meters, one scored 82 points and the other scored 103 points.
        conde((eq((82,"Olive",var()),case1),eq((103,var(),96.3),case4)),(eq((82,var(),96.3),case1),eq((103,"Olive",var()),case4))),
        #3. Madeline scored 7 more points than the skier who jumped 86.4 meters.
        right_of(cases,(var(),"Madeline",var()),(var(),var(),86.4),1),
        #4. The jumper who jumped 95.0 meters was either Elaine or Robyn.
        lany(membero((var(),"Elaine",95.0),cases),membero((var(),"Robyn",95.0),cases)),
        #dominio sin inicializar
        membero((var(),var(),102.9),cases),
        membero((var(),"Elaine",var()),cases)
    )
seg_init=time.time()
solution=run(0,cases,problemsolver(cases))
print(solution)
print(time.time()-seg_init)
