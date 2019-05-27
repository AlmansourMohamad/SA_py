# main Datei.py:
import sys
import analyse 
import makro


datei = ''
# Aufrufen: python3 codeDatei.py datei.txt
# sys.argv = ['codeDatei.py', 'datei.txt']
if(len(sys.argv) == 2):
    datei = sys.argv[1] # datei = 'datei.txt'
else:
    print('Bitte nur zwei Argumente nach python3\nprobieren Sie nochmal:') # der Interpreter soll hier abbrechen.

f = open(datei, "r")
s = f.read()
f.close()
print(s) # cd ~/Sommer_Aufgabe_2/; python makro_expandierung.py ein.txt

a = analyse.Analyse(s) # String s (Inhalt der Datei datei.txt) analysieren und ihre Makros in Liste speichern.

for k in a.feld:
    makro.Makro.makro_imp(s,k) # nach dieser Schleife ist schon s geandert und soll in der Datei speichern.

# Inhalt der Datei andern:
f = open(datei, "w")
f.write(s)
f.close()