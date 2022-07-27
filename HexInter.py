#!/usr/bin/python3 

print("hello world!")

# Import math damit später sinus geht und auch pi lol
import math
import readchar

f_value = "{:>3}"       # Platzhalter rechtsbündig für Farbwert
f_graphic = "{:<27}"    # Platzhalter linksbündig für Darstellung mit Zeichen
f_rgb = "{:>8}"            # Platzhalter 8 Stellen rechtsbündig
rgbkeys = ['r', 'g', 'b']
#  phasendiff = {'r':0, 'g':120, 'b':240}

# class. Rauskopiert wo, RED, GREEN, BLUE und RGB dazugebastelt
class bcolors:
    ENDC = '\033[0m'
    BOLD = '\033[1m'

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

def out2(z, letter):
    sinus = math.sin(z) 
    sinus_color = int((sinus + 1) * 127.5)   # Wertebereich 0 ... 255 für Farbcode
    graphic = sinus * 12 + 13          # Wertebereich für Darstellung mit Zeichen
    sinus_str = (int(graphic) * letter)
    return (sinus_color, graphic, sinus_str)

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
      f_value.format(sinus_1_color),(f_graphic.format(sinus_1_str)), \
      (f"{bcolors.GREEN}"), \
      f_value.format(sinus_2_color), (f_graphic.format(sinus_2_str)), \
      (f"{bcolors.BLUE}"), \
      f_value.format(sinus_3_color), (f_graphic.format(sinus_3_str)), \
      (f"{rgb_bcolors}"), \
      (f"{bcolors.BOLD}"), \
      (f_rgb.format(rgb))+("  haha gay")+\
      f"{bcolors.ENDC}")



def outline(color, graphic, ostr, rgb):
    rgb_bcolors = ("\033[38;2;"+str(color['r'])+";"+str(color['g'])+";"+str(color['b'])+"m"'')

    print( (f"{bcolors.RED}"), \
    f_value.format(color['r']),(f_graphic.format(ostr['r'])), \
    (f"{bcolors.GREEN}"), \
    f_value.format(color['g']), (f_graphic.format(ostr['g'])), \
    (f"{bcolors.BLUE}"), \
    f_value.format(color['b']), (f_graphic.format(ostr['b'])), \
    (f"{rgb_bcolors}"), \
    (f"{bcolors.BOLD}"), \
    (f_rgb.format(rgb))+("  haha gay")+\
    (f"{bcolors.ENDC}"), )





def ctrl():
  graphic = {}
  ostr = {}
  char = {}
  color = {}
  z = {}
  for col in rgbkeys:
    char[col] = col.upper()
    z[col] = 10

  while True:
    #i = input()
    i = readchar.readchar()
    if i.isupper():
      z[i.lower()] += 0.1
    else:
      z[i] -= 0.1

    for col in rgbkeys:
      #color[col], graphic[col], ostr[col] = out(z[col], phasendiff[col], char[col])
      color[col], graphic[col], ostr[col] = out2(z[col], char[col])
    rgb_tuple = color['r'], color['g'], color['b']
    rgb = '%02x%02x%02x' % rgb_tuple

    outline(color, graphic, ostr, rgb) 




if __name__ == '__main__':
  sinusrainbows()
  ctrl()


