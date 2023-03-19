"""
    Tarea-1
    Autor: Óscar Antonio Hinojosa Salum A00821930
    Febrero 20 2023
    Documentación de librerías o métodos STACK (lifo), QUEUE (fifo), TABLE/HASH/DICTIONARY (order)
    Resumen de repaso o calentamiento del lenguaje.
"""

# STACK or DEQUE (LIFO: Last-In-First-Out)
'''
    Referencia (G4G): https://www.geeksforgeeks.org/stack-in-python/

    El Stack o Deque es una manera de organizar y manipular el orden de datos o elementos.
    Es el que posiblemente consideran de forma aformal o en ojos de un cliente, "el injusto",
    porque es una fila o lista donde el último elemento que llegó, es el primero en ser atendido.

    Las operaciones principales del stack o pila son:
        - empty() : Regresa True si la pila está vacía, False si no – Complejidad de Tiempo: O(1)
        - size() : Regresa el tamaño de la pila – Complejidad de Tiempo: O(1)
        - top() / peek() : Regresa la referencia al elemento en la cima de la pila – Complejidad de Tiempo: O(1)
        - push(a) / append(a) : Inserta el elemento "a" en la cima de la pila – Complejidad de Tiempo: O(1)
        - pop() : Borra el elemento en la cima de la pila – Complejidad de Tiempo: O(1)

    Existen tres maneras (librerías) de utilizar el Stack en Python:
        - La clase lista predeterminada en el lenguaje
        - Collections.deque
        - queue.LifoQueue


    -- Ejemplo de Implementación con Collections.deque, el más recomendado, no tan complejo, no tan simple:
    
    from collections import deque
    
    stack = deque()
    
    # append() : función para insertar elementos en la cima de la pila
    stack.append('a')
    stack.append('b')
    stack.append('c')
    
    print('Initial stack:')
    print(stack)
    
    # pop() : función para quitar el elemento en la cima de la pila, en orden Last-In, First-Out
    print('\nElements popped from stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    
    print('\nStack after elements are popped:')
    print(stack)
    
    # Hacer "print(stack.pop())" regresaría IndexError, porque la pila estaría vacía
'''
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #



# QUEUE (FIFO: First-In, First-Out)
'''
    Referencia (G4G): https://www.geeksforgeeks.org/queue-in-python/

    El Queue es otra forma de manipular los datos o elementos, el opuesto al Deque.
    Primer elemento que llegue, es el primero que se atiende.

    Las operaciones principales del Queue son:
        - Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
        - Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
        - Front: Get the front item from queue – Time Complexity : O(1)
        - Rear: Get the last item from queue – Time Complexity : O(1)

    Existen tres maneras (librerías) de utilizar el Queue en Python:
        - La clase lista predeterminada en el lenguaje
        - collections.deque
        - queue.Queue


    -- Ejemplo de Implementación con Collections.deque, el más recomendado, no tan complejo, no tan simple:

    from collections import deque

    q = deque()
    
    # append() : función para insertar elementos en la cima de la pila
    q.append('a')
    q.append('b')
    q.append('c')
    
    print("Initial queue")
    print(q)
    
    # popleft() : función para quitar el elemento en la cima de la pila, en orden First-In, First-Out
    # creo le añadieron "left" para diferencialo y visualizarlo mejor, como una pila horizontal o fila de elementos...
    print("\nElements dequeued from the queue")
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    
    print("\nQueue after removing elements")
    print(q)
    
    # Hacer "q.popleft()" regresaría IndexError, porque el Queue estaría vacío
'''
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = #



# TABLE/HASH/DICTIONARY (Order)
'''
    Referencias: 
    https://stackoverflow.com/questions/2061222/what-is-the-true-difference-between-a-dictionary-and-a-hash-table
    https://stackoverflow.com/questions/48073380/hashsets-and-hashtables-in-python

    Para empezar, un diccionario y una tabla de hash son algo distintos. El diccionario es lo más general:
    una manera de enlazar elementos o valores con ciertas llaves ("mapping keys and values").
    Una hash table o hash es una manera de implementar un diccionario.


    -- Ejemplo de un diccionario sencillo:

    # Declarar diccionario tipo 'llave/key' : 'valor/value'
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    # Accediendo a diccionario con sus llaves
    print("dict['Name']: ", dict['Name'])
    print("dict['Age']: ", dict['Age'])

    # Se pueden editar valores o añadir entradas nuevas
    dict['Age'] = 8; # actualizar
    dict['School'] = "DPS School"; # nueva entrada


    -- Ejemplo de una hash table compleja:
    Igualmente, así como vimos con el diccionario, una hash puede subir de nivel y ser más compleja, como tener una función de por medio.
    Esto es muy útil en cuestiones de ciberseguridad, para encriptar valores de gran importancia. Para ello se puede declarar una clase hash
    con sus propios utensilios, como se hará a continuación:

    # Clase HashSet, el cual recibe un input, lo transforma a algo distinto y regresa ciertos valores según ciertas llaves
    class HashSet:
        CONST = 2 ** 61 - 1

        def __init__(self, size = 10_000):
            self.size = size * 2
            self.contents = [None] * self.size

        def hash(self, x):
            return x % CONST

        def put(self, key):
            idx = self.hash(key) % self.size
            arr = self.contents[idx]
            if arr is None:
                self.contents[idx] = [key]
            elif key not in arr:
                arr.append(key)
            return None

        def get(self, key):
            idx = self.hash(key) % self.size
            arr = self.contents[idx]
            if arr is None or key not in arr:
                return False
            return True

    myset = HashSet()
    myset.put(123)
    myset.put(145)
    myset.put(138)
    res = myset.get(145)
    print(res)
    res = myset.get(10)
    print(res)



    # Clase HashMap, el cual funciona más apegado a un diccionario
    class HashMap:
        def __init__(self, size = 10_000):
            self.size = size * 2
            self.contents = [None] * self.size

        class __Pair:
            def __init__(self, key, value):
                self.key = key
                self.value = value

        def find(self, arr, key):
            for pair in arr:
                if pair.key == key:
                    return pair
            return None

        def put(self, key, value):
            idx = hash(key) % self.size
            pair = self.__Pair(key, value)
            arr = self.contents[idx]
            if arr is None:
                self.contents[idx] = [pair,]
                return None

            t = self.find(arr, key)
            if t != None:
                t.value = value
            else:
                arr.append(pair)

        def get(self, key):
            idx = hash(key) % self.size
            arr = self.contents[idx]
            if arr == None:
                raise KeyError(f'{key} is not a valid key')
            t = self.find(arr, key)
            if t == None:
                raise KeyError(f'{key} is not a valid key')
            return t.value

    mymap = HashMap()
    mymap.put('abc', [123,456])
    mymap.put('def', [456,789])
    res = mymap.get('abc')
    print(res)
    res = mymap.get('def')
    print(res)
    res = mymap.get('defx')
    print(res)
'''