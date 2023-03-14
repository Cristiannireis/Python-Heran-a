import carro, moto

uno_vermelho = carro.Carro("vermelho", "Flex", 1, 4)
uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(60)
print(f"A quantidade de combustivel do carro é {uno_vermelho.qtd_combustivel}")

moto_vermelha = moto.Moto("vermelha", "Gasolina", 1, 2)
moto_vermelha.ligar()
print(moto_vermelha.is_ligado)