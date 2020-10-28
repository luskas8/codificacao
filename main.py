import os
import encriptar as ec

def main():
    print("Bem Vindo!\n")

    options = """O QUE GOSTARIA DE FAZER EM NOSSO PROGRAMA?
> 1. Encriptografar
> 2. Decriptografar
> 0. Sair\n
Escolha: """
    
    while True:
        escolha = int(input(options))
        if escolha == 1:
            choiceOne()
        elif escolha == 2:
            choiceTwo()
        else:
            print("Obrigado por usar nosso programa, até uma outra vez :)\n")
            break
    
def choiceOne():
    mensagem = input("\nInforme sua mensagem: ")
    semiCripto = ec.semiCriptografar(mensagem) # Mensagem transformada em ASCII
    
    n = int(input("Informe o número n: ")) # número 'n' (chave pública)

    e = int(input("Informe  o número e: ")) # número 'e' (chave pública)

    
    mensagemCriptografada = ec.criptografar(semiCripto, e, n)

    print("Chaves públicas no formato [n, e]: [{}, {}]\n".format(n, e))
    print("Blocos criptografados: {}\n".format(mensagemCriptografada))

def choiceTwo():
    mensagem = input("\nEntre com os blocos criptografados, separados por espaco: ")
    mensagem = mensagem.split()
    mensagem = [int(i) for i in mensagem]

    d = int(input("Entre com o valor de d (chave privada): "))
    n = int(input("Entre com o valor de n (chave publica): "))
    
    # aplica a descriptografia e transforma em uma string sem espaços
    raw_decrypt = "".join([str((i**d) % n) for i in mensagem])

    decrypt = []
    i = 0
    
    while i < len(raw_decrypt):
        if int(raw_decrypt[i]) > 1:
            decrypt.append(int(raw_decrypt[i:i+2]))
            i += 2
        else:
            decrypt.append(int(raw_decrypt[i:i+3]))
            i += 3
            
    decrypt = "".join([chr(i) for i in decrypt])

    print("Mensagem decriptografada:", decrypt, "\n")

if __name__ == "__main__":
    main()
