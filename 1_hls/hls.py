import cv2
import numpy as np

def colored_mask( src , threshold = -1):
    src = cv2.imread( src ) 
    
    # Bild Verwischen ( kleine Geräusche zu entfernen )
    entrauscht = cv2.medianBlur( src , 3 )
    cv2.imwrite( 'entrauscht.bmp' , entrauscht )

    # Speichern in Schwarzweiß ( die Maske zu bekommen )
    grau = cv2.cvtColor( entrauscht , cv2.COLOR_BGR2GRAY )
    cv2.imwrite( 'grau.bmp' , grau )

    # den farbigen Teil des Bildes extrahieren
    adaptiveThreshold = threshold if threshold >= 0 else cv2.mean( src )[0]
    farbe = cv2.cvtColor( entrauscht , cv2.COLOR_BGR2HLS )
    maske = cv2.inRange( farbe , ( 0 , int( adaptiveThreshold / 6 ) , 60 ) , ( 180 , adaptiveThreshold , 255 ) )

    # Erstellen eine Maske für den farbigen Teil des Bildes
    dst = cv2.bitwise_and( grau , grau , mask = maske )
    cv2.imwrite( 'farben_maske.bmp' , dst ) # ergebniss

    print( dst )


colored_mask( 'input.png' )
