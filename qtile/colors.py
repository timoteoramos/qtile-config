from os import path
import subprocess

colors = {}

subprocess.run(['xrdb', path.expanduser('~/.Xresources')])

for line in subprocess.run(['xrdb', '-query', '-all'], capture_output=True).stdout.decode('utf8').replace('\t', '').splitlines():
    p = line.split(':')

    if p[0].startswith('*color'):
        colors[p[0][6:].rjust(2, '0')] = p[1]
