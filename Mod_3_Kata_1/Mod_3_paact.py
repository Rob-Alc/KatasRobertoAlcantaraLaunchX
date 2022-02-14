print('        === *** === P A A C T === *** ===')
print('Programa de Alerta para Asteroides Cercanos a la Tierra')
asteroide = input('Escriba el nombre del Asteroide: ')
velocidad = input('¿Qué velocidad presenta? ')
if int(velocidad) >= 25 :
    print('El asteroide: ' +"'"+ str(asteroide) + "'"+',rebasó la atmósfera a una velocidad de: ' + str(velocidad) + ' km/s, ¡¡TENGAMOS CUIDADO!!')
else :
    print('No existe peligro con el Asteroide '+ "'" + str(asteroide) + "'" + ', ya que su velocidad es de ' + str(velocidad) + ' km/s.')