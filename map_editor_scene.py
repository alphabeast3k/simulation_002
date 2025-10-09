from scene import Scene, SceneState
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
        pygame.draw.rect(surface, square_color, (0, 0, square_size, square_size))

        hex_points = hexagon((300, 300), 20, 90)
        pygame.draw.polygon(surface, (0, 255, 0), hex_points)

        hex_points_1 = hexagon((331, 318), 20, 90)
        pygame.draw.polygon(surface, (0, 200, 0), hex_points_1)

        hex_points_1 = hexagon((331, 282), 20, 90)
        pygame.draw.polygon(surface, (0, 150, 0), hex_points_1)

        # Additional drawing for the map editor can be added here


