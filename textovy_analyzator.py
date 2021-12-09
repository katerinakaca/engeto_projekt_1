'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# uživatelský vstup
# oddelovac = 30 * "="
# oddelovac1 = 30 * "-"
# registrovani_uzivatele = ["bob", "ann", "mike", "liz"]
# hesla = ["123", "pass123", "password123", "pass123"]
# uzivatele_hesla = dict(zip(registrovani_uzivatele, hesla))
# print(uzivatele_hesla)
# uzivatel = input("Jméno: ")
# heslo = input("Heslo: ")
#
# if uzivatel in uzivatele_hesla and uzivatele_hesla[uzivatel] == heslo:
#     print(f"{oddelovac1}\n     Vítej uživateli {uzivatel}!\n{oddelovac1}")
#
# else:
#     print("Zadali jste neplatné uživatelské jméno nebo heslo. Ukončuji...")
#     exit()

#výběr textu
print("Pro výběr textu zadejte číslo textu. Máte k dispozici 3 texty. Výběr textu musí být číslo od 1 do 3.")
vyber_textu = input("Zadejte číslo textu: ")
if not vyber_textu.isnumeric():
    print("Tento text není k dispozici. Ukončuji.")
    exit()
elif int(vyber_textu) not in range(1,4):
    print("Tento text není k dispozici. Ukončuji.")
    exit()
else:
    print("Vybral jste text č.", vyber_textu)

#výpis textu
vybrany_text = TEXTS[int(vyber_textu) - 1]
print(vybrany_text)
vycisteny_text = []
for slova in vybrany_text.split():
    vycisteny_text.append(slova.strip(".,:;"))

vyskyt_slov = {}
for slovo in vycisteny_text:
    if slovo not in vyskyt_slov:
        vyskyt_slov.setdefault(slovo, 1)
    elif slovo in vyskyt_slov:
        vyskyt_slov[slovo] += 1


pocet_slov = sum(vyskyt_slov.values())
pocet_velka_zac = {}
pocet_velka = {}
pocet_mala = {}
pocet_cisel = {}
suma_cisel = {}
cisla_v_textu = []

for sl, vyskyt in vyskyt_slov.items():
    if sl.istitle() == True:
        pocet_velka_zac[sl] = vyskyt
    elif sl.islower() == True:
        pocet_mala[sl] = vyskyt
    elif sl.isupper() == True:
        pocet_velka[sl] = vyskyt
    elif sl.isnumeric == True:
        for cisla in sl:
            print(cisla)
            cisla_v_textu.append(cisla)
print(cisla_v_textu)


print(pocet_velka_zac)
print(pocet_mala)
print(pocet_velka)

    # vyskyt_slov["počet slov"] = tuple(enumerate(vycisteny_text))[-1][0]
    # if slovo.istitle() == True:
    #     velka_pismena_zac = []
    #     velka_pismena_zac.append(slovo)
    #     print(velka_pismena_zac)
    #     vyskyt_slov["Počet slov začínajících velkým písmenem"] = tuple(enumerate(velka_pismena_zac))[-1][0]
    # elif slovo.isupper() == True:
    #     velka_pismena = []
    #     velka_pismena.append(slovo)
    #     vyskyt_slov["Počet slov psaných velkým písmenem"] = tuple(enumerate(velka_pismena))[-1][0]
    # elif slovo.islower() == True:
    #     mala_pismena = []
    #     mala_pismena.append(slovo)
    #     vyskyt_slov["Počet slov psaných malým písmenem"] = tuple(enumerate(mala_pismena))[-1][0]




# print(pocet_velke)


