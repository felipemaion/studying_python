import psutil
import pickle
import socket
def visualizarMenu():
    opts = {
        '1': ('Uso de Processamento'),
        '2': ('Arquivos e Diretórios'),
        '3': ('Memoria'),
        '4': ('Uso de Disco'),
        '5': ('Processos Ativos'),
        '6': ('Redes'),
        'x': ('pressione x para sair'),
}

    menu_text = '\n'
    for opt, (opt_text) in sorted(opts.items()):
        menu_text += '\n{} - {}'.format(opt, opt_text)
    print(menu_text)

host = socket.gethostname()
porta = 9765

s = socket.socket()
try:

    s.connect((host, porta))
except Exception as erro:
    print(str(erro))


print('Conexão realizada com:',host)

msg = s.recv(1024)
print(msg.decode('utf-8'))
while True:
    
    visualizarMenu()
    
    escolha= input('Digite a opção desejada:')
    s.send(escolha.encode('utf-8'))
   
    bytes = s.recv(100000)
    info = pickle.loads(bytes)
    if not info:
        bytes = s.recv(100000).decode()
            
    else:
        sair = False
    
    if info == 'Caminho':
        path = input('Digite o caminho :')
        info1 = pickle.dumps(path)
        s.send(info1)
        s.recv(100000)
        info = pickle.loads(bytes)
        print(info)
        
    else:
        print(info)
                
        
    




