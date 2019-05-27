'''
Created on May 26, 2019
@author: Almansour, Mohamad
'''

class Makro:
    '''
    Makro-Klasse: jedes Makro hat 4 Attribute (b: Befehlsname, g: Begrenzer, e: Ersatztext, i: Index des Makros in einem Text).
    '''
    
    def __init__(self, Befhlesname, Begrenzer, Ersatztext, i):
        '''
        Constructor
        '''
        self.b = Befhlesname
        self.g = Begrenzer
        self.e = Ersatztext
        self.i = i
    
    # Methode zum Ueberschreiben:
    @classmethod
    def makro_imp(cls,s,*feld): # s: String (Inhalt des Texts), *feld: Liste von Makro-Objekte.
#         for j in feld:
#             ab Index i in s 
#             if (wort ohne \ am Anfang w == j.b): 
#                 w = j.e
        pass
    
class Makro_Ziffer(Makro):
    '''
    Makro mit Ziffern (zusatzlich gibt es ein Attribut ziffer)
    '''
    def __init__(self, Befhlesname, Begrenzer, Ersatztext, i, Ziffer):
        '''
        Constructor
        '''
        super().__init__(Befhlesname, Begrenzer, Ersatztext, i)
        self.z = Ziffer
