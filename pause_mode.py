import os

import game_framework
import game_world
from pico2d import *


def init():
    global font
    font_path = os.path.join(os.environ['WINDIR'], 'Fonts', 'malgun.ttf')
    font = load_font(font_path, 36)


def finish():
    global font
    del font


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
            return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    font.draw(270, 330, '일시정지 중', (255, 255, 255))
    update_canvas()
