from collections import namedtuple

ButtonOptions = namedtuple('ButtonOptions', ['text', 'osc_content', 'command', 'width', 'height', 'color', 'bg', 'fg'])
ButtonOptions.__new__.__defaults__ = (None, None, None, None, None, None, None)
