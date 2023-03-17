imie_Nazwisko = input("pytanie 1: Jak masz na imie i nazwisko: ")
print(f"odpowiedz: {imie_Nazwisko}")
print("\nWpisz numer odpowiedzi\n")

odpowiedzi = ["oglądanie telewizji/filmów/seriali",
              "czytanie książek/czasopism",
              "słuchanie muzyki",
              "spotkania z rodziną/przyjaciółmi",
              "podróżowanie",
              "uprawianie sportu",
              "inne, jakie: "]
odp1 = input("pytanie 2: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n"
            f"\r\r 5. {odpowiedzi[4]} \n"
            f"\r\r 6. {odpowiedzi[5]} \n"
            f"\r\r 7. {odpowiedzi[6]}  \n")
print(f"odpowiedz: {odpowiedzi[int(odp1)-1]}")

odpowiedzi = ["podczas podróży",
              "w czasie wolnym (po pracy, na urlopie)",
              "podczas pracy/nauki (to ich element)",
              "w ogóle nie czytam",
              "inne, jakie: "]
odp2 = input("pytanie 3: W jakich okolicznościach czytasz książki najczęściej? \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n"
            f"\r\r 5. {odpowiedzi[4]} \n")
print(f"odpowiedz: {odpowiedzi[int(odp2)-1]}")

odpowiedzi = ["chęć poszerzenia wiedzy",
              "czytanie mnie relaksuje/odpręża",
              "fakt, że czytanie jest modne",
              "czytanie to moje hobby",
              "konieczność nauki w związku z wykonywaną pracą/studiami",
              "odczuwam presję rodziny/środowiska, żeby czytać",
              "inny, jaki: "]
odp3 = input("pytanie 4: Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n"
            f"\r\r 5. {odpowiedzi[4]} \n"
            f"\r\r 6. {odpowiedzi[5]} \n"
            f"\r\r 7. {odpowiedzi[6]}  \n")
print(f"odpowiedz: {odpowiedzi[int(odp3)-1]}")

odpowiedzi = ["papierowej (tradycyjnej)",
              "e-booki (książki elektroniczne) na komputerze",
              "e-booki na tablecie/telefonie",
              "e-booki na specjalnym czytniku (np. Kindle)"]
odp4 = input("pytanie 5: Po książki w jakiej formie sięgasz najczęściej? \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n")
print(f"odpowiedz: {odpowiedzi[int(odp4)-1]}")

odpowiedzi = ["0",
              "żadnej w całości - jedynie fragmenty",
              "1",
              "2 lub 3",
              "4-10",
              "powyżej 10"]
odp5 = input("pytanie 6: Ile książek czytasz średnio w ciągu roku? \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n"
            f"\r\r 5. {odpowiedzi[4]} \n"
            f"\r\r 6. {odpowiedzi[5]} \n")
print(f"odpowiedz: {odpowiedzi[int(odp5)-1]}")

odpowiedzi = ["codziennie",
              "raz w tygodniu",
              "raz w miesiącu",
              "raz na kilka miesięcy",
              "raz na pół roku",
              "raz na rok",
              "wcale"]
odp6 = input("pytanie 7: Jak często średnio czytasz książki? \n"
            f"\r\r 1. {odpowiedzi[0]} \n"
            f"\r\r 2. {odpowiedzi[1]} \n"
            f"\r\r 3. {odpowiedzi[2]} \n"
            f"\r\r 4. {odpowiedzi[3]} \n"
            f"\r\r 5. {odpowiedzi[4]} \n"
            f"\r\r 6. {odpowiedzi[5]} \n"
            f"\r\r 7. {odpowiedzi[6]}  \n")
print(f"odpowiedz: {odpowiedzi[int(odp6)-1]}")

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
              "hobbystyczne (gotowanie, wędkarstwo itp.)",
              "inny, jaki: "]
odp7 = input("pytanie 8: Po jaki gatunek książek sięgasz najczęściej? \n"
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
            f"\r\r 14. {odpowiedzi[13]}  \n"
            f"\r\r 15. {odpowiedzi[14]}  \n")
print(f"odpowiedz: {odpowiedzi[int(odp7)-1]}")