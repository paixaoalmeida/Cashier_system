import psycopg2 #Lib to connect to de PostgreeSQL database

#CONNECTING TO DATABASE
conn = psycopg2.connect(database="Sistema_caixa",
                        host="localhost",
                        user="postgres",
                        password="teste",
                        port="5432")
cursor = conn.cursor()
#--------------------------------------------#------------------------------------#-----------------
class Produto():
    def __init__(self):
        pass

    def AddProductInfoAndQuerry(self):
        prod_list = []  # LIsta vazia que vai pegar os valores
        arg = {'nome do produto:': str, 'preço do produto:': float, 'a quantidade:': int}
        # Dicionário com o nome das perguntas e valores como tipos de dados

        for nome, tipo in arg.items():  # dois argumentos no loop, key e valor
            quest = tipo(input(f'Digite {nome} '))
            prod_list.append(quest)  # A cada rodada do loop, acrescenta o resultado a lista

        try:
            cursor.execute(f"""
            INSERT INTO produtos (nome_produto,preco_produto,quantidade_produto)
            VALUES(%s,%s,%s); 
            """, (
            prod_list[0], prod_list[1], prod_list[2]))  # Usando a função %s para definir uma váriavel - função do C
            conn.commit()  # Comitar as mudanças no banco
        except:
            print('Há algo de errado com os dados ou o banco!')

    def ShowAllProducts():
        cursor.execute("""
            SELECT * FROM produtos
        """)
        all_itens = cursor.fetchall() #Como é uma tupla dentro de uma lista, eu preciso fornecer dois indexes

        for item in all_itens:
            print(f'''
                nome: {item[0]} #Dando um loop em todos os valores das tuplas retornadas
                preço: {item[1]}
                quantidade: {item[2]}
            ''')