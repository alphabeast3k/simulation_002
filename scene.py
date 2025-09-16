from enum import Enum

class SceneState(Enum):
    MAIN_MENU = 1
    GAME = 2
    PAUSED = 3
    SETTINGS = 4

class Scene():
    def __init__(self, scene_state: SceneState, background_color: tuple):
        self.state = scene_state
        self.background_color = background_color
    
    def draw(self, surface):
        surface.fill(self.background_color)

class SceneManager():
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, scene: Scene):
        self.scenes[scene.state] = scene

    def set_scene(self, state: SceneState):
        self.current_scene = self.scenes.get(state)

    def draw(self, surface):
        if self.current_scene:
            self.current_scene.draw(surface)
