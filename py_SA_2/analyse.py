import csv

class Analyse:
    '''
    Attribute:
    s: String (Inhalt der TextDatei)
    feld: Liste von Makro-Objekte, die in der Datei sind.
    '''

    def __init__(self, s):
        self.s = s
        self.feld = Analyse.set_feld(self.s)
#         self.feld = feld # und in set_feld append(neues Element)
     
    @classmethod
    def set_feld(cls,s): # Inhalt der Datei (String s) analysieren und feld erstellen. feld = [Makro-Objekte, die in Datei sind]
        # \def\bgeg 
        # b = Befehlname, g = Begrenzer, e = Ersatztext
        x = csv.reader(open(dateiName, "rw"))
        # statt Datei ein String s.
        feld = [[]]
        for zeile in x:
            for wort in zeile:
                if(wort.startswith('\\')):
                    if(wort[:4] =='\def'): # \def\abc?abcA\?B\?Cabc? # oder wort.startwith('\def')
                        s = wort[5:] # abc?abcA\?B\?Cabc?
                        g = s[s.find(s[-1])] # ?
                        e = s[s.find(g)+1:s.rfind(g)] # abcA\?B\?Cabc
                        e = e.replace('\\','') # da Strings sind immutable.
                        b = s[:s.find(g)] # abc             
                        feld.append([b,g,e])
    #                     self.objekte.append([b,g,e])
                        wort = ' '
                    else:
                        w = wort
                        for i in feld: # Mit dieser Schleife wurde jedes Wort, nach dem eine \def... gefunden wurde, pruft, ob es einen Befehlnamen entspricht.
                            if(wort[1:] == feld[i][0]):
                                wort = feld[i][2]    
                        if(w == wort):
                            wort = wort[1:]    
        return feld