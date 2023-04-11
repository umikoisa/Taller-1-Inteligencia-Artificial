from logicpuzzles import *
#1.Charlie es la persona que trabajará con Nelson o la persona que trabajará con Rafael.
#2. La persona que trabajará con Nelson empezará 1 hora después que la persona que trabajará con Rafael.
#3. Darren trabajará con Margarita.
#4. Harold empezará 1 hora antes que el intérprete que trabajará con Tyler.
#5. Harold empezará a trabajar a las 10:00.

actividad1=(9,var(),var())
actividad2=(10,var(),var())
actividad3=(11,var(),var())
actividad4=(12,var(),var())
actividades=(actividad1,actividad2,actividad3,actividad4)

def solveractividad(actividades):
    return lall(
        lany(membero((var(),'Charlie','Nelson'), actividades),membero((var(),'Charlie','Rafael'), actividades)),
        right_of(actividades, (var(),var(),'Nelson'),(var(),var(),'Rafael')),
        membero((var(),'Darren','margarita'), actividades),
        left_of(actividades,  (var(),'Harold',var()), (var(),var(),'Tyler')),
        membero((10, 'Harold',var()),actividades),
        membero((var(),'Brent',var()),actividades)
        
        )
solucion=run(0,actividades,solveractividad(actividades))
print(solucion)