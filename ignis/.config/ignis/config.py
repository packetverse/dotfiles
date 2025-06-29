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
    #     # margin_top=64,
    #     # margin_bottom=64,
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

    PopoutDarken(
        anchor=["top", "left", "bottom"],
        layer="top",
        exclusivity="ignore",
        namespace="testing",
        css_classes=["bar-popout"],
        hide_delay=200,
        visible=False,
        reveal_child=True,
        transition_type="slide_right",
        transition_duration=200,
        # margin_top=64,
        # margin_bottom=64,
        child=widgets.Box(
            hexpand=True,
            child=[
                widgets.CenterBox(
                    hexpand=True,
                    vertical=True,
                    start_widget=widgets.Label(label="start"),
                    center_widget=widgets.Label(label="center"),
                    end_widget=widgets.Label(label="end"),
                ),
            ]
        )
    )

    # darken_overlay = widgets.Window(
    #     namespace="test-darken",
    #     exclusivity="ignore",
    #     anchor=["top", "bottom", "left", "right"],
    #     layer="overlay",
    #     kb_mode="none",
    #     child=widgets.Box(
    #         style="background-color: rgba(0, 0, 0, 0.25);",
    #         visible=False,
    #     ),
    #     visible=True,
    #     css_classes=["unset"],
    # )

    # darken_overlay.set_decorated(False)
    # darken_overlay.fullscreen()
    # darken_overlay.set_fullscreen()
    # .darken_overlay.set_app_paintable(True)
    # darken_overlay.set_can_focus(False)

    # rgba = Gdk.RGBA(0, 0, 0, 0.5)
    # darken_overlay.set_background_color(rgba)

    # darken_overlay.set_accept_focus(False)
    # darken_overlay.set_focusable(False)
    # darken_overlay.set_keep_above(True)
