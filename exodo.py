class Controle:
    def __init__(self):
        self.ch = 5
        self.tvligada = False

    def canal(self,canal = None):
        if canal:
            if self.tvligada:
                self.ch = canal
                print("Mudou o canal para:", self.ch)
            else:
                print("Você precisa ligar a TV para mudar de canal")
        else:
            return self.ch

    def botao_ligar_tv(self):
        if self.tvligada :
            self.tvligada = False # desliga
            print("TV desligada.")
        else:
            self.tvligada = True # liga
            print("TV ligada no canal", self.canal())
        return self.tvligada

tv = Controle()
tv.botao_ligar_tv()
tv.canal(10)
tv.botao_ligar_tv()
tv.canal(4)
tv.botao_ligar_tv()
tv.canal(4)
tv.botao_ligar_tv()
tv.botao_ligar_tv()

