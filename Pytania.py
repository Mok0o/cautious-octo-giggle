print("Wychodzimy na randke?")
print("1. Tak")
print("0. Nie")
a = float(input())
if a == 0:
    print("A no to niema o czym gadać")
elif a == 1:
    print("Dobra to najpierw odpowiedz na kilka pytań.")
    print("Ile masz wzrostu?")
    b = float(input())
    if b < 150:
        print("O wiele za niski...")
    elif b > 200:
        print("O wiele za wysoki...")
    else:
        print("W sam raz")
        print("Ile masz lat?")
        c = float(input())
        if c < 15:
            print("Too young")
        elif c > 16:
            print("Too old")
        else:
            print("No i luz")
            print("Ile masz kg?")
            d = float(input()) 
            if d < 40:
                print("Jak ty się trzymasz wgl")
            elif d > 90:
                print("I'll pass on that one.")
            else:
                print("Perfecto")
                print("Jesteś wgl gejem? albo coś podobnego?")
                print("1. Tak")
                print("0. Nie")
                e = float(input())
                if e == 1:
                    print("Luzik")
                    print("SUPER ważne pytanie. Ile godzin tygodniowo grałbyś ze mną w minecraft?")
                    f = float(input())
                    if f < 10:
                        print("Za mało")  
                    else:
                        print("Przekupiłeś mnie.")
                        print("Jaki masz kolor włosów?")
                        print("1. Blond")
                        print("2. Brązowe")
                        print("3. Czarne")
                        print("4. Rude")
                        print("5. Inny")
                        g = float(input())
                        if g == 4 or g == 5:
                            print("I am GOOD. Sorry")
                        else:
                            print("No i gitara.")
                            print("Kolor oczu?")
                            print("1. Niebieskie")
                            print("2. Zielone")
                            print("3. Brązowe")
                            print("4. Inny")
                            h = float(input())
                            if h == 1 or h == 2 or h == 3:
                                print("Ładne.")
                                print("kolejne WAŻNE pytanie. Najpierw płatki czy mleko?")
                                print("1. Płatki")
                                print("0. Mleko")
                                i = float(input())
                                if i == 1:
                                    print("Okej ty się znasz.")
                                    print("Teraz będzie na rozkminkę.")
                                    print("Czy cytryna smakuje wolno czy szybko?")
                                    print("1. Wolno")
                                    print("0. Szybko")
                                    j = float(input())
                                    if j == 1:
                                        print("No tak troche NIE")
                                    else:
                                        print("No dobra.")
                                        print("Ostatnie pytanie. Czy wolisz koty czy psy?")
                                        print("1. Koty")
                                        print("0. Psy")
                                        k = float(input())
                                        if k == 1:
                                            print("Valid. Możemy się umówić na randkę. :D")
                                        elif k == 0:
                                            print("Valid. Możemy się umówić na randkę. :D")
                                elif i == 0:
                                    print("hell NO WTF")
                            else:
                                print("Jesteś człowiekiem czy kosmitą? :sob:")
                elif e == 0:
                    print("Stick to the script vro. :sob:")
                else:
                    print("Możesz wybrać tylko 1 lub 0 GENIUSZU")
else:
    print("Możesz wybrać tylko 1 lub 0 GENIUSZU")
