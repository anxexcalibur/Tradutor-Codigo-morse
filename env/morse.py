# Função para traduzir uma mensagem para código Morse
def tradutorMorse(mensagem='HELLO WORLD'):
    # Converte a mensagem para maiúsculas
    mensagem1 = mensagem.upper()
    
    # Dicionário contendo o alfabeto Morse
    morse_alphabet = {
        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ',
        'F': '..-. ', 'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ',
        'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ',
        'P': '.--. ', 'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ',
        'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ', 'Y': '-.-- ',
        'Z': '--.. ', ' ': '/', 'Ã':'penis'
    }
    
    # Traduz a mensagem para Morse
    mensagem_em_morse = "".join([morse_alphabet[letra] for letra in mensagem1])
    
    # Retorna a mensagem traduzida
    return mensagem_em_morse
