from scene import Scene, SceneState, SceneManager
from pygame_gui import UIManager, UI_BUTTON_PRESSED
import pygame_gui
from pygame_gui.elements import UIButton
import pygame


class MainMenuScene(Scene):
    def __init__(self, scene_state: SceneState, background_color: tuple, scene_manager: SceneManager, window_size: tuple):
        super().__init__(scene_state, background_color)

        self.active_elements = []
        self.ui_manager = UIManager(window_size)

        self.active_elements.append(self.create_button((0,-100), 'Play', self.ui_manager, lambda: scene_manager.set_scene(
            SceneState.GAME
        )))

        self.active_elements.append(self.create_button((0,0), 'Settings', self.ui_manager, lambda: scene_manager.set_scene(
            SceneState.SETTINGS
        )))

        self.active_elements.append(self.create_button((0,100), 'Map Editor', self.ui_manager, lambda: scene_manager.set_scene(
            SceneState.MAP_EDITOR
        )))

        self.active_elements.append(self.create_button((0,200), 'Exit', self.ui_manager, lambda: pygame.event.post(pygame.event.Event(pygame.QUIT))))
    
    def draw(self, surface):
        super().draw(surface)
        surface.fill(self.background_color)

        self.ui_manager.draw_ui(surface)

    def event_update(self, event):
        if event.type == UI_BUTTON_PRESSED:
            if event.ui_element in self.active_elements:
                event.ui_element.on_click()
        
        self.ui_manager.process_events(event)
    
    def update(self, time_delta):
        self.ui_manager.update(time_delta)


    def create_button(self, position: tuple, text: str, ui_manager: UIManager, action) -> UIButton:
        button = UIButton(
            relative_rect=pygame.Rect(position, (200, 50)),
            text=text,
            manager=ui_manager,
            anchors={'centerx':'centerx',
                  'centery':'centery'}
        )

        button.on_click = action

        return button
        