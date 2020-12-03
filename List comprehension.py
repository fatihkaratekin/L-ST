#Listeyi başka bir listeye eklemek için
#ilk yöntem
liste1  = [1,2,3,4,5]
liste2 = list()

for i in liste1:
    liste2.append(i)
print(liste2)

#İkinci yöntem

liste3 = [1,2,3,4,5]
liste4 = [i for i in  liste3]
print(liste4)
#İKİYLE YADA BAŞKA BİR SAYIYLA ÇARPARAK BAŞKA BİR LİSTEYE EKLEMEK İÇİNSE



liste5 = [2,3,4,5]
liste6 = [i * 2 for i in liste5]
print(liste6)

#for içinde for ile içiçe listeyi başka bir listeye düz olarak aktarma

Alistesi = [[1,2,3],[4,5,6],[7,8,9]]
Blistesi = list() #boş liste demek

for i in Alistesi :
    for x in i :
     Blistesi.append(x)

print(Blistesi)