movieName = "Top Gun"
movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura 
muito consagrado na indústria
"""

print(movieName.upper()) # tudo maiúsculo
print(movieName.lower()) # tudo minusculo
print(movieName.capitalize()) # primeira letra maiúscula
print(movieName.title()) # primeira letra maiuscula
print(movieName.center(10, '-')) # retorna string centralizada com caractere de preenchimento
print(movieName.find("u")) # retorna a posição de um determinado caractere
print(movieName.find("o")) # conta caracteres
print(movieName.replace("Top", "Matrix")) #altera elementos por outros
print(movieDescription.split(','))
