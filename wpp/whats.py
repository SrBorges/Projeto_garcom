import pywhatkit as kit

def wpp(wha):
    msg = input("Digite sua mensagem: ")
    num = input("Informe o número: ")

    kit.sendwhatmsg(f'{num}', f"{msg}", 12, 9)
    print("Mensagem enviada... ")


