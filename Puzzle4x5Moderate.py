'''

Years,Owners,Breed,Dogs
2006,Ginger,bulldog,Shadow
2007,Fernando,irish setter,Riley
2008,Anita,great dane,Princess
2009,Douglas,pekingese,Harley
2010,Barbara,dalmatian,Molly
'''
from logicpuzzles import *
# año, dueño, raza, nombre
dueño1 = (2006, var(), var(), var())
dueño2 = (2007, var(), var(), var())
dueño3 = (2008, var(), var(), var())
dueño4 = (2009, var(), var(), var())
dueño5 = (2010, var(), var(), var())
dueños = (dueño1, dueño2, dueño3, dueño4, dueño5)

def dueñosproblem(dueños):
    return lall(
#1. El bulldog ganó un tiempo antes que el canino de Fernando.
    somewhat_left_of(dueños, (var(), var(), 'bulldog', var()), (var(), 'Fernando', var(), var())),
#2. El canino de Bárbara no es el gran danés.
    
#3. El perro de Anita no ganó en 2009.
    neq((2009,'Anita'),(dueño4[0],dueño4[1])),

#4. El perro que ganó en 2010 es Molly.
    membero((2010, var(), var(), 'Molly'), dueño5),
#5. El canino de Ginger ganó 1 año antes que Riley.
    left_of(dueños, (var(), 'Ginger', var(), var()), (var(), var(),var(), 'Riley')),
#6. Del setter irlandés y el perro que ganó en 2010, uno es Riley y el otro es de Bárbara.
    conde((membero((var(),var(),'setter irlandes','Riley'),dueños),eq((2010,'Barbara',var(),var()),dueño5)),
          (membero((var(),'Bárbara','setter irlandes',var()),dueños),eq((2010,var(),var(),'Riley'),dueño5))),
    neq((2010, 'Barbara', 'setter irlandes', 'Riley'), dueño5),
#7. El canino de Anita es el canino que ganó en 2010 o Princesa.
    lany(eq((2010, 'Anita', var(), var()), dueño5), membero((var(), 'Anita', var(), 'Princesa'), dueños)),
    neq((2010, 'Anita', 'Princesa'), (dueño5[0],dueño5[1], dueño5[3])),

#8. El perro de Fernando ganó antes que Harley.
    somewhat_left_of(dueños, (var(), 'Fernando', var(), var()), (var(), var(), var(), 'Harley')),
#9. Del pequinés y el canino que ganó en 2008, uno es de Anita y el otro es Harley.
    conde((membero((var(), 'Anita', 'pequines', var()),dueños),eq((2008, var(), var(), 'Harley'),dueño3)),
          (membero((var(), var(), 'pequines', 'Harley'),dueños),eq((2008, 'Anita', var(), var()),dueño3))),
    membero((var(),'Douglas',var(),var()),dueños),
    membero((var(),'Barbara',var(),var()),dueños),
    membero((var(),var(),'setter irlandes',var()),dueños),
    membero((var(),var(),'Gran danes',var()),dueños),
    membero((var(),var(),'dalmata',var()),dueños),
    membero((var(),var(),var(),'Shadow'),dueños),
    membero((var(),var(),var(),'Princesa'),dueños),
    )
solutions = run(0, dueños, dueñosproblem(dueños),
                lall(neq(('Barbara','Gran danes'),(d,r)) for _,d,r,_ in dueños),

                )
print(solutions)