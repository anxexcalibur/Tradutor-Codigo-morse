from tkinter import *
import morse
from tkinter import ttk

def obter_entrada():
    valor = caixa_entrada.get()
    resultado = morse.tradutorMorse(valor)
    resultado_label.config(text=f"Resultado: {resultado}")

def copiar_resultado():
    resultado_completo = resultado_label.cget("text")
    
    # Extrai a parte do texto após o ":"
    parte_a_copiar = resultado_completo.split(":")[1].strip()
    
    janela.clipboard_clear()
    janela.clipboard_append(parte_a_copiar)
    janela.update()

janela = Tk()
janela.title("Tradutor Morse")

# Cria um estilo
estilo = ttk.Style()

# Define a cor de fundo e de texto para o estilo 'EstiloBotao'
estilo.configure('EstiloBotao.TButton', background='#4CAF50', foreground='black', font=('Arial', 12))

# Rótulo para orientação
texto_orientacao = Label(janela, text="Digite o texto:")
texto_orientacao.grid(row=0, column=0, padx=10, pady=10)

# Caixa de entrada
caixa_entrada = Entry(janela)
caixa_entrada.grid(row=0, column=1, padx=10, pady=10)

# Botão estilizado
botao = ttk.Button(janela, text="Enviar", command=obter_entrada, style='EstiloBotao.TButton')
botao.grid(row=1, column=0, columnspan=2, pady=10)

# Rótulo para exibir o resultado
resultado_label = Label(janela, text="Resultado: ")
resultado_label.grid(row=2, column=0, columnspan=2, pady=10)

# Botão para copiar o resultado
botao_copiar = ttk.Button(janela, text="Copiar Resultado", command=copiar_resultado)
botao_copiar.grid(row=3, column=0, columnspan=2, pady=10)

janela.mainloop()
