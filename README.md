# WordPress Átméretezett Képek Tisztító

Ez a Python szkript segít megtisztítani a WordPress által automatikusan generált átméretezett képeket.

## Funkciók

- Bejárja a megadott könyvtár összes alkönyvtárát
- Azonosítja a WordPress által generált átméretezett képeket a fájlnév alapján
- Megtartja az eredeti képeket és a `-scaled` végződésű verziókat
- Szimuláció módban előzetesen megmutatja, mely fájlokat törölné
- Részletes jelentést ad a felszabadított tárhelyről

## Telepítés

```bash
git clone https://github.com/felhasznalónév/wordpress-keptisztito.git
cd wordpress-keptisztito
```

## Használat

```bash
# Szimuláció mód - csak kilistázza a törlendő fájlokat, de nem törli őket
python wordpress-tisztito.py /elérési/út/a/wordpress/mappához

# Tényleges törlés végrehajtása
python wordpress-tisztito.py /elérési/út/a/wordpress/mappához --execute
```

### Paraméterek

- `directory`: A kezdő könyvtár elérési útja (kötelező)
- `--execute`: Ténylegesen törli a fájlokat (alapértelmezetten csak szimuláció)

## Példa kimenetek

### Szimuláció mód
```
SZIMULÁCIÓ MÓD: A fájlok nem lesznek törölve. Használd a --execute paramétert a tényleges törléshez.

Könyvtár ellenőrzése: /var/www/html/wp-content/uploads/2022
Törlésre jelölve: /var/www/html/wp-content/uploads/2022/05/pelda-kep-150x150.jpg (15.20 KB)
Törlésre jelölve: /var/www/html/wp-content/uploads/2022/05/pelda-kep-300x200.jpg (25.60 KB)
...

Szimuláció befejeződött. 156 fájl lenne törölve, összesen 12.25 MB helyet szabadítana fel.
```

### Végrehajtási mód
```
VÉGREHAJTÁS MÓD: A fájlok ténylegesen törlésre kerülnek!

Könyvtár ellenőrzése: /var/www/html/wp-content/uploads/2022
Törölve: /var/www/html/wp-content/uploads/2022/05/pelda-kep-150x150.jpg (15.20 KB)
Törölve: /var/www/html/wp-content/uploads/2022/05/pelda-kep-300x200.jpg (25.60 KB)
...

Tisztítás befejeződött. 156 fájl törölve, összesen 12.25 MB hely felszabadítva.
```

## Biztonsági óvintézkedések

- **Mindig készíts biztonsági mentést a futtatás előtt!**
- Először szimuláció módban futtasd a szkriptet a törlendő fájlok ellenőrzéséhez
- Ha nagy mennyiségű fájlt törölsz egy közvetlenül elérhető éles weboldal mappájából, a folyamat idejére fontold meg a webszerver ideiglenes leállítását vagy a weboldal karbantartási módba helyezését

## Rendszerkövetelmények

- Python 3.6 vagy újabb verzió
- Nem igényel külső függőségeket

## Licenc

Ez a projekt [GNU General Public License v3.0](LICENSE) alatt áll.
