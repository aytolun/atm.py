#3.soru
#ATM'DEN CEKİLEN PARAYI AYIRMA PROGRAMI
banknot100=0 #oncelikle banknotlarımıza deger atıyoruz
banknot50=0
banknot20=0
banknot10=0
banknot5=0
kalan=0

ucret=int(input("Cekmek istediginiz tutari giriniz: ")) 
#musteriden cekmek istedigi ucreti ogreniyoruz

while True: 
#cekilen miktarı donguye sokup giderek azaltarak en az miktarda banknotu vermesini saglıyoruz
    banknot100=ucret/100
    kalan=ucret%100
#"kalan"degiskeni ile banknottan arta kalan degeri alt katmana atıyoruz
    banknot50=kalan/50
    kalan=kalan%50

    banknot20=kalan/20
    kalan=kalan%20

    banknot10=kalan/10
    kalan=kalan%10

    banknot5=kalan/5
    kalan=kalan%5
    print("{0:.0f} tane 100,\n{1:.0f}tane 50,\n{2:.0f}tane 20,\n{3:.0f}tane 10,\n{4:.0f}tane 5".format(int(banknot100),int(banknot50),int(banknot20),int(banknot10),int(banknot5)))
    #banknotları yazdırdık
    break #donguyu sonlandırdık