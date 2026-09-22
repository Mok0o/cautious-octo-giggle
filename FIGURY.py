print("a - bryly b - figury plaskie")
inp = input(": ").lower().strip()

if inp == "a":
    print("a - pole powierzchni b - objetosc")
    inp = input(": ").lower().strip()

    if inp == "a":
        print("a - szescian  b - prostopadloscian  c - walec  d - stozek  e - kula")
        inp = input(": ").lower().strip()

        if inp == "a":
            a = float(input("a: "))
            print(f"Szescian: Pc = {6 * a * a}")
        elif inp == "b":
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            print(f"Prostopadloscian: Pc = {2*a*b + 2*a*c + 2*b*c}")
        elif inp == "c":
            r = float(input("r: "))
            h = float(input("h: "))
            print(f"Walec: Pc = {2*3.14*r*r + 2*3.14*r*h}")
        elif inp == "d":
            r = float(input("r: "))
            l = float(input("l (tworzaca): "))
            print(f"Stozek: Pc = {3.14*r*r + 3.14*r*l}")
        elif inp == "e":
            r = float(input("r: "))
            print(f"Kula: Pc = {4*3.14*r*r}")
        else:
            print("Nie ma takiej komendy")

    elif inp == "b":
        print("a - szescian  b - prostopadloscian  c - walec  d - stozek  e - kula")
        inp = input(": ").lower().strip()

        if inp == "a":
            a = float(input("a: "))
            print(f"Szescian: V = {a*a*a}")
        elif inp == "b":
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            print(f"Prostopadloscian: V = {a*b*c}")
        elif inp == "c":
            r = float(input("r: "))
            h = float(input("h: "))
            print(f"Walec: V = {3.14*r*r*h}")
        elif inp == "d":
            r = float(input("r: "))
            h = float(input("h: "))
            print(f"Stozek: V = {(1/3)*3.14*r*r*h}")
        elif inp == "e":
            r = float(input("r: "))
            print(f"Kula: V = {(4/3)*3.14*r*r*r}")
        else:
            print("Nie ma takiej komendy")

    else:
        print("Nie ma takiej komendy")

elif inp == "b":
    print("a - kwadrat  b - prostokat  c - trojkat  d - kolo  e - trapez  f - romb  g - trojkat rownoboczny")
    inp = input(": ").lower().strip()

    if inp == "a":
        a = float(input("a: "))
        print(f"Kwadrat: Obwod = {4*a}   Pole = {a*a}")
    elif inp == "b":
        a = float(input("a: "))
        b = float(input("b: "))
        print(f"Prostokat: Obwod = {2*a + 2*b}   Pole = {a*b}")
    elif inp == "c":
        a = float(input("podstawa a: "))
        h = float(input("wysokosc h: "))
        print(f"Trojkat: Pole = {0.5 * a * h}")
    elif inp == "d":
        r = float(input("r: "))
        print(f"Kolo: Obwod = {2*3.14*r}   Pole = {3.14*r*r}")
    elif inp == "e":
        a = float(input("podstawa a: "))
        b = float(input("podstawa b: "))
        h = float(input("wysokosc h: "))
        print(f"Trapez: Pole = {0.5 * (a + b) * h}")
    elif inp == "f":
        e = float(input("przekatna e: "))
        f = float(input("przekatna f: "))
        print(f"Romb: Pole = {(e * f) / 2}")
    elif inp == "g":
        a = float(input("a: "))
        print(f"Trojkat rownoboczny: Obwod = {3*a}   Pole = {(a*a * 1.732) / 4}")
    else:
        print("Nie ma takiej komendy")

else:
    print("Nie ma takiej komendy")