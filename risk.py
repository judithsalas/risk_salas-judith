import itertools

def generate_combinations(resources, costs, min_units):
    """Genera todas las combinaciones posibles de tropas respetando los recursos disponibles."""
    combinations = []
    for inf in range(min_units['inf'], resources // costs['inf'] + 1):
        for cav in range(min_units['cav'], (resources - inf * costs['inf']) // costs['cav'] + 1):
            for art in range(min_units['art'], (resources - inf * costs['inf'] - cav * costs['cav']) // costs['art'] + 1):
                if inf * costs['inf'] + cav * costs['cav'] + art * costs['art'] <= resources:
                    combinations.append({'inf': inf, 'cav': cav, 'art': art})
    return combinations

def prioritize_territories(territories):
    """Ordena los territorios por fuerza de defensa (priorizando los más débiles)."""
    return sorted(territories, key=lambda x: x['defense'])

def calculate_attack_strength(troops, strengths):
    """Calcula la fuerza total de ataque según la combinación de tropas."""
    return (troops['inf'] * strengths['inf'] +
            troops['cav'] * strengths['cav'] +
            troops['art'] * strengths['art'])

def optimize_combinations(combinations, territories, strengths):
    """
    Optimiza las combinaciones de tropas para maximizar las conquistas usando programación dinámica.
    Devuelve la mejor combinación de tropas y las conquistas logradas.
    """
    max_conquests = 0
    best_combination = None

    for combo in combinations:
        attack_strength = calculate_attack_strength(combo, strengths)
        conquered = 0

        for territory in territories:
            terrain_type = territory['terrain']
            # Ajustar la fuerza de ataque basada en el tipo de terreno
            if terrain_type == 'plano':
                attack_strength += combo['cav'] * 1  # Caballería tiene ventaja
            elif terrain_type == 'montañoso':
                attack_strength += combo['art'] * 1  # Artillería tiene ventaja
            elif terrain_type == 'boscoso':
                attack_strength += combo['inf'] * 1  # Infantería tiene ventaja

            if attack_strength >= territory['defense']:
                conquered += 1
                attack_strength -= territory['defense']
            else:
                break

        if conquered > max_conquests:
            max_conquests = conquered
            best_combination = combo

    return best_combination, max_conquests

def represent_board(territories):
    """Representa el tablero con una estructura de datos."""
    board = {f'Territory {i+1}': (territory['defense'], territory['terrain']) for i, territory in enumerate(territories)}
    return board

# Datos iniciales
def main():
    resources = 20
    costs = {'inf': 1, 'cav': 3, 'art': 5}
    strengths = {'inf': 1, 'cav': 3, 'art': 5}
    min_units = {'inf': 1, 'cav': 1, 'art': 1}
    territories = [
        {'defense': 10, 'terrain': 'plano'},
        {'defense': 15, 'terrain': 'montañoso'},
        {'defense': 12, 'terrain': 'boscoso'}
    ]

    # Priorizar territorios más débiles
    territories = prioritize_territories(territories)
    print("Territorios ordenados por prioridad (más débiles primero):")
    print(territories)

    # Generar combinaciones de tropas
    troop_combinations = generate_combinations(resources, costs, min_units)
    print("\nCombinaciones de tropas posibles:")
    for combo in troop_combinations:
        print(combo)

    # Representar el tablero
    board = represent_board(territories)
    print("\nRepresentación del tablero:")
    for territory, (defense, terrain) in board.items():
        print(f"{territory}: Defensa = {defense}, Terreno = {terrain}")

    # Optimizar combinaciones
    best_combination, max_conquests = optimize_combinations(troop_combinations, territories, strengths)
    print("\nMejor combinación optimizada:")
    print(f"Tropas: {best_combination}, Conquistas máximas: {max_conquests}")

if __name__ == "__main__":
    main()
