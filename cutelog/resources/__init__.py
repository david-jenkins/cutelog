

from importlib.resources import files, as_file
from qtpy.QtGui import QIcon

theme_icons = {
    'cross' : "ion-cross.svg",
    'check' : "ion-check.svg",
    'search' : "ion-search.svg",
    'arrow-up' : "ion-up.svg",
    'arrow-down' : "ion-down.svg",
    'arrow-left' : "ion-left.svg",
    'arrow-right' : "ion-right.svg",
}

light_theme_qss = files("cutelog.resources").joinpath("light_theme.qss").read_text()
dark_theme_qss = files("cutelog.resources").joinpath("dark_theme.qss").read_text()

for key,value in theme_icons.items():
    with as_file(files("cutelog.resources").joinpath("icons").joinpath("light_theme").joinpath(value)) as icon_path:
        light_theme_qss = light_theme_qss.replace(":/light_theme/icons/"+key, str(icon_path))
    with as_file(files("cutelog.resources").joinpath("icons").joinpath("dark_theme").joinpath(value)) as icon_path:
        dark_theme_qss = dark_theme_qss.replace(":/dark_theme/icons/"+key, str(icon_path))

with as_file(files("cutelog.resources").joinpath("images").joinpath("cutelog.png")) as cutelog_icon_path:
    cutelog_icon_path = str(cutelog_icon_path)