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
oddelovac = 30 * "="
oddelovac1 = 30 * "-"
# registrovani_uzivatele = ["bob", "ann", "mike", "liz"]
# hesla = ["123", "pass123", "password123", "pass123"]
# uzivatele_hesla = dict(zip(registrovani_uzivatele, hesla))
#
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

print("Máte k dispozici 3 texty.\nZadejte ČÍSLO od 1 do 3.")
print(oddelovac)
vyber_textu = input("Zadejte číslo textu: ")
print(oddelovac)
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


vycisteny_text = []
for slova in vybrany_text.split():
    vycisteny_text.append(slova.strip(".,:;"))

pocet_slov = 0
pocet_velka_zac = 0
pocet_velka = 0
pocet_mala = 0
pocet_cisel = 0
suma_cisel = 0
graf_priprava = []

for slovo in vycisteny_text:
        graf_priprava.append(len(slovo))
        pocet_slov = pocet_slov + 1
        if slovo.istitle():
            pocet_velka_zac += 1
        elif slovo.isupper():
            pocet_velka +=1
        elif slovo.islower():
            pocet_mala += 1
        elif slovo.isnumeric():
            pocet_cisel += 1
            suma_cisel += int(slovo)



print("Celkový počet slov v textu je:", pocet_slov)
print("Počet slov začínajících velkým písmenem je: ", pocet_velka_zac)
print("Počet slov psaných velkým písmem je: ", pocet_velka)
print("Počet slov psaných malým písmem je: ", pocet_mala)
print("Počet čísel v textu je: ", pocet_cisel)
print("Součet čísel je: ", suma_cisel)


graf = {}

for x in graf_priprava:
    if x not in graf:
        graf[x] = graf_priprava.count(x)

nejvice_hvezdicek_v_grafu = sorted(graf.values())[-1]
print(nejvice_hvezdicek_v_grafu)
oddelovac_grafu = (nejvice_hvezdicek_v_grafu + 14) * "="
cislo_pro_mezeru = nejvice_hvezdicek_v_grafu - 14


delka = "délka"
vyskyt = "výskyt"
pocet = "počet"
print(oddelovac_grafu)
print(f"|{delka:^5}|{vyskyt:^16}|{pocet:>5}|")
print(oddelovac_grafu)
for a, b in sorted(graf.items()):
    hvezdicky = int(b) * "*"
    print(f"|{a:^5}|{hvezdicky:<16}|{b:^5}|")








