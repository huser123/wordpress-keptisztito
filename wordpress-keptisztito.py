#!/usr/bin/env python3
import os
import re
import argparse

def is_resized_image(filename):
    """
    Ellenőrzi, hogy a fájl átméretezett kép-e.
    
    A WordPress általános átméretezett fájl mintái:
    - filename-100x100.jpg
    - filename-300x169.jpg
    - filename-150x150.jpg
    - filename-768x432.jpg
    - filename-1024x576.jpg
    
    A -scaled végződésű fájlokat megtartjuk.
    """
    # Regex minta a méretezett fájlokra
    pattern = r'.*-\d+x\d+\.(jpg|jpeg|png|gif|webp)$'
    
    # Ha illeszkedik a mintára és nem -scaled végződésű
    return bool(re.match(pattern, filename, re.IGNORECASE)) and not filename.lower().endswith('-scaled.jpg') and not filename.lower().endswith('-scaled.jpeg') and not filename.lower().endswith('-scaled.png') and not filename.lower().endswith('-scaled.gif') and not filename.lower().endswith('-scaled.webp')

def clean_resized_images(directory, dry_run=True):
    """
    Bejárja a megadott könyvtárat és törli az átméretezett képeket.
    
    Args:
        directory (str): A kezdő könyvtár elérési útja
        dry_run (bool): Ha True, csak kilistázza a törlendő fájlokat, de nem törli őket
    """
    deleted_count = 0
    deleted_size = 0
    
    # Csak a közvetlen alkönyvtárakat járjuk be
    for root_dir in [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]:
        print(f"Könyvtár ellenőrzése: {root_dir}")
        
        # Bejárjuk a könyvtárat és alkönyvtárait
        for root, dirs, files in os.walk(root_dir):
            for filename in files:
                if is_resized_image(filename):
                    file_path = os.path.join(root, filename)
                    file_size = os.path.getsize(file_path)
                    
                    if dry_run:
                        print(f"Törlésre jelölve: {file_path} ({file_size / 1024:.2f} KB)")
                    else:
                        try:
                            os.remove(file_path)
                            print(f"Törölve: {file_path} ({file_size / 1024:.2f} KB)")
                            deleted_count += 1
                            deleted_size += file_size
                        except Exception as e:
                            print(f"Hiba a fájl törlésekor {file_path}: {e}")
    
    if dry_run:
        print(f"\nSzimuláció befejeződött. {deleted_count} fájl lenne törölve, összesen {deleted_size / (1024*1024):.2f} MB helyet szabadítana fel.")
    else:
        print(f"\nTisztítás befejeződött. {deleted_count} fájl törölve, összesen {deleted_size / (1024*1024):.2f} MB hely felszabadítva.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='WordPress átméretezett képek törlése')
    parser.add_argument('directory', help='A kezdő könyvtár elérési útja')
    parser.add_argument('--execute', action='store_true', help='Ténylegesen töröljük a fájlokat (alapértelmezetten csak szimuláció)')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.directory):
        print(f"Hiba: A megadott elérési út '{args.directory}' nem létezik vagy nem könyvtár.")
        exit(1)
    
    dry_run = not args.execute
    
    if dry_run:
        print("SZIMULÁCIÓ MÓD: A fájlok nem lesznek törölve. Használd a --execute paramétert a tényleges törléshez.\n")
    else:
        print("VÉGREHAJTÁS MÓD: A fájlok ténylegesen törlésre kerülnek!\n")
    
    clean_resized_images(args.directory, dry_run=dry_run)
