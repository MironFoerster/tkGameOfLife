mit diesem Programm l�sst sich "Conway`s Game Of Life" simulieren.

Funktionen:
-�ber dem Trennstrich liegt das Einstellungsfeld, in dem man die Gr��e des simulationsfeldes, die Gr��e der Zellen,
 und die Regeln der Simulation festlegen kann:
	-das Original-Regelwerk ist das (2,3/3)-Regelwerk 
	-empfehlenswert sind (1,2,3,4,5/3) und (1,3,5,7/1,3,5,7)
	(weitere Infos zu den Regelwerken und andere interessante Regelwerke kennt Tante Wiki)
-durch klick auf den "Create New Simulation"-Button wird ein Feld
 mit den eingestellten Eigenschaften, bestehend aus schwarzen Pixeln erstellt;
 nur so werden die Einstellungen �bernommen 
 dieser Schritt kann, abh�ngig von der Feldgr��e, einige Sekunden dauern. Es wird ausdr�cklich um Geduld gebeten.
-per klick auf die Pixel des Feldes kann man sie an bzw. abschalten
-die restlichen Funktionen sind selbsterkl�rend

Hinweise:
-das Programm ben�tigt die Pythonbibliotheken tkinter, numpy und copy
-die Simulation funktioniert nicht �ber den Rand des Feldes hinaus,
 f�r ein Unverf�lschtes Ergebnis muss f�r eine gr��ere Simulation auch ein gr��eres Fenster erstellt werden
-bevor man anf�ngt, eine Figur aus Pixeln zu zeichnen, sollte man eine laufende Simulation pausieren xD f�rLeuteWieMich...

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

(0 f�r an;.f�r aus)
...finde ich pers�nlich sehr sch�n...
-Wiki kennt �brigens auch andere sch�ne Startkombinationen


das w�re alles von meiner Seite
viel Spa� beim rumspielen ;)

Miron F�rster

PS: Nat�rlich habe ich dass Programm nicht ohne einige Nachschl�ge im Internet geschrieben,
    diese alle im Programm zu kennzeichnen w�re irrsinnig,
    es sind jedoch keine Programmabschnitte gecopypasted