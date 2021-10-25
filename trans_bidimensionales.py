from matplotlib import pyplot as plt
import numpy as np

def graficar(x, y, plt):
    plt.set_xlim([-10,10])
    plt.set_ylim([-10,10])
    plt.plot(x,y)

def request_points():
    n_points = int(input('Ingrese la cantidad de puntos: '))
    # Genero la matriz de puntos
    matriz_points = [[],[],[1 for _ in range(n_points)]]
    #Capturo los puntos y los incluyo en la matriz inicial
    for _ in range(n_points):
        puntos = input('Ingrese los puntos x,y : ')
        x, y= puntos.split(',')
        matriz_points[0].append(float(x))
        matriz_points[1].append(float(y))
        print(f'({x},{y})')
    # Convierto la matriz inciial en np.array
    matriz_points = np.array(matriz_points)
    return matriz_points

def traslation(matriz_points, vector_traslation):
    matriz_traslation = np.identity(3)
    matriz_traslation[0][2] = vector_traslation[0]
    matriz_traslation[1][2] = vector_traslation[1]
    return matriz_traslation@matriz_points

def transf_traslation():
    figure = plt.figure()
    figure.suptitle('Traslación')
    matriz_points = request_points()
    graficar(matriz_points[0], matriz_points[1], figure.add_subplot(1,2,1, title='Matriz inicial'))
    #Ingreso el vector traslacion y los convierto a np.array
    vector_traslation = input('Ingrese el vector traslación x,y: ')
    xt, yt = vector_traslation.split(',')
    vector_traslation = np.array(([float(xt)], [float(yt)]))
    # Hago la transformación bidimensional de traslación
    matriz_points_traslation = traslation(matriz_points, vector_traslation)
    graficar(matriz_points_traslation[0], matriz_points_traslation[1], figure.add_subplot(1,2,2, title='Matriz transformada'))
    plt.show()

def escala(matriz_points, vector_escala):
    matriz_escala = np.identity(3)
    matriz_escala[0][0] = vector_escala[0]
    matriz_escala[1][1] = vector_escala[1]
    return matriz_escala@matriz_points

def trans_escala():
    figure = plt.figure()
    figure.suptitle('Escala')
    matriz_points = request_points()
    graficar(matriz_points[0], matriz_points[1], figure.add_subplot(1,2,1, title='Matriz inicial'))
    #Ingreso el vector traslacion y los convierto a np.array
    vector_escala = input('Ingrese el factor de escala para x,y separado por comas: ')
    xt, yt = vector_escala.split(',')
    vector_escala = np.array(([float(xt)], [float(yt)]))
    # Hago la transformación bidimensional de traslación
    matriz_points_escala = escala(matriz_points, vector_escala)
    graficar(matriz_points_escala[0], matriz_points_escala[1], figure.add_subplot(1,2,2, title='Matriz transformada'))
    plt.show()

def rotation(matriz_points, ang_rotation):
    matriz_rotation = np.identity(3)
    matriz_rotation[0][0] = np.cos(ang_rotation)
    matriz_rotation[0][1] = (-1)*np.sin(ang_rotation)
    matriz_rotation[1][0] = np.sin(ang_rotation)
    matriz_rotation[1][1] = np.cos(ang_rotation)
    return matriz_rotation@matriz_points

def trans_rotation():
    figure = plt.figure()
    figure.suptitle('Rotaciòn')
    matriz_points = request_points()
    graficar(matriz_points[0], matriz_points[1], figure.add_subplot(1,2,1, title='Matriz inicial'))
    #Ingreso el vector traslacion y los convierto a np.array
    ang_rotation = input('Ingrese el angulo de rotación en sexagesimal: ')
    ang_rotation = float(ang_rotation)*(np.pi/180)
    # Hago la transformación bidimensional de traslación
    matriz_points_rotation = rotation(matriz_points, ang_rotation)
    graficar(matriz_points_rotation[0], matriz_points_rotation[1], figure.add_subplot(1,2,2, title='Matriz transformada'))
    plt.show()

def run():
    flag = True
    print('Transformaciones Geometricas Bidimensionales')
    while flag:
        option = input('1. Traslation\n2. Escalamiento\n3. Rotación\nIngrese opción: ')
        if option == '1':
            transf_traslation()
        if option == '2':
            trans_escala()
        if option == '3':
            trans_rotation()
        if option not in '123':
            flag = False
            print('Saliendo de programa')
    
run()