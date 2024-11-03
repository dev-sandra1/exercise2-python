usuario= [("nana",5), 
          ("susi",66),
            ("lili",7)]


# el:  se puede usar cuando solo hay lambdas y si la vas utilizar solo unica vez
usuario.sort(key=lambda el:el[1], reverse=True)#ordena la lista de menor a mayor #el[1] es el segundo elemento de la tupla
usuario.sort(key=lambda el:el[1])#ordena la lista de menor a mayor
print(usuario) #imprime la lista ordenada

#La función lambda es como una pequeña función que se usa para acceder a un elemento específico dentro
#  de las tuplas (en este caso el segundo elemento) para ordenar la lista.