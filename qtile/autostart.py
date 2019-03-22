from libqtile import hook
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(['/usr/libexec/polkit-mate-authentication-agent-1'])
    subprocess.Popen(['xautolock', '-time', '5', '-locker', '/usr/bin/slock', '-nowlocker', '/usr/bin/slock'])
    subprocess.Popen(['pulseaudio', '--start', '-D'])
