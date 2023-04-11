'''pistas
1. Gordon's team will include Gwendolyn.
2. Gordon's expedition will leave 2 months before Jacob's team.
3. Jacob's expedition won't include Brittany.
4. Of Brittany's expedition and the expedition going to Angola, one will include Horace and the other will leave in March.
5. The expedition going to Grenada will leave 1 month after the expedition going to Turkmenistan.
6. Horace's expedition will leave sometime after Bob's expedition.
7. Connie's expedition will leave 1 month after the expedition going to Turkmenistan.
'''
'''solucion
January     -Gordon  -Gwendolyn   -Turkmenistan
February    -Bob     -Connie      -Grenada
March       -Jacob   Velma       -Angola
April       -Horace  -Brittany    Chile
'''
import time
from logicpuzzles import *
from logicpuzzles import differents as diff
case1=("january",var(),var(),var())
case2=("february",var(),var(),var())
case3=("march",var(),var(),var())
case4=("april",var(),var(),var())
cases=(case1,case2,case3,case4)
def problemsolver(cases):
    return lall(
        #Months 	Chiroptologists 	Speleologists 	Countries
        #1. Gordon's team will include Gwendolyn.
        membero((var(),"Gordon","Gwendolyn",var()),cases),
        #2. Gordon's expedition will leave 2 months before Jacob's team.
        left_of(cases,(var(),"Gordon",var(),var()),(var(),"Jacob",var(),var()),2),
        #4. Of Brittany's expedition and the expedition going to Angola, one will include Horace and the other will leave in March.
        conde(((membero((var(),"Horace","Brittany",var()),cases)),(eq(("march",var(),var(),"Angola"),case3))),((membero((var(),"Horace",var(),"Angola"),cases)),(eq(("march",var(),"Brittany",var()),case3)))),
        #5. The expedition going to Grenada will leave 1 month after the expedition going to Turkmenistan.
        right_of(cases,(var(),var(),var(),"Grenada"),(var(),var(),var(),"Turkmenistan"),1),
        #6. Horace's expedition will leave sometime after Bob's expedition.
        somewhat_right_of(cases,(var(),"Horace",var(),var()),(var(),"Bob",var(),var())),
        #7. Connie's expedition will leave 1 month after the expedition going to Turkmenistan.
        right_of(cases,(var(),var(),"Connie",var()),(var(),var(),var(),"Turkmenistan"),1),
        #dominio no iniciado
        membero((var(),var(),"Brittany",var()),cases),
        membero((var(),"Horace",var(),var()),cases),
        #dominio sin mencion
        membero((var(),var(),"Velma",var()),cases),
        membero((var(),var(),var(),"Chile"),cases)

    )
seg_init=time.time()
solutions=run(0,cases,problemsolver(cases),
              #3. Jacob's expedition won't include Brittany.
              nmembero(cases,("Jacob","Brittany"),(1,2)),
              )
print(solutions)
print(time.time()-seg_init)
