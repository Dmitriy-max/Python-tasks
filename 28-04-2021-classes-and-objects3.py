class instrumenty_dlya_risovaniya:
    def kto_roditel(self):
        print('Родитель:инструменты для рисования!')
    pass

class kraski(instrumenty_dlya_risovaniya):
    pass

class kistochki(instrumenty_dlya_risovaniya):
    def  __init__ (self, price):
        self.my_price = price
    def read_price(self):
        print('Моя цена: %s  грн.' % self.my_price )
    def wright_price(self, new_price):
        self.my_price = new_price
    def kto_ya(self):
        print("Я, кисточка!")

obj1=kistochki(100)
obj1.read_price()
obj1.wright_price(200)
obj1.read_price()

obj2=kistochki(300)
obj2.read_price()

obj3=kistochki(400)
obj3.read_price()

obj3.kto_ya()



