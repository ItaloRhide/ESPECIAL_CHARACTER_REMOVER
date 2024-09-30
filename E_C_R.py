import tkinter as tk

def trade(texto):
    codigo = texto
    for symbol in '-./':
        codigo = codigo.replace(symbol, '')

    resultado.config(state=tk.NORMAL)
    resultado.delete(1.0, tk.END)
    resultado.insert(tk.END, codigo)
    resultado.config(state=tk.DISABLED)

def clicar():
    texto = entrada.get()
    trade(texto)


janela = tk.Tk()
janela.title("Remover Caracteres")
janela.geometry("600x400")
janela.config(bg="#D8B4E2")

titulo = tk.Label(janela, text="Remover caracteres", font=("Helvetica", 16, "bold"), bg="#D8B4E2", fg="#333")
titulo.pack(pady=20)

frame = tk.Frame(janela, bg="#D8B4E2")
frame.pack(pady=10)

entrada_label = tk.Label(frame, text="Insira o texto:", font=("Helvetica", 12), bg="#D8B4E2", fg="#333")
entrada_label.grid(padx=10, pady=5)
entrada = tk.Entry(frame, width=40, font=("Arial", 12), bd=2, relief="groove")
entrada.grid(row=0, column=1, padx=10, pady=5)

executar = tk.Button(janela, text="EXECUTAR", command=clicar, bg="#2EC0F9", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5, activebackground="#45a049")
executar.pack(pady=15)

fechar = tk.Button(janela, text="FECHAR", command=janela.quit, bg="#FF8CC6", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5, activebackground="#c0392b")
fechar.pack(pady=5)

resultado_label = tk.Label(janela, text="Resultado:", font=("Helvetica", 12), bg="#D8B4E2", fg="#333")
resultado_label.pack(pady=10)

resultado = tk.Text(janela, width=50, height=2, font=("Arial", 12), bd=2, relief="sunken")
resultado.config(state=tk.DISABLED)
resultado.pack(pady=5)

janela.mainloop()
