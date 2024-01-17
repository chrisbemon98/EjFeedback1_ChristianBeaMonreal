# EjFeedback1_ChristianBeaMonreal
Entrega del ejercicio de feedback 1 de la asignatura 'Algoritmos y Estructuras de Datos'.

https://github.com/chrisbemon98/EjFeedback1_ChristianBeaMonreal

En la clase Paciente se ha optado por ponerle un atributo Identificador en lugar de Nombre, ya que es mucho más sencillo de generarlo.

Se han implementado montículos basados en herencia, utilizando el MaxHeap para gestionar el nivel de urgencia y el MinHeap para las horas de espera (aplicando como criterio 12-horas_espera, para que sea posible aplicar un MinHeap teniendo que mantener en nodos superiores los que más tiempo lleven esperando).

La clase SalaEmergencias hace uso del MaxHeap y el MinHeap que se encuentran en el archivo Heap.py, que es la versión utilizada durante las clases. Por otro lado, desde SalaEmergencias se puede hacer uso del MaxHeap y MinHeap que se encuentran en el archivo Heap2.py, que es una versión realizada por mi modificando ligeramente la versión original.

Esta modificación se realiza debido a que, a pesar de que lo llego a entender, lo que más me cuesta de captar es la función de comparación. Por ello, modifico ligeramente la forma de usar las partes en las que se utiliza. Se puede comprobar que funciona correctamente, y procedo a explicar los cambios:
*   Se crea el método _above_index, que recibe como parámetros dos índices. En este método se utiliza la función de comparación para determina el índice que contiene el elemento que debería ir en una posición superior del montículo. Es decir, cuando self.compare devuelve True, quiere decir que el elemento del segundo parámetro debería estar por encima del del primer parámetro en el montículo.
*   Utilizando este método se pueden gestionar las condiciones más fácilmente (al menos a mi parecer), tal como se puede comprobar en el código.

Por otra parte, en Heap2.py se han creado dos métodos que no se encuentran en la versión original. Estos métodos simplemente factorizan partes del código que se usan (o podrían ser usadas) más de una vez. Los métodos son las siguientes (ver el código para comprobar su funcionamiento):
*   _exchange_positions
*   _readjust

En cuanto al programa principal (main.py), existen una serie de constantes al inicio del código que permiten la gestión del número de pacientes, así como la forma en la que se mostrarán los resultados. Es fácil comprobar el funcionamiento del programa modificando los distintos parámetros.