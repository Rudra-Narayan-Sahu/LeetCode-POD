from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        sx = sy = -1
        litter_coords = []
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    sx, sy = r, c
                elif cell == 'L':
                    litter_coords.append((r, c))

        num_litter = len(litter_coords)
        if num_litter == 0:
            return 0
        target_mask = (1 << num_litter) - 1
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}

        best_energy = {}
        queue = deque([(sx, sy, 0, energy, 0)])
        best_energy[(sx, sy, 0)] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            x, y, mask, e, steps = queue.popleft()

            if mask == target_mask:
                return steps

            if e == 0:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    cell = classroom[nx][ny]
                    next_e = energy if cell == 'R' else e - 1
                    next_mask = mask

                    if cell == 'L' and (nx, ny) in litter_map:
                        next_mask |= (1 << litter_map[(nx, ny)])

                    state_key = (nx, ny, next_mask)
                    if state_key not in best_energy or best_energy[state_key] < next_e:
                        best_energy[state_key] = next_e
                        queue.append((nx, ny, next_mask, next_e, steps + 1))

        return -1