from scene import Scene, SceneState
from tile import Tile, TileType
import math
import pygame

def hexagon(center: tuple, size: int, rotation: float = 0):
    cx, cy = center
    points = []
    for i in range(6):
        angle = math.radians(60 * i - 30 + rotation)
        x = cx + size * math.cos(angle)
        y = cy + size * math.sin(angle)
        points.append((x, y))
    return points

class MapEditorScene(Scene):
    def __init__(self, scene_state: SceneState, background_color: tuple):
        super().__init__(scene_state, background_color)

    def draw(self, surface):
        super().draw(surface)
        surface.fill(self.background_color)

        #draw a square the size of the height
        square_size = surface.get_height()
        square_color = (255, 0, 0)
        map_area : pygame.Rect = pygame.draw.rect(surface, square_color, (0, 0, square_size, square_size))

        grass_tile = Tile(TileType.GRASS)
        grass_tile.draw(surface, (0, 0), square_size)

        # Additional drawing for the map editor can be added here


