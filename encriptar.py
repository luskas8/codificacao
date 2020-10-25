# Função tranforma a string m em ASCII retornando o resultado numa lista de inteiros
def semiCriptografar(m: str) -> list:
    # Lista de inteiros de mesmo tamanho de m
    semiCripto: list = [0 for x in range(len(m))]

    for i in range(len(m)):
        # Percorre string m tranformando caracter em ASCII e colocando no vetor de inteiros
        semiCripto[i] = ord(m[i])
    return semiCripto

# Função criptografa vetor m de inteiros com os inteiros e, n. Retornando outro vetor de inteiros
def criptografar(m: list, e: int, n: int) -> list:
    message: list = [0 for i in range(len(m))]
    
    for i in range(len(m)):
        # Transforma os números em listas para facilitar no agrupamento
        if (m[i] < 100):
            message[i] = list(str(m[i]))
            message[i].insert(0, '0')
        else:
            message[i] = list(str(m[i]))
    
    lenN: int = contaAlgarismo(n)
    lenFaltante = 0
    passed = 1
    for i in range(1, len(message)):
        # Se não tiver nada no indice anterior pegasse o indice anterior a este
        if (message[i-1] == None): passed += 1

        if (len(message[i-passed]) <= lenN):
            # Calcula quantos espaçoes faltam para compretar o limite de algarismos de n
            lenFaltante = lenN-len(message[i-passed])

        if (len(message[i]) < lenFaltante):
            # Se o espaço faltante é maior q o indice atual
            # coloca-se ele inteiro no grupo e passa ao indice posterior
            lenFaltante -= len(message[i])
            message[i-passed].extend(message[i])
            message[i] = None
        else:
            # Caso falso, passa-se todos os espaços que são necessários
            aux = message[i][:lenFaltante]
            message[i-passed].extend(aux)
            for x in range(lenFaltante): message[i].pop(0)

    # Tira-se os indices None (nulos)
    newMessege = [number for number in message if number != None]
    message.pop(len(newMessege)-len(message))
    
    # Transforma as listas em strings
    for i in range(len(newMessege)):
        message[i] = int("".join(newMessege[i]))
    
    # Transforma strings em números
    for i in range(len(message)):
        message[i] = (message[i] ** e) % n

    return message

def contaAlgarismo(n):
    # Conta quantos algarismos o número n tem
    return len(list(str(n)))