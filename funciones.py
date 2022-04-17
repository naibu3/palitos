import time
from subprocess import call
import random

#GRAFICOS-------------------------------------------------------------------------

def titulo():
    call('clear')
    print'______   ___   _      _____  _____  _____  _____ '
    time.sleep(1)
    call('clear')

    print'______   ___   _      _____  _____  _____  _____ '
    print'| ___ \ / _ \ | |    |_   _||_   _||  _  |/  ___|'
    time.sleep(1)
    call('clear')

    print'______   ___   _      _____  _____  _____  _____ '
    print'| ___ \ / _ \ | |    |_   _||_   _||  _  |/  ___|'
    print'| |_/ // /_\ \| |      | |    | |  | | | |\ `--. '
    time.sleep(1)
    call('clear')

    print'______   ___   _      _____  _____  _____  _____ '
    print'| ___ \ / _ \ | |    |_   _||_   _||  _  |/  ___|'
    print'| |_/ // /_\ \| |      | |    | |  | | | |\ `--. '
    print'|  __/ |  _  || |      | |    | |  | | | | `--. |'
    time.sleep(1)
    call('clear')

    print'______   ___   _      _____  _____  _____  _____ '
    print'| ___ \ / _ \ | |    |_   _||_   _||  _  |/  ___|'
    print'| |_/ // /_\ \| |      | |    | |  | | | |\ `--. '
    print'|  __/ |  _  || |      | |    | |  | | | | `--. |'
    print'| |    | | | || |____ _| |_   | |  \ \_/ //\__/ |'
    time.sleep(1)
    call('clear')

    print'______   ___   _      _____  _____  _____  _____ '
    print'| ___ \ / _ \ | |    |_   _||_   _||  _  |/  ___|'
    print'| |_/ // /_\ \| |      | |    | |  | | | |\ `--. '
    print'|  __/ |  _  || |      | |    | |  | | | | `--. |'
    print'| |    | | | || |____ _| |_   | |  \ \_/ //\__/ |'
    print'\_|    \_| |_/\_____/ \___/   \_/   \___/ \____/ '
    time.sleep(1)
    call('clear')

    print'______   ___   _      _____  _____  _____  _____ '
    print'| ___ \ / _ \ | |    |_   _||_   _||  _  |/  ___|'
    print'| |_/ // /_\ \| |      | |    | |  | | | |\ `--. '
    print'|  __/ |  _  || |      | |    | |  | | | | `--. |'
    print'| |    | | | || |____ _| |_   | |  \ \_/ //\__/ |'
    print'\_|    \_| |_/\_____/ \___/   \_/   \___/ \____/ '
    time.sleep(1)
    call('clear')

    print'______   ___   _      _____  _____  _____  _____ '
    print'| ___ \ / _ \ | |    |_   _||_   _||  _  |/  ___|'
    print'| |_/ // /_\ \| |      | |    | |  | | | |\ `--. '
    print'|  __/ |  _  || |      | |    | |  | | | | `--. |'
    print'| |    | | | || |____ _| |_   | |  \ \_/ //\__/ |'
    print'\_|    \_| |_/\_____/ \___/   \_/   \___/ \____/ '
    print'******************by n41bu***********************\n\n'
    time.sleep(3)
    intro = raw_input('                  pulsa intro                   ')
    print'\n_________________________________________v1.2____'
    call('clear')

def gameover():
        print('  ___                           ___                    ')
        time.sleep(1)
        call('clear')

        print('  ___                           ___                    ')
        print(' / __|  __ _   _ __    ___     / _ \  __ __  ___   _ _ ')
        time.sleep(1)
        call('clear')

        print('  ___                           ___                    ')
        print(' / __|  __ _   _ __    ___     / _ \  __ __  ___   _ _ ')
        print("| (_ | / _` | | '  \  / -_)   | (_) | \ V / / -_) | '_|")
        time.sleep(1)
        call('clear')

        print('  ___                           ___                    ')
        print(' / __|  __ _   _ __    ___     / _ \  __ __  ___   _ _ ')
        print("| (_ | / _` | | '  \  / -_)   | (_) | \ V / / -_) | '_|")
        print(' \___| \__,_| |_|_|_| \___|    \___/   \_/  \___| |_|  ')
        time.sleep(2)
        call('clear')

        for i in (0,5):

            print('*******************************************************\n\n')
            print('  ___                           ___                    ')
            print(' / __|  __ _   _ __    ___     / _ \  __ __  ___   _ _ ')
            print("| (_ | / _` | | '  \  / -_)   | (_) | \ V / / -_) | '_|")
            print(' \___| \__,_| |_|_|_| \___|    \___/   \_/  \___| |_|  ')
            print('\n\n*******************************************************')
            time.sleep(1)
            call('clear')

            print('\n\n\n')
            print('  ___                           ___                    ')
            print(' / __|  __ _   _ __    ___     / _ \  __ __  ___   _ _ ')
            print("| (_ | / _` | | '  \  / -_)   | (_) | \ V / / -_) | '_|")
            print(' \___| \__,_| |_|_|_| \___|    \___/   \_/  \___| |_|  ')
            print('\n\n\n')
            time.sleep(1)
            call('clear')

        print('*******************************************************\n\n')
        print('  ___                           ___                    ')
        print(' / __|  __ _   _ __    ___     / _ \  __ __  ___   _ _ ')
        print("| (_ | / _` | | '  \  / -_)   | (_) | \ V / / -_) | '_|")
        print(' \___| \__,_| |_|_|_| \___|    \___/   \_/  \___| |_|  ')
        print('\n                      pulsa intro                      ')
        print(raw_input('*******************************************************'))
        call('clear')

def hasganado():
        print('\n\n\n')
        print('                                                           _ ')
        print('                                                         | |')
        print('                                                         | _')
        print('                                                         |_|')
        print('\n\n\n')
        time.sleep(0.7)
        call('clear')

        print('\n\n\n')
        print('                                                       _  _  ')
        print('                                                      | || | ')
        print('                                                      | __ | ')
        print('                                                      |_||_| ')
        print('\n\n\n')
        time.sleep(0.7)
        call('clear')

        print('\n\n\n')
        print('                                                  _  _       ')
        print('                                                 | || |  __ _')
        print('                                                 | __ | / _` ')
        print('                                                 |_||_| \__,_')
        print('\n\n\n')
        time.sleep(0.7)
        call('clear')

        print('\n\n\n')
        print('                                            _  _             ')
        print('                                           | || |  __ _   ___')
        print('                                           | __ | / _` | (_-<')
        print('                                           |_||_| \__,_| /__/')
        print('\n\n\n')
        time.sleep(0.7)
        call('clear')

        print('\n\n\n')
        print('                                     _  _                  __')
        print('                                    | || |  __ _   ___    / _')
        print('                                    | __ | / _` | (_-<   | (_')
        print('                                    |_||_| \__,_| /__/    \__')
        print('\n\n\n')
        time.sleep(0.7)
        call('clear')

        print('\n\n\n')
        print('                            _  _                  ___        ')
        print('                           | || |  __ _   ___    / __|  __ _ ')
        print('                           | __ | / _` | (_-<   | (_ | / _` |')
        print('                           |_||_| \__,_| /__/    \___| \__,_|')
        print('\n\n\n')
        time.sleep(0.7)
        call('clear')

        print('\n\n\n')
        print('                   _  _                  ___                 ')
        print('                  | || |  __ _   ___    / __|  __ _   _ _    ')
        print("                  | __ | / _` | (_-<   | (_ | / _` | | ' \  /")
        print('                  |_||_| \__,_| /__/    \___| \__,_| |_||_| \ ')
        print('\n\n\n')
        time.sleep(0.7)
        call('clear')

        print('\n\n\n')
        print(' _  _                  ___                           _       ')
        print('| || |  __ _   ___    / __|  __ _   _ _    __ _   __| |  ___ ')
        print("| __ | / _` | (_-<   | (_ | / _` | | ' \  / _` | / _` | / _ \ ")
        print('|_||_| \__,_| /__/    \___| \__,_| |_||_| \__,_| \__,_| \___/')
        print('\n\n\n')
        time.sleep(0.7)
        call('clear')

        for i in (0,5):
            print('************************************************************\n\n')
            print(' _  _                  ___                           _       ')
            print('| || |  __ _   ___    / __|  __ _   _ _    __ _   __| |  ___ ')
            print("| __ | / _` | (_-<   | (_ | / _` | | ' \  / _` | / _` | / _ \ ")
            print('|_||_| \__,_| /__/    \___| \__,_| |_||_| \__,_| \__,_| \___/')
            print('\n\n************************************************************')
            time.sleep(1)
            call('clear')

            print('\n\n\n')
            print(' _  _                  ___                           _       ')
            print('| || |  __ _   ___    / __|  __ _   _ _    __ _   __| |  ___ ')
            print("| __ | / _` | (_-<   | (_ | / _` | | ' \  / _` | / _` | / _ \ ")
            print('|_||_| \__,_| /__/    \___| \__,_| |_||_| \__,_| \__,_| \___/')
            print('\n\n\n')
            time.sleep(1)
            call('clear')

        print('\n\n\n')
        print(' _  _                  ___                           _       ')
        print('| || |  __ _   ___    / __|  __ _   _ _    __ _   __| |  ___ ')
        print("| __ | / _` | (_-<   | (_ | / _` | | ' \  / _` | / _` | / _ \ ")
        print('|_||_| \__,_| /__/    \___| \__,_| |_||_| \__,_| \__,_| \___/')
        print('\n\n\n')
        raw_input('***************************pulsa intro***********************')
        call('clear')

def descripcion():
    print('\n\n*******************************************************')
    print('*                                                     *')
    print('*     Consigue quitar el ultimo palito para ganar     *')
    print('*                                                     *')
    print('*******************************************************')
    time.sleep(1.4)
    call('clear')

#LOGICA---------------------------------------------------------------------------

class display():
    numpalitos = random.randint(16,24)
    numronda = 0
    dificultad = None
    coin = random.choice([True,False])
    listadificultades = ['uf','f','n','i']
    ultimo = None

    def ronda(self):
        self.numronda+=1
        print('*******************************************************\n\n')
        print('                        ronda '+ str(self.numronda) + '                        \n\n')
        print('*******************************************************')
        time.sleep(2.3)
        call('clear')

    def imprimirpantalla(self):
        print('\nPalitos = '+ str(self.numpalitos) + '************************************'+'Ronda '+str(self.numronda)+'\n\n\n')
        sobra = self.numpalitos%4
        multiplo = (self.numpalitos-sobra)/4
        print((' | | | | '*multiplo) + ' ' +'| '*sobra )
        print((' | | | | '*multiplo) + ' ' +'| '*sobra )
        print((' | | | | '*multiplo) + ' ' +'| '*sobra )
        print('\n\n\n*******************************************************')

    def gana(self):
        if self.numpalitos == 0:
            if self.ultimo == True:
                hasganado()
            if self.ultimo == False:
                gameover()
        while True:
            respuesta = raw_input('Quieres volver a jugar (s/n) ')
            if respuesta == 's':
                self.numpalitos = random.randint(16,24)
                self.numronda = 0
                self.dificultad = None
                coin = random.choice([True,False])
                break
            if respuesta == 'n':
               quit()
            
def turnopl(pantalla):
    pantalla.ultimo = True
    while True:
        pantalla.imprimirpantalla()
        resta = raw_input('cuantos palitos quieres quitar? (1,2,3 o 4)')
        time.sleep(1)
        call('clear')
        try:
            resta = int(resta)
            if resta in range(1,5):
                pantalla.numpalitos -= resta
                break
        except:
            call('clear')
            print('Introduce un NUMERO del 1 al 4...')
            time.sleep(1)
            call('clear')
    pantalla.imprimirpantalla()
    time.sleep(2)
    call('clear')

def turnocpu(pantalla):
    pantalla.ultimo = False
    pantalla.imprimirpantalla()
    print 'turno de la cpu...'
    time.sleep(2)
    call('clear')

    if pantalla.dificultad == 0:    #para bebes-------------------------------------------
        while True:
            if pantalla.numpalitos > 4:
                resta = random.randint(1,5)
                pantalla.numpalitos -= resta
                break
            if pantalla.numpalitos <= 4:
                pantalla.numpalitos = 0
                break

    if pantalla.dificultad == 1:    #para medio tontos---------------------------------
       while True:
            if pantalla.numpalitos > 10:
                resta = random.randint(1,4)
                pantalla.numpalitos -= resta
                break
            if pantalla.numpalitos in range(5,11):
                if pantalla.numpalitos == 10:
                    pantalla.numpalitos=9
                    break
                if pantalla.numpalitos in range(6,10):
                    pantalla.numpalitos=5
                    break
                if pantalla.numpalitos == 5:
                    pantalla.numpalitos=4
                    break
            if pantalla.numpalitos <= 4:
                pantalla.numpalitos = 0
                break 

    if pantalla.dificultad == 2:    #modo para la media de IQ de la poblacion------------------
        while True:
            if pantalla.numpalitos in range(16,21):
                if pantalla.numpalitos == 20:
                    pantalla.numpalitos = 19
                    break
                if pantalla.numpalitos in range(16,20):
                    pantalla.numpalitos=15
                    break
            if pantalla.numpalitos in range(11,16):
                if pantalla.numpalitos == 15:
                    pantalla.numpalitos = 14
                    break
                if pantalla.numpalitos in range(11,14):
                    pantalla.numpalitos=10
                    break
            if pantalla.numpalitos in range(5,11):
                if pantalla.numpalitos == 10:
                    pantalla.numpalitos=9
                    break
                if pantalla.numpalitos in range(6,10):
                    pantalla.numpalitos=5
                    break
                if pantalla.numpalitos == 5:
                    pantalla.numpalitos=4
                    break
            if pantalla.numpalitos <= 4:
                pantalla.numpalitos = 0
                break

    if pantalla.dificultad == 3:     #modo para p**os genios-----------------------------------
        while True:
            if pantalla.numpalitos in range(21,25):
                pantalla.numpalitos = 20
                break
            if pantalla.numpalitos in range(16,21):
                if pantalla.numpalitos == 20:
                    pantalla.numpalitos = 19
                    break
                if pantalla.numpalitos in range(16,20):
                    pantalla.numpalitos=15
                    break
            if pantalla.numpalitos in range(11,16):
                if pantalla.numpalitos == 15:
                    pantalla.numpalitos = 14
                    break
                if pantalla.numpalitos in range(11,14):
                    pantalla.numpalitos = 10
                    break
            if pantalla.numpalitos in range(5,11):
                if pantalla.numpalitos == 10:
                    pantalla.numpalitos = 9
                    break
                if pantalla.numpalitos in range(6,10):
                    pantalla.numpalitos = 5
                    break
                if pantalla.numpalitos == 5:
                    pantalla.numpalitos = 4
                    break
            if pantalla.numpalitos <= 4:
                pantalla.numpalitos = 0
                break

    pantalla.imprimirpantalla()
    time.sleep(2)
    call('clear')

def difficulty(pantalla):

    while True:
        print('*******************************************************')
        print('*                                                     *')
        print('* -@- Bebe (ultra facil)     -@-                      *')
        print('* -@- Tontico (facil)        -@-                      *')
        print('* -@- IQ normal (normal)     -@-                      *')
        print('* -@- El Profesor(imposible) -@-                      *')
        print('*                                                     *')
        print('*******************************************************')

        eleccion = str(raw_input('Elige dificultad (uf/f/n/i) '))
        if eleccion in pantalla.listadificultades:
            if eleccion == 'uf':
                pantalla.dificultad = 0
                break
            if eleccion == 'f':
                pantalla.dificultad = 1
                break
            if eleccion == 'n':
                pantalla.dificultad = 2
                break
            if eleccion == 'i':
                pantalla.dificultad = 3
                break
        time.sleep(1.3)
        call('clear')
    call('clear')

def partida(pantalla):
    if pantalla.coin == True:
        pantalla.ronda()
        turnopl(pantalla)
        print 'tu turno mostrado'
        if pantalla.numpalitos == 0:
            pantalla.gana()
        turnocpu(pantalla)
        print 'cpu turno mostrado'
        if pantalla.numpalitos == 0:
            pantalla.gana()
    if pantalla.coin == False:
        pantalla.ronda()
        turnocpu(pantalla)
        print 'cpu turno mostrado'
        if pantalla.numpalitos == 0:
            pantalla.gana()
        turnopl(pantalla)
        print 'tu turno mostrado'
        if pantalla.numpalitos == 0:
            pantalla.gana()

