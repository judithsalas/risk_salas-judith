# Planificación de Ataques en el Juego Risk con Estrategias Avanzadas

## Descripción

Este programa extiende las funcionalidades del simulador de ataques en el juego Risk, añadiendo características avanzadas como:
- Sistema de probabilidades para simular la incertidumbre en los ataques.
- Evolución de tropas que incrementa su fuerza con eventos positivos.
- Eventos aleatorios que afectan el desempeño de las tropas y las defensas enemigas.

## Funcionalidades Principales

1. **Generación de combinaciones de tropas:** Calcula todas las combinaciones posibles respetando los recursos disponibles y las restricciones mínimas.
2. **Optimización basada en probabilidades:** Los ataques tienen probabilidades de éxito específicas según el tipo de terreno.
3. **Eventos aleatorios:** Introduce eventos que afectan las tropas o los territorios, como tormentas, refuerzos enemigos o clima favorable.
4. **Evolución de tropas:** Las tropas pueden ganar fuerza en ciertas condiciones.
5. **Prioridad de territorios:** Ordena los territorios enemigos por defensa, priorizando los más débiles.

## Datos Iniciales

### Recursos
- **Recursos disponibles:** 20 puntos.
- **Costos de tropas:**
  - Infantería: 1 punto por tropa.
  - Caballería: 3 puntos por tropa.
  - Artillería: 5 puntos por tropa.

### Fuerza de las Tropas
- Infantería: 1 de fuerza.
- Caballería: 3 de fuerza.
- Artillería: 5 de fuerza.

### Probabilidades de Éxito por Terreno
- Plano: 80% de éxito.
- Montañoso: 60% de éxito.
- Boscoso: 70% de éxito.

### Territorios Enemigos
- Territorio 1: Defensa = 10, Terreno = Plano.
- Territorio 2: Defensa = 15, Terreno = Montañoso.
- Territorio 3: Defensa = 12, Terreno = Boscoso.

### Eventos Aleatorios
- Tormenta: Reduce la fuerza de la caballería.
- Refuerzos enemigos: Aumentan la defensa de un territorio.
- Clima favorable: Incrementa la fuerza de la artillería.

## Uso

### Requisitos
- Python 3.x

### Ejecución
1. Clona o descarga el repositorio.
2. Asegúrate de tener Python instalado en tu sistema.
3. Ejecuta el programa con el siguiente comando:
   ```bash
   python risk_attack_strategy.py
   
## Ejemplo de salida

Territorios ordenados por prioridad (más débiles primero):
[{'defense': 10, 'terrain': 'plano'}, {'defense': 12, 'terrain': 'boscoso'}, {'defense': 15, 'terrain': 'montañoso'}]

Combinaciones de tropas posibles:
{'inf': 1, 'cav': 1, 'art': 3}
{'inf': 2, 'cav': 2, 'art': 2}
...

Representación del tablero:
Territory 1: Defensa = 10, Terreno = plano
Territory 2: Defensa = 12, Terreno = boscoso
Territory 3: Defensa = 15, Terreno = montañoso

Evento aleatorio: Tormenta afecta la caballería (-10% fuerza)
El ataque falló.

Evento aleatorio: Clima favorable aumenta la artillería (+10% fuerza)
¡Territorio conquistado! Quedan 3 puntos de ataque.

