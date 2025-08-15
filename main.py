import unicodedata

dic_morse_letters = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..'
}

dic_morse_numbers = {
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

dic_morse_specials = {
    '.': '.-.-.-',   ',': '--..--',   '?': '..--..',
    "'": '.----.',   '!': '-.-.--',   '/': '-..-.',
    '(': '-.--.',    ')': '-.--.-',   '&': '.-...',
    ':': '---...',   ';': '-.-.-.',   '=': '-...-',
    '+': '.-.-.',    '-': '-....-',   '_': '..--.-',
    '"': '.-..-.',   '$': '...-..-',  '@': '.--.-.'
}

dicionario_unico = {**dic_morse_letters, **dic_morse_numbers, **dic_morse_specials}

def remover_acentos(texto):
    # Normaliza para separar letras e acentos
    texto_normalizado = unicodedata.normalize("NFD", texto)
    # Filtra apenas caracteres que NÃO sejam de categoria "Mn" (marcas de acento)
    return "".join(
        c for c in texto_normalizado if unicodedata.category(c) != "Mn"
    )

def tradutor(texto_informado):

    texto_informado_sem_acentos = remover_acentos(texto_informado)

    texto_traduzido = []

    for i in texto_informado_sem_acentos.upper():

        if i in dicionario_unico:
            texto_traduzido.append(dicionario_unico[i] + " ")

        else:
            texto_traduzido.append(" / ")
    
    return "".join(texto_traduzido)



print("""Olá, seja bem vindo(a) ao tradutor de texto para código morse. Aqui trabalhamos com letras (a, b, c, d, etc), números (1, 2, 3, 4, etc) e caracteres especiais (!, @, #, etc).
Você pode realizar mais traduções ao continuar inserindo os caracteres após cada tradução. Para sair, digite 'SAIR'.""")

texto_usuario = ""
palavra_traduzida = ""

rodando = True

while rodando:
    texto_usuario = input("Insira o texto:\n")

    if texto_usuario.upper() == "SAIR":
        rodando = False
    else:
        palavra_em_morse = tradutor(texto_usuario)
        print(f"\nA tradução de:  ---  {texto_usuario}  ---  em morse é:\n{palavra_em_morse}\n")
