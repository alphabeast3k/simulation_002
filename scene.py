from enum import Enum

class SceneState(Enum):
    MAIN_MENU = 1
    GAME = 2
    PAUSED = 3
    SETTINGS = 4
    MAP_EDITOR = 5

class Scene():
    def __init__(self, scene_state: SceneState, background_color: tuple):
        self.state = scene_state
        self.background_color = background_color
    
    def draw(self, surface):
        surface.fill(self.background_color)
    
    def update(self, time_delta):
        pass

    def event_update(self, event):
        pass

class SceneManager():
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def register_scene(self, scene: Scene):
        self.scenes[scene.state] = scene
        print(f'Registered scene: {scene.state}')

    def set_scene(self, state: SceneState):
        print(f'Switching to scene: {state}')
        self.current_scene = self.scenes.get(state)

    def draw(self, surface):
        if self.current_scene:
            self.current_scene.draw(surface)

    def update(self, time_delta):
        if self.current_scene:
            self.current_scene.update(time_delta)

    def event_update(self, event):
        if self.current_scene:
            self.current_scene.event_update(event)
