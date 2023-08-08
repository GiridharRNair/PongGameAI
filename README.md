# Pong Game with NEAT AI

![PongGameAI](https://github.com/GiridharRNair/PongGameAI/assets/49298134/33de8a8d-e916-4346-a6a3-0da603e741fe)


This is a Pong game implemented using the Pygame library and integrated with NEAT 
(NeuroEvolution of Augmenting Topologies) AI algorithm. NEAT is an evolutionary algorithm that utilizes neural networks 
to evolve artificial intelligence. In this game, NEAT is used to train the AI opponent to learn and improve its gameplay 
over multiple generations. The AI evolves by adapting its neural network's structure and weights through a process of 
mutation and crossover. This allows the AI to learn and optimize its strategies for playing Pong. The game offers three 
difficulty modes: easy, medium, and hard. Each mode adjusts the AI opponent's skill level to provide different levels of 
challenge. Choose your preferred difficulty mode and test your skills against the AI. The game allows you 
to control the paddle using either the arrow keys or the 'W' and 'S' keys to move it up and down.

## Requirements
* Python 3.6 or above
* Pygame
* NEAT

## Run Locally
1. Install Python (if not already installed) from the official Python [website](https://www.python.org/).
2. Download or clone this repository to your local machine.
    ```bash
    git clone https://github.com/GiridharRNair/PongGameAI.git
    ```
3. Open a terminal or command prompt and navigate to the project directory.
    ```bash
    cd PongGameAI
    ```
4. Install all the dependencies, Pygame and NEAT.
    ```bash
    pip install neat-python pygame
    ```
5. Run the game using the following command:
    ```bash
    python main.py
    ```
6. The game will start, and you will be prompted to choose a difficulty level: easy, medium, or hard. 
Enter your choice and press Enter.
7. Enjoy playing Pong against an AI opponent!

## Credits
* This Project was inspired by the tutorial 
[video](https://www.youtube.com/watch?v=2f6TmKm7yx0) by Tech With Tim.
