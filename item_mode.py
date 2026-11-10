import game_framework
import game_world
from pico2d import clear_canvas, get_events, load_image, update_canvas
from sdl2 import SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE, SDLK_q


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key in (SDLK_q, SDLK_ESCAPE):
            game_framework.pop_mode()
            return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()
