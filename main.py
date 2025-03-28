import matplotlib.pyplot as plt
import numpy as np
import time
import argparse
from agents.a_star_agent import AStarAgent
from environment import Environment
from enums import Directions

def visualize(env):
    color_grid = np.zeros((env.rows, env.cols, 4))
    for x in range(env.rows):
        for y in range(env.cols):
            if env.grid[x, y] == 1:
                color_grid[x, y] = [0, 0, 0, 1]
            else:
                if (x, y) in env.cleaned_cells:
                    color_grid[x, y] = [0, 1, 0, 0.3]
                else:
                    color_grid[x, y] = [1, 1, 1, 1]
    ax, ay = env.agent_pos
    color_grid[ax, ay] = [1, 0, 0, 1]
    return color_grid

def simulate(env, visualize_step=True, step_delay=0.1):
    agent = AStarAgent()
    plt.ion()
    fig, ax = plt.subplots()
    img = ax.imshow(visualize(env), interpolation='nearest')
    plt.pause(0.5)
    
    steps = 0
    while True:
        agent.update_memory(env.get_neighbors())
        agent.clean()

        direction = agent.calculate_next_step()

        if not isinstance(direction, Directions):
            print(f"Code {direction}: Agent cannot move!")
            break

        agent.move(direction)
        env.move_agent(direction)
        steps += 1
        if visualize_step:
            img.set_data(visualize(env))
            fig.canvas.flush_events()
            time.sleep(step_delay)

    plt.ioff()
    plt.show()
    print(f"Task completed in {steps} steps. Cleaned {len(env.cleaned_cells)}/{env.total_to_clean} cells.")

if __name__ == "__main__":
    grid_simple = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    start_simple = (2, 3)

    grid_large = [
    [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
    [0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
    ]
    start_large = (21, 2)

    grid_complex = [
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,1,1,1,0,1,0,1,0,1,0,1,1,1,0],
    [0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
    [0,1,0,1,1,1,1,1,1,1,1,1,0,1,0],
    [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,1,1,1,0,1,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
    [1,1,0,1,1,1,0,1,0,1,1,1,0,1,1],
    [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
    [0,1,1,1,0,1,1,1,1,1,0,1,1,1,0],
    [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,1,0,1,1,1,1,1,1,1,1,1,0,1,0],
    [0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
    [0,1,1,1,0,1,0,1,0,1,0,1,1,1,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    ]
    start_complex = (7, 8)

    parser = argparse.ArgumentParser(description='Autonomous Cleaning Agent Simulation')
    parser.add_argument('--grid_choice', type=str, choices=['simple', 'complex', 'large'], default='large',
                        help='Grid type: simple, complex, or large (default: large)')
    parser.add_argument('--start_pos', nargs=2, type=int,
                        help='Custom start position (x y). Must be valid for chosen grid')
    args = parser.parse_args()

    grid_config = {
        'simple': (grid_simple, start_simple),
        'complex': (grid_complex, start_complex),
        'large': (grid_large, start_large)
    }

    selected_grid, default_start = grid_config[args.grid_choice]
    start_pos = tuple(args.start_pos) if args.start_pos else default_start

    try:
        env = Environment(selected_grid, start_pos)
        simulate(env, step_delay=0.05, visualize_step=True)
    except ValueError as e:
        print(f"Error: {str(e)}")