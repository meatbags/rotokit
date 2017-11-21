Config = {
    'Global': {
        'Font': ('Arial', 9)
    },
    'Core': {
        'Easing': {
            'Default': 'EASING_LINEAR',
            'Linear': 'EASING_LINEAR',
            'In': 'EASING_EASE_IN',
            'Out': 'EASING_EASE_OUT',
            'InAndOut': 'EASING_EASING_IN_AND_OUT',
            'Soften': 'EASING_SOFTEN',
            'Centre': 'EASING_CENTRE'
        },
        'Weight': {
            'Length': 1,
            'CentreOfGravity': 1,
            'InternalAngle': 1
        }
    },
    'Root': {
        'InitialDimensions': '1060x640'
    },
    'Canvas': {
        'DefaultSize': (600, 400),
        'BackgroundColour': '#ffffff',
        'Padding': {
            'x': 16,
            'y': 16
        }
    },
    'PreviewCanvas': {
        'DefaultSize': (400, 250)
    },
    'Workspace': {
        'DefaultSize': (960, 540),
    },
    'Tool': {
        'FloatRadius': 4
    },
    'Tools': {
        'Draw': {
            'Select': 'TOOL_DRAW_SELECT',
            'Pen': 'TOOL_DRAW_PEN',
            'Brush': 'TOOL_DRAW_BRUSH',
            'Transform': 'TOOL_DRAW_TRANSFORM',
            'Hand': 'TOOL_DRAW_HAND',
            'Zoom': 'TOOL_DRAW_ZOOM',
            'Sculpt': 'TOOL_DRAW_SCULPT',
            'Mask': 'TOOL_DRAW_MASK'
        },
        'Transfer': {
            'Transfer': 'TOOL_TRANSFER_TRANSFER',
            'Proxy': 'TOOL_TRANSFER_PROXY'
        },
        'Match': {
            'Match': 'TOOL_MATCH_MATCH',
            'Break': 'TOOL_MATCH_BREAK',
            'Conform': 'TOOL_MATCH_CONFORM',
            'Highlight': 'TOOL_MATCH_HIGHLIGHT'
        },
        'Preview': {
            'Render': 'TOOL_PREVIEW_RENDER',
            'RealTime': 'TOOL_PREVIEW_REAL_TIME'
        }
    },
    'Menu': {
        'File': {
            'New': {'ID': 'MENU_FILE_NEW', 'Shortcut': 'Ctrl+N'},
            'Open': {'ID': 'MENU_FILE_OPEN', 'Shortcut': 'Ctrl+O'},
            'Save': {'ID': 'MENU_FILE_SAVE', 'Shortcut': 'Ctrl+S'},
            'Save As': {'ID': 'MENU_FILE_SAVEAS', 'Shortcut': 'Ctrl+Alt+S'},
            'Close': {'ID': 'MENU_FILE_CLOSE', 'Shortcut': 'Ctrl+X'},
        },
        'Frame': {
            'New': {'ID': 'MENU_FRAME_NEW', 'Shortcut': 'Ctrl+F'},
        },
        'About': {
            'About': {'ID': 'MENU_ABOUT_ABOUT', 'Shortcut': ''},
        }
    },
};
