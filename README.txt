SECURE MESSENGER - IDIOTENSICHERE ANLEITUNG
=========================================

WAS IST DAS?
------------
Dieses Programm ist ein einfacher verschlüsselter Messenger.
Zwei oder mehrere Personen können über das Netzwerk miteinander chatten.
Die Nachrichten werden mithilfe eines gemeinsamen Schlüssels verschlüsselt.

WAS BRAUCHE ICH?
----------------
1. Python 3 installiert
2. Die Dateien:
   - messenger.py
   - requirements.txt
3. Eine Eingabeaufforderung (CMD, PowerShell oder Terminal)

SCHRITT 1: DATEIEN IN EINEN ORDNER LEGEN
----------------------------------------
Erstelle einen Ordner, zum Beispiel:

C:\Messenger

Lege dort messenger.py und requirements.txt hinein.

SCHRITT 2: TERMINAL ÖFFNEN
--------------------------
Windows:
- Im Ordner mit gedrückter Umschalttaste rechts klicken
- 'PowerShell hier öffnen' auswählen

SCHRITT 3: BENÖTIGTE PAKETE INSTALLIEREN
----------------------------------------
Befehl eingeben:

pip install -r requirements.txt

Warten bis die Installation abgeschlossen ist.

SCHRITT 4: SCHLÜSSEL ERZEUGEN
-----------------------------
Auf EINEM Computer:

python messenger.py --generate-key

Es wird eine Datei namens:

secret.key

erstellt.

WICHTIG:
Die Datei secret.key muss an alle Teilnehmer verteilt werden.
Alle Teilnehmer benötigen DIESELBE Datei.

SCHRITT 5: SERVER STARTEN
-------------------------
Auf dem Computer, der den Chat bereitstellt:

python messenger.py --server --host 0.0.0.0 --port 5555

Wenn alles funktioniert, erscheint eine Meldung ähnlich zu:

[+] Server gestartet
[+] Lauscht auf 0.0.0.0:5555

SCHRITT 6: IP-ADRESSE HERAUSFINDEN
----------------------------------
Auf dem Server-PC:

Windows:

ipconfig

Suche nach einer Adresse wie:

192.168.1.100

Diese Adresse benötigen die anderen Teilnehmer.

SCHRITT 7: CLIENT STARTEN
-------------------------
Auf dem zweiten Computer:

python messenger.py --client --host 192.168.1.100 --port 5555 --username Max

Ersetze:
- 192.168.1.100 durch die echte Server-IP
- Max durch deinen Namen

BEISPIEL
---------
Computer 1:

python messenger.py --server --host 0.0.0.0 --port 5555

Computer 2:

python messenger.py --client --host 192.168.1.100 --port 5555 --username Finn

Computer 3:

python messenger.py --client --host 192.168.1.100 --port 5555 --username Lisa

CHATTEN
--------
Nach dem Verbinden einfach Nachrichten eingeben:

Finn > Hallo

Lisa erhält:

Finn: Hallo

FEHLERBEHEBUNG
--------------
Fehler: 'python wird nicht erkannt'
Lösung:
- Python installieren
- Python zum PATH hinzufügen

Fehler: 'No module named cryptography'
Lösung:

pip install -r requirements.txt

Fehler: Verbindung nicht möglich
Lösung:
- Prüfen ob der Server läuft
- Prüfen ob die richtige IP verwendet wird
- Firewall überprüfen
- Prüfen ob alle dieselbe secret.key verwenden

SICHERHEITSHINWEIS
------------------
Dieses Projekt ist ein Lernprojekt.
Es ist nicht mit professionellen Messengern wie Signal, Matrix oder WhatsApp vergleichbar.
Für produktive Nutzung wären zusätzliche Sicherheitsfunktionen erforderlich.

DATEIEN
--------
messenger.py      = Hauptprogramm
requirements.txt  = Benötigte Bibliotheken
secret.key        = Verschlüsselungsschlüssel
README.txt        = Diese Anleitung
