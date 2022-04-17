
from funciones import*

#bucle principal del juego---------------------------------------------------------

screen = display()

while True:

	if screen.numronda == 0:
		titulo()
		#print 'titulo mostrado'
		descripcion()
		difficulty(screen)
		#print 'dificultad elegida'
	partida(screen)
