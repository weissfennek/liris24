# Programme simple à tester

def calculer_moyenne(nombres):
    """
    Calcule la moyenne d'une liste de nombres.
    
    Parameters:
        nombres (list of float): Une liste de nombres (int ou float).
    
    Returns:
        float: La moyenne des nombres.
    """
    if not nombres:
        return 0  # Retourne 0 si la liste est vide
    return sum(nombres) / len(nombres)

def celsius_vers_fahrenheit(celsius):
    """
    Convertit une température de Celsius à Fahrenheit.
    
    Parameters:
        celsius (float): La température en degrés Celsius.
    
    Returns:
        float: La température en degrés Fahrenheit.
    """
    return (celsius * 9/5) + 32

# Exemples d'utilisation
if __name__ == "__main__":
    # Exemple de calcul de moyenne
    notes = [12, 15, 14, 10, 18]
    print("Moyenne des notes:", calculer_moyenne(notes))
    
    # Exemple de conversion de température
    temperature_celsius = 25
    print("25°C en Fahrenheit:", celsius_vers_fahrenheit(temperature_celsius))
