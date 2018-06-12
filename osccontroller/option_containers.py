from collections import namedtuple

ButtonOptions = namedtuple('ButtonOptions', ['activebackground', 'activeforeground', 'anchor',
                                             'background', 'bitmap', 'borderwidth', 'cursor',
                                             'disabledforeground', 'font', 'foreground',
                                             'highlightbackground', 'highlightcolor',
                                             'highlightthickness', 'image', 'justify',
                                             'padx', 'pady', 'relief', 'repeatdelay',
                                             'repeatinterval', 'takefocus', 'text',
                                             'textvariable', 'underline', 'wraplength'])
ButtonOptions.__new__.__defaults__ = (None,) * len(ButtonOptions._fields)
