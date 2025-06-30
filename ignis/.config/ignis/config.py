from pathlib import Path
from ignis.app import IgnisApp
from ignis import widgets
from ignis import utils
from modules import (
    Bar,
    OSD,
    Corners,
    CornerLeft,
    CornerTop,
    CornerRight,
    CornerBottom,
    Dashboard,
    SlideTopBar,
    PowerMenu
)

from modules.shared_widgets import (
    Popout,
    PopoutDarken,
)

from gi.repository import Gdk

scss = str(Path(__file__).parent.resolve() / "styles" / "default.scss")
app = IgnisApp.get_default()
app.apply_css(scss)

for monitor in range(utils.get_n_monitors()):
    Bar(monitor)
    # OSD(monitor)

    PowerMenu()
