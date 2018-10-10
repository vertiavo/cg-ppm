# cg-ppm

Format pliku PPM. Zaimplementować funkcję wczytującą oraz wyświetlającą pliki graficzne
w formacie PPM P6 oraz P3. Należy zwrócić uwagę na obsługę błędów (np. uszkodzonych plików) oraz
wydajność algorytmu wczytującego (blokowo zamiast bajt po bajcie). Użytkownik powinien mieć możliwość
dodatkowo wczytania i zapisania pliku JPEG.

## Cele

* Wczytywanie i wyświetlanie plików graficznych w formacie PPM P3,
* Wczytywanie i wyświetlanie plików graficznych w formacie PPM P6,
* Obsługa błędów (komunikaty w przypadku nieobsługiwanego formatu pliku oraz błędów w obsługiwanych formatach plików),
* Wydajny sposób wczytywania plików (blokowy zamiast bajt po bajcie),
* Wczytywanie plików JPEG,
* Zapisywanie wczytanego pliku w formacie JPEG,
* Możliwość wyboru stopnia kompresji przy zapisie do JPEG,
* Skalowanie liniowe kolorów,
* Proszę nie używać gotowych bibliotek do wczytywania plików PPM.