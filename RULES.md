# Jass-Regeln (Schieber)

Diese Datei ist die **verbindliche Spezifikation** der Regeln. Claude Code und alle
Tests richten sich danach. Wo etwas fehlt oder unklar ist, wird gefragt, nicht geraten.

## 1. Spieler und Teams

- 4 Spieler, 2 Teams. Partner sitzen sich gegenüber.
- Gespielt wird im Gegenuhrzeigersinn.
- Erste Runde: Wer nach dem Verteilen die Rosen 7 (französisch: Herz 7) hat,
  ist Vorhand. Der Spieler links von ihm gilt als Geber.
- Ab der zweiten Runde wechselt der Geber nach jeder Runde einen Platz im
  Gegenuhrzeigersinn. Vorhand ist immer der Spieler rechts vom Geber.
- Vorhand sagt Trumpf an oder schiebt und spielt den ersten Stich aus.

## 2. Karten

36 Karten in 4 Farben mit je 9 Karten.

| Deutschschweizer Karten | Französische Karten |
| --- | --- |
| Eicheln | Ecken ♦ |
| Rosen | Herz ♥ |
| Schellen | Kreuz ♣ |
| Schilten | Schaufeln ♠ |

| Deutschschweizer Karten | Französische Karten |
| --- | --- |
| Ass | Ass |
| König | König |
| Ober | Dame |
| Under | Bube |
| Banner | 10 |
| 9,8,7,6 | 9,8,7,6 |


## 3. Ablauf einer Runde

1. Karten mischen und je 9 Karten verteilen.
2. Vorhand bestimmt Trumpf
3. Der Ansager wählt einen Trumpf oder **schiebt** zum Partner, der dann wählen muss.
   - Zurückschieben standard mässig nicht erlaubt. Soll in den Einstellungen konfigurierbar sein.
4. Vorhand beginnt mit dem ersten Stich
5. 9 Stiche werden gespielt, danach wird gezählt.

## 4. Trumpfarten

- Eine der vier Farben als Trumpf
- **Obenabe:** kein Trumpf, die höchste Karte der ausgespielten Farbe gewinnt
- **Undenufe:** kein Trumpf, die tiefste Karte der ausgespielten Farbe gewinnt
- Weitere Arten (z.B. Slalom) vorerst nicht.

## 5. Reihenfolge der Trumpfkarten

Von hoch nach tief: Under (Puur), Nell (9), Ass, König, Ober, Banner, 8, 7, 6

## 6. Spielregeln im Stich

- **Farbe angeben:** Wer die ausgespielte Farbe hat, muss sie spielen.
  - Ausnahme: Man darf jederzeit Trumpf spielen, auch wenn man Farbe hätte.
- **Under-Regel:** Wird Trumpf ausgespielt und man hat als einzigen Trumpf den Under,
  muss man ihn nicht spielen.
- **Untertrumpfen:** Wurde eine Nicht-Trumpffarbe ausgespielt und liegt bereits
  ein Trumpf im Stich, darf kein tieferer Trumpf gespielt werden.
  Einzige Ausnahme: Man hat nur noch Trumpfkarten auf der Hand und alle sind tiefer.
  Wurde Trumpf ausgespielt, gilt diese Regel nicht (normales Farbe angeben).
- **Stich gewinnen:** Der höchste Trumpf gewinnt. Ohne Trumpf im Stich gewinnt die
  höchste Karte der ausgespielten Farbe (bei Undenufe die tiefste).
- Wer den Stich gewinnt, spielt den nächsten aus.

## 7. Kartenwerte (Punkte)

| Karte | Trumpffarbe | Andere Farbe | Obenabe | Undenufe |
| --- | --- | --- | --- | --- |
| Ass | 11 | 11 | 11 | 0 |
| König | 4 | 4 | 4 | 4 |
| Ober | 3 | 3 | 3 | 3 |
| Under | 20 | 2 | 2 | 2 |
| Banner (10) | 10 | 10 | 10 | 10 |
| 9 | 14 | 0 | 0 | 0 |
| 8 | 0 | 0 | 8 | 8 |
| 7 | 0 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 11 |

- Letzter Stich: 5 Punkte
- Match (alle 9 Stiche): 100 Bonuspunkte, also 257 statt 157
- Summe pro Runde: 157 Punkte (152 Karten + 5 letzter Stich)

## 8. Einstellungen pro Spielraum

| Einstellung | Optionen | Standard |
| --- | --- | --- |
| Kartenbild | deutsch, französisch | deutsch |
| Trumpf-Faktoren | an, aus | aus |
| Zielpunktzahl | frei wählbar | 1000 |


- Werden die Faktoren eingeschaltet, wird als Zielpunktzahl 2500 vorgeschlagen
    (änderbar). Ohne Faktoren ist der Vorschlag 1000.

Faktoren, wenn eingeschaltet:

| Trumpfart | Faktor |
| --- | --- |
| Eicheln, Rosen (französisch: Ecken, Herz) | ×1 |
| Schellen, Schilten (französisch: Kreuz, Schaufeln) | ×2 |
| Obenabe, Undenufe | x3 |

## 9. Spielende

- Die Punkte werden nach jedem Stich gezählt, inklusive Faktor.
- Das Spiel endet sofort, wenn ein Team die Zielpunktzahl erreicht,
  auch mitten in der Runde. Dieses Team gewinnt.
- Kein manuelles Bedanken: Das Programm erkennt das Spielende automatisch.
- Da pro Stich nur ein Team Punkte bekommt, können im MVP nicht beide Teams
  gleichzeitig die Zielpunktzahl erreichen.
- Später, mit Weis und Stöck, gilt die Ausmachregel: Stöck, Wys, Stich.

## 10. Später (nicht im MVP)

- Weis (Drei-, Vier-, Fünfblatt, Vier Gleiche …)
- Stöck (König und Ober im Trumpf)
- Weitere Varianten wie Differenzler oder Coiffeur

## 11. Beispiele

Konkrete Situationen, die zu Tests werden. Format: Trumpf, gespielte Karten der Reihe
nach, erwarteter Gewinner des Stichs.

1. Trumpf Rosen. Gespielt: Eicheln Ass, Eicheln König, Rosen 6, Eicheln 9.
   Gewinner: Rosen 6 (Trumpf schlägt Farbe).
2. Obenabe. Gespielt: Schellen 8, Schellen Ass, Rosen Ass, Schellen 10.
   Gewinner: Schellen Ass (Rosen ist nicht die ausgespielte Farbe).
3. Trumpf Rosen. Ausgespielt: Eicheln Ass. Zweiter Spieler sticht mit Rosen König.
   Dritter Spieler hat Schellen 6 und Rosen 8, aber keine Eicheln.
   Erlaubt: Schellen 6. Nicht erlaubt: Rosen 8 (Untertrumpfen).
4. Wie Beispiel 4, aber der dritte Spieler hat nur noch Rosen 8 und Rosen 6.
   Erlaubt: beide Karten (nur noch Trümpfe, Untertrumpfen ist Pflicht).
5. Trumpf Rosen. Ausgespielt: Rosen König. Zweiter Spieler hat Rosen 6.
   Erlaubt: Rosen 6 (Trumpf wurde ausgespielt, kein Untertrumpfen).
