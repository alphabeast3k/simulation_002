from scene import Scene, SceneState
import pygame


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
        # Additional drawing for the map editor can be added here
