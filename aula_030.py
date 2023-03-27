"""
CONSTANTE = "Variáveis" que não vão mudar
            Python não possui um tipo de dado "constante" em si,
            mas é uma prática comum nomear variáveis que armazenam
            valores constantes em letras maiúsculas para indicar
            que elas não devem ser alteradas. Isso é conhecido como
            "convenção de nomenclatura de constantes".
Muitas condições no mesmo if(ruim)
    Quanto mais condições em um IF, mais difícil será para 
    entender o código.
<- Contagem de complexidade (ruim)
    Quanto mais houver recuo de código, mais complexo pode ficar
    seu código. Quanto mais evitar, melhor.
"""

velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')
    
if carro_multado_radar_1:
    print('Carro multado em radar 1')