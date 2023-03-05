# Ping

## 🇩🇪 Deutsch

In letzter Zeit verliere ich wieder öfters die Verbindung zum Internet. Meistens genau dann, wenn ich es eigentlich 
gerade brauche - man kennt es. Mit diesem Python Script möchte ich das Ganze aufzeichnen. Ich habe bestimmt irgendwas
im Script vergessen zu beachten, aber dafür ist es ja öffentlich. 

Ich werde dieses Script auf meinem Raspberry Pi Zero W alle 5 Minuten über einen Cronjob laufen lassen. Am Start des
Scripts wird überprüft, ob überhaupt eine Verbindung zur FritzBox besteht. Sollte das nicht der Fall sein, wird nach 10
Sekunden erneut versucht, das Internet zu überprüfen. Immerhin will ich keine falschen Meldungen erzeugen, nur weil
das WLAN gerade nicht will :)


### Erklärung der Dateien

#### `fails.csv`

In dieser Datei stehen die verschiedenen IP Adressen von DNS Servern, welche genutzt werden, um zu überprüfen, ob
wirklich keine Verbindung zum Internet besteht. Es werden mehrere Server getestet, da diese auch einmal ausfallen 
können. Des Weiteren findet man die Zeit, zu welcher die bestimmte IP Adresse getestet wurde und der Vermerk, ob es nun
eine Verbindung aufbauen konnte oder nicht.


#### `log.txt`

Hierin befinden sich genauere Ergebnisse der einzelnen Verbindungstests. Dazu zählt, welche Seite angepingt wurde, die 
durchschnittliche Antwortzeit, die zurück erhaltenen Pakete und der Verweis, ob eine Verbindung zum Internet möglich
war oder nicht. Jede Meldung ist mit einem Zeitstempel versehen.


#### `stats.json`

In dieser Datei findet man fünf Werte.

- `total_failed`: Wie viele Tests waren bisher fehlgeschlagen?
- `total_success`: Wie viele Tests waren bisher erfolgreich?
- `total_tests`: Wie viele Tests wurden bisher durchgeführt?
- `last_failed`: Zu welcher Uhrzeit wurde zuletzt ein Ausfall aufgezeichnet?
- `all_failed_times`: Eine Liste aller Daten und Uhrzeiten, zu welcher keine Verbindung zum Internet möglich war.


## 🇬🇧 English

Recently, I've been losing my internet connection more often again. Usually exactly when I need it - you know how it is.
With this Python script, I want to record all of this. I'm sure I forgot to consider something in the script, but that's
why it's public.

I will run this script on my Raspberry Pi Zero W every 5 minutes using a cron job. At the start of the script, it checks
whether there is a connection to the FritzBox at all. If not, it will try to check the internet again after 10 seconds. 
After all, I don't want to create false reports just because the Wi-Fi is not cooperating :)


### Explanation of Files

#### `fails.csv`

This file contains various IP addresses of DNS servers used to verify whether there is actually no internet connection.
Multiple servers are tested because they can also go down. Additionally, it records the time at which each IP address 
was tested and whether it was able to establish a connection or not.


#### `log.txt`

This file contains more detailed results of each connection test, including the site that was pinged, the average 
response time, the number of packets received, and whether a connection to the internet was possible or not. Each 
message is timestamped.


#### `stats.json`

This file contains five values:

`total_failed`: How many tests have failed so far?
`total_success`: How many tests have been successful so far?
`total_tests`: How many tests have been performed so far?
`last_failed`: What time was the last outage recorded?
`all_failed_times`: A list of all dates and times when a connection to the internet was not possible.
