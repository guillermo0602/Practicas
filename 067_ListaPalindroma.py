lista=[1,2,3,2,1]
palindrmo= False

if lista==lista[::-1]:
    palindrmo=True

if palindrmo:
    print("es palindromo")
else:
    print("no es palindromo")

