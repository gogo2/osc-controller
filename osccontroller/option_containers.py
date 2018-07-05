from collections import namedtuple

ButtonOptions = namedtuple('ButtonOptions',
                           ['activebackground', 'activeforeground', 'anchor', 'background', 'bitmap', 'borderwidth',
                            'disabledforeground', 'font', 'foreground', 'highlightbackground', 'highlightcolor',
                            'highlightthickness', 'image', 'justify', 'padx', 'pady', 'relief', 'repeatdelay',
                            'repeatinterval', 'takefocus', 'textvariable', 'underline', 'wraplength', 'compound',
                            'default', 'height', 'cursor', 'overrelief', 'state', 'width'])
ButtonOptions.__new__.__defaults__ = (None,) * len(ButtonOptions._fields)

ScaleOptions = namedtuple('ScaleOptions',
                          ['activebackground', 'background', 'bigincrement', 'bd', 'bg', 'borderwidth', 'cursor',
                           'digits', 'fg', 'font', 'foreground', 'highlightbackground', 'highlightcolor',
                           'highlightthickness', 'label', 'length', 'orient', 'relief', 'repeatdelay', 'repeatinterval',
                           'resolution', 'showvalue', 'sliderlength', 'sliderrelief', 'state', 'takefocus',
                           'tickinterval', 'troughcolor', 'variable', 'width'])

ButtonOptions.__new__.__defaults__ = (None,) * len(ScaleOptions._fields)
