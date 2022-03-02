def Lv():
    '''
    ---> x = (Limite regulamento - envergadura) - dist_motor até c.a.
    ---> b = Área da asa
    ---> c_medium = Corda média da asa
    ---> AR = Alongamento
    ---> teta = Inclinação entre centro aerodiâmico da asa e do profundor
    ---> cht = Intervalos de cordas possíveis - profundor
    ---> s_it = Area da asa pela relação (S = c**2)*AR
    ---> v_ht = São lmitações#LISTAS CRIADAS
    ---> Vht = Volume de cauda
    ---> Sht_old = Área de cauda inicial
    ---> lht_save = Distância entre c.a. da asa e do profundor inicial
    ---> lht_f = Distância entre c.a. da asa e do profundor final
    ---> Sht_f = Área de cauda final
    ---> teta_save = Inclinação entre c.a. da asa e do profundo 
    '''
    import numpy as np

    teta = np.linspace(np.pi/36, np.pi/18, 20)
    cht = np.linspace(.150, .400, 20)
    s_it = (cht ** 2) * AR
    V_ht = [0.35, 0.5]

    #LISTAS CRIADAS

    #Variando pra cada ângulo
    for k in teta:
        l_ht = (x - cht * (3 / 4)) / np.cos(k) 
    return l_ht




x = 889.43 / 1000 
S = 0.843         # Área da asa  
b = 1.86          # Envergadura 
c_medium = 0.463  # Corda média da asa
AR = 3            # Alongamento

l_ht = Lv()
print(f'{l_ht}')