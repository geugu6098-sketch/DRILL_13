import game_framework
from pico2d import *
import game_world
from boy import Boy
from grass import Grass


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode
            game_framework.push_mode(pause_mode)
            return
        else:
            boy.handle_event(event)


def init():
    global boy
    game_world.clear()
    grass = Grass()
    game_world.add_object(grass, 0)
    boy = Boy()
    game_world.add_object(boy, 1)


def update():
    game_world.update()


def pause():
    pass


def resume():
    pass


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()
