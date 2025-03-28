import numpy as np
from agents.agent import Agent
from enums import Grid_State, Directions
from heapq import heappush, heappop
from collections import defaultdict

class AStarAgent():

    def __init__(self):
        self.memory = {}
        self.position = (0, 0)
        self.last_goal = None
        self.cached_path = []

        self.memory[self.position] = Grid_State.FREE


    def clean(self):
        self.memory[self.position] = Grid_State.CLEANED

    
    def update_memory(self, cells):
        for direction in cells.keys():
            dx, dy = direction.value
            cx, cy = self.position
            self.memory[(cx + dx, cy + dy)] = Grid_State(cells[direction])


    def move(self, direction):
        
        dx, dy = direction.value
        cx, cy = self.position

        self.position = (dx + cx, dy + cy)

    def get_direction(self, next_step):

        cx, cy = self.position
        nx, ny = next_step

        if cx - nx == 1: return Directions.UP
        if cx - nx == -1: return Directions.DOWN
        if cy - ny == 1: return Directions.LEFT
        if cy - ny == -1: return Directions.RIGHT


    def is_frontier(self, cell):

        if self.memory.get(cell) != Grid_State.FREE:
            return False
        
        x, y = cell
        all_neighbors_cleaned = True
        for dx, dy in [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value, Directions.RIGHT.value]:
            if (x+dx, y+dy) not in self.memory:
                return True
            if not self.memory[x+dx, y+dy] == Grid_State.CLEANED:
                False
            
        return all_neighbors_cleaned
    
    def get_frontiers(self):
        return [cell for cell in self.memory if self.is_frontier(cell)]
    
    def get_num_adjacent_unknowns(self, cell):

        num_adjacent_unknowns = 0
        
        x, y = cell
        for dx, dy in [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value, Directions.RIGHT.value]:
            if (x+dx, y+dy) not in self.memory:
                num_adjacent_unknowns += 1

        return num_adjacent_unknowns
    
    def manhattan(self, current_cell, target_cell):
        cx, cy = current_cell
        tx, ty = target_cell

        return abs(cx - tx) + abs(cy - ty)

    
    def heuristic(self, current_cell, target_cell):

        return max(0, self.manhattan(current_cell, target_cell) - self.get_num_adjacent_unknowns(current_cell))    
    
    
    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path
    
    def get_valid_neighbors(self, cell):
        x, y = cell
        directions = [Directions.UP.value, Directions.DOWN.value, Directions.LEFT.value, Directions.RIGHT.value]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if self.memory.get((nx, ny)) in [Grid_State.FREE, Grid_State.CLEANED]:
                neighbors.append((nx, ny))
        return neighbors


    def reverse_a_star(self, frontiers):

        open_set = []
        came_from = {}
        g = defaultdict(lambda: float('inf'))
        visited = set()

        for frontier in frontiers:
            g[frontier] = 0
            h = self.heuristic(frontier, self.position)
            f = g[frontier] + h
            heappush(open_set, (f, frontier))

        while open_set:
            f_score, current = heappop(open_set)

            if current in visited:
                continue
            visited.add(current)

            if current == self.position:
                return self.reconstruct_path(came_from, self.position)

            for neighbor in self.get_valid_neighbors(current):
                tentative_g = g[current] + 1
                if tentative_g < g[neighbor]:
                    came_from[neighbor] = current
                    g[neighbor] = tentative_g
                    h = self.heuristic(neighbor, self.position)
                    f = g[neighbor] + h
                    heappush(open_set, (f, neighbor))

        return None

    def calculate_next_step(self):

        if not self.cached_path or self.position == self.last_goal:
            frontiers = self.get_frontiers()
            if not frontiers:
                free_cells = [
                    cell for cell, state in self.memory.items() 
                    if state == Grid_State.FREE
                ]
                if not free_cells:
                    return 0
                
                path = self.reverse_a_star(free_cells)
                if not path:
                    return -1
                
                self.cached_path = path[1:]
                self.last_goal = path[-1]
            else:
                path = self.reverse_a_star(frontiers)
                if not path:
                    return -1
                
                self.cached_path = path[1:]
                self.last_goal = path[-1]

        if self.cached_path:
            next_step = self.cached_path.pop(0)
            direction = self.get_direction(next_step)
            return direction

        return -1