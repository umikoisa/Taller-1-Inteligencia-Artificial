#https://logic.puzzlebaron.com/play.php?u2=b84dbc8582792eaa91cf335784e7d047
'''
1. The student who gave the presentation on President Truman spoke for a somewhat longer time than the student who gave the presentation on President Nixon.
2. Muriel spoke 6 minutes less than the student who got the A-.
3. Of the student who got the D and the student who got the B+, one spoke for 5 minutes and the other talked about President Monroe.
4. The student who gave the presentation on President Lincoln spoke 3 minutes more than the student who got the C-.
5. Inez spoke 6 minutes more than the presenter who gave the presentation on President Lincoln.
6. The seven students were the student who spoke for 17 minutes, the student who gave the presentation on President Garfield, the student who gave the presentation on President Coolidge, the presenter who gave the presentation on President Nixon, the presenter who gave the presentation on President Lincoln, Zachary and Yvonne.
7. The student who gave the presentation on President Nixon spoke 3 minutes more than Zachary.
8. The presenter who got the B- spoke 6 minutes more than the student who got the A.
9. Vicki was either the student who gave the presentation on President Garfield or the student who gave the presentation on President Lincoln.
10. Of the student who got the D and the presenter who spoke for 23 minutes, one was Peggy and the other talked about President Garfield.
11. The presenter who got the D was either the presenter who spoke for 14 minutes or the presenter who gave the presentation on President Monroe.
'''
'''
Lengths     Names   Presidents  Grades
5 minutes   -Zachary Jackson     -B+
8 minutes   Chris   -Nixon       -A
11 minutes  +Yvonne  -Truman      -C-
14 minutes  -Muriel  -Lincoln     -B-
17 minutes  -Peggy   -Monroe      -D
20 minutes  -Inez    +Coolidge    -A-
23 minutes  -Vicki   -Garfield    C+
'''
import time
from logicpuzzles import *
from logicpuzzles import differents as diff
case1=(5,var(),var(),var())
case2=(8,var(),var(),var())
case3=(11,var(),var(),var())
case4=(14,var(),var(),var())
case5=(17,var(),var(),var())
case6=(20,var(),var(),var())
case7=(23,var(),var(),var())
cases=(case1,case2,case3,case4,case5,case6,case7)
def problemsolver(cases):
    return lall(
        #1. The student who gave the presentation on President Truman spoke for a somewhat longer time than the student who gave the presentation on President Nixon.
        somewhat_right_of(cases,(var(),var(),"Truman",var()),(var(),var(),"Nixon",var())),
        #2. Muriel spoke 6 minutes less than the student who got the A-.
        left_of(cases,(var(),"Muriel",var(),var()),(var(),var(),var(),"A-"),2),
        #3. Of the student who got the D and the student who got the B+, one spoke for 5 minutes and the other talked about President Monroe.
        conde((eq((5,var(),var(),"D"),case1),membero((var(),var(),"Monroe","B+"),cases)),(eq((5,var(),var(),"B+"),case1),membero((var(),var(),"Monroe","D"),cases))),
        #4. The student who gave the presentation on President Lincoln spoke 3 minutes more than the student who got the C-.
        right_of(cases,(var(),var(),"Lincoln",var()),(var(),var(),var(),"C-"),1),
        #5. Inez spoke 6 minutes more than the presenter who gave the presentation on President Lincoln.
        right_of(cases,(var(),"Inez",var(),var()),(var(),var(),"Lincoln",var()),2),
        #7. The student who gave the presentation on President Nixon spoke 3 minutes more than Zachary.
        right_of(cases,(var(),var(),"Nixon",var()),(var(),"Zachary",var(),var()),1),
        #8. The presenter who got the B- spoke 6 minutes more than the student who got the A.
        right_of(cases,(var(),var(),var(),"B-"),(var(),var(),var(),"A"),2),
        #9. Vicki was either the student who gave the presentation on President Garfield or the student who gave the presentation on President Lincoln.
        lany(membero((var(),"Vicki","Garfield",var()),cases),membero((var(),"Vicki","Lincoln",var()),cases)),
        #10. Of the student who got the D and the presenter who spoke for 23 minutes, one was Peggy and the other talked about President Garfield.
        conde((membero((var(),"Peggy",var(),"D"),cases),eq((23,var(),"Garfield",var()),case7)),(membero((var(),var(),"Garfield","D"),cases),eq((23,"Peggy",var(),var()),case7))),
        #11. The presenter who got the D was either the presenter who spoke for 14 minutes or the presenter who gave the presentation on President Monroe.
        lany(eq((14,var(),var(),"D"),case4),membero((var(),var(),"Monroe","D"),cases)),
        #dominio sin inicializar
        membero((var(),"Chris",var(),var()),cases),
        membero((var(),"Yvonne",var(),var()),cases),
        membero((var(),var(),"Jackson",var()),cases),
        membero((var(),var(),"Coolidge",var()),cases),
        membero((var(),var(),var(),"C+"),cases)
    )
seg_init=time.time()
solution=run(0,cases,problemsolver(cases),
             #6. The seven students were the student who spoke for 17 minutes, the student who gave the presentation on President Garfield, the student who gave the presentation on President Coolidge, the presenter who gave the presentation on President Nixon, the presenter who gave the presentation on President Lincoln, Zachary and Yvonne.
             diff(cases,((17,),("Zachary","Yvonne"),("Garfield","Coolidge","Nixon","Lincoln"),(var(),)))
        )
print(solution)
print(time.time()-seg_init)
"""
un aspecto interesante es la cantidad de tiempo que se demora el ejecutar este algoritmo
algo curioso es que si modificamos el codigo para que entregue una sola respuesta el tiempo de ejecucion se reduce drasticamente
la mayoria de las pistas hacian referencias poscionales(right_of,left_of,etc)
a pesar de ser un puzle "dificil" la complejidad de programar cada pista no era especialmente elevada

"""
