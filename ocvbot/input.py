import logging as log
import random as rand

import pyautogui as pag

from ocvbot import CLIENT_WIDTH, CLIENT_HEIGHT
from ocvbot import misc


def click_coord(left, top, width, height, button='left'):
    """
    Clicks within the provided coordinates. If width and height are both
    0, then this function will click in the exact same location every
    time.

    Args:
        left (int): The left edge (x) of the coordinate space to click
                    within.
        top (int): The top edge (y) of the coordinate space to click
                   within.
        width (int): The x width of the coordinate space to randomize
                     the click within.
        height (int): The y height of the coordinate space to randomize
                      the click within.
        button (str): The mouse button to click with, default is left.

    Returns:
        Always returns 0.
    """
    move_to(left, top, xmin=0, xmax=width, ymin=0, ymax=height)
    click(button=button)
    return 0


def move_to(x, y, xmax, ymax, xmin=0, ymin=0,
            duration_min=50, duration_max=1500):
    """
    Moves the mouse pointer to the specified coordinates. Coordinates
    are relative to the display's dimensions. Units are in pixels.

    Args:
        x (int): The X coordinate to move the mouse to.
        y (int): The Y coordinate to move the mouse to.
        xmax (int): The maximum random pixel offset from x.
        ymax (int): The maximum random pixel offset from y.
        xmin  (int): The minimum random pixel offset from x, default is
                     0.
        ymin (int): The minimum random pixel offset from y, default is
                     0.
        duration_min (int): The minumum number of miliseconds to take to
                            move the mouse cursor to its destination,
                            default is 50.
        duration_max (int): The maximum number of miliseconds to take to
                            move the mouse cursor to its destination,
                            default is 1500.

    Returns:
        Always returns 0.
    """

    xrand = rand.randint(xmin, xmax)
    yrand = rand.randint(ymin, ymax)

    pag.moveTo((x + xrand),
               (y + yrand),
               move_duration(move_duration_min=duration_min,
                             move_duration_max=duration_max),
               move_path())
    return 0


def move_away(direction=rand.choice(['left', 'right'])):
    """
    Moves the mouse to a random spot on right half or the left half
    of the client window, away from wherever it clicked, to prevent
    tooltips from interfering with the script.

    Args:
        direction: Which side of the screen to move the mouse, by
                   default this function randomly selects between left
                   and right.

    Returns:
        Always returns 0.
    """

    log.debug('Moving mouse away towards ' + str(direction) +
              ' side of client.')
    misc.sleep_rand(0, 500)

    if direction == 'right':
        # TODO: Refactor this to input.move_to.
        pag.moveTo(
            (rand.randint((CLIENT_WIDTH / 2),
                          CLIENT_WIDTH)),
            (rand.randint(0, CLIENT_HEIGHT)),
            move_duration(), move_path())
        misc.sleep_rand(0, 500)

    elif direction == 'left':
        pag.moveTo(
            (rand.randint(0, (CLIENT_WIDTH / 2))),
            (rand.randint(0, CLIENT_HEIGHT)),
            move_duration(), move_path())
        misc.sleep_rand(0, 500)

    return 0


def move_to_neutral(x, y, xmin=50, xmax=300, ymin=300, ymax=500):
    """
    Moves the mouse to a 'neutral zone', away from any buttons or
    tooltop icons that could get in the way of the script. Units are in
    pixels.

    Args:
        xmin (int): The minimum X-distance to move, default is 50.
        xmax (int): The maximum X-distance to move, default is 300.
        ymin (int): The minimum Y-distance to move, default is 300.
        ymax (int): The maximum X-distance to move, default is 500.

    Returns:
        Always returns 0.
    """

    log.debug('Moving mouse towards neutral area.')

    move_to(x=x, y=y, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)
    return 0


def click(button='left',
          sleep_before_min=0, sleep_before_max=500,
          sleep_after_min=0, sleep_after_max=500,
          click_duration_min=0, click_duration_max=100):
    """
    Clicks the left or right mouse button, waiting before and after
    for a randomized period of time.

    Args:
        button (str): Which mouse button to click, default is left.
        sleep_before_min (int): Minimum number of miliseconds to
                                wait before clicking, default is 0.
        sleep_before_max (int): Maximum number of miliseconds to
                                wait before clicking, default is 500.
        sleep_after_min (int): Minimum number of miliseconds to
                               wait after clicking, default is 0.
        sleep_after_max (int): Maximum number of miliseconds to
                               wait after clicking, default is 500.
        click_duration_min (int): Minimum number of miliseconds to
                                  hold down the mouse button, default
                                  is 0.
        click_duration_max (int): Maximum number of miliseconds to
                                  hold down the mouse button, default is
                                  100.
    Returns:
        Always returns 0.
    """

    misc.sleep_rand(sleep_before_min, sleep_before_max)

    duration = misc.rand_seconds(rmin=click_duration_min,
                                 rmax=click_duration_max)

    log.debug('Holding down ' + button + ' mouse button for ' + str(duration) +
              ' seconds.')

    pag.click(button=button, duration=duration)
    misc.sleep_rand(sleep_after_min, sleep_after_max)
    return 0


def move_duration(move_duration_min=50, move_duration_max=1500):
    """
    Randomizes the amount of time the mouse cursor takes to move to a
    new location. Input arguments are in miliseconds but return value is
    in seconds.

    Args:
        move_duration_min (int): Minimum number of miliseconds the mouse
                                 pointer will take to move to its
                                 destination, default is 50.
        move_duration_max (int): Maximum number of miliseconds the mouse
                                 pointer will take to move to its
                                 destination, default is 1500.
    Returns:
        Returns a float.
    """

    move_duration_var = (misc.rand_seconds(move_duration_min,
                                           move_duration_max))
    return move_duration_var


def keypress(key,
             timedown_min=1, timedown_max=180,
             sleep_before_min=50, sleep_before_max=1000,
             sleep_after_min=50, sleep_after_max=1000):
    """
    Holds down the specified key for a random period of time. All
    values are in miliseconds.

    Args:
        key (str): The key on the keyboard to press, according to
                   PyAutoGUI.
        timedown_min (int): The shortest time the key can be
                            down, default is 1.
        timedown_max (int): The longest time the key can be
                            down, default is 180.
        sleep_before_min (int): The shortest time to wait before
                                pressing the key down, default is 50.
        sleep_before_max (int): The longest time to wait before
                                pressing the key down, default is 1000.
        sleep_after_min (int): The shortest time to wait after
                               releasing the key, default is 50.
        sleep_after_max (int): The longest time to wait after
                               releasing the key, default is 1000.
    Returns:
        Always returns 0.
    """

    log.debug('Pressing key: ' + str(key) + '.')
    misc.sleep_rand(sleep_before_min, sleep_before_max)
    pag.keyDown(key)
    misc.sleep_rand(timedown_min, timedown_max)
    pag.keyUp(key)
    misc.sleep_rand(sleep_after_min, sleep_after_max)
    return 0


def double_hotkey_press(key1, key2, timedown_min=5, timedown_max=190,
                        before_min=500, before_max=1000,
                        after_min=500, after_max=1000):
    """
    Performs a two-key hotkey shortcut, such as Ctrl-c for copying
    text.

    Args:
        key1 (str): The first hotkey used in the two-hotkey shortcut,
                    sometimes also called the modifier key.
        key2 (str): The second hotkey used in the two-hotkey shortcut.
        timedown_min (int): See keypress()'s docstring, default is 5.
        timedown_max (int): See keypress()'s docstring, default is 190.
        before_min (int): See keypress()'s docstring, default is 500.
        before_max (int): See keypress()'s docstring, default is 1000.
        after_min (int): See keypress()'s docstring, default is 500.
        after_max (int): See keypress()'s docstring, default is 1000.

    Returns:
        Always returns 0.
    """

    log.debug('Pressing hotkeys: ' + str(key1) + ' + ' + str(key2))
    misc.sleep_rand(before_min, before_max)
    pag.keyDown(key1)
    misc.sleep_rand(timedown_min, timedown_max)
    pag.keyDown(key2)
    misc.sleep_rand(timedown_min, timedown_max)
    pag.keyUp(key1)
    misc.sleep_rand(timedown_min, timedown_max)
    pag.keyUp(key2)
    misc.sleep_rand(after_min, after_max)
    return 0


def move_path():
    """
    Randomizes the movement behavior of the mouse cursor as it moves
    to a new location. One of 22 different movement patters is chosen at
    random.

    Returns:
        Returns a random PyAutoGUI function for different mouse
        movement.
    """

    # to do: implement bezier-curve mouse behavior
    # https://stackoverflow.com/questions/44467329/pyautogui-mouse-movement-with-bezier-curve
    rand_path = rand.randint(1, 22)
    if rand_path == 1:
        log.debug('Generated rand_path easeInQuad.')
        return pag.easeInQuad
    elif rand_path == 2:
        log.debug('Generated rand_path easeOutQuad.')
        return pag.easeOutQuad
    elif rand_path == 3:
        log.debug('Generated rand_path easeInOutQuad.')
        return pag.easeInOutQuad

    elif rand_path == 4:
        log.debug('Generated rand_path easeInQuart.')
        return pag.easeInQuart
    elif rand_path == 5:
        log.debug('Generated rand_path easeOutQuart.')
        return pag.easeOutQuart
    elif rand_path == 6:
        log.debug('Generated rand_path easeinOutQuart.')
        return pag.easeInOutQuart

    elif rand_path == 7:
        log.debug('Generated rand_path easeInQuint.')
        return pag.easeInQuint
    elif rand_path == 8:
        log.debug('Generated rand_path easeOutQuint.')
        return pag.easeOutQuint
    elif rand_path == 9:
        log.debug('Generated rand_path easeInOutQuint.')
        return pag.easeInOutQuint

    elif rand_path == 10:
        log.debug('Generated rand_path easeInBack.')
        return pag.easeInBack
    elif rand_path == 11:
        log.debug('Generated rand_path easeOutBack.')
        return pag.easeOutBack
    elif rand_path == 12:
        log.debug('Generated rand_path easeInOutBack.')
        return pag.easeInOutBack

    elif rand_path == 13:
        log.debug('Generated rand_path easeInCirc.')
        return pag.easeInCirc
    elif rand_path == 14:
        log.debug('Generated rand_path easeOutCirc.')
        return pag.easeOutCirc
    elif rand_path == 15:
        log.debug('Generated rand_path easeInOutCirc.')
        return pag.easeInOutCirc

    elif rand_path == 16:
        log.debug('Generated rand_path easeInSine.')
        return pag.easeInSine
    elif rand_path == 17:
        log.debug('Generated rand_path easeOutSine.')
        return pag.easeOutSine
    elif rand_path == 18:
        log.debug('Generated rand_path easeInOutSine.')
        return pag.easeInOutSine

    elif rand_path == 19:
        log.debug('Generated rand_path linear.')
        return pag.linear

    elif rand_path == 20:
        log.debug('Generated rand_path easeInExpo.')
        return pag.easeInExpo
    elif rand_path == 21:
        log.debug('Generated rand_path easeOutExpo.')
        return pag.easeOutExpo
    elif rand_path == 22:
        log.debug('Generated rand_path easeInOutExpo.')
        return pag.easeInOutExpo
    else:
        return 1
