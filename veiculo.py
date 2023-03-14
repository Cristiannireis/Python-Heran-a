class Veiculo():
    def __init__(self, cor, tipo_combustivel, potencia):
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0

    def __del__(self):
        print("O objeto foi removido da memória")
    
    def abastecer(self, qtd_combustivel):
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.is_ligado:
            print("O veiculo foi ligado")
        else:
            self.is_ligado = True
            print("O veiculo já está ligado")

    def desligar(self):
        if self.is_ligado == False:
            print("O veiculo já está ligado")
        else:
            self.is_ligado = False
    
    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print("O veiculo precisa estar ligado para ser acelerado")
       
        