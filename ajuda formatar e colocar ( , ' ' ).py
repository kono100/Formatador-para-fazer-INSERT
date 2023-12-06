import re
from datetime import datetime


strings = []

while True:
    texto = input("Digite o texto ('exit'): ").lower()

    
    if texto == "exit":
        break 


    #teste


    partes = texto.split('&')

    # Remover espaços em branco fora das partes entre &
    texto = '&'.join([parte if i % 2 == 0 else parte.replace(" ", "&&&") for i, parte in enumerate(partes)])







    # fim teste

    texto = texto.replace(" ", ", ")


    posicao = len(texto) - 0  
    texto = texto[:posicao] + ')' + texto[posicao+1:]


    posicao = 0
    texto = texto[:posicao] + '(' + texto[posicao:]



    # Inicio modifica (", a", ", 'a")

    for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        texto = texto.replace(f", {letter}", f", '{letter}")
    
    # Fim modifica (", a", ", 'a")



    # Inicio modifica ("a,", "a',")


    for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        texto = texto.replace(f"{letter},", f"{letter}',")

    
    # FIM modifica ("a,", "a',")


    
        #Ajuda formatar usando & INICIO

        texto = texto.replace("&&&", " ")
        texto = texto.replace("&", "'")

        #Ajuda formatar usando & FIM

    
    #  Inicio da converção dos numeors com ( , virgula )  para ( . Ponto )

    for i in range(10):
        for j in range(10):
            old_value = f"{i},{j}"
            new_value = f"{i}.{j}"
            texto = texto.replace(old_value, new_value)


    #  FIM da converção dos numeors com ( , virgula )  para ( . Ponto )



    #  INICIO da converção dos numeros com EXEMPLO (".999")  para ("999")

    # remeove dos numeros exemplos 000.,  vai ficar 000,
    texto = texto.replace(".,", ",")


    for i in range(1000):
        old = f".{i:03d}"
        new = f"{i:03d}"
        texto = texto.replace(old, new)


    #  FIM da converção dos numeros com EXEMPLO (".999")  para ("999")



    # INICIO colocando ("(a", "('a")
    
    for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        texto = texto.replace(f"({letter}", f"('{letter}")

    # FIM colocando  ("(a", "('a")




    # INICIO colocando  ("Z)", "Z')")


    for letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        texto = texto.replace(f"{letter})", f"{letter}')")


    # FIM colocando  ("Z)", "Z')")

    
    # Inicio dos dia mes ano    # Inicio data formatada com -




    # Expressão regular para reconhecer datas no formato dd-mm-yyyy ou dd/mm/yyyy
    regex = r"(\d{2})[-/](\d{2})[-/](\d{4})"

    # Função para converter a data para o formato yyyy-mm-dd
    def convert_date(match):
        day = match.group(1)
        month = match.group(2)
        year = match.group(3)
        date_obj = datetime.strptime(f"{day}-{month}-{year}", "%d-%m-%Y")
        return date_obj.strftime("'%Y-%m-%d'")

    # Substitui as datas no formato dd-mm-yyyy ou dd/mm/yyyy pelo formato yyyy-mm-dd
    texto = re.sub(regex, convert_date, texto)


    # fim dos dia mes ano    # Inicio data formatada com -


    



    strings.append(texto) 
    



print("\nAs strings digitadas foram:\n")

#teste









# fim teste



for i, s in enumerate(strings):
    if i == len(strings) - 1:  # verifica se é a última string

        print(f"{s};")


    else:

        print(f"{s},")
        
print()






'''
# modo super otimizado



import re
from datetime import datetime


strings = []

while True:
    texto = input("Digite o texto ('exit'): ")
    
    if texto == "exit":
        break 

    # Substitui espaços por vírgulas e adiciona parênteses no início e no final
    texto = '(' + texto.replace(" ", ", ") + ')'

    # Substitui padrões de ", a" e "a," por ", 'a" e "'a',"
    texto = re.sub(r',\s+([a-zA-Z])', r", '\1", texto)
    texto = re.sub(r'([a-zA-Z])\s+,', r"\1',", texto)

    # Substitui números com vírgula por números com ponto e remove zeros à esquerda
    texto = re.sub(r'(\d+),(\d{1,2})', r"\1.\2", texto)

    # Substitui "(a" por "('a" e "Z)" por "Z')"
    texto = re.sub(r'\(([a-zA-Z])', r"('\1", texto)
    texto = re.sub(r'([a-zA-Z])\)', r"\1')", texto)

    # Converte datas no formato dd-mm-yyyy ou dd/mm/yyyy para o formato yyyy-mm-dd
    regex = r"(\d{2})[-/](\d{2})[-/](\d{4})"
    texto = re.sub(regex, lambda match: datetime.strptime(match.group(0), "%d-%m-%Y").strftime("'%Y-%m-%d'"), texto)

    strings.append(texto) 

print("\nAs strings digitadas foram:\n")
print(",\n".join(strings) + ';')

'''