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
    # Bar(monitor)
    # OSD(monitor)
    # Corners(monitor)
    # CornerLeft(monitor)
    # CornerTop(monitor)
    # CornerRight(monitor)
    # CornerBottom(monitor)
    # Dashboard(monitor)
    # SlideTopBar(monitor)
    PowerMenu()

    # Popout(
    #     anchor=["top", "left", "bottom"],
    #     layer="top",
    #     exclusivity="ignore",
    #     namespace="testing",
    #     css_classes=["bar-popout"],
    #     hide_delay=1000,
    #     visible=False,
    #     reveal_child=True,
    #     transition_type="slide_right",
    #     transition_duration=300,
    #     margin_top=64,
    #     margin_bottom=64,
    #     child=widgets.Box(
    #         hexpand=True,
    #         child=[
    #             widgets.CenterBox(
    #                 hexpand=True,
    #                 vertical=True,
    #                 start_widget=widgets.Label(label="start"),
    #                 center_widget=widgets.Label(label="center"),
    #                 end_widget=widgets.Label(label="end"),
    #             ),
    #         ]
    #     )
    # )

    # PopoutDarken(
    #     anchor=["top", "left", "bottom"],
    #     layer="top",
    #     exclusivity="ignore",
    #     namespace="testing",
    #     css_classes=["bar-popout"],
    #     hide_delay=200,
    #     visible=False,
    #     reveal_child=True,
    #     transition_type="slide_right",
    #     transition_duration=200,
    #     margin_top=64,
    #     margin_bottom=64,
    #     child=widgets.Box(
    #         hexpand=True,
    #         child=[
    #             widgets.CenterBox(
    #                 hexpand=True,
    #                 vertical=True,
    #                 start_widget=widgets.Label(label="start"),
    #                 center_widget=widgets.Label(label="center"),
    #                 end_widget=widgets.Label(label="end"),
    #             ),
    #         ]
    #     )
    # )
