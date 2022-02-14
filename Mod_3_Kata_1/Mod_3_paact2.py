print('        === *** === P A A C T === *** ===')
print('Programa de Alerta para Asteroides Cercanos a la Tierra')
asteroide = input('Escriba el nombre del Asteroide: ')
velocidad = input('¿Qué velocidad presenta? ')
if int(velocidad) > 20 :
    print('Vean el cielo, el Asteroide ' + "'" + str(asteroide) + "'" + ', ha dejado una estela de luz.')
elif int(velocidad) == 20 :
    print('Vean el cielo, el Asteroide ' + "'" + str(asteroide) + "'" + ', ha dejado una estela de luz.')
else :
        print('El Asteroide ' + "'" + str(asteroide) + "'" + ', NO presenta peligro alguno.')

