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

    main_menu_scene = Scene(SceneState.MAIN_MENU, (19, 42, 19))
    game_scene = Scene(SceneState.GAME, (49, 87, 44))
    paused_scene = Scene(SceneState.PAUSED, (79, 119, 45))
    settings_scene = Scene(SceneState.SETTINGS, (144, 169, 85))

    scene_manager = SceneManager()
    scene_manager.add_scene(main_menu_scene)
    scene_manager.add_scene(game_scene)
    scene_manager.add_scene(paused_scene)
    scene_manager.add_scene(settings_scene)

    scene_manager.set_scene(SceneState.SETTINGS)

    play_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((100, 100), (200, 50)),
        text='Play',
        manager=ui_manager
    )
    play_button.on_click = lambda: scene_manager.set_scene(SceneState.GAME)

    settings_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((100, 200), (200, 50)),
        text='Settings',
        manager=ui_manager
    )
    settings_button.on_click = lambda: scene_manager.set_scene(SceneState.SETTINGS)

    exit_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((100, 300), (200, 50)),
        text='Exit',
        manager=ui_manager
    )
    exit_button.on_click = lambda: quit_game()

    active_elements = [play_button, settings_button, exit_button]

    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element in active_elements:
                  event.ui_element.on_click()

            ui_manager.process_events(event)

        ui_manager.update(time_delta)

        screen.fill((0, 0, 0))

        scene_manager.draw(screen)
        ui_manager.draw_ui(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
