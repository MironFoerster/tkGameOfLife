mit diesem Programm lässt sich "Conway`s Game Of Life" simulieren.

Funktionen:
-über dem Trennstrich liegt das Einstellungsfeld, in dem man die Größe des simulationsfeldes, die Größe der Zellen,
 und die Regeln der Simulation festlegen kann:
	-das Original-Regelwerk ist das (2,3/3)-Regelwerk 
	-empfehlenswert sind (1,2,3,4,5/3) und (1,3,5,7/1,3,5,7)
	(weitere Infos zu den Regelwerken und andere interessante Regelwerke kennt Tante Wiki)
-durch klick auf den "Create New Simulation"-Button wird ein Feld
 mit den eingestellten Eigenschaften, bestehend aus schwarzen Pixeln erstellt;
 nur so werden die Einstellungen übernommen 
 dieser Schritt kann, abhängig von der Feldgröße, einige Sekunden dauern. Es wird ausdrücklich um Geduld gebeten.
-per klick auf die Pixel des Feldes kann man sie an bzw. abschalten
-die restlichen Funktionen sind selbsterklärend

Hinweise:
-das Programm benötigt die Pythonbibliotheken tkinter, numpy und copy
-die Simulation funktioniert nicht über den Rand des Feldes hinaus,
 für ein Unverfälschtes Ergebnis muss für eine größere Simulation auch ein größeres Fenster erstellt werden
-bevor man anfängt, eine Figur aus Pixeln zu zeichnen, sollte man eine laufende Simulation pausieren xD fürLeuteWieMich...

Tipp:
-in(2,3/3), feld(100x100), ca. in der Mitte, delay(20ms):
 000
 0.0
 0.0
 ...
 ...
 0.0
 0.0
 000

(0 für an;.für aus)
...finde ich persönlich sehr schön...
-Wiki kennt übrigens auch andere schöne Startkombinationen


das wäre alles von meiner Seite
viel Spaß beim rumspielen ;)

Miron Förster

PS: Natürlich habe ich dass Programm nicht ohne einige Nachschläge im Internet geschrieben,
    diese alle im Programm zu kennzeichnen wäre irrsinnig,
    es sind jedoch keine Programmabschnitte gecopypasted