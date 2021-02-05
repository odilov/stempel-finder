import cv2
import numpy as np
import math

def polarkoordinatensystem_konverter( src ):
    src = cv2.imread( src ) 

    maxRadius = math.sqrt( math.pow( src.shape[0] , 2 ) + math.pow( src.shape[1] , 2 ) ) / 2
    magnitude = src.shape[0] / math.log( maxRadius )
    center = ( src.shape[0] / 2, src.shape[1] / 2 )
    polar = cv2.logPolar( src , center , magnitude , cv2.INTER_AREA )


    cv2.imshow( 'Polarkoordinatensystem' , polar )
    cv2.waitKey( 0 )
    cv2.destroyAllWindows()

    cv2.imwrite( 'log_polar_kovertiert.bmp' , polar ) # speichern


polarkoordinatensystem_konverter( 'test.jpeg' )