import pygame, time




class Disco:
    def __init__(self, tamanho, p = 0):
        self.tamanho = tamanho
        self.pino = p
    
    def __str__(self):
        return str(self.tamanho)
    @property
    def pino(self):
        return self._pino
    @pino.setter
    def pino(self,p):
        self._pino = p
        
class Pino(list):
    def __init__(self,id):
        self.id = id
    
    def __str__(self):
        strng = "" 
        for disco in reversed(self):
            strng += int(disco.tamanho)*"*" + "\n"
        return strng


    def adiciona(self, disco):
        discos = len(self)
        if discos >= 1:
            tamanho_ultimo = self[-1].tamanho
            if tamanho_ultimo < disco.tamanho:
                print("Tamanho do último disco:{}, disco a ser movido: {}".format(tamanho_ultimo, disco.tamanho))  
                print("Erro: Tentando colocar disco maior por cima do menor.")
                return False
        self.append(disco)
        disco.pino = self.id
        return True
    
    def remove(self):
        if len(self) >= 1:
            disco = self.pop()
            disco.pino = 0
            return disco
        else:
            return False


class Jogo:
    def __init__(self, n_discos = 6):
        self.cores = ['#ff0000','#ff8000','#ffff00','#008000','#0000ff','#a000c0']

        
        self.w, self.h = 1024, 512                    # Tamanho da janela
        self.st = 0.005                          # Velocidade da animação, menor mais rápido.

        self.wx = int(self.w/6)
        self.dh = int(self.h/ndiscos)
        self.raio = 60
        self.rect=[0 for i in range(ndiscos)]

        self.d = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption("Torre de Hanoi")
        self.n_discos = n_discos
        self.pinos = [Pino(0), Pino(1), Pino(2)]
        self.contador = 0
        self.discos = []
        for d in reversed(range(0,n_discos)):
            disco = Disco(d)
            self.pinos[0].adiciona(disco)
            self.discos.append(disco) 
        self.discos.reverse()
        self.iniciar()

    def iniciar(self):
        print("Jogo iniciado. {} Discos estão no Pino 0".format(self.n_discos))
        print("\tRegras:")
        print("\t\tVence quando mover todos os discos para o Pino 1")
        print("\t\tNão pode colocar disco maior em cima do menor")
        print("\t\tMova um disco por vez, com o comando>> jogo.moverDisco(disco,pino)")
        print("\t\tDisco (0 -> ndisco - 1) e pino (0 -> 2)")
        print("\t\tDigite>> jogo.reset() para reinicializar")
        
        self.desenhar()

    def possivel_mover(self, do_pino, para_pino):
        disco = self.pinos[do_pino].remove()
        # print("Tentando mover do pino {} para o pino {}".format(do_pino, para_pino))
        if disco:
            self.contador += 1
            if self.pinos[para_pino].adiciona(disco):
                print("Movido disco {} do pino {} para o pino {}".format(disco,self.pinos[do_pino].id,self.pinos[para_pino].id))
                return True
            else:
                self.pinos[do_pino].adiciona(disco)
                return False


    def venceu(self):
        if len(self.pinos[1]) ==  self.n_discos:
            return True
        return False

    def desenhar(self):
        for disco in range(ndiscos):
            pygame.event.get()
            r = self.raio*(disco+1)
            self.rect[disco]=pygame.Rect(self.wx-r/2,self.dh*disco,r,self.dh) # salva coordenadas, tamanho do disco
            pygame.draw.rect(self.d, pygame.Color(self.cores[disco]), self.rect[disco])
        pygame.display.flip()
        pygame.event.get()
        #time.sleep(2)

    def moverDisco(self,disco, to): # Desenha o movimento!
        if self.possivel_mover(self.discos[disco].pino,to):
            # print("Movendo desenho do disco {} para o pino {}".format(disco, to))
            r = self.raio*(disco+1)
            c = pygame.Color(self.cores[disco])
            (x1,_,_,_)=self.rect[disco]              # Posição atual
            x2=self.wx+to*2*self.wx-r/2                   # posição desejada
            dx = (x2-x1)/50                     # passo do movimento
            # Animação:
            for i in range(50):                
                pygame.event.get()
                # Apaga o disco na posição atual:
                pygame.draw.rect(self.d, pygame.Color('#000000'), self.rect[disco])
                self.rect[disco]=pygame.Rect(x1+dx*(i+1),self.dh*disco,r,self.dh)
                pygame.draw.rect(self.d, c, self.rect[disco])  # Desenha disco na nova posição
                pygame.display.flip()               # Update a tela
                time.sleep(self.st)                      # velocidade do movimento...
        if self.venceu():
            print("Venceu!! Precisou de {} jogadas".format(self.contador))
    

    def reset(self):
        self.__init__()
    
    def resolve(self,ndiscos=6, startPeg=0, endPeg=1):
        if ndiscos:
            # Move todos os discos exceto um para outro pino
            self.resolve(ndiscos-1, startPeg, 3-startPeg-endPeg)
            # move 1 disco para o pino livre
            
            self.moverDisco(ndiscos-1, endPeg)      
            # Agora move o restante para ele.
            self.resolve(ndiscos-1, 3-startPeg-endPeg, endPeg)
            
ndiscos = 6                         # Numero de discos
jogo = Jogo(ndiscos)
