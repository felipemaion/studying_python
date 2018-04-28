from collections import OrderedDict
import socket
import psutil
import time
import os
import cpuinfo
import pickle

def sair_exit(socket_cliente):
    socket_cliente.shutdown(socket.SHUT_RDWR)
    socket_cliente.close()
   
    
    

def uso_ram(socket_cliente):
    mem = psutil.virtual_memory()
    info = '\nMemoria Total: {}'.format(mem.total/(1024*1024*1024))
    info += '\nMemoria Usada: {}'.format(mem.used/(1024*1024*1024))
    info += '\nMemoria Disponivel: {}'.format((mem.total - mem.used)/(1024*1024*1024))
    
    info1 = pickle.dumps(info)
    socket_cliente.send(info1)

def uso_cpu(socket_cliente):
    chave = ['arch','brand','bits']
    valor = cpuinfo.get_cpu_info()
    nunLogico = psutil.cpu_count()
    nunFisico = psutil.cpu_count(logical=False)
    info = '\nArquitetura: {} \nNome: {} \nPalavra: {} \nThreads: {} \nNúcleos Físicos: {}'.format(valor[chave[0]],valor[chave[1]],valor[chave[2]],nunLogico,nunFisico)
    info +='\nPercentual do uso de CPU:{}'.format(psutil.cpu_percent())
    
    info1 = pickle.dumps(info)
    socket_cliente.send(info1)



def lista_diret(socket_cliente):
    
    info2 = "Caminho"
    info1 = pickle.dumps(info2)
    socket_cliente.send(info1)
    path = socket_cliente.recv(100000)
    path1 = pickle.loads(path)
    dic = listDiretorio(path1)
    titulo = '{:11}'.format("Tamanho")
    titulo = titulo + ' {:27}'.format("Data de Modificação")
    titulo = titulo + ' {:27}'.format("Data de Criação")
    titulo = titulo + "Nome"
    info = '{}\n'.format(titulo)
    for i in dic:
        kb = dic[ i] [ 0] /1000
        tamanho = '{:10}'.format(str(' {:.2f}'.format(kb)+'KB' ))
        info += '\n{} {} {} {} {} {}'.format(tamanho, time.ctime(dic[ i] [ 2] )," ", time.ctime(dic[ i] [ 1] )," ", i)
        
    info1 = pickle.dumps(info)
    socket_cliente.send(info1)

def listDiretorio(path):
    try:
        if os.path.isdir(path):
            
            os.chdir(path)
    except:
        pass
    lista = os.listdir(path)
   

    dic = {}
    for i in lista:
        if os.path.isfile(i):
            dic[i] = []
            dic[i].append(os.stat(i).st_size)
            dic[i].append(os.stat(i).st_atime)
            dic[i].append(os.stat(i).st_mtime)
            dicSorted = sorted(dic.items(), key= lambda t: t[1])
            dicSorted.reverse()
            x = (OrderedDict(dicSorted))
    return x


def uso_disco(socket_cliente):
    disco = psutil.disk_usage('.')
    info = '\nTotal: {0} GB'.format(str(round(disco.total/(1024*1024*1024), 2)))
    info += '\nEm uso: {0} GB'.format(str(round(disco.used/(1024*1024*1024), 2)))
    info += '\nLivre: {0} GB'.format(str(round(disco.free/(1024*1024*1024), 2)))
    info += '\nPercentual de Disco Usado: {} %'.format(str(disco.percent))
    info1 = pickle.dumps(info)
    socket_cliente.send(info1)
    
def processo_ativo(socket_cliente):
    
    
    titulo = '{:^7}'.format("PID")
    titulo = titulo + '{:^11}'.format("# Threads")
    titulo = titulo + '{:^26}'.format("Criação")
    titulo = titulo + '{:^9}'.format("T. Usu.")
    titulo = titulo + '{:^9}'.format("T. Sis.")
    titulo = titulo + '{:^12}'.format("Mem. (%)")
    titulo = titulo + '{:^12}'.format("RSS")
    titulo = titulo + '{:^12}'.format("VMS") # Maion: Fix Typo. 
    titulo = titulo + " Executável"
    
    lista = psutil.pids()
    info = '{}'.format(titulo)
    for pid in lista:
        try:        
            p = psutil.Process(pid)
            texto = '{:6}'.format(pid)
            texto = texto + '{:11}'.format(p.num_threads())
            texto = texto + " " + time.ctime(p.create_time()) + " "
            texto = texto + '{:8.2f}'.format(p.cpu_times().user)
            texto = texto + '{:8.2f}'.format(p.cpu_times().system)
            texto = texto + '{:10.2f}'.format(p.memory_percent()) + " MB"
            rss = p.memory_info().rss/1024/1024
            texto = texto + '{:10.2f}'.format(rss) + " MB"
            vms = p.memory_info().vms/1024/1024
            texto = texto + '{:10.2f}'.format(vms) + " MB"
            texto = texto + " " + p.exe()
            info += '\n{}'.format(texto)
            
        except:
            pass
    info1 = pickle.dumps(info)
    socket_cliente.send(info1)

def info_Pid(socket_cliente,pid):

    try:
        p = psutil.Process(pid)
        texto = '{:6}'.format(pid)
        texto = texto + '{:11}'.format(p.num_threads())
        texto = texto + " " + time.ctime(p.create_time()) + " "
        texto = texto + '{:8.2f}'.format(p.cpu_times().user)
        texto = texto + '{:8.2f}'.format(p.cpu_times().system)
        texto = texto + '{:10.2f}'.format(p.memory_percent()) + " MB"
        rss = p.memory_info().rss/1024/1024
        texto = texto + '{:10.2f}'.format(rss) + " MB"
        vms = p.memory_info().vms/1024/1024
        texto = texto + '{:10.2f}'.format(vms) + " MB"
        texto = texto + " " + p.exe()
        return texto
        
    except:
          pass



    

def network(socket_cliente):
    info = '\nUsuario solicitou Informações sobre Rede'
    interfaces = psutil.net_if_addrs()
    nomes = []
    for i in interfaces:
        nomes.append(str(i))
    titulo = '{:^11}'.format("Nome")
    titulo = titulo + '{:^15}'.format("Familia")
    titulo = titulo + '{:^60}'.format("Endereço")
    titulo = titulo + '{:^25}'.format("Máscara")
    titulo = titulo + '{:^24}'.format("Broadcast")
    titulo = titulo + '{:^21}'.format("Ptp")
    
    info = '{}'.format(titulo)
    for i in nomes:
        info = '{}:\n'.format(i)
        for j in interfaces[i]:
           info +="\t"+ '{:<40}'.format(str(j[0]))+ '{:<45}'.format(str(j[1])) + '{:^15}'.format(str(j[2])) + '{:^30}'.format(str(j[3])) + '{:^10}'.format(str(j[4]))
    

    info1 = pickle.dumps(info)
    socket_cliente.send(info1) 
 
opts = {
    '1': ('Uso de Processamento', uso_cpu),
    '2': ('Arquivos e Diretórios', lista_diret),
    '3': ('Memoria', uso_ram),
    '4': ('Redes', network),
    '5': ('Uso de Disco', uso_disco),
    '6': ('Processos Ativos',processo_ativo),
    'x': ('pressione x para sair',sair_exit),
}


menu_text = '\n'

for opt, (opt_text, func) in sorted(opts.items()):
    menu_text += '\n{} - {}'.format(opt, opt_text)


socket_servidor = socket.socket()
socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_servidor.setsockopt
host = socket.gethostname()
porta = 9765
socket_servidor.bind((host, porta))
socket_servidor.listen()
print("Servidor", host, "esperando na porta:", porta)
socket_cliente, addr = socket_servidor.accept()
print("Conectado a:", str(addr))

recepçao = "Escolha uma opção abaixo..."
socket_cliente.send(recepçao.encode('utf-8'))

while True:
    try:
        msg = socket_cliente.recv(1024).decode()
    except Exception as err:
        break
    if (msg == '$'):
        close_conn(socket_cliente)
        break
        
    elif(msg not in opts):
        socket_cliente.send('Opção inválida'.encode('utf8'))
    else:
        opts[msg][1](socket_cliente)
    

