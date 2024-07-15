# Pong_game

Ett enkelt Pong-spel skrivet i Python med hjälp av Pygame-biblioteket. Spelet innehåller två paddlar som styrs av två spelare och en boll. Målet är att få bollen att gå förbi motståndarens paddel. Varje gång en spelare lyckas med detta får den spelaren en poäng.

## Installation

För att köra detta spel behöver du ha Python och Pygame installerat.

### Steg för steg guide:

1. **Installera Pygame**:
    Öppna terminalen eller kommandotolken och kör följande kommando:
    ```sh
    pip install pygame
    ```

## Hur man kör spelet

1. Klona eller ladda ner detta repository.
2. Navigera till mappen där du har sparat spelet.
3. Kör följande kommando för att starta spelet:
    ```sh
    python pong_game.py
    ```

## Spelkontroller

- **Vänster paddel**:
    - Upp: `W`
    - Ner: `S`

- **Höger paddel**:
    - Upp: `Uppåtpilen (↑)`
    - Ner: `Nedåtpilen (↓)`

## Spelregler

- Varje gång bollen passerar en paddel får den motsatta spelaren en poäng.
- Spelet fortsätter tills du stänger av det.

## Kodstruktur

```python
pong_game.py 
