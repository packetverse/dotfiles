from ignis.widgets import Widget
from ignis.app import IgnisApp

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib

EDGE_HEIGHT = 30     # px: hover-capture zone
BAR_HEIGHT = 30     # px: full bar height

class SlideTopBar:
    def __init__(self, monitor: int = 0):
        # 1) Hover zone: a thin always-visible overlay to detect pointer at top
        self.hover = Widget.Window(
            namespace="hover-zone",
            monitor=monitor,
            anchor=["left", "right", "top"],
            layer="overlay",
            exclusivity="ignore",
            dynamic_input_region=True,
            child=Widget.Box(
                height_request=EDGE_HEIGHT,
                # css_classes=["hover-zone"]
            )
        )

        # 2) Slide‑down bar using RevealerWindow
        revealer = Widget.Revealer(
            transition_type="slide_down",
            transition_duration=250,
            reveal_child=True,
            child=Widget.Box(
                height_request=BAR_HEIGHT,
                # css_classes=["slide-bar"],
                child=Widget.Label(label="👋 Slide‑down bar!")
            )
        )

        self.bar_win = Widget.Window(
            namespace="slide-bar",
            monitor=monitor,
            anchor=["left", "right", "top"],
            layer="overlay",
            exclusivity="ignore",
            dynamic_input_region=True,
            child=Widget.Box(child=[revealer])
        )
        # Attach the revealer so we can control it later
        self.bar_revealer = revealer

        # Connect motion event on hover zone
        motion = Gtk.EventControllerMotion()
        self.hover.add_controller(motion)
        motion.connect("motion", self.on_motion)
        motion.connect("leave", self.on_leave)

    def on_motion(self, controller, x, y):
        print(f"[DEBUG] Pointer at x={x} y={y}")
        # Only reveal when pointer is within hover zone
        if y <= EDGE_HEIGHT:
            self.bar_revealer.set_reveal_child(True)

    def on_leave(self, controller):
        # Delay hiding for a smoother experience
        GLib.timeout_add(300, lambda: self.bar_revealer.set_reveal_child(False))

