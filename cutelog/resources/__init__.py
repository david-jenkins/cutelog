

from importlib import resources

theme_icons = {
    'cross' : "ion-cross.svg",
    'check' : "ion-check.svg",
    'search' : "ion-search.svg",
    'arrow-up' : "ion-up.svg",
    'arrow-down' : "ion-down.svg",
    'arrow-left' : "ion-left.svg",
    'arrow-right' : "ion-right.svg",
}

light_theme_qss = resources.files("cutelog.resources").joinpath("light_theme.qss").read_text()
dark_theme_qss = resources.files("cutelog.resources").joinpath("dark_theme.qss").read_text()

for key,value in theme_icons.items():
    light_theme_qss = light_theme_qss.replace(":/light_theme/icons/"+key, str(resources.files("cutelog.resources.icons.light_theme").joinpath(value)))
    dark_theme_qss = dark_theme_qss.replace(":/dark_theme/icons/"+key, str(resources.files("cutelog.resources.icons.dark_theme").joinpath(value)))

cutelog_icon_path = str(resources.files("cutelog.resources.images").joinpath("cutelog.png"))