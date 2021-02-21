# Projekt1: analyzator textu
# Author: Jiri Romanovsky
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
oddelovac = 50*'-'
#1. vstup uzivatele
username = input("Zadej uzivatelske jmeno: ")
password = input("Zadej heslo: ")
print(oddelovac)
# 2. overeni vstupu
# 3. Vytiskni pozdrav a pokracuj v aplikaci
# vymyslet overeni typu dat 
databaze_uzivatelu = {'bob' : '123','ann':'pass123','mike':'password123','liz':'pass123'}
for jmeno, heslo in databaze_uzivatelu.items():    
    if username != jmeno or password != heslo:
        continue
        print(f'Jmeno: {username} neni v dabazi nebo jsi zadal spatne heslo. Program bude ukoncen.')
    else:
        print(f"Vitej v aplikaci, {username}\nMas k dispozici {len(TEXTS)} texty k analyze.")
        print(oddelovac)

# 4. Vyber textu a overeni
vyber_textu = input(f"Vyber cislo mezi 1 a {len(TEXTS)}: ")
if vyber_textu.isalpha() or int(vyber_textu) > len(TEXTS):
    print(f"Musis vybrat cislo v danem rozsahu! Program se ukonci.")
else:
  vyber_textu = int(vyber_textu) - 1
  text = TEXTS[vyber_textu].split()
  for slovo in text:
    ocistene_slovo = slovo.strip('.,!?()')