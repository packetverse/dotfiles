from ignis import widgets
from .widgets import (
    Clock,
    Workspaces,
    ActiveWindow,
)

class Bar(widgets.Window):
    def __init__(self, monitor):
        super().__init__(
            namespace=f"bar-window-{monitor}",
            monitor=monitor,
            anchor=["left", "top", "bottom"],
            layer="top",
            width_request=30,
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
                        start_widget=widgets.Box(
                            vertical=True,
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
                            child=[Clock()],
                        ),
                        # style="margin-top: 24px; margin-bottom: 24px",
                    ),
                ],
            ),
        )
