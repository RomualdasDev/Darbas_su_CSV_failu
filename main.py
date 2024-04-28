import functions as fun

file_name = 'Naglis.csv'
income, outcome, islaidos, pajamos, balansas, balansasValiutomis = fun.transakcijos(file_name)

print("2.kokios valiutos buvo naudotos?-------------------------------------------------------------------------------")
def main():
    currency = fun.skaitytiValiutas(file_name)
    print("Buvo naudotos sios valiutos:", currency)

if __name__ == "__main__":
    main()



print("3.kiek income, outcome pagal kiekvieną valiutą?")

def income_outcome(file_name):
    Valiutos = set(income.keys()).union(set(outcome.keys()))
    for currency in Valiutos:
        pelnas = income.get(currency, 0.0)
        islaidos = outcome.get(currency, 0.0)
        print(f"{currency}: Uzdirbta: {pelnas}, Isleista: {islaidos}")

if __name__ == "__main__":
    income_outcome(file_name)



print("4.kiek buvo išleista kiekvieną mėnesį?--------------------------------------------------------------------------")

def islaidosPerMen(file_name):
    for menesis, islaideles in islaidos.items():
        bendrosIslaidos = sum(islaideles.values())
        print(f"{menesis} : {bendrosIslaidos}")

if __name__ == "__main__":
    islaidosPerMen(file_name)



print("5.kiek buvo uždirbta kiekvieną mėnesį?--------------------------------------------------------------------------")

def UzdarbisPerMen(file_name):
    for menesis, uzdarbis in pajamos.items():
        bendrosPajamos = sum(uzdarbis.values())
        print(f"{menesis} : {bendrosPajamos}")

if __name__ == "__main__":
    UzdarbisPerMen(file_name)


print("6.koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas)--------")

def MenesioBalansas(file_name):
    Pradinis = 0.0
    for menesis in sorted(balansas.keys()):
        galutinis = Pradinis + balansas[menesis]
        print(f"{menesis} : {galutinis}")
        Pradinis = galutinis

if __name__ == "__main__":
    MenesioBalansas(file_name)



print("7.koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00) pagal kiekvieną valiutą?----")

def BalansasPagalValiuta(file_name):
    for menesis in sorted(balansas.keys()):
        print(f"{menesis}:")
        for valiuta, likutis in balansasValiutomis[menesis].items():
            print(f"  {valiuta}: {likutis}")

if __name__ == "__main__":
    BalansasPagalValiuta(file_name)




print("8.atvaizduokite per procentinę išraišką pamėnesiui pajamas ir išlaidas procentine išraiška: (žemiau pvz)-------")

from functions import procentuSkaiciavimas
def Procentai(procentas):
    for menesis, valiutos in procentas.items():
        for valiuta, procentas in valiutos.items():
            pajamuProc = procentas["Pajamos"]
            islaiduProc = procentas["Islaidos"]
            print(f"Valiuta: {valiuta}")
            print(f"Pajamas sudaro {pajamuProc:.2f}%")
            print(f"Islaidas sudaro {islaiduProc:.2f}%")

if __name__ == "__main__":
    procentas = procentuSkaiciavimas(file_name)
    Procentai(procentas)


