from ignis import widgets
from ignis.window_manager import WindowManager
from .widgets import (
    Clock,
    Workspaces,
    ActiveWindow,
    Tray,
)

window_manager = WindowManager.get_default()

class PowerMenuButton(widgets.Button):
    def __init__(self):
        super().__init__(
            child=widgets.Icon(
                image="system-shutdown-symbolic",
                pixel_size=16,
            ),
            on_click=lambda *_: window_manager.toggle_window("power-menu-revealer-window")
        )

class Bar(widgets.Window):
    def __init__(self, monitor):
        super().__init__(
            namespace=f"bar-window-{monitor}",
            monitor=monitor,
            anchor=["left", "top", "bottom"],
            layer="top",
            width_request=40,
            exclusivity="exclusive",
            kb_mode="none",
            css_classes=["bar-window"],
            child=widgets.Box(
                halign="center",
                css_classes=["bar-container"],
                child=[
                    widgets.CenterBox(
                        vertical=True,
                        halign="center",
                        css_classes=["bar"],
                        start_widget=widgets.Box(
                            vertical=True,
                            spacing=8,
                            child=[Workspaces()],
                        ),
                        center_widget=widgets.Box(
                            css_classes=["active-window"],
                            vertical=True,
                            valign="center",
                            width_request=30,
                            # child=[ActiveWindow()]
                            # NOTE: Not sure what to put in center yet
                            child=[],
                        ),
                        end_widget=widgets.Box(
                            vertical=True,
                            spacing=8,
                            child=[Tray(), Clock(), PowerMenuButton()],
                        ),
                        # style="margin-top: 24px; margin-bottom: 24px",
                    ),
                ],
            ),
        )
