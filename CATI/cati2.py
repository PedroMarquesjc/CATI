# Metragem Quadrada 
def metragem_quadrada():
	altura  = float(input("Digite a altura em metros: "))
	comprimento = float(input("Digite a soma dos comprimentos: "))
	medida_quadrada = altura * comprimento 
	return medida_quadrada

# Criação do menu
menu = int(input("Menu:\n 1 - Calcular Tinta \n 2 - Calcular Massa corrida \n 3 - Calcular textura \n 4 - Sair \n Qual é sua opção ? "))
if menu == 1:
    print(" VAMOS CALCULAR A TINTA ! \n\n Começando pelas paredes.\n")	
    medida_parede = metragem_quadrada()
    print(medida_parede)

    # Esquadrias
    esquadrias = input("Temos esquadrias como  portas ou janelas ? S/N: ").lower().strip()
    if esquadrias == "s":
        qtd_esquadrias = int(input("Quantas ?: "))
        contador_esquadrias = 0
        for i in range(qtd_esquadrias):
            
            calculo_esquadrias = metragem_quadrada()	
            medida_esquadrias = calculo_esquadrias
            contador_esquadrias += calculo_esquadrias  
			                        
    elif esquadrias  == "n":
        print("Ok. Vamos continuar.")
    else:				
        print("Opção inválida.")
        
    # Calculo de Tinta 
    rendimento = float(input("Digite a rendimento da sua tinta em metros quadrados por litros: "))
    metragem_final = medida_parede - contador_esquadrias
    qtd_tinta = metragem_final / rendimento
    print("Será necessário {:.2f} litros de tinta para {:.2f} metros quadrados".format(qtd_tinta, metragem_final))

else:
    print("Operação inválida!")