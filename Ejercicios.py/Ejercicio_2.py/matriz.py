def regla_Sarrus (matriz):
    for i in range (len(matriz)):
        for j in range (len(matriz)):
            return matriz[0][0]*matriz[1][1]*matriz[2][2]+matriz[0][1]*matriz[1][2]*matriz[2][0]+matriz[0][2]*matriz[1][0]*matriz[2][1]-matriz[0][2]*matriz[1][1]*matriz[2][0]-matriz[0][1]*matriz[1][0]*matriz[2][2]-matriz[0][0]*matriz[1][2]*matriz[2][1]
            
           
    
matriz = [[1,2,0],
          [4,0,6]
        , [7,0,9]]
print(matriz)
print (regla_Sarrus(matriz))
