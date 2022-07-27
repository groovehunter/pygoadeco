#!/usr/bin/python3 

print("hello world!")

# Import math damit später sinus geht und auch pi lol
import math

spalte_value = "{:>3}"       # Platzhalter rechtsbündig für Farbwert
spalte_graphic = "{:<27}"    # Platzhalter linksbündig für Darstellung mit Zeichen
spalte_rgb = "{:>8}"            # Platzhalter 8 Stellen rechtsbündig

# class. Rauskopiert wo, RED, GREEN, BLUE und RGB dazugebastelt
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[96m'

    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'

def int2hex(i):
    """ Umwandlung R/G/B in zweistellig hex als str, einstellig mit Führungsnull """
    i_hex = hex(i).lstrip('0x').zfill(2)  # 0x links weg-strippen und fill laenge 2 
    return i_hex

def out(zahl_1, phasendiff, letter):
    sinus = math.sin((zahl_1) + math.degrees(phasendiff)) 
    sinus_color = int((sinus + 1) * 127.5)   # Wertebereich 0 ... 255 für Farbcode
    sinus_graphic = sinus * 12 + 13          # Wertebereich für Darstellung mit Zeichen
    sinus_str = (int(sinus_graphic) * letter)
    return (sinus_color, sinus_graphic, sinus_str)

def out2():
    pass

def output():
    pass

# Löööp
def sinusrainbows():
  zahlen = range(0, 200, 2)
  for zahl in zahlen:
      zahl_1 = (zahl) / 10

      sinus_1_color, sinus_1_graphic, sinus_1_str = out(zahl_1, 0, "R")
      sinus_2_color, sinus_2_graphic, sinus_2_str = out(zahl_1, 120, "G")
      sinus_3_color, sinus_3_graphic, sinus_3_str = out(zahl_1, 240, "B")

      # HEX-Farbcode, 6-Stellig

      # R/G/B-Werte:
      r = sinus_1_color
      g = sinus_2_color
      b = sinus_3_color

      rgb_tuple = r,g,b
      rgb = '%02x%02x%02x' % rgb_tuple

      # String-Erzeugung mit Ausgabe '\033[38;2;RRR;GGG;BBBm'
      rgb_bcolors = ("\033[38;2;"+str(sinus_1_color)+";"+str(sinus_2_color)+";"+str(sinus_3_color)+"m"'')

      # Ausgabe nebeneinander
     
      print( (f"{bcolors.RED}"), \
      spalte_value.format(sinus_1_color),(spalte_graphic.format(sinus_1_str)), \
      (f"{bcolors.GREEN}"), \
      spalte_value.format(sinus_2_color), (spalte_graphic.format(sinus_2_str)), \
      (f"{bcolors.BLUE}"), \
      spalte_value.format(sinus_3_color), (spalte_graphic.format(sinus_3_str)), \
      (f"{rgb_bcolors}"), \
      (f"{bcolors.BOLD}"), \
      (spalte_rgb.format(rgb))+("  haha gay")+\
      f"{bcolors.ENDC}")


def ctrl():
  r = 100
  g = 100
  b = 100
  z = 10.0

  while True:
    inp_keys = {
      'a' : 'r',
    }
    i = input()
    if (i=='r'):  z -= 0.2
    if (i=='R'):  z += 0.2
    print(z)
    color, graphic, ostr = out(z, 0, "R")

    rgb_tuple = r,g,b
    rgb = '%02x%02x%02x' % rgb_tuple
    print(rgb)

    print( (f"{bcolors.RED}"), \
    spalte_value.format(r),(spalte_graphic.format(ostr)), \
    (f"{bcolors.BOLD}"), \
    (spalte_rgb.format(rgb))+("  haha gay")+\
    f"{bcolors.ENDC}")
    

if __name__ == '__main__':
  sinusrainbows()
  ctrl()


