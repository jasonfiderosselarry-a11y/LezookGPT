BOLD = "\033[1m"
# theme.py - Thème ANSI simple pour l'interface terminal LezookGPT

import os
import shutil
import sys

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_BLUE = "\033[44m"


def _supports_color():
    try:
        return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()
    except Exception:
        return False


def clear_console():
    """Clear terminal screen in a cross-platform way."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def _terminal_width(default=80):
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return default


def _center_lines(text):
    width = _terminal_width()
    return "\n".join(line.center(width) for line in text.splitlines())


def _color(text, code):
    if _supports_color():
        return f"{code}{text}{RESET}"
    return text


def banner(name="LezookGPT"):
    bar = _color("=" * 60, CYAN + BOLD)
    title = _color(f"  {name} - ASSISTANT OFFENSIF MODULAIRE v1.0  ", MAGENTA + BOLD)
    subtitle = _color("Un assistant local orienté analyse et discussion interactive sur la cybersec", CYAN + DIM)
    block = f"{bar}\n{title}\n{subtitle}\n{bar}"
    return _center_lines(block)


def big_banner():
    # ASCII art for LEZOOKGPT (simple, multi-line)
    art = r"""
██╗     ███████╗███████╗ ██████╗  ██████╗ ██╗  ██╗
██║     ██╔════╝╚══███╔╝██╔═══██╗██╔═══██╗██║ ██╔╝
██║     █████╗    ███╔╝ ██║   ██║██║   ██║█████╔╝ 
██║     ██╔══╝   ███╔╝  ██║   ██║██║   ██║██╔═██╗ 
███████╗███████╗███████╗╚██████╔╝╚██████╔╝██║  ██╗
╚══════╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
"""
    header = _color(art, MAGENTA + BOLD)
    contact = (
        _color("\t\tContact:", BOLD + CYAN) + " +261 34 06 604 50 | "
        + _color("email:", BOLD + CYAN) + " jason.fiderosse.larry@gmail.com"
    )
    credit = _color("\t\tCréé par Jason (LeszooksHacker)", DIM + YELLOW)
    repo = _color("\t\thttps://github.com/jasonfiderosselarry-a11y", BLUE + BOLD)
    Info = _color("\t     Info:", BOLD + CYAN) + " Un IA pour l'usage offensif sur le sécurité"
    block = f"{header}\n{contact}\n{credit}\n{repo}\n{Info}\n"
    return _center_lines(block)


def small_banner(text):
    return _color(text, BOLD + BLUE)


def prompt_label(text):
    return _color(text, BOLD + BLUE)


def info(text):
    return _color(text, GREEN)


def success(text):
    return _color(text, GREEN + BOLD)


def warn(text):
    return _color(text, YELLOW)


def error(text):
    return _color(text, RED + BOLD)
