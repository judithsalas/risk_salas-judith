# Planificación de Ataques en el Juego Risk

## Descripción
Este programa resuelve el problema de planificación de ataques en el juego Risk utilizando combinaciones óptimas de tropas y simulaciones de ataque a territorios enemigos. Incluye la generación de combinaciones de tropas basadas en recursos limitados, permutaciones del orden de ataque a los territorios y simulaciones de resultados de las batallas.

## Funcionalidades Principales
1. **Generación de combinaciones de tropas:** Calcula todas las combinaciones posibles de tropas respetando los recursos disponibles y las restricciones mínimas de unidades.
2. **Permutaciones del orden de ataque:** Genera todas las permutaciones posibles para el orden en el que se atacan los territorios enemigos.
3. **Representación del tablero:** Representa el tablero con una estructura de datos basada en diccionarios.
4. **Simulaciones de ataque:** Evalúa el resultado de las combinaciones de tropas y el orden de ataque para determinar los territorios conquistados.

## Datos Iniciales
- **Recursos disponibles:** 20 puntos.
- **Costos de tropas:**
  - Infantería: 1 punto por tropa.
  - Caballería: 3 puntos por tropa.
  - Artillería: 5 puntos por tropa.
- **Fuerza de las tropas:**
  - Infantería: 1 de fuerza.
  - Caballería: 3 de fuerza.
  - Artillería: 5 de fuerza.
- **Defensas de los territorios enemigos:**
  - Territorio 1: Defensa 10.
  - Territorio 2: Defensa 15.
  - Territorio 3: Defensa 12.
- **Restricciones mínimas:** Al menos 1 unidad de infantería, caballería y artillería.

## Uso

### Requisitos
- Python 3.x

### Ejecución
1. Clona o descarga el repositorio.
2. Asegúrate de tener Python instalado en tu sistema.
3. Ejecuta el programa con el siguiente comando:
   ```bash
   python risk_attack_strategy.py
