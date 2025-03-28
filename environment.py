import numpy as np
from enums import Directions, Grid_State

class Environment:
    def __init__(self, grid, start_pos):
        self.grid = np.array(grid)
        self.rows, self.cols = self.grid.shape
        self.start_pos = tuple(start_pos)
        self.validate_start_position()
        self.agent_pos = self.start_pos
        self.cleaned_cells = set([self.start_pos])
        self.reachable_cells = self.compute_reachable_cells()
        self.total_to_clean = len(self.reachable_cells)
        self.grid[self.start_pos] = Grid_State.CLEANED.value
    
    def validate_start_position(self):
        x, y = self.start_pos
        if not (0 <= x < self.rows and 0 <= y < self.cols):
            raise ValueError("Start position out of bounds.")
        if self.grid[x][y] == 1:
            raise ValueError("Start position is an obstacle.")
    
    def compute_reachable_cells(self):
        visited = set()
        queue = [self.start_pos]
        visited.add(self.start_pos)
        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols:
                    if self.grid[nx, ny] == 0 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        return visited
    
    def get_neighbors(self):
        x, y = self.agent_pos
        neighbors = {}
        for direction in [Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT]:
            dx, dy = direction.value
            nx, ny = x + dx, y + dy
            if 0 > nx or nx >= self.rows or 0 > ny or ny >= self.cols:
                neighbors[direction] = (Grid_State.OBSTACLE)
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                neighbors[direction] = (Grid_State(self.grid[nx, ny]))
        return neighbors
    
    def move_agent(self, direction):
        cx, cy = self.agent_pos
        dx, dy = direction.value
        new_pos = (cx + dx, cy + dy) 
        if self.grid[new_pos] in (Grid_State.FREE.value, Grid_State.CLEANED.value):
            self.agent_pos = new_pos
            self.cleaned_cells.add(new_pos)
            self.grid[new_pos] = Grid_State.CLEANED.value
            return True
        return False
    
    def is_task_complete(self):
        return len(self.cleaned_cells) >= self.total_to_clean