# D:\Python27\ python
# -*- coding: utf-8 -*-

import kinterbasdb

def InsereRegistros(linhas):
    #em um banco de dados local ou na rede, a forma de conexão para uma base de dados firebird é semelhante ao método abaixo:
    conexao = kinterbasdb.connect(dsn='127.0.0.1:C:\Users\kable\PycharmProjects\RSP\estatistica.fdb', user='JOAO', password='teste', dialect=3)
    consulta = conexao.cursor() #criará um novo cursor para executar os comandos
    consulta.execute("SELECT COALESCE(MAX(ID),0) FROM EXAMPLE") #método que executa uma string de comando
    # forma utilizada para pegar a próxima chave primária. Em um banco de dados robusto e com grande volume de dados, essa não é a melhor forma.
    chave = list(consulta.fetchall()) #lê _todo o retorno
    novosregistros = []
    i = list(chave[0]) #transformar o retorno do select em uma lista
    j = 0
    j = i[0] #converter em um valor a tupla que foi retornada da lista
    try:
        for linha in linhas:
            j += 1
            novosregistros.append((j, int(linha.replace('\n', ''))))

        consulta.executemany("INSERT INTO EXAMPLE (ID, VALUE_) VALUES (?, ?)", novosregistros) #executará o comando INSERT até que a lista de novos registros esteja vazia
        conexao.commit() #confirma a transação com o banco de dados
        conexao.close() #encerra a conexão
        return 1

    except:
        print 'Some problems found on this connection...'
        conexao.close() #encerra a conexão em caso de problemas
        return 0