"""
1. The architect, the football player, and Francisco are three different people.
2. The golf player received fewer votes than the musician.
3. Of Jorge and the soccer player, one is the garbage man and the other received 25 votes.
4. The person who got 11 votes isn't the waiter.
5. Colin, the contestant who got 18 votes and Francisco are all different people.
6. The hockey player received 7 votes fewer votes than Pablo.
7. Of Pablo and the contestant who got 39 votes, one is the garbage man and the other played football.
8. The dentist received 7 votes fewer votes than Colin.
9. The person who got 39 votes, Jorge, and Francisco are three different people.
10. Zachary received 21 votes more votes than the musician.
11. The person who got 11 votes played lacrosse.
12. Colin isn't the architect.
13. The contestant who got 39 votes never played soccer.
votes= 4, 11, 18, 25, 32, 39.
"""
import time
from logicpuzzles import *
from logicpuzzles import differents as diff
#vote,contestant,sport,occupations
case1=(4,var(),var(),var())
case2=(11,var(),var(),var())
case3=(18,var(),var(),var())
case4=(25,var(),var(),var())
case5=(32,var(),var(),var())
case6=(39,var(),var(),var())
cases=(case1,case2,case3,case4,case5,case6)
def solvingproblem(cases):
    return lall(

        #1.The architect, the football player, and Francisco are three different people.
            #neq((membero((var(),var(),var(),"architect"),cases), membero((var(),var(),"football",var()),cases),membero((var(),"francisco",var(),var()),cases)),cases),
        #2. The golf player received fewer votes than the musician.
        somewhat_left_of(cases,(var(),var(),"golf",var()),(var(),var(),var(),"musician")),
        #3. Of Jorge and the soccer player, one is the garbage man and the other received 25 votes.
        conde((eq((25, var(), "soccer", var()), case4), membero((var(), 'jorge', var(),'garbage man'), cases)),(eq((25, 'jorge', var(), var()), case4), membero((var(), var(), 'soccer', 'garbage man'), cases))),
        neq((25, 'jorge','soccer', 'garbage man'), case4),
        #4. The person who got 11 votes isn't the waiter.
            #lall(neq((11,"waiter"),(n,s)) for n ,_,_,s in cases),
        #5. Colin, the contestant who got 18 votes and Francisco are all different people.
#este creo que no lo toma
            #lall(neq((18,"francisco"),(n,s)) for n ,s,_,_ in cases),
            #lall(neq((18,"colin"),(n,s)) for n ,s,_,_ in cases),
        #6. The hockey player received 7 votes fewer votes than Pablo.
        left_of(cases,(var(),var(),"hockey",var()),(var(),"pablo",var(),var()),1),
        #7. Of Pablo and the contestant who got 39 votes, one is the garbage man and the other played football.
        conde((membero((var(),"pablo","football",var()),cases),eq((39,var(),var(),"garbage man"),case6)),(membero((var(),"pablo",var(),"garbage man"),cases),eq((39,var(),"football",var()),case6))),
        #8. The dentist received 7 votes fewer votes than Colin.
        left_of(cases,(var(),var(),var(),"dentist"),(var(),"colin",var(),var()),1),
        #9. The person who got 39 votes, Jorge, and Francisco are three different people.
            #lall(neq((39,"francisco"),(n,s)) for n ,s,_,_ in cases),
            #lall(neq((39,"jorge"),(n,s)) for n ,s,_,_ in cases),
        #10. Zachary received 21 votes more votes than the musician.
        right_of(cases,(var(),"zachary",var(),var()),(var(),var(),var(),"musician"),3),
        #11. The person who got 11 votes played lacrosse.
        eq((11,var(),"lacrosse",var()),case2),
        #12. Colin isn't the architect.
            #lall(neq(("colin","architect"),(n,s)) for  _,n,_,s in cases),
        #13. The contestant who got 39 votes never played soccer.
            #lall(neq((39,"soccer"),(n,s)) for  n,_,s,_ in cases)
        #valores en dominio no mencionados
        membero((var(),"nathaniel",var(),var()),cases),
        membero((var(),var(),"baseball",var()),cases),
        membero((var(),var(),var(),"lawyer"),cases),
        membero((var(),var(),var(),"waiter"),cases),
        membero((var(),var(),var(),"architect"),cases),
        membero((var(),"francisco",var(),var()),cases)
    )
sec_start=time.time()
solutions = run(0, cases, solvingproblem(cases),
                #1.The architect, the football player, and Francisco are three different people.
                diff(cases,((var(),),("francisco",),("football",),("architect",))),
                #4. The person who got 11 votes isn't the waiter.
                diff(cases,((11,),(var(),),(var(),),("waiter",))),
                #5. Colin, the contestant who got 18 votes and Francisco are all different people.
                diff(cases,((18,),("colin","francisco"),(var(),),(var(),))),
                #9. The person who got 39 votes, Jorge, and Francisco are three different people.
                diff(cases,((39,),("jorge","francisco"),(var(),),(var(),))),
                #12. Colin isn't the architect.
                diff(cases,((var(),),("colin",),(var(),),("architect",))),
                #13. The contestant who got 39 votes never played soccer.
                diff(cases,((39,),(var(),),("soccer",),(var(),)))
                )
print(solutions)
print(time.time()-sec_start)
"""
tenia demasiadas pistas que hablaban sobre que miembros eran diferentes
"""
