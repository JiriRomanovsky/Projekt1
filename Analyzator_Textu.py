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
which traverse the valley.''',

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
username = input("Username: ")
password = input("Password: ")
print(oddelovac)
# 2. overeni vstupu
# 3. Vytiskni pozdrav a pokracuj v aplikaci
databaze_uzivatelu = {'bob' : '123','ann':'pass123','mike':'password123','liz':'pass123'}
if username not in databaze_uzivatelu or password != str(databaze_uzivatelu[username]):
     print(f'Name {username} is not in the database or the password is incorrect. Program will be exited.')
     exit()
else:
    print(f"Welcome to the app, {username}\nWe have {len(TEXTS)} texts to be analyzed.")
    print(oddelovac)

# 4. Vyber textu a overeni
vyber_textu = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print(oddelovac)
if vyber_textu == '' or vyber_textu.isalpha() or int(vyber_textu) > len(TEXTS) or int(vyber_textu) == 0 :
    print(f"You have to select a number within a range! Program will be exited.")
    exit()
else:
  vyber_textu = TEXTS[int(vyber_textu) - 1]
  ocistena_slova = [slovo.strip(".,!?)(\n") for slovo in vyber_textu.split(' ')]
#   for slovo in vyber_textu.split(" "):
#     ocistena_slova.append(slovo.strip(".,!?)(\n"))
# Priprava promenych
  pocet_slov = len(ocistena_slova)
  pocet_slov_titlecase = 0
  pocet_slov_uppercase = 0
  pocet_slov_lowercase = 0
  pocet_slov_numeric = 0
  soucet_cisel = []
# 5. Vypocet statistik
  for slovo in ocistena_slova:
    if slovo.istitle():
      pocet_slov_titlecase += 1 
    elif slovo.isupper():
      pocet_slov_uppercase += 1
    elif slovo.islower():
      pocet_slov_lowercase += 1
    elif slovo.isnumeric():
      pocet_slov_numeric += 1
      for cislo in slovo:
        soucet_cisel.append(int(cislo))

# Vytisknuti statistik    
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {pocet_slov_titlecase} titlecase words.")
print(f"There are {pocet_slov_uppercase} uppercase words.")
print(f"There are {pocet_slov_lowercase} lowercase words.")
print(f"There are {pocet_slov_numeric} numeric strings.")
print(f"The sum of all the numbers {sum(soucet_cisel)}.")
print(oddelovac)

# 6. Graficke znazorneni

print("LEN| OCCURENCIES |NR.")
my_list = []
for i in range(1,len(max(ocistena_slova,key=len))+1):
  for slovo in ocistena_slova:
    if len(slovo) == i:
      my_list.append(slovo)
  print(f"{i}|  {len(my_list) * '*'}| {len(my_list)}")
  my_list.clear()