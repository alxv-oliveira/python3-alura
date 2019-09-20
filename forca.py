def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not acertou and not enforcou):
        chute = input("Qual letra? ")
        index = 0

        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra '{}' na posição {}".format(chute, index))
            index += 1

        print("Jogando ... ")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()