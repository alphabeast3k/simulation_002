from map_editor_scene import MapEditorScene
from main_menu_scene import MainMenuScene
import pygame
import pygame_gui
from scene import Scene, SceneState, SceneManager

pygame.init()
window_size = (1200, 800)
running = True

def quit_game():
    global running
    running = False

def main():
    screen = pygame.display.set_mode(window_size)
    clock = pygame.time.Clock()

    ui_manager = pygame_gui.UIManager(window_size)

    scene_manager = SceneManager()

    main_menu_scene = MainMenuScene(SceneState.MAIN_MENU, (19, 42, 19), scene_manager, window_size)
    game_scene = Scene(SceneState.GAME, (49, 87, 44))
    paused_scene = Scene(SceneState.PAUSED, (79, 119, 45))
    settings_scene = Scene(SceneState.SETTINGS, (144, 169, 85))
    map_editor_scene = MapEditorScene(SceneState.MAP_EDITOR, (236, 243, 158))

    
    scene_manager.register_scene(main_menu_scene)
    scene_manager.register_scene(game_scene)
    scene_manager.register_scene(paused_scene)
    scene_manager.register_scene(settings_scene)
    scene_manager.register_scene(map_editor_scene)

    scene_manager.set_scene(SceneState.MAIN_MENU)

    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            
            # hacky work around to switch to main menu with M key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    scene_manager.set_scene(SceneState.MAIN_MENU)
            
            ui_manager.process_events(event)
            scene_manager.event_update(event)

        ui_manager.update(time_delta)
        scene_manager.update(time_delta)


        screen.fill((0, 0, 0))

        scene_manager.draw(screen)
        ui_manager.draw_ui(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
