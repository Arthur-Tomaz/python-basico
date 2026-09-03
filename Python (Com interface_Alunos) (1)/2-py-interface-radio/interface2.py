import tkinter as tk
from tkinter import ttk

class InterfaceAvancada:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Interface Avançada")
        self.janela.geometry("400x500")
        self.criar_widgets()

    def criar_widgets(self):
        # Caixa de entrada para nome
        tk.Label(self.janela, text="Digite seu nome:").pack(pady=5)

        self.caixa_texto = tk.Entry(self.janela, width=40)
        self.caixa_texto.pack(pady=5)

        # Botões de rádio
        tk.Label(self.janela, text="Escolha sua preferência:").pack(pady=5)

        self.var_radio = tk.StringVar(value="Café")

        for opcao in ["Café", "Chá", "Suco"]:
            tk.Radiobutton(
                self.janela,
                text=opcao,
                variable=self.var_radio,
                value=opcao
            ).pack()

        # Checkboxes
        self.var_check_saudacao = tk.BooleanVar()
        tk.Checkbutton(
            self.janela,
            text="Saudação informal",
            variable=self.var_check_saudacao
        ).pack(pady=5)

        self.var_check_personalizada = tk.BooleanVar()
        tk.Checkbutton(
            self.janela,
            text="Saudação personalizada",
            variable=self.var_check_personalizada
        ).pack(pady=5)

        # Combobox
        tk.Label(self.janela, text="Escolha sua cor favorita:").pack(pady=5)

        self.combo_cor = ttk.Combobox(
            self.janela,
            values=["Vermelho", "Azul", "Verde", "Amarelo", "Preto", "Branco"]
        )
        self.combo_cor.pack(pady=5)

        # Botão de ação

        # Atualizar
        tk.Button(
            self.janela, text="Atualizar", command=self.atualizar_resultado
        ).pack(pady=10)

        # Limpar
        tk.Button(
            self.janela, text="Limpar", command=self.limpar_campos
        ).pack(pady=10)

        # Rotulo "label" onde a mensagem final é exibida
        self.label_resultados = tk.Label(self.janela, text="", wraplength=350)
        self.label_resultados.pack(pady=10)

    def montar_saudacao(self):
        # Saudação normal
        saudacao = "Olá" if self.var_check_personalizada.get() else "Bem-Vindo"

        # Saudação personalizada
        if self.var_check_saudacao.get():
            saudacao = f"{saudacao}. caro(a)"

        return saudacao

    def atualizar_resultado(self):
        # Captura todas as opçoes escolhidas pelo usúario
        nome = self.caixa_texto.get()
        preferencia = self.var_radio.get()
        saudacao = self.montar_saudacao()
        cor_favorita = self.combo_cor.get()

        # Forma a frase dizendo as opções escolhidas pelo usuario
        mensagem = f"{saudacao} {nome}! Você prefere {preferencia}."
        if cor_favorita:
            mensagem += f" Sua cor favorita é {cor_favorita}."

        self.label_resultados.config(text=mensagem)

    def limpar_campos(self):
        # Limpa todos as opçoes para voltar ao estado inicial
        self.caixa_texto.delete(0, tk.END)
        self.var_radio.set("Café")
        self.var_check_saudacao.set(False)
        self.var_check_personalizada.set(False)
        self.combo_cor.set("")
        self.label_resultados.config(text="")

    def executar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = InterfaceAvancada()
    app.executar()