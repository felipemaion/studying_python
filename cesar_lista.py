


class MyList(list): # Extende a Classe list
    def excluir(self, lista_interna, elemento): # cria o método excluir
        try: # tenta fazer isso... (e se não existir o elemento?)
            return self[lista_interna].remove(elemento) # Entra na própria lista, e apaga o elemento.
        except:
            return None

lista = MyList([["a", "b", "c", "d"], [5, 8, 2], []]) # Instancia a lista como sendo MyList

lista.excluir(0,"d") # roda...



def excluir(lista, lista_interna, elemento): # cria o método excluir
    try: # tenta fazer isso... (e se não existir o elemento?)
        return lista[lista_interna].remove(elemento) # Entra na própria lista, e apaga o elemento.
    except:
        return None

lista = [["a", "b", "c", "d"], [5, 8, 2], []]                          

excluir(lista,0,"d")                                                   