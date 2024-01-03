import tkinter as tk

janela =tk.Tk()
janela.geometry("350x500+400+200")
janela.resizable(False,False)
janela.config(background="#00007f")


def metragem_quadrada():
    entrada1 = float(altura.get())
    entrada2 = float(comprimento.get())
    multiplicar = entrada1 * entrada2
    entrada3 = float(rendimento.get())
    cal_rendimento = multiplicar / entrada3
    lb_resultado = tk.Label(janela,text=f'Resultado: {multiplicar:.2f} metros quadrados\n Você vai precisar de {cal_rendimento:.2f} litros de tinta.',font=("Arial",9),fg="green",bg="#00007f",bd=0, highlightthickness=0)
    lb_resultado.grid(row=8,column=1,)


janela.title("CATI")
mensagem = tk.Label(text = "Pintura", font=("Mensch", 18), fg="white", bg="#00007f", width=5, height=5)
mensagem.grid(row=0, column=0,columnspan=2, sticky="E")

mensagem2 = tk.Label(text=" ********\n VAMOS CALCULAR A TINTA ! \n\n Começando pelas paredes.\n ********\n",font=("Arial Black",10),fg="white",bg="#00007f",bd=0)
mensagem2.grid(row=1, column=0,columnspan=2, sticky="E")

lb_mensagem=tk.Label(janela,text="CALCULAR METRAGEM QUADRADA",font=("Arial Black",9),fg="white",bg="#00007f",bd=0, highlightthickness=0)
lb_mensagem.grid(row=2,column=1, pady=15)

lb_num1=tk.Label(janela,text="Digite a altura em metros : ",font=("Arial",9),fg="white",bg="#00007f",bd=0, highlightthickness=0)
lb_num1.grid(row=3,column=1, pady=15)
altura = tk.Entry(janela)
altura.grid(row=3, column=2)

lb_num2=tk.Label(janela,text="Digite o comprimetro em metros: ",font=("Arial",9),fg="white",bg="#00007f",bd=0, highlightthickness=0)
lb_num2.grid(row=4,column=1, pady=15) 
comprimento = tk.Entry(janela)
comprimento.grid(row=4 ,column=2)

lb_num3=tk.Label(janela,text="Digite a rendimento da sua tinta\n em metros quadrados por litros: ",font=("Arial",9),fg="white",bg="#00007f",bd=0, highlightthickness=0)
lb_num3.grid(row=5, column=1)
rendimento = tk.Entry(janela)
rendimento.grid(row=5,column=2)
             
botao_metragem= tk.Button(text= "Calcular", command=metragem_quadrada)
botao_metragem.grid(row=7, column=1)


janela.mainloop()