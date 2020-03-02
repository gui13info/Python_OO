from formulario import Form

dados = Form(input("Digite seu nome: "), input("Informe seu email: "), int(input("Digite seu número: ")), int(input("Informe sua idade: ")), str(input("Informe seu sexo: ")))

print("\nSEUS DADOS: ")
print("\tNome: ",dados.nome)
print("\tEmail: ",dados.email)
print("\tTelefone: ",dados.telefone)
print("\tIdade: ",dados.idade)
print("\tSexo: ",dados.sexo[:1])

