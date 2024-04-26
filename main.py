print("2.kokios valiutos buvo naudotos?-------------------------------------------------------------------------------")

import csv

valiutuSarasas = set()
with open('Naglis.csv', 'r') as f:
    reader = csv.DictReader(f)
    for eilute in reader:
        valiutuSarasas.add(eilute["Valiuta"])

print("Buvo naudotos sios valiutos:", valiutuSarasas)

print("3.kiek income, outcome pagal kiekvieną valiutą?")

import csv

income = {}
outcome = {}

with open('Naglis.csv', 'r') as f:
    reader1 = csv.DictReader(f)
    for eilute1 in reader1:
        valiuta = eilute1["Valiuta"]
        suma = float(eilute1["Suma"])
        dk = eilute1["D/K"]
        if valiuta not in income:
            income[valiuta] = 0.0
            outcome[valiuta] = 0.0
        if dk == "K":
            income[valiuta] += suma
        else:
            outcome[valiuta] += suma

print("Uzdirbta per valiuta:")
for valiuta, gauta in income.items():
    print(f"{valiuta}: {gauta}")

print("\nIsleista per valiuta:")
for valiuta, isleista in outcome.items():
    print(f"{valiuta}: {isleista}")



print("4.kiek buvo išleista kiekvieną mėnesį?--------------------------------------------------------------------------")

import csv

islaidos = {}

with open('Naglis.csv', 'r') as f: #nuskaitom csv faila
    reader2 = csv.DictReader(f)
    for eilute2 in reader2:
        data = eilute2["Data"]  #priskiriam data is csv
        suma = float(eilute2["Suma"])  #priskiriam suma is csv
        dk = eilute2["D/K"] #priskiriam D/K is csv
        valiuta1 = eilute2["Valiuta"] # priskiriam valiutas is csv
        menesiai = data.split("-")[1] # atsifiltrojam tik menesius per bruksniuka , metai - 0, menesiai-1, dienos -2
        if menesiai not in islaidos: # jei tokio menesio nera tada sukuriam nauja rakta
            islaidos[menesiai] = {}
        if valiuta1 not in islaidos[menesiai]: # jei tokios valiutos nera tada priskiriam jai 0.0
            islaidos[menesiai][valiuta1] = 0.0
        if dk == "D": #jei tam menesi yra islaidu "D" tai prideda ta suma
            islaidos[menesiai][valiuta1] += suma

print("Islaidos per menesi:")
for menesiai, valiutos in islaidos.items():
    print(f"{menesiai}:")
    for valiuta, isleista1 in valiutos.items():
        print(f"  {valiuta}: {isleista1}")





print("5.kiek buvo uždirbta kiekvieną mėnesį?--------------------------------------------------------------------------")

import csv

pelnas = {}

with open('Naglis.csv', 'r') as f:
    reader = csv.DictReader(f)
    for eilute in reader:
        data = eilute["Data"]
        suma = float(eilute["Suma"])
        dk = eilute["D/K"]
        valiuta2 = eilute["Valiuta"]
        menesiai = data.split("-")[1]
        if menesiai not in pelnas:
            pelnas[menesiai] = {}
        if valiuta2 not in pelnas[menesiai]:
            pelnas[menesiai][valiuta2] = 0.0
        if dk == "K":
            pelnas[menesiai][valiuta2] += suma

print("Uzdirbta per menesi:")
for menesiai, valiutos in pelnas.items():
    print(f"{menesiai}:")
    for valiuta, uzdirbta in valiutos.items():
        print(f"  {valiuta}: {uzdirbta}")


print("6.koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas)--------")

import csv

balansas = {}

with open('Naglis.csv', 'r') as f:
    reader = csv.DictReader(f)
    for eilute in reader:
        data = eilute["Data"]
        menesiai1 = data.split("-")[1]
        suma = float(eilute["Suma"])
        dk = eilute["D/K"]
        if menesiai1 not in balansas:
            balansas[menesiai1] = 0.0
        if dk == "K":
            balansas[menesiai1] += suma
        else:
            balansas[menesiai1] -= suma

print("Balansas kiekvieno mėnesio gale:")
for menesiai1, menGalas in balansas.items():
    print(f"{menesiai1}: {menGalas}")



print("7.koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00) pagal kiekvieną valiutą?----")


import csv

balansas = {}

with open('Naglis.csv', 'r') as f:
    reader = csv.DictReader(f)
    for eilute in reader:
        data = eilute["Data"]
        menesiai2 = data.split("-")[1]
        suma = float(eilute["Suma"])
        dk = eilute["D/K"]
        valiuta3 = eilute["Valiuta"]
        if menesiai2 not in balansas:
            balansas[menesiai2] = {}
        if valiuta3 not in balansas[menesiai2]:
            balansas[menesiai2][valiuta3] = 0.0
        if dk == "K":
            balansas[menesiai2][valiuta3] += suma
        else:
            balansas[menesiai2][valiuta3] -= suma

print("Balansas kiekvieno mėnesio gale:")
for menesiai2, balansasGale in balansas.items():
    print(f"{menesiai2}:")
    for valiuta, balansas in balansasGale.items():
        print(f"  {valiuta}: {balansas}")


print("8.atvaizduokite per procentinę išraišką pamėnesiui pajamas ir išlaidas procentine išraiška: (žemiau pvz)-------")

import csv

totalPagalMen = {
    "01": {"EUR": {"income": 0, "expenses": 0}, "GBP": {"income": 0, "expenses": 0}},
    "02": {"EUR": {"income": 0, "expenses": 0}, "GBP": {"income": 0, "expenses": 0}},
    "03": {"EUR": {"income": 0, "expenses": 0}, "GBP": {"income": 0, "expenses": 0}},
    "04": {"EUR": {"income": 0, "expenses": 0}, "GBP": {"income": 0, "expenses": 0}}
}

total = {"EUR": {"income": 0, "expenses": 0}, "GBP": {"income": 0, "expenses": 0}}

with open('Naglis.csv', 'r') as f:
    reader = csv.DictReader(f)
    for eilute in reader:
        data = eilute["Data"]
        menesis = data.split("-")[1]
        suma = float(eilute["Suma"])
        dk = eilute["D/K"]
        valiuta = eilute["Valiuta"]
        if dk == "K":
            totalPagalMen[menesis][valiuta]["income"] += suma
            total[valiuta]["income"] += suma
        elif dk == "D":
            totalPagalMen[menesis][valiuta]["expenses"] += suma
            total[valiuta]["expenses"] += suma

for menesis, suma_valiuta in totalPagalMen.items():
    print(f"Pajamos ir islaidos pagal {menesis} menesi:")
    for valiuta, suma in suma_valiuta.items():
        pajamos = suma["income"]
        islaidos = suma["expenses"]
        bendrosPajamos = total[valiuta]["income"]
        bendrosIslaidos = total[valiuta]["expenses"]

        if bendrosPajamos != 0 and bendrosIslaidos != 0:
            print(f"Valiuta: {valiuta}")
            print(f"Pajamas sudaro {(pajamos / bendrosPajamos) * 100:.2f}%")
            print(f"Islaidas sudaro {(islaidos / bendrosIslaidos) * 100:.2f}%")
        else:
            print(f"Valiuta: {valiuta}")
            print("Pajamos sudaro 0% bendros sumos.")




