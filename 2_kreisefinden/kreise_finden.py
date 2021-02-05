import cv2
import numpy as np

def kreise_finden( src ):
    maske = cv2.imread( src , 0 )
    maske = cv2.medianBlur( maske , 5 )
    bild  = cv2.cvtColor( maske , cv2.COLOR_GRAY2BGR )

    kreise = cv2.HoughCircles( maske , cv2.HOUGH_GRADIENT , 1 , 20 , param1 = 50 , param2 = 30 , minRadius = 48 , maxRadius = 0 )

    kreise = np.uint16( np.around( kreise ) )
    for kreis in kreise[0,:]:
        # zeichnen den äußeren Kreis
        cv2.circle( bild , ( kreis[0] , kreis[1] ) , kreis[2] , ( 0 , 255 , 0 ) , 2 )
        # zeichnen den Mittelpunkt des Kreises
        cv2.circle( bild , ( kreis[0] , kreis[1] ) , 2 , ( 0 , 0 , 255 ) , 3 )

    cv2.imshow( 'erkannte Kreise' , bild )
    cv2.waitKey( 0 )
    cv2.destroyAllWindows()
    

kreise_finden( 'farben_maske.bmp' )

