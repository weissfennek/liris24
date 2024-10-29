def calculatrice():
    print("=== Calculatrice Python ===")
    print("Opérations disponibles:")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            # Saisie des nombres
            nombre1 = float(input("\nEntrez le premier nombre: "))
            nombre2 = float(input("Entrez le deuxième nombre: "))
            
            # Choix de l'opération
            operation = input("Entrez l'opération (+, -, *, /): ")
            
            # Calcul du résultat
            if operation == '+':
                resultat = nombre1 + nombre2
                print(f"\n{nombre1} + {nombre2} = {resultat}")
            
            elif operation == '-':
                resultat = nombre1 - nombre2
                print(f"\n{nombre1} - {nombre2} = {resultat}")
            
            elif operation == '*':
                resultat = nombre1 * nombre2
                print(f"\n{nombre1} * {nombre2} = {resultat}")
            
            elif operation == '/':
                if nombre2 != 0:
                    resultat = nombre1 / nombre2
                    print(f"\n{nombre1} / {nombre2} = {resultat}")
                else:
                    print("\nErreur: Division par zéro impossible!")
            
            else:
                print("\nErreur: Opération non valide!")
            
            # Demander si l'utilisateur veut continuer
            continuer = input("\nVoulez-vous faire un autre calcul? (oui/non): ")
            if continuer.lower() != 'oui':
                print("\nAu revoir!")
                break
                
        except ValueError:
            print("\nErreur: Veuillez entrer des nombres valides!")

if __name__ == "__main__":
    calculatrice()