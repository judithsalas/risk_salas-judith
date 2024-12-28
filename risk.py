import itertools
import random

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

def simulate_attack(troops, territory, strengths, probabilities):
    """
    Simula un ataque a un territorio.
    Aplica probabilidades y calcula si el ataque tiene éxito.
    """
    attack_strength = calculate_attack_strength(troops, strengths)
    terrain = territory['terrain']
    success_chance = probabilities[terrain]
    # Aplicar probabilidades al ataque
    if random.random() <= success_chance:
        if attack_strength >= territory['defense']:
            return True, attack_strength - territory['defense']
    return False, attack_strength

def handle_events():
    """Genera eventos aleatorios que afectan las tropas o los territorios."""
    events = [
        "Tormenta afecta la caballería (-10% fuerza)",
        "Rebeldes refuerzan un territorio (+5 defensa)",
        "Clima favorable aumenta la artillería (+10% fuerza)"
    ]
    event = random.choice(events)
    print(f"Evento aleatorio: {event}")
    return event

def apply_event_effects(event, troops, territory):
    """Aplica los efectos del evento a las tropas o al territorio."""
    if "Tormenta" in event:
        troops['cav'] = max(0, troops['cav'] - 1)
    elif "Rebeldes" in event:
        territory['defense'] += 5
    elif "Clima favorable" in event:
        troops['art'] += 1

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
    probabilities = {'plano': 0.8, 'montañoso': 0.6, 'boscoso': 0.7}

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

    # Simulación de ataques con eventos aleatorios
    for combo in troop_combinations:
        print(f"\nSimulando ataques con combinación: {combo}")
        for territory in territories:
            event = handle_events()
            apply_event_effects(event, combo, territory)
            success, remaining_strength = simulate_attack(combo, territory, strengths, probabilities)
            if success:
                print(f"¡Territorio conquistado! Quedan {remaining_strength} puntos de ataque.")
            else:
                print("El ataque falló.")

if __name__ == "__main__":
    main()
