import pywhatkit as kit

def writ(wr):
    wr = str(input("Assinatura: "))

    kit.text_to_handwriting(f'{wr}')
    print("Assinatura digital concluída. ")


