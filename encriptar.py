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
    block: list = ["" for i in range(len(m))]

    for i in range(len(m)):
        if (i+1 < len(m)):
            block[i] += str(message[i])
            for i in range(len(str(n))):
                if m[i] < 100:
                    block[i] += '0'
                else:
                    block[i] += str(m[i+1] / 10)
                if (len(block[i]) >= len(str(n))): pass
                else: i -= 1
        # message[i] = (m[i]**e) % n

    return block