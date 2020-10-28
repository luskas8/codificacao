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
            for j in range(len(message[i])):
                if lenFaltante <= 0: break
                aux = message[i][0]
                message[i-passed].extend(aux)
                # verifica se o numero é maior que N
                if (int("".join(message[i-passed])) > n):
                    # reverte o processo caso não seja
                    message[i-passed].pop(len(message[i-passed])-1)
                    break
                else:
                    message[i].pop(0)
                    lenFaltante -= 1
                    if not message[i]: message[i] = None
        else:
        # Caso falso, passa-se todos os espaços que são necessários
            while lenFaltante > 0:
                aux = message[i][0]
                message[i-passed].extend(aux)
                if (int("".join(message[i-passed])) > n):
                    message[i-passed].pop(len(message[i-passed])-1)
                    break
                else:
                    message[i].pop(0)
                    if not message[i]: message[i] = None
                    lenFaltante -= 1
        passed = 1

    # Tira-se os indices None (nulos) e transforma em inteiro
    newMessege = [int("".join(number)) for number in message if number != None and len(number) > 0]
    
    stringReturn = ""
    # Transforma strings em números
    for i in range(len(newMessege)):
        newMessege[i] = str((newMessege[i] ** e) % n)
        stringReturn += newMessege[i]+" "

    return stringReturn

def contaAlgarismo(n):
    # Conta quantos algarismos o número n tem
    return len(list(str(n)))