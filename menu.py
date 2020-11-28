import pygame
import pygame_menu
from pygame_menu.themes import Theme
from pygame_menu import sound
from app import start

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.mixer.init()

engine = sound.Sound()
engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'static/audio/mouse-click.ogg')
pygame.mixer.music.load("static/audio/background.ogg")


def start_the_game():
    # Do the job here !
    color = color_settings_button.get_value()[0]
    level = level_settings_button.get_value()[0]
    return start(level=level, color=color)


def set_level(value, difficulty):
    pass


def set_color(value, difficulty):
    pass


mytheme = Theme(background_color=(0, 0, 0, 0),  # transparent background
                title_shadow=False,
                title_background_color=(0, 0, 0))

myimage = pygame_menu.baseimage.BaseImage(
    image_path='static/images/bck.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
    drawing_offset=(0, 0)
)
mytheme.background_color = myimage

menu = pygame_menu.Menu(768, 1024, '',
                        theme=mytheme)

menu.add_vertical_margin(100)

new_font = pygame_menu.font.FONT_8BIT

settings = pygame_menu.Menu(768, 1024, '',
                            theme=mytheme)
menu.set_sound(engine, recursive=True)
settings.set_sound(engine, recursive=True)

# buttons
name_button = menu.add_text_input('', default='Username', font_name=new_font, font_size=30)
menu.add_vertical_margin(20)
play_button = menu.add_button('Play', start_the_game, font_name=new_font, font_size=30)
menu.add_vertical_margin(20)
setting_button = menu.add_button('Settings', settings, font_name=new_font, font_size=30)
menu.add_vertical_margin(20)
exit_button = menu.add_button('Exit', pygame_menu.events.EXIT, font_name=new_font, font_size=30)

level_settings_button = settings.add_selector('Select map ',
                                              [('SKELD', 'SKELD'),
                                               ('MIRA HQ', 'MIRA HQ')],
                                              onchange=set_level,
                                              selector_id='select_level', font_name=new_font, font_size=30)
settings.add_vertical_margin(30)
color_settings_button = settings.add_selector('Select color ',
                                              [('Green', 'Green'),
                                               ('Blue', 'Blue')],
                                              onchange=set_color,
                                              selector_id='select_color', font_name=new_font, font_size=30)

settings.add_vertical_margin(50)

return_button = settings.add_button('Return to menu', pygame_menu.events.BACK, font_name=new_font, font_size=15)

pygame.mixer.music.play(loops=-1)

while True:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == settings:
            settings

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen, clear_surface=True)

    pygame.display.update()
