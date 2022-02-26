# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401from typing import List  # noqa: F401

mod = "mod4"            # Sets mod key to SUPER/WINDOWS
myTerm = "urxvt"        # My Terminal of choice
myBrowser = "firefox"   # My Browser of choice

keys = [
### The Keybindings 
         Key([mod], "b",                lazy.spawn(myBrowser)),
         Key([mod], "e",                lazy.spawn(myTerm + " -e ranger")),
         Key([mod], "r",                lazy.spawn("rofi -show drun -show-icons")),
         Key([mod], "x",                lazy.window.kill()),
         Key([mod], "Return",           lazy.spawn(myTerm)),
         Key([mod], "space",            lazy.next_layout()),
         Key([mod, "shift"], "r",       lazy.restart()),
         Key([mod, "shift"], "q",       lazy.shutdown()),
         Key([mod, "shift"], "Return",  lazy.spawn("dmenu_run -p '   '")),
         Key([mod, "control"], "r",     lazy.spawn("rofi -show run")), 
         Key([mod, "control"], "Return",lazy.spawn("xterm")), 
         Key(["control", "shift"], "e", lazy.spawn("emacsclient -c -a emacs")),
## Window Focus controls
         Key([mod], "s",                lazy.layout.down()),
         Key([mod], "w",                lazy.layout.up()),
         Key([mod], "a",                lazy.layout.left()),
         Key([mod], "d",                lazy.layout.right()),
## Move Focused window
         Key([mod, "shift"], "s",       lazy.layout.shuffle_down(), lazy.layout.section_down()),
         Key([mod, "shift"], "w",       lazy.layout.shuffle_up(), lazy.layout.section_up()),
         Key([mod, "shift"], "a",       lazy.layout.shuffle_left(), lazy.layout.section_left()),
         Key([mod, "shift"], "d",       lazy.layout.shuffle_right(), lazy.layout.section_right()),
## Grow Focused Window
         Key([mod, "control"], "w",     lazy.layout.grow_up(), lazy.layout.decrease_nmaster()),
         Key([mod, "control"], "s",     lazy.layout.grow_down(), lazy.layout.increase_nmaster()),
         Key([mod, "control"], "a",     lazy.layout.grow_left(), lazy.layout.increase_nmaster()),
         Key([mod, "control"], "d",     lazy.layout.grow_right(), lazy.layout.increase_nmaster()),
## Other Window Controls
         Key([mod], "n",                lazy.layout.normalize()),
         Key([mod], "m",                lazy.layout.maximize()),
         Key([mod, "shift"], "f",       lazy.window.toggle_floating()),
         Key([mod], "f",                lazy.window.toggle_fullscreen()),
### Stack controls
         Key([mod, "shift"], "Tab",     lazy.layout.rotate(),lazy.layout.flip()),
         Key([mod], "Tab",              lazy.layout.next()),
         Key([mod, "shift"], "space",   lazy.layout.toggle_split()),
]

groups = [Group("I", layout='monadtall'),
          Group("II", layout='monadtall'),
          Group("III", layout='bsp'),
          Group("IV", layout='bsp'),
          Group("V", layout='bsp'),
          Group("VI", layout='bsp'),
          Group("VII", layout='bsp'),
          Group("VIII", layout='bsp'),
          Group("IX", layout='max'),
          Group("X", layout='floating')]

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "6c5e5e",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    layout.Floating(**layout_theme),
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme)
    #layout.Stack(num_stacks=2),
]

colors = [["#282828", "#282828"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff7376", "#ff5155"],
          ["#6c5e5e", "#322b2b"],
          ["#f0c674", "#f0c67f"],
          ["#99cc99", "#83a598"],
          ["#d3869b", "#b16286"],
          ["#fabd2f", "#d79921"],
          ["#8ec07c", "#689d6a"]]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(font="Hack Nerd Font", fontsize = 13, padding = 2, background=colors[2])
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
            widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
            widget.Image(
                       filename = "~/.config/qtile/icons/python.png",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("rofi -show run")}
                       ),
            widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
            widget.GroupBox(
                       font = "Mononoki Nerd Font Bold",
                       fontsize = 11,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = '777777',
                       rounded = True,
                       hide_unused = True,
                       highlight_color = colors[0],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[3],
                       other_screen_border = colors[0],
                       foreground = colors[2],
                       background = colors[0]
                       ),
            widget.TextBox(
                       text = '\uE0B0',
                       font = "Hack Nerd Font",
                       background = colors[3],
                       foreground = colors[0],
                       padding = -3,
                       fontsize = 30
                       ),
            widget.TextBox(
                       text = '\uE0B0',
                       font = "Hack Nerd Font",
                       background = colors[4],
                       foreground = colors[3],
                       padding = -3,
                       fontsize = 30
                       ),
            widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5,
                       scale = 0.7
                       ),
            # widget.CurrentLayout(
            #           foreground = colors[2],
            #           background = colors[4],
            #           padding = 5
            #           ),
            widget.TextBox(
                       text = '\uE0B0',
                       font = "Hack Nerd Font",
                       background = colors[0],
                       foreground = colors[4],
                       padding = -3,
                       fontsize = 30
                       ),
            widget.WindowName(
                       font = "Hack Nerd Font Bold",
                       fontsize = 12,
                       foreground = colors[5],
                       background = colors[0],
                       padding =  8 
                       ),
            widget.Systray(
                       background = colors[4],
                       padding = 5
                       ),
            widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
            widget.TextBox(
                       text = '',
                       font = "Hack Nerd Font",
                       background = colors[0],
                       foreground = colors[3],
                       padding = -5,
                       fontsize = 30
                       ),
            widget.Net(
                       format = ' {down}↓↑{up}',
                       foreground = colors[1],
                       background = colors[3],
                       padding = 5
                       ),
            widget.TextBox(
                       text = '',
                       font = "Hack Nerd Font",
                       background = colors[3],
                       foreground = colors[5],
                       padding = -5,
                       fontsize = 30
                       ),
            widget.ThermalSensor(
                       foreground = colors[1],
                       background = colors[5],
                       threshold = 90,
                       fmt = ' {}',
                       padding = 5
                       ),
            widget.TextBox(
                       text = '',
                       font = "Hack Nerd Font",
                       background = colors[5],
                       foreground = colors[6],
                       padding = -5,
                       fontsize = 30
                       ),
            widget.Memory(
                       foreground = colors[1],
                       background = colors[6],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       fmt = '{}',
                       padding = 5
                       ),
            widget.TextBox(
                       text = '',
                       font = "Hack Nerd Font",
                       background = colors[6],
                       foreground = colors[7],
                       padding = -5,
                       fontsize = 30
                       ),
            widget.CPU(
                      foreground = colors[1],
                      background = colors[7],
                      format = ' {load_percent}% '
                      ),
            widget.TextBox(
                       text = '',
                       font = "Hack Nerd Font",
                       background = colors[7],
                       foreground = colors[8],
                       padding = -5,
                       fontsize = 30
                       ),
            widget.Volume(
                       foreground = colors[1],
                       background = colors[8],
                       fmt = '墳 {}',
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e alsamixer')},
                       padding = 5
                       # volume_down_command =
                       # volume_up_command =
                       ),
            widget.TextBox(
                       text = '',
                       font = "Hack Nerd Font",
                       background = colors[8],
                       foreground = colors[9],
                       padding = -5,
                       fontsize = 30
                       ),
            widget.Clock(
                       foreground = colors[1],
                       background = colors[9],
                       format = " %d %b,%a %H:%M "
                       ),
            widget.TextBox(
                       text = '',
                       font = "Hack Nerd Font",
                       background = colors[9],
                       foreground = colors[4],
                       padding = -4,
                       fontsize = 30
                       ),
            widget.Systray(
                       background = colors[4],
                       padding = 5
                       ),
            widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[2],
                       background = colors[4]
                       )
              ]
    return widgets_list
def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[9:10]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1
def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list
def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]
if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)
def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)
def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)
def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='alsamixer'),        # alsamixer 
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

wmname = "LG3D"           
