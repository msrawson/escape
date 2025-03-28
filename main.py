import pygame
import random


TEXT_OUTLINE = 2  # pixels thick (lower looks better close up)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen = pygame.display.set_mode(size=(1920, 1080)) #full HD
# screen = pygame.display.set_mode(size=(1366, 768))  # regular HD

clock = pygame.time.Clock()
running = True

minutes_left = 60.0
clock_speed = 1.0  # 1 means clock runs at true speed

office_background: pygame.Surface
steve_message: pygame.Surface
lisa_message: pygame.Surface

changing_timer = False
new_time = ""

hint_number = 0
hints = [
    "Check the skeletons\nin your closet,\nSteve!",
    "Check the skeletons\nin your closet!",
    "You reap\nwhat you sow,\nSteve!",
    "You reap\nwhat you sow!",
    "The missing piece\nwill reveal\nyour secrets,\nSteve!",
    "The missing piece\nwill reveal\nyour secrets!",
]


def load_image(file_path: str) -> pygame.Surface:
    global screen
    surface = pygame.image.load(file_path)
    return pygame.transform.scale(surface, screen.get_size())


def preload():
    global office_background, steve_message, lisa_message
    office_background = load_image("img/room1.jpeg")
    steve_message = load_image("img/Steve text.png")
    lisa_message = load_image("img/Lisa text.png")


def darken(surface: pygame.surface.Surface):
    surface.convert_alpha()


pygame.font.init()

preload()

screen.blit(office_background, (0, 0))

TIMER_MODE = 1
HINT_MODE = 2
MESSAGE_MODE = 3
FLICKER_MODE = 4
mode = TIMER_MODE
timer_running = False

FONT_NAME = "Georgia"

message_number = 0
escape_count = 0


def calculate_pixels_per_point() -> float:
    "Calculate pixels / points"
    global FONT_NAME
    font_size_pts = 500
    my_font = pygame.font.SysFont(FONT_NAME, font_size_pts)
    surface = my_font.render("TEST", False, "black")
    height = surface.get_rect().height
    return height / font_size_pts


pixels_per_point = calculate_pixels_per_point()


def draw_background() -> None:
    global screen, office_background
    office_background.convert()
    screen.blit(office_background, (0, 0))
    screen.fill((20, 20, 20), special_flags=pygame.BLEND_RGB_SUB)  # darken it


def draw_text(text: str, font_size: int | float) -> None:
    global screen, TEXT_OUTLINE, FONT_NAME, pixels_per_point
    my_font = pygame.font.SysFont(FONT_NAME, int(font_size + 0.5))
    lines = text.split("\n")
    line_height = font_size * pixels_per_point * 1.1
    x = screen.get_width() / 2
    y = screen.get_height() / 2 - (len(lines) - 1) * line_height / 2
    for line in lines:
        for i in range(5):
            surface = my_font.render(
                line, False, "black" if i < 4 else "yellow")
            dx = [-1, 0, 1, 0, 0][i] * TEXT_OUTLINE
            dy = [0, -1, 0, 1, 0][i] * TEXT_OUTLINE
            rect = surface.get_rect(center=(x + dx, y + dy))
            screen.blit(surface, rect)
        y += line_height


def draw_timer() -> None:
    global minutes_left, clock_speed, screen, pixels_per_point
    draw_background()
    minutes, seconds = divmod(int(minutes_left * 60), 60)
    draw_text(f"{minutes}:{seconds:02d}",
              screen.get_height() * 0.45 / pixels_per_point)


def draw_flicker() -> None:
    global screen
    screen.fill("Black")
    w = screen.get_width()
    h = screen.get_height()
    left = 0
    top = 0
    size = 20
    for x in range(0, w, size):
        for y in range(0, h, size):
            grey = random.randint(0, 255)
            pygame.draw.rect(screen, (grey, grey, grey), (x, y, size, size))
    draw_text("STAND BY", screen.get_height() * 0.4 / pixels_per_point)


def advance_time():
    global minutes_left, clock, timer_running
    if timer_running:
        minutes_left -= clock_speed * clock.get_time() / 60 / 1000


def select_mode(event_key) -> None:
    global mode, escape_count, timer_running, changing_timer, new_time, hint_number, message_number
    match event_key:
        case pygame.K_t:
            mode = TIMER_MODE
        case pygame.K_h:
            mode = HINT_MODE
            hint_number = 0
        case pygame.K_m:
            mode = MESSAGE_MODE
            message_number = 0
        case pygame.K_s:
            timer_running = not timer_running
        case pygame.K_ESCAPE:
            escape_count += 1
        case pygame.K_c:
            changing_timer = not changing_timer
            new_time = ""
        case pygame.K_f:
            mode = FLICKER_MODE


def panic_button() -> None:
    "Press the space bar at any time to jump back to Timer mode."
    global mode, changing_timer, new_time
    mode = TIMER_MODE
    changing_timer = False
    new_time = ""


def select_hint(event: pygame.event.Event):
    "Selecting hint zero will show the background and no hint."
    global mode, hint_number, hints
    if event.type != pygame.KEYDOWN or mode != HINT_MODE:
        return
    if event.unicode.isdigit():
        x = int(event.unicode)
        if x <= len(hints):  # deliberately allowing 0 here
            hint_number = x
    elif event.key == pygame.K_LEFT:
        hint_number = max(0, hint_number - 1)
    elif event.key == pygame.K_RIGHT:
        hint_number = min(len(hints), hint_number + 1)


def draw_hint() -> None:
    global hints, hint_number, screen, pixels_per_point
    draw_background()
    if 1 <= hint_number <= len(hints):
        draw_text(hints[hint_number - 1], screen.get_height()
                  * 0.22 / pixels_per_point)


def select_message(event: pygame.event.Event):
    global mode, message_number
    if event.type != pygame.KEYDOWN or mode != MESSAGE_MODE:
        return
    if event.unicode.isdigit():
        x = int(event.unicode)
        if x <= 2:  # deliberately allowing 0 here
            message_number = x
    elif event.key == pygame.K_LEFT:
        message_number = max(0, message_number - 1)
    elif event.key == pygame.K_RIGHT:
        message_number = min(2, message_number + 1)


def draw_message():
    global screen, steve_message, lisa_message, message_number
    if message_number == 1:
        screen.blit(steve_message, (0, 0))
    elif message_number == 2:
        screen.blit(lisa_message, (0, 0))
    else:
        draw_background()


def change_clock_speed(event_key):
    global clock_speed, mode
    if mode != TIMER_MODE:
        return
    match event_key:
        case pygame.K_PLUS | pygame.K_KP_PLUS | pygame.K_RIGHT:
            clock_speed = min(2.0, clock_speed + 0.1)  # 10 steps to 2x normal
        case pygame.K_MINUS | pygame.K_KP_MINUS | pygame.K_LEFT:
            clock_speed = max(0.5, clock_speed - 0.05)  # 10 steps to normal/2
        case pygame.K_ASTERISK | pygame.K_KP_MULTIPLY | pygame.K_UP | pygame.K_DOWN:
            clock_speed = 1.0


def game_over():
    global running
    draw_background()
    draw_text("GAME\nOVER!", 400)


def change_timer(event: pygame.event.Event):
    global changing_timer, new_time, minutes_left
    if not changing_timer:
        return
    if event.key == pygame.K_RETURN:
        try:
            global minutes_left
            new_time = float(new_time)
            if 0 <= new_time <= 60:
                minutes_left = new_time
        except ValueError:
            pass
        changing_timer = False
    else:
        new_time += event.unicode


frame = 0
while running:
    frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT or escape_count > 2:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.unicode == " ":
                panic_button()
            elif changing_timer:
                change_timer(event)
            else:
                select_mode(event.key)
                select_hint(event)
                select_message(event)
                change_clock_speed(event.key)

    advance_time()

    if minutes_left <= 0:
        game_over()
    elif mode == HINT_MODE:
        draw_hint()
    elif mode == MESSAGE_MODE:
        draw_message()
    elif mode == FLICKER_MODE:
        draw_flicker()
    else:
        draw_timer()

    # escape_count should die off fairly quickly
    if frame % 10 == 0 and escape_count > 0:
        escape_count -= 1

    # Update the screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS

pygame.quit()
