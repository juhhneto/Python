# Conceitos de String (Imagem 4)
movieName = "Top Gun"
movieName2 = "top Gun"
print(movieName == movieName2) # False (Case Sensitive)

movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura
muito consagrado na indústria
"""

# 1- Multiplicação de Strings
line = "="
print(line * 50)
print(movieDescription)

# 2- Procurar uma palavra dentro de um texto
print("Top" in movieName)  # True
print("ação" in movieName) # False