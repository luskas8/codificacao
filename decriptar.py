# Função descriptografa vetor de inteiros c com os inteiros d, n. Retornando uma string
def descriptografar(c: list, d: int, n: int) -> list:
    # Vetor de mesmo tamanho de c
    message: list = [0 for i in range(len(c))]
    
    for i in range(len(c)):
        # Percorre vetor c tranformando elm[i] em caracter
        message[i] = chr((c[i]**d) % n)
    
    string = ""
    for i in message:
        # Percorre a lista de string message adicionando em cada elemento na string
        string += i
    print(string+"\n")

    return message

# Função para achar o inverso do inteiro e modular com o inteiro m, retornando esse inteiro achado
def inversoModular(e: int, m: int) -> int:
    for x in range(m-1):
        # Percorre a tabela Zm a procura do inverso modular de e mod m
        if ((x*e) % m == 1): return x