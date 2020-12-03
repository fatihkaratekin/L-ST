
#Liste veri tipine javadaki diziler mantıgı denebilir.

liste = ["merhaba" , 3 , "sayı" , 17 ,30]
print(liste) #bütün listeyi gösterdik
print(len(liste)) #Listedeki eleman sayısını gösterdik
print(liste[3] , liste[-1]) #indeks numarasıyla sayı çagırmak #-1 sondaki sayıyı çagırır.
liste2 = list("merhaba")
print(liste2) # string bir ifadeyi harflerini böle böle yazdırmak (fonksiyon olarak list)
print(liste[::2]) #ikişer ikişer atlıyarak git
print(liste[: : -1]) #sondan başlayarak yaz
print(liste[2 : : -1]) # sondan başla ama 2.indeksinden sonrasını yaz.


listem = [1,2,3,4,5]
listem2 =[6,7,8,9]
listem3 = listem+listem2
print(listem3)
listem2[2] = 10   #3 degerini degiştirdik
print(listem2)
listem2[:2] = [8,8] #ilk iki satırı degiştirdik
print(listem2)
listem2 = liste2 + ["fatih"]
print(listem2)
#*******************************************************************************
#LİSTEYE EKLEME YAPMAYI .APPEND METODUYLA YAPARIZ

listem.append(66)
listem.append("eklendim")
print(listem)
#LİSTEDEN ÇIKARMA İŞLEMİNİ .POP METODUYLA YAPARIZ AMA İNDEKS NUMARASINI GİRMEMİZ LAZIM.
#HİÇBİR DEĞER GİRMEDEN SİLMEYE ÇALIŞIRSAK EN SONDAKİ ELEMANI SİLER.
listem.pop(5)
print(listem)

#LİSTEYİ KÜÇÜKTEN BÜYÜGE SIRALAMAYI .SORT METODUYLA YAPIYORUZ.
#BÜYÜKTEN KÜÇÜGE YAPMAK İÇİN .SORT(REVERSE(TRUE) DİYORUZ.

sayılar = [5,20,40,35,95,100]
sayılar.sort()
print(sayılar)

sayılar.sort(reverse=True)
print(sayılar)
#*********************************************************

#İÇ İÇE LİSTELER OLUŞTURMAK
içiçeliste = [[1,2,3] ,["fatih" , "esra"] , [8,9,10]]
print(içiçeliste)

print(içiçeliste[0][0]) # 0 indeksindeki 1. listedeki 1.sayısı çagırdık.




