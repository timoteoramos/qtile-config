from libqtile.config import Screen
from libqtile import bar, widget
from colors import colors

_top = {
    'background': '#222d32',
    'foreground': '#b7c1c5',
    'fontname': 'Noto Sans Regular',
    'inactive': '#6a7479'
}

screens = [
    Screen(
        bottom=bar.Bar([
            widget.GroupBox(active=colors['07'], borderwidth=1, disable_drag=True, inactive=colors['08'], this_current_screen_border=colors['02'], this_screen_border=colors['02'], urgent_border=colors['01']),
            widget.Prompt(foreground=colors['07']),
            widget.Spacer(),
            widget.TextBox('', foreground=colors['07'], fontsize=18),
            widget.CPUGraph(border_color=colors['07'], border_width=1, graph_color=colors['02'], line_width=1, type='line'),
            widget.TextBox('', foreground=colors['07'], fontsize=18),
            widget.HDDBusyGraph(border_color=colors['07'], border_width=1, device='sda', graph_color=colors['03'], line_width=1, type='line'),
            widget.TextBox('', foreground=colors['07'], fontsize=18),
            widget.NetGraph(border_color=colors['07'], border_width=1, graph_color=colors['01'], line_width=1, type='line'),
            widget.TextBox('﬘', foreground=colors['07'], fontsize=18),
            widget.Memory(foreground=colors['07']),
            widget.Battery(charge_char='', discharge_char='', foreground=colors['07'], low_foreground=colors['01']),

        ], 24, background=colors['00']),
        top=bar.Bar([
            widget.WindowName(font=_top['fontname'], foreground=_top['foreground']),
            widget.Systray(icon_size=24),
            widget.Clock(font=_top['fontname'], foreground=_top['foreground'], format='%d/%m/%Y  %a %H:%M %p'),
        ], 24, background=_top['background']),
    ),
]
