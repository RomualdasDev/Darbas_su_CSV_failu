#funkcija 2 uzduociai

import csv

def skaitytiValiutas(file_name):
    valiutuSarasas = set()  #sukuriam tuscia kintamaji valiutom saugoti

    with open(file_name, 'r', newline='', encoding='utf-8') as f:  #nuskaitome csv faila
        reader = csv.DictReader(f)
        for eilute in reader:  #paleidziam cikla patikrinti ar yra stulpelis valiuta ir is jo ims reiksme
            if 'Valiuta' in eilute:
                valiuta = eilute['Valiuta']
                valiutuSarasas.add(valiuta) #pridedame valiuta i tuscia kintamaji
    return valiutuSarasas #graziname gautas reiksmes



# funkcija 3-7 uzduociai

def transakcijos(file_name):
    income = {}   #susikuriam tuscius kintamosius reikiamom reiksmem saugoti
    outcome = {}
    islaidos = {}
    pajamos = {}
    balansas = {}
    balansasValiutomis = {}
    ProcBendras = {}

    with open(file_name, 'r') as f: #nuskaitome csv faila
        reader = csv.DictReader(f)
        for row in reader:
            valiuta = row["Valiuta"] #priskiriame valiuta is csv failo
            suma = float(row["Suma"]) # priskiriame sumas is csv failo
            dk = row["D/K"] #priskiriame pajamas ir islaidas is csv failo
            data = row["Data"] #priskiriame data
            menesis = data.split("-")[1] #naudojant split is datos atsiskyriame menesi per bruksneli. Metai[0], menuo[1], diena[2]

            if valiuta not in income: #ieskome pajamu ir islaidu pagal valiuta
                income[valiuta] = 0.0
                outcome[valiuta] = 0.0
            if dk == "K":
                income[valiuta] += suma
            else:
                outcome[valiuta] += suma

            if menesis not in islaidos: #ieskome pajamu ir islaidu pagal valiuta ir menesi
                islaidos[menesis] = {}
                pajamos[menesis] = {}
                balansas[menesis] = 0.0
                balansasValiutomis[menesis] = {}
            if valiuta not in islaidos[menesis]:
                islaidos[menesis][valiuta] = 0.0
                pajamos[menesis][valiuta] = 0.0
                balansasValiutomis[menesis][valiuta] = 0.0
            if dk == "D":
                islaidos[menesis][valiuta] += suma
            else:
                pajamos[menesis][valiuta] += suma

            if dk == "K":  # skaiciuojame balansa pagal menesi
                balansas[menesis] += suma
            else:
                balansas[menesis] -= suma

            if dk == "K":   # skaiciuojame balansa pagal menesi ir valiuta
                balansasValiutomis[menesis][valiuta] += suma
            else:
                balansasValiutomis[menesis][valiuta] -= suma


    return income, outcome, islaidos, pajamos, balansas, balansasValiutomis

# funkcija 8 uzduociai

def procentuSkaiciavimas(file_name):
    totalPagalMen = { #sukuriami tusti kintamieji reikalingiems rodykliams saugoti
        "01": {"EUR": {"income": 0, "expenses": 0}, "GBP": {"income": 0, "expenses": 0}},
        "02": {"EUR": {"income": 0, "expenses": 0}, "GBP": {"income": 0, "expenses": 0}},
        "03": {"EUR": {"income": 0, "expenses": 0}, "GBP": {"income": 0, "expenses": 0}},
        "04": {"EUR": {"income": 0, "expenses": 0}, "GBP": {"income": 0, "expenses": 0}}
    }

    total = {"EUR": {"income": 0, "expenses": 0}, "GBP": {"income": 0, "expenses": 0}}

    with open('Naglis.csv', 'r') as f: #nuskaitome csv faila
        reader = csv.DictReader(f)
        for eilute in reader:
            data = eilute["Data"] #priskiriame data is csv failo
            menesis = data.split("-")[1] #naudojant split is datos atsiskyriame menesi per bruksneli. Metai[0], menuo[1], diena[2]
            suma = float(eilute["Suma"]) #priskiriama suma is csv failo
            dk = eilute["D/K"] #priskiriame pajamas ir islaidas is csv failo
            valiuta = eilute["Valiuta"] #priskiriame valiuta is csv failo
            if dk == "K": #suskaiciuojama bendra iplauku suma
                totalPagalMen[menesis][valiuta]["income"] += suma
                total[valiuta]["income"] += suma
            elif dk == "D": #suskaiciuojame bendra islaidu suma
                totalPagalMen[menesis][valiuta]["expenses"] += suma
                total[valiuta]["expenses"] += suma

    procentai = {} #sukuriam tuscia kintamaji procentams saugoti

    for menesis, valiutosSuma in totalPagalMen.items(): #skaiciuojame procentalia israiska kiekvienam menesiui nuo bendros sumos
        procentai[menesis] = {}
        for valiuta, suma in valiutosSuma.items():
            pajamos = suma["income"]
            islaidos = suma["expenses"]
            bendrosPajamos = total[valiuta]["income"]
            bendrosIslaidos = total[valiuta]["expenses"]

            if bendrosPajamos != 0 and bendrosIslaidos != 0:
                pajamuProc = (pajamos / bendrosPajamos) * 100
                islaiduProc = (islaidos / bendrosIslaidos) * 100
            else:
                pajamuProc = 0.0
                islaiduProc = 0.0

            procentai[menesis][valiuta] = {
                "Pajamos": pajamuProc,
                "Islaidos": islaiduProc
            }

    return procentai


# kaip veikia items is W3schools

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.items()
#
# print(x) is cia gauname dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


