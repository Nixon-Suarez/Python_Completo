import sys
import ataquemodulo
import estatusmodulo

def inicio():
    print("Bienvenido al juego")
    print("Elija una dificultad:\n [1]Facil [2]Medio [3]Dificil [#]Salir")
    numero = int(input(" => "))
    return numero

def dificultad(num):
    if num == 1:
        print("Escogiste el camino de los miricas y bebes recien nacidos")
        print("tu batalla sera contra el paladin")
        return 100
    elif num == 2:
        print("Escogiste el camino de los niños pubertos que se masturban con las fotos de sus primas")
        print("tu batalla sera contra el Ogro")
        return 200
    elif num == 3:
        print("Escogiste el camino de los Hombres de pecho plateado olfatea culos")
        print("tu batalla sera contra el Dragon")
        return 300
    else:
        print("saliste del juego escogiste el camino de los que les gusta chupar pene de negro con sarna")
        sys.exit()
    
def main():
    numero = inicio()
    hp_enemy = dificultad(numero)
    print("******")
    hp = 100
    turno = True
    print("****Tu Batalla Inicia****")
    while hp_enemy > 0 and hp > 0:
        ataque_enemigo = ataquemodulo.atk_enemy(numero)
        print("El ataque de tu enemigo fue de {}".format(ataque_enemigo))
        hp -= ataque_enemigo
        if hp > 0:
            if turno == True:
                estatusmodulo.status(hp, hp_enemy)
                print("Es tu turno de atacar un golpe de suerte")
                print("Elige entre dos ataques")
                print("Ataque Fuerte baja entre 20 y 60 de vida")
                print("Ataque Normal baja estre 10 y 30")
                print("[1] Ataque Fuerte [#] Ataque Normal")
                mi_ataque = int(input(" => "))
                el_ataque = ataquemodulo.atk(mi_ataque)
                mi_daño = el_ataque[0]
                turno = el_ataque[1]
                print("Tu ataque fue de {}".format(mi_daño))
                hp_enemy -= mi_daño 
                if hp_enemy <=  0:
                    print("Derribaste a tu enemigo GANASTE")
                    sys.exit()
                else:
                    estatusmodulo.status(hp, hp_enemy)
                    pass
            else:
                turno = True
                pass
        



        else:
            print("Has perdido la batalla maricon")
            sys.exit()
        

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        sys.exit()

