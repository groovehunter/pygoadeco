print("Hello World!")

import math

# FARBEN
color_1 = 255, 238, 170
color_2 = 255, 212, 0
color_3 = 0, 202, 0

# Ranges
zahlen_sinus = range(0, 200, 2)

# Platzhalter für Tabellenspalten
spalte_value = "{:>3}"       # Platzhalter für Farbwert
spalte_hex = "{:<14}"        # Platzhalter für Hexfarbcode


# LAS FUNCIONAS
def sinusandscale(color, sinus, phasendiff):
    """Generiert Sinuswerte inkl Phasenverschiebung und scaled diese aus dem Wertebereich -1...1 (Sinus) in 0...255 als integer"""
    sinus_value = math.sin(sinus + math.degrees(phasendiff))
    factor = (sinus_value + 1) / 2  # resultiert aus gekürzter Scalingformel für Wertebereich -1...1 auf 0...255
    r = int(color[0] * factor)
    g = int(color[1] * factor)
    b = int(color[2] * factor)
    return (r, g, b)


def rescolorlimit(color1, color2, color3):
    """Addiert R-. G- und B-Werte der Einzelfarben und limitiert die einzelnen Werte der Returnvariable auf max. 255"""
    r = color1[0] + color2[0] + color3[0]
    g = color1[1] + color2[1] + color3[1]
    b = color1[2] + color2[2] + color3[2]
    return (255 if r > 255 else r, 255 if g > 255 else g, 255 if b > 255 else b)


def txt_color(color):
    """Erstellt Strings mit Escape-Code für RGB-Farben, (wenn Tupel reinkommt) oder für Standardformatierung (wenn 0 reinkommt)"""
    if color == 0:
        escapestring = (f'\033[0m')
    else:
        escapestring = (f'\033[38;2;{str(color[0])};{str(color[1])};{str(color[2])}m')
    return escapestring


def value_out(color):
    """Erstellt einen in Spalten formatierten String aus Tupel (r, g, b)"""
    value = (f'{spalte_value.format(color[0])} {spalte_value.format(color[1])} {spalte_value.format(color[2])}')
    return value


def hex_out(color):
    """Erstellt formatierten String mit 6-stelligen Hexcode (thx Flow! :* )"""
    color_hex = spalte_hex.format('%02x%02x%02x' % color)
    return color_hex


# LÖÖÖP
for zahl_sinus in zahlen_sinus:
    zahl_sinus /= 10   # macht aus der Integerrange a gschmeidige Range zum Sinusfunktion füttern

    # Farbwerte im Löööp
    color_1_value = sinusandscale(color_1, zahl_sinus, 0)
    color_2_value = sinusandscale(color_2, zahl_sinus, 120)
    color_3_value = sinusandscale(color_3, zahl_sinus, 240)

    # Resultierende Farbe aus den Dreien zusammen
    color_res_value = rescolorlimit(color_1_value, color_2_value, color_3_value)


    # Ausgabe nebeneinander
    print(txt_color(0), value_out(color_1_value),
          txt_color(color_1_value), hex_out(color_1_value),

          txt_color(0), value_out(color_2_value),
          txt_color(color_2_value), hex_out(color_2_value),

          txt_color(0), value_out(color_3_value),
          txt_color(color_3_value), hex_out(color_3_value),

          txt_color((255, 255, 255)), value_out(color_res_value),
          txt_color(color_res_value), hex_out(color_res_value),

          "GOA GOA GOA GOA GOA GOA GOA GOA GOA GOA GOA GOA")