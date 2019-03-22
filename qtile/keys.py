from libqtile.command import lazy
from libqtile.config import Click, Drag, Key
from groups import groups
from misc import mod

keys = [
    # Bsp layout recommended shortcuts
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),
    Key([mod], 'h', lazy.layout.left()),
    Key([mod], 'l', lazy.layout.right()),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up()),
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
    Key([mod, 'mod1'], 'j', lazy.layout.flip_down()),
    Key([mod, 'mod1'], 'k', lazy.layout.flip_up()),
    Key([mod, 'mod1'], 'h', lazy.layout.flip_left()),
    Key([mod, 'mod1'], 'l', lazy.layout.flip_right()),
    Key([mod, 'control'], 'j', lazy.layout.grow_down()),
    Key([mod, 'control'], 'k', lazy.layout.grow_up()),
    Key([mod, 'control'], 'h', lazy.layout.grow_left()),
    Key([mod, 'control'], 'l', lazy.layout.grow_right()),
    Key([mod, 'shift'], 'n', lazy.layout.normalize()),

    # Inherited from default configuration
    Key([mod], 'space', lazy.layout.next()),
    Key([mod, 'shift'], 'space', lazy.layout.rotate()),
    Key([mod, 'shift'], 'Return', lazy.layout.toggle_split()),
    Key([mod], 'Tab', lazy.next_layout()),
    Key([mod], 'w', lazy.window.kill()),
    Key([mod, 'control'], 'r', lazy.restart()),
    Key([mod, 'control'], 'q', lazy.shutdown()),
    Key([mod], 'r', lazy.spawncmd()),

    # 3rd party shortcuts
    Key([mod], 'Return', lazy.spawn('xst')),
    Key([mod], 'd', lazy.spawn('rofi -show combi')),
    Key(['control', 'mod1'], 'l', lazy.spawn('xautolock -locknow')),
    Key([], 'Print', lazy.spawn("scrot '%Y%m%d%H%M%S_$wx$h_screenshot.png' -e 'mv $f ~/Imagens/scrot/'")),
]

for group in groups:
    keys.extend([
        Key([mod], group.name, lazy.group[group.name].toscreen()),
        Key([mod, 'shift'], group.name, lazy.window.togroup(group.name)),
    ])

# Drag floating layouts.
mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front())
]
