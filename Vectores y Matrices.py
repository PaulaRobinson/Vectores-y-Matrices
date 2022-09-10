importar  mathcplx  como  lc
importar  matematicas

def  adiciónVectores ( v , w , z ):
    si  z == 'resta' :
        w = multiescalar (( - 1 , 0 ), w )
    si ( len ( v ) !=  len ( w )):
        devolver  "NO"
    suma = [( 0 , 0 ) for  i  in  range ( len ( v ))]
    para  i  en  rango ( 0 , len ( v )):
        suma [ yo ] = lc . sumacplx ( v [ yo ], w [ yo ])
    volver  suma

def  multiescalar ( c , v ):
    mult = [( 0 , 0 ) para  i  en  rango ( len ( v ))]
    para  i  en  rango ( 0 , len ( v )):
        multi [ yo ] = lc . multicplx ( c , v [ i ])
    retorno  múltiple

def  inversoVectorAdd ( v ):
    inv = [( 0 , 0 ) for  i  in  range ( len ( v ))]
    para  i  en el  rango ( 0 , len ( inv )):
        inv [ yo ] = ( v [ yo ][ 0 ] * - 1 , v [ yo ][ 1 ] * - 1 )
    retorno  inv

def  matrices Agregar ( v , w , z ):
    si ( len ( v ) != len ( w )):
        devuelve  'No'
    si ( largo ( v [ 0 ]) != largo ( w [ 0 ])):
        devuelve  'No'

    newMatrix = [( 0 , 0 ) for  i  in  range ( len ( v ))]

    para  i  en el  rango ( len ( v )):
        nuevaMatriz [ i ] = adicionVectores ( v [ i ], w [ i ], z )

    volver  matriz nueva

def  inversaMatrizAdd ( v ):
    nuevaMatriz  = []
    para  i  en el  rango ( len ( v )):
        nuevoMatrix . agregar ([])
        para  j  en el  rango ( len ( v [ 0 ])):
            nuevaMatriz [ i ]. agregar ( Ninguno )

    para  i  en  rango ( 0 , len ( v )):
        para  j  en el  rango ( 0 , len ( v [ i ])):
            nuevaMatriz [ i ][ j ] = v [ i ][ j ][ 0 ] * - 1 , v [ i ][ j ][ 1 ] * - 1


    volver  matriz nueva

def  multiplicacionMatrizEscalar ( c , v ):
    nuevaMatriz  = []
    para  i  en  rango ( 0 , len ( v )):
        nuevoMatrix . agregar ( multiescalar ( c , v [ i ]))

    volver  matriz nueva

def  transpuestaMV ( v ):
    transpuesto = []

    para  i  en  rango ( len ( v [ 0 ])):
        transpuesta _ agregar ([])
        para  j  en  rango ( len ( v )):
            transpuesta [ yo ] añadir ( v [ j ][ i ])

    volver  transpuesta

def  conjugadaMV ( v ):
    conjugado = []
    para  i  en el  rango ( len ( v )):
        conjugada _ agregar ([])
        para  j  en el  rango ( len ( v [ i ])):
            conjugada [ yo ]. añadir (( v [ i ][ j ][ 0 ], v [ i ][ j ][ 1 ] * - 1 ))
    volver  conjugada

def  dagaMV ( v ):
    volver  transpuestaMV ( conjugadaMV ( v ))

def  prodMv ( v , w ):
    si  largo ( v ) != largo ( w [ 0 ]):
        devuelve  'No'

    producción = []
    yo = 0
    mientras  yo < len ( v [ 0 ]):
        producto _ agregar ([])
        j = 0
        mientras que  j < len ( w ):
            k = 0
            suma = ( 0 , 0 )

            mientras que  k < len ( v ):

                suma = lc . sumacplx ( suma , lc . multcplx ( v [ k ][ i ], w [ j ][ k ]))
                k += 1
            prod [ yo ] agregar ( suma )
            j += 1
        yo += 1


    volver  transpuestaMV ( prod )

def  prodInterno ( v , w ):
    daga = dagaMV ( v )
    volver  prodMv ( daga , w )

definición  normaV ( v ):
     matemáticas de retorno . raíz cuadrada ( prodInterno ( v , v )[ 0 ][ 0 ][ 0 ])

def  distanciaVectores ( v , w ):
    gap = adicionVectores ( v , w , 'resta' )
    imprimir ( brecha )
    volver  normaV ([ brecha ])

def  matrizU ( v ):
    matrizIdentidad = []
    para  i  en el  rango ( len ( v )):
        matrizIdentidad . agregar ([])
        para  j  en el  rango ( len ( v [ 0 ])):
            matrizIdentidad [ i ]. agregar (( 0 , 0 ))
            si  yo == j :
                matrizIdentidad [ i ][ j ] = ( 1 , 0 )
    daga = dagaMV ( v )
    valor1 = prodMv ( v , daga )
    valor2 = prodMv ( daga , v )
    si  valor1 == valor2 :
        if  valor1 == matrizIdentidad :
            if  valor2 == matrizIdentidad :
                volver  'Matriz Unitaria'
    volver  'Matriz no Unitaria'


def  matrizH ( v ):
    h = dagaMV ( v )
    si  h == v :
        volver  'Matriz Hermitiana'
    volver  'Matriz no Hermitiana'


def  tensorMV ( v , w ):
    tensor = []
    para  i  en  rango ( len ( v ) * len ( w )):
        tensor _ agregar ([])
        para  j  en  rango ( len ( v [ 0 ]) * len ( w [ 0 ])):
            tensor [ yo ]. agregar ( Ninguno )

    para  k  en  rango ( len ( tensor )):
        para  j  en  rango ( len ( tensor [ k ])):
            #imprimir(v[k//len(w)][j//len(w[0])])
            #print(w[k%largo(w)][j%largo(w[0])])
            tensor [ k ][ j ] = lc . multcplx ( v [ k // largo ( w )][ j // largo ( w [ 0 ])], w [ k % largo ( w )][ j % largo ( w [ 0 ])])

     tensor de retorno



#print(adicionVectores([(-5, -6), (-6, -8)],[(5,6),(6,8)],'resta'))
#print(multiescalar((2,3),[(5,6),(6,8)]))
#print(inversoVectorAdd([(5,6),(6,8)]))
#print(matricesAdd([[(5,4),(17,12)], [(8,-2),(1,3)]],[[(2,6),(5,8)] ,[(5,1),(2,5)]],'suma'))
#print(inversaMatrizAdd([[(5,4),(17,12)], [(8,-2),(1,3)]]))
#print(multiplicacionMatrizEscalar((5,9),[[(5,4),(17,12)], [(8,-2),(1,3)]]))
#print(transpuestaMV([[(5,4),(17,12)], [(8,-2),(1,3)]]))
#print(conjugadaMV([[(5,4),(17,12)], [(8,-2),(1,3)], [(8,-2),(1,3)]] ))
#print(dagaMV([[(5,4),(17,12)], [(8,-2),(1,3)], [(8,-2),(1,3)]] ))
#print(prodMv([[(3,2),(1,0),(4,-1)],[(0,0),(4,2),(0,0)],[(5 ,-6),(0,1),(4,0)]],[[(5,0),(0,0),(7,-4)],[(2,-1),( 4,5),(2,7)],[(6,-4),(2,0),(0,0)]]))
#print(prodMv([[(-1,0),(2,-1),(0,0)],[(1,1),(0,0),(1,-1)],[ (0,0),(1,0),(0,1)]],[[(1,0),(1,1),(0,1)]])) #Matriz sobre un vector
#print(prodInterno([[(1,0),(0,1),(1,-3)]],[[(2,1),(0,1),(2,0)]]) )
#print(normaV([[(6,3.3),(4.9,-5.8)]]))
#print(distanciaVectores([(-5, -6), (-6, -8)],[(3,1),(8,5)]))
#imprimir(matrizU([[(1/2,1/2),(1/2,-1/2)],[(1/2,-1/2),(1/2,1/2) ]]))
#print(matrizH([[(5,0),(4,-5),(6,16)],[(4,5),(13,0),(7,0)],[(6 ,-16),(7,0),(-2.1,0)]]))
#print(tensorMV([[(1,0),(3,0)],[(2,0),(1,0)]],[[(0,0),(2,0)], [(3,0),(1,0)]]))
#imprimir(matrizU([[(0,2),(0,0)],[(0,0),(0,-2)]]))
#print(transpuestaMV(tensorMV([[(1,0),(2,0),(5,0)]],[[(4,0),(-3,0)]])))
#print(MVtensor([[(0,0),(1,0)],[(1,0),(0,0)]],[[(1/math.sqrt(2),0), (1/matemáticas.raíz cuadrada(2),0)],[(1/matemáticas.raíz cuadrada(2),0),(-1/matemáticas.raíz cuadrada(2),0)]]))
