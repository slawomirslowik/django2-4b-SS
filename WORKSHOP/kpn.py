import os, random, time

menu = """
Witaj w grze kamień-papier-nożyce.
1 - Kamien
1 - Papier
3 - Nozyce
0 - Koniec gry
"""

moves = {1: "Kamień", 2: "Papier", 3: "Nożyce"}
cycle = [1, 2, 3, 1]
play = True

while play:
    os.system("cls")
    print(menu)
    your_move = int(input("Wybierz ruch (1-3):"))
    if your_move == 0:
        print("Dzięki za grę!")
        play = False
    elif your_move > 0 and your_move <= 3:
        computer_move = random.choice((1, 2, 3))
        print("Wybrales:", moves.get(your_move))
        print("Komputer wybrał:", moves.get(computer_move))
        if (your_move == computer_move):
            print("Remis!")
        # elif (your_move == 1 and computer_move == 2) or 
        # (your_move == 2 and computer_move == 3) 
        # or (your_move == 3 and computer_move == 1):
        elif (cycle[cycle.index(your_move) + 1] == computer_move):
            print("Przegrałeś!")
        else:
            print("Wygrałeś!")
    else:
        print("Nie ma takiego ruchu - spróbuj jeszcze raz!")
    time.sleep(4)