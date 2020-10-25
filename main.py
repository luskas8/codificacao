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
    mensagem = input("\nInforme sua mensagem: ")
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

    d = int(input("\nEntre com o valor de d (chave privada): "))
    n = int(input("Entre com o valor de n (chave publica): "))
    
    decript = "".join([chr((i**d) % n) for i in mensagem])

    print("Mensagem decriptografada:", decript, "\n")

if __name__ == "__main__":
    main()
