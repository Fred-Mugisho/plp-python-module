def calculator(num1, num2, op):
    match op:
        case '+':
            return f"{num1} + {num2} = {num1 + num2}"
        case '-':
            return f"{num1} - {num2} = {num1 - num2}"
        case '*':
            return f"{num1} * {num2} = {num1 * num2}"
        case '/':
            if num2 == 0:
                return "Erreur: Division par zéro"
            return f"{num1} / {num2} = {num1 / num2}"
        case _:
            return "Opération non reconnue"
try:
    number_one = float(input("Entrer le premier nombre: "))
    number_two = float(input("Entrer le deuxième nombre: "))
    operation = input("Entrer l'opération (+, -, *, /): ")

    resultat = calculator(number_one, number_two, operation)
    print("Résultat:", resultat)
except ValueError:
    print("Erreur: Veuillez entrer des nombres valides.")
