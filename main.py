from ytdownloader import yt
from search import sea
from wpp import whats
from write import wrt
from leia import help

print("Suas possibilidades. :) \n")
print("Opção 1: Barra de pesquisa. \n")
print("Opção 2: Whatsapp. \n")
print("Opção 3: Assinatura. \n")
print("Opção 4: Youtube Downloader  \n")
print("Opção 5: Sobre o Garçom. \n")
print("Opção 9: Sair. \n")


opcao = int(input("Digite sua opção: "))
op = [1, 2, 3, 4, 5, 9]


if opcao == 1:
    num = 0
    sea.search(num)
elif opcao == 2:
    num = 0
    whats.wpp(num)
elif opcao == 3:
    num = 0
    wrt.writ(num)
elif opcao == 4:
    num = 0
    yt.down()
elif opcao == 5:
    help.help()
elif opcao == 9:
    print("Você encerrou o programa... ")
else:
    while opcao not in op:
        print("Opção inválida. ")
        opcao = int(input("Digite sua opção: "))
        if opcao == 1:
            num = 0
            sea.search(num)
        elif opcao == 2:
            num = 0
            whats.wpp(num)
        elif opcao == 3:
            num = 0
            wrt.writ(num)
        elif opcao == 4:
            num = 0
            ytdownloader.yt.down(num)
        elif opcao == 5:
            help.help()
        elif opcao == 9:
            print("Você encerrou o programa... ")


### Sr. Borges ###

