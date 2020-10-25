import random
import os
import decriptar as dc
import encriptar as ec

def main():
    print("Bem Vindo!\n")

    options = """O QUE GOSTARIA DE FAZER EM NOSSO PROGRAMA?
> 1. Encriptografar
> 2. Decriptografar
> 0. Sair\n
Escolha: """

    loop = True # Controla se esta ou não em loop, default: em loop
    escolha = 0 # Controla escolha do usuário

    os.system('cls' if os.name == 'nt' else 'clear')
    while loop:
        escolha = int(input(options))
        if escolha == 1:
            choiceOne()
        elif escolha == 2:
            choiceTwo()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Obrigado por usar nosso programa, até uma outra vez :)\n")
            exit()
    
def choiceOne():
    mensagem = input("Informe sua mensagem: ")
    semiCripto = ec.semiCriptografar(mensagem) #morte ao miojo # Mensagem transformada em ASCII
    
    n = int(input("Informe o número n: ")) # número e da chave pública

    e = int(input("nforme  o número e: ")) # número e usado na chave pública

    
    mensagemCriptografada = ec.criptografar(semiCripto, e, n)

    # Limpa a tela e mostra as informações
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("Chave pública, formato [n, e]: [{},{}]\n".format(n, e))
    print("Bloco criptografada: {}\n".format(mensagemCriptografada))

def choiceTwo():
    mensagem = input("Entre com os blocos, separados por espaco: ")
    mensagem = mensagem.split()
    mensagem = [int(i) for i in mensagem]

    d = int(input("Entre com o valor de d (chave privada): "))
    n = int(input("Entre com o valor de n (chave publica): "))
    
    decript = "".join([chr((i**d) % n) for i in mensagem])

    print("Mensagem decriptografada:", decript, "\n")

# Função pede numero E, recebendo o totiente de N
def getEs(n: int) -> list:
    Es = []
    for i in range(2, n):
        if ((i > 1 and i < n) and (i%n != 0)): Es.append(i)
    return Es
    # Verifica de E está de acordo com a regra 1 < e < totienteN. Caso não recursivamente pede novamente
    # return num if ((num > 1 and num < n) and (num%n != 0)) else getE(n)

# Função verifica se número inteiro n é primo ou não, retornando a resposta desta pergunta
def isPrimo(n: int) -> bool:
    for i in range(2, int(n/2)):
        # i testa os possiveis dividores de n
        if (n % i == 0): return False

    return True

if __name__ == "__main__":
    main()
