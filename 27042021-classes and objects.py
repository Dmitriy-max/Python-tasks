class instrumenty_dlya_risovaniya:
    def _poisk (self):
        print('Где кисточка?')
    pass
class kraski(instrumenty_dlya_risovaniya):
    def ya_kraski(self):
        print('Я краска!')
    pass
class kistochka(instrumenty_dlya_risovaniya ):
    def krasota (self):
        print("Я, красивая кисточка.")
    pass
obj1 = kistochka()
obj1._poisk()
obj1.krasota()
obj2 = kraski()
obj2.ya_kraski()
