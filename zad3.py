
ques = {}

pytania = ["Jak masz na imie i nazwisko:",
           "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:",
           "W jakich okolicznościach czytasz książki najczęściej?",
           "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
           "Po książki w jakiej formie sięgasz najczęściej?",
           "Ile książek czytasz średnio w ciągu roku?",
           "Jak często średnio czytasz książki?",
           "Po jaki gatunek książek sięgasz najczęściej?"]

imie_Nazwisko = input(f"pytanie 1: {pytania[0]} ")
print(f"odpowiedz: {imie_Nazwisko}")
ques[pytania[0]] = imie_Nazwisko

odpowiedzi = ["oglądanie telewizji/filmów/seriali",
              "czytanie książek/czasopism",
              "słuchanie muzyki",
              "spotkania z rodziną/przyjaciółmi",
              "podróżowanie",
              "uprawianie sportu"]
odp1 = input(f"pytanie 2: {pytania[1]} \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n"
            f"\r\r 5. {odpowiedzi[4]} \n"
            f"\r\r 6. {odpowiedzi[5]} \n")
ques[pytania[1]] = odpowiedzi[int(odp1)-1]

odpowiedzi = ["podczas podróży",
              "w czasie wolnym (po pracy, na urlopie)",
              "podczas pracy/nauki (to ich element)",
              "w ogóle nie czytam"]
odp2 = input(f"pytanie 3: {pytania[2]} \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n")
ques[pytania[2]] = odpowiedzi[int(odp2)-1]

odpowiedzi = ["chęć poszerzenia wiedzy",
              "czytanie mnie relaksuje/odpręża",
              "fakt, że czytanie jest modne",
              "czytanie to moje hobby",
              "konieczność nauki w związku z wykonywaną pracą/studiami",
              "odczuwam presję rodziny/środowiska, żeby czytać"]
odp3 = input(f"pytanie 4: {pytania[3]} \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n"
            f"\r\r 5. {odpowiedzi[4]} \n"
            f"\r\r 6. {odpowiedzi[5]} \n")
ques[pytania[3]] = odpowiedzi[int(odp3)-1]

odpowiedzi = ["papierowej (tradycyjnej)",
              "e-booki (książki elektroniczne) na komputerze",
              "e-booki na tablecie/telefonie",
              "e-booki na specjalnym czytniku (np. Kindle)"]
odp4 = input(f"pytanie 5: {pytania[4]} \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n")
ques[pytania[4]] = odpowiedzi[int(odp4)-1]

odpowiedzi = ["0",
              "żadnej w całości - jedynie fragmenty",
              "1",
              "2 lub 3",
              "4-10",
              "powyżej 10"]
odp5 = input(f"pytanie 6: {pytania[5]} \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n"
            f"\r\r 5. {odpowiedzi[4]} \n"
            f"\r\r 6. {odpowiedzi[5]} \n")
ques[pytania[5]] = odpowiedzi[int(odp5)-1]

odpowiedzi = ["codziennie",
              "raz w tygodniu",
              "raz w miesiącu",
              "raz na kilka miesięcy",
              "raz na pół roku",
              "raz na rok",
              "wcale"]
odp6 = input(f"pytanie 7: {pytania[6]} \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n"
            f"\r\r 5. {odpowiedzi[4]} \n"
            f"\r\r 6. {odpowiedzi[5]} \n"
            f"\r\r 7. {odpowiedzi[6]}  \n")
ques[pytania[6]] = odpowiedzi[int(odp6)-1]

odpowiedzi = ["kryminały/thrillery",
              "horrory",
              "fantastykę",
              "science fiction",
              "przygodowe",
              "romanse",
              "naukowe",
              "biograficzne",
              "podróżnicze",
              "poezję",
              "psychologiczne",
              "dla dzieci i młodzieży",
              "historyczne",
              "hobbystyczne (gotowanie, wędkarstwo itp.)"]
odp7 = input(f"pytanie 8: {pytania[7]} \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n"
            f"\r\r 5. {odpowiedzi[4]} \n"
            f"\r\r 6. {odpowiedzi[5]} \n"
            f"\r\r 7. {odpowiedzi[6]}  \n"
            f"\r\r 8. {odpowiedzi[7]} \n"
            f"\r\r 8. {odpowiedzi[8]} \n"
            f"\r\r 10. {odpowiedzi[9]} \n"
            f"\r\r 11. {odpowiedzi[10]} \n"
            f"\r\r 12. {odpowiedzi[11]} \n"
            f"\r\r 13. {odpowiedzi[12]} \n"
            f"\r\r 14. {odpowiedzi[13]}  \n")
ques[pytania[7]] = odpowiedzi[int(odp7)-1]

for key,value in ques.items():
    print(f"pytanie: {key}")
    print(f"odpowiedź: {value}")