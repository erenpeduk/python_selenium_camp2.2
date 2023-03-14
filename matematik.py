class Matematik:
    def __init__(self):
        print("Matematik başladı(referansı oluştu)")
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2
    
matematik = Matematik()
sonuc = matematik.topla(3,5)
print(f"Sonuç: {sonuc}")



        
        
