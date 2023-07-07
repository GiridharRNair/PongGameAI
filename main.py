from pong_game import PongGame
from menu import Menu
import pygame
import neat
import os
import pickle


def eval_genomes(genomes, config):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    for i, (genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0
        for genome_id2, genome2 in genomes[i + 1:]:
            genome2.fitness = 0 if genome2.fitness is None else genome2.fitness
            game = PongGame(window, width, height)
            game.train_ai(genome1, genome2, config)


def run_neat(config, file_name, generations):
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-27')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(15))

    # Runs NEAT's genetic algorithm for at most n generations, based on their fitness given from the eval_genomes
    winner = p.run(eval_genomes, generations)
    with open(file_name, 'wb') as f:
        pickle.dump(winner, f)


def test_ai(config, file_name):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))
    with open(file_name, 'rb') as f:
        winner = pickle.load(f)

    game = PongGame(window, width, height)
    game.test_ai(winner, config)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)

    config_paths = {
        'config_path_1': os.path.join(local_dir, "config_1.txt"),
        'config_path_2': os.path.join(local_dir, "config_2.txt"),
        'config_path_3': os.path.join(local_dir, "config_3.txt")
    }

    config = {
        'config_1': neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_paths['config_path_1']),
        'config_2': neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_paths['config_path_2']),
        'config_3': neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_paths['config_path_2'])
    }

    # run_neat(config['config_1'], 'difficulty_1.pickle', 1)
    # run_neat(config['config_2'], 'difficulty_2.pickle', 25)
    # run_neat(config['config_3'], 'difficulty_3.pickle', 50)

    test_ai(config['config_2'], Menu().draw())




