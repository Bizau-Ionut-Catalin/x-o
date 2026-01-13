def afiseaza(tabla):
    print()
    for i in range(3):
        print(" | ".join(tabla[i]))
        if i < 2:
            print("-" * 9)
    print()
def citeste_mutare(tabla, jucator):
    while True:
        try:
            linie = int(input(f"Jucătorul {jucator}, introdu linia (0-2): "))
            coloana = int(input(f"Jucătorul {jucator}, introdu coloana (0-2): "))

            if linie < 0 or linie > 2 or coloana < 0 or coloana > 2:
                print("Eroare: coordonatele trebuie să fie între 0 și 2.")
            elif tabla[linie][coloana] != ".":
                print("Eroare: poziția nu este liberă.")
            else:
                return linie, coloana
        except ValueError:
            print("Eroare: trebuie introduse numere întregi.")
def stare_joc(tabla):
    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] != ".":
            return tabla[i][0]
    for j in range(3):
        if tabla[0][j] == tabla[1][j] == tabla[2][j] != ".":
            return tabla[0][j]
    if tabla[0][0] == tabla[1][1] == tabla[2][2] != ".":
        return tabla[0][0]

    if tabla[0][2] == tabla[1][1] == tabla[2][0] != ".":
        return tabla[0][2]
    for linie in tabla:
        if "." in linie:
            return "CONTINUA"
    return "EGAL"
tabla = [["." for _ in range(3)] for _ in range(3)]
jucator = "X"
while True:
    afiseaza(tabla)
    linie, coloana = citeste_mutare(tabla, jucator)
    tabla[linie][coloana] = jucator
    stare = stare_joc(tabla)
    if stare != "CONTINUA":
        afiseaza(tabla)
        if stare == "EGAL":
            print("Jocul s-a terminat la egal!")
        else:
            print(f"Jucătorul {stare} a câștigat!")
        break
    jucator = "O" if jucator == "X" else "X"

