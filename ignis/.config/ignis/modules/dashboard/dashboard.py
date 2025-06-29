from ignis.widgets import Widget

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class DashboardRevealer(Widget.Revealer):
    def __init__(self):
        super().__init__(
            hexpand=True,
            # css_classes=["dashboard-revealer"],
            transition_type="slide_down",
            height_request=30,
            transition_duration=500,
            reveal_child=False,
            child=Widget.CenterBox(
                # css_classes=["dashboard-center-box"],
                hexpand=True,
                center_widget=Widget.Label(label="animation!!!")
            ),
        )

class DashboardContainer(Widget.EventBox):
    def __init__(self):
        self.revealer = DashboardRevealer()
        super().__init__(
            visible=True,
            height_request=30,
            hexpand=True,
            margin_top=64,
            on_hover=self.on_hover,
            on_hover_lost=self.on_hover_lost,
            child=[self.revealer],
        )

    def on_hover(self, widget):
        print("EventBox is hovered")
        self.revealer.set_reveal_child(True)

    def on_hover_lost(self, widget):
        print("EventBox is no longer hovered")
        self.revealer.set_reveal_child(False)

class Dashboard(Widget.Window):
    def __init__(self, monitor):
        self.dashboard = DashboardRevealer()

        super().__init__(
            namespace=f"dashboard-{monitor}",
            monitor=monitor,
            exclusivity="ignore",
            layer="overlay",
            kb_mode="none",
            # css_classes=["dashboard-window"],
            anchor=["left", "top", "right"],
            popup=False,
            visible=True,
            child=Widget.Box(
                hexpand=True,
                child=[
                    DashboardContainer(),
                ],
            ),
        )

    def on_hover(self):
        self.dashboard.set_visible(True)

    def on_hover_lost(self):
        self.dashboard.set_visible(False)
