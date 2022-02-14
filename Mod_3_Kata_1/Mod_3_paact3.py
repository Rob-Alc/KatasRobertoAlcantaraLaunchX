print('        === *** === P A A C T === *** ===')
print('Programa de Alerta para Asteroides Cercanos a la Tierra')
asteroide = input('Escriba el nombre del Asteroide:  ')
velocidad = input('¿Qué velocidad en km/s presenta? ')
diametro = input('¿Qué diámetro en metros tiene? ')

if int(velocidad) > 25 and int(diametro) > 25:
    print('El asteroide: ' +"'"+ str(asteroide) + "'"+',presenta una velocidad de: ' + str(velocidad) + ' km/s, y un diámetro de: ' +str(diametro) + ' metros, ¡¡TENGAMOS CUIDADO!!')
elif int(velocidad) >= 20 :
     print('Vean el cielo, el Asteroide ' + "'" + str(asteroide) + "'" + ', ha dejado una estela de luz.')
elif int(diametro) < 25 :
     print('No existe peligro con el Asteroide '+ "'" + str(asteroide) + "'" + ', ya que su diámetro es de ' + str(diámetro) + ' metros')
else:
      print('El Asteroide ' + "'" + str(asteroide) + "'" + ', NO presenta peligro alguno.')
