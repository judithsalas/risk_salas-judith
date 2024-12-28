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

def generate_permutations(territories):
    """Genera todas las permutaciones posibles para el orden de ataque."""
    return list(itertools.permutations(territories))

def calculate_attack_strength(troops, strengths):
    """Calcula la fuerza total de ataque según la combinación de tropas."""
    return (troops['inf'] * strengths['inf'] +
            troops['cav'] * strengths['cav'] +
            troops['art'] * strengths['art'])

def represent_board(territories):
    """Representa el tablero con una estructura de datos."""
    board = {f'Territory {i+1}': defense for i, defense in enumerate(territories)}
    return board

# Datos iniciales
def main():
    resources = 20
    costs = {'inf': 1, 'cav': 3, 'art': 5}
    strengths = {'inf': 1, 'cav': 3, 'art': 5}
    min_units = {'inf': 1, 'cav': 1, 'art': 1}
    territories = [10, 15, 12]  # Defensas de los territorios enemigos

    # Generar combinaciones de tropas
    troop_combinations = generate_combinations(resources, costs, min_units)
    print("Combinaciones de tropas posibles:")
    for combo in troop_combinations:
        print(combo)

    # Generar permutaciones del orden de ataque
    attack_orders = generate_permutations(territories)
    print("\nPermutaciones de orden de ataque:")
    for order in attack_orders:
        print(order)

    # Representar el tablero
    board = represent_board(territories)
    print("\nRepresentación del tablero:")
    for territory, defense in board.items():
        print(f"{territory}: Defensa = {defense}")

    # Calcular y optimizar ataque
    print("\nSimulaciones de ataques:")
    for combo in troop_combinations:
        attack_strength = calculate_attack_strength(combo, strengths)
        print(f"Con {combo}, fuerza de ataque total: {attack_strength}")
        
        for order in attack_orders:
            print(f"  Orden de ataque: {order}")
            for i, defense in enumerate(order):
                if attack_strength >= defense:
                    print(f"    Territorio {i+1} conquistado! (Defensa {defense})")
                    attack_strength -= defense
                else:
                    print(f"    Territorio {i+1} no conquistado. (Defensa {defense})")
                    break

if __name__ == "__main__":
    main()
