# Planificación de Ataques en el Juego Risk con Estrategias de Terreno

## Descripción
Este programa simula la planificación de ataques en el juego Risk, incorporando:
- Generación de combinaciones de tropas basadas en recursos limitados.
- Optimización mediante programación dinámica para maximizar las conquistas.
- Prioridad para atacar territorios más débiles primero.
- Estrategias basadas en el tipo de terreno para priorizar ciertos tipos de tropas.

## Funcionalidades Principales
1. **Generación de combinaciones de tropas:** Calcula todas las combinaciones posibles respetando los recursos disponibles y las restricciones mínimas de tropas.
2. **Optimización de conquistas:** Utiliza programación dinámica para seleccionar las combinaciones de tropas que maximizan los territorios conquistados.
3. **Prioridad a territorios más débiles:** Ordena los territorios enemigos por fuerza de defensa en orden ascendente.
4. **Estrategias de terreno:** Ajusta la fuerza de ataque según el tipo de terreno:
   - Caballería tiene ventaja en terrenos planos.
   - Artillería tiene ventaja en terrenos montañosos.
   - Infantería tiene ventaja en terrenos boscosos.

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
- **Territorios enemigos:**
  - Territorio 1: Defensa = 10, Terreno = Plano.
  - Territorio 2: Defensa = 15, Terreno = Montañoso.
  - Territorio 3: Defensa = 12, Terreno = Boscoso.
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
