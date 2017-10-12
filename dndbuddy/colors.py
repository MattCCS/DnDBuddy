
def _color(string, ansi, bold=False):
    """Colors the given string with the given ANSI color index."""
    return "\x1b[1;{}m{}\x1b[0m".format(ansi, string)


def green(string):
    return _color(string, 32)


def yellow(string):
    return _color(string, 33)


def red(string):
    return _color(string, 31)
