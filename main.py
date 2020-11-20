import numpy as np
import copy

# a presente resolução considera a utilização do segundo vetor apresentado na especificação da prática
# nele são realizadas as operações necessárias

# dicionário de conversão, recebe o valor do elemento no vetor e retorna sua posição
conv_dict = {
    "21":0,
    "20":1,
    "19":2,
    "18":3,
    "17":4,
    "15":5,
    "14":6,
    "13":7,
    "12":8,
    "11":9,
    "10":10,
    "9":11,
    "7":12,
    "6":13,
    "5":14,
    "3":15,
    "16":16,
    "8":17,
    "4":18,
    "2":19,
    "1":20,
}

# dicionário de reconversão, recebe a posição do elemento no vetor e retorna seu valor
conv_back_dict = {
    "0 ":21,
    "1 ":20,
    "2 ":19,
    "3 ":18,
    "4 ":17,
    "5 ":15,
    "6 ":14,
    "7 ":13,
    "8 ":12,
    "9 ":11,
    "10":10,
    "11":9,
    "12":7,
    "13":6,
    "14":5,
    "15":3,
    "16":16,
    "17":8,
    "18":4,
    "19":2,
    "20":1,
}

# dicionário com máscaras a serem aplicadas para se obter a paridade dos elementos do vetor
masks_dict = {
    "1"  : [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    "2"  : [0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    "4"  : [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    "8"  : [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "16" : [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}

num_lines = int(input())

for i in range(num_lines):
    # value armazena a string de entrada, convertida para um vetor de inteiros
    value = []
    line = str(input())
    for c in line:
        value.append(int(c))

    # n_value armazena uma cópia de value, mas os últimos elementos serão modificados
    n_value = copy.deepcopy(value)

    # laço para cada um dos 5 bits de paridade
    for k in range(5):
        # key representa a potência de 2 para os diferentes valores de k
        key = str(2**k)
        
        # key é usada para acessar os dicionários conv_dict e masks_dict
        # n_value é acessado na posição correspondente ao bit de paridade de valor correspondente a key
        # ex: o bit de paridade correspondente a 8 será acessado na posição 17
        # a máscara correspondente é aplicada ao vetor value, e o resultado é somado
        # esta soma corresponde ao número de bits 1 após a aplicação da máscara e é submetida a módulo 2 a fim de obter o valor 1 ou 0
        n_value[conv_dict[key]] = np.sum(np.multiply(masks_dict[key], value))%2

    # se value for igual a n_value, não é preciso modificar os bits
    if value != n_value:
        # wrong_val armazena o valor do elemento incorreto
        wrong_val = 0

        # um laço percorrendo apenas os bits de paridade verifica quais bits de paridade são diferentes entre value e n_value
        # a partir dos bits diferentes, chega-se ao valor incorreto que precisa ser modificado
        for j in range(16, 21):
            if value[j] != n_value[j]:
                wrong_val += conv_back_dict[str(j)]
        
        # o valor incorreto é invertido mediante aplicação de XOR lógico
        # caso o bit incorreto seja um dos bits de paridade, a correção será realizada corretamente
        n_value[conv_dict[str(wrong_val)]] ^= 1
        
    # visto que n_value agora armazena os valores corretos, os últimos 5 elementos são eliminados
    n_value = n_value[:-5]  

    # n_value é convertido em uma única string
    final_value = ""
    for v in n_value:
        final_value += str(v) 

    # a string final é exibida
    print(final_value)