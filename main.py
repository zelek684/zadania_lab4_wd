#zadanie 1

liczba = [x*2 for x in range(31)]
plik = open("liczba_z1.txt","w")
for element in liczba:
    plik.write(str(element)+" ")
#plik.writelines(srt(liczba))
plik.close()

#zadanie 2

plik = open("liczba_z1.txt","r")
liczba_2 = plik.readlines()
plik.close()
print(liczba_2)

#zadanie3

with open("tekst.txt",'w') as plik:
    plik.write("1\n")
    plik.write("2\n")
    plik.write("3\n")


#zadanie4
class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        return self.nazwa_produktu,self.ile_produktu(),self.ile_kosztuje()

    def ile_produktu(self):
        return  str(self.ilosc)+ " " + self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed

produkt1 = NaZakupy("Chleb",2,"sztuka",5)
print(produkt1.wyswietl_produkt())


#zadnaie 6

class robaczek:
    def __init__ (self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self,ile_k=1):
        self.y += self.krok*ile_k

    def idz_w_dol(self,ile_k=1):
        self.y -= self.krok*ile_k

    def idz_w_lewo(self,ile_k=1):
        self.x -= self.krok*ile_k

    def idz_w_prawo(self,ile_k=1):
        self.x += self.krok*ile_k

    def gdzie_jestes(self):
        return self.x, self.y

robaczek1 = robaczek(0,0,1)
print (robaczek1.gdzie_jestes())
robaczek1.idz_w_gore(3)
print (robaczek1.gdzie_jestes())
robaczek1.idz_w_prawo(2)
print (robaczek1.gdzie_jestes())





