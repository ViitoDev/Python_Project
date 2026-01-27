def cpf_validation(cpf):
    if not cpf.isdigit():
        return "\nYour cpf should only countain numbers."
    if len(cpf) != 11:
        return "\nYour cpf should countain 11 numbers."
    return "\nValid cpf"
    

cpf = input("Enter your cpf: \n")
print(cpf_validation((cpf)))