from ignis import widgets

class CornerLeft(widgets.Window):
    def __init__(self, monitor):
        super().__init__(
            namespace=f"corners-window-left-{monitor}",
            monitor=monitor,
            exclusivity="exclusive",
            layer="top",
            kb_mode="none",
            css_classes=["screen-border-left-window"],
            anchor=["top", "left", "bottom"],
            child=widgets.Box(
                css_classes=["screen-border-left"],
                child=[
                    widgets.CenterBox(
                        vertical=True,
                        vexpand=True,
                        start_widget=widgets.Label(label="l"),
                        center_widget=widgets.Label(label="l"),
                        end_widget=widgets.Label(label="l"),
                    ),
                ],
            ),
        )

class CornerTop(widgets.Window):
    def __init__(self, monitor):
        super().__init__(
            namespace=f"corners-window-top-{monitor}",
            monitor=monitor,
            exclusivity="exclusive",
            layer="top",
            kb_mode="none",
            css_classes=["screen-border-top-window"],
            anchor=["left", "top", "right"],
            child=widgets.Box(
                css_classes=["screen-border-top"],
                child=[
                    widgets.CenterBox(
                        setup=lambda self: self.set_size_request(10, 10),
                        hexpand=True,
                        start_widget=widgets.Label(label="t"),
                        center_widget=widgets.Label(label="t"),
                        end_widget=widgets.Label(label="t"),
                    ),
                ],
            ),
        )

class CornerRight(widgets.Window):
    def __init__(self, monitor):
        super().__init__(
            namespace=f"corners-window-right-{monitor}",
            monitor=monitor,
            exclusivity="exclusive",
            layer="top",
            kb_mode="none",
            css_classes=["screen-border-right-window"],
            anchor=["top", "right", "bottom"],
            child=widgets.Box(
                css_classes=["screen-border-right"],
                child=[
                    widgets.CenterBox(
                        vertical=True,
                        vexpand=True,
                        start_widget=widgets.Label(label="r"),
                        center_widget=widgets.Label(label="r"),
                        end_widget=widgets.Label(label="r"),
                    ),
                ],
            ),
        )

class CornerBottom(widgets.Window):
    def __init__(self, monitor):
        super().__init__(
            namespace=f"corners-window-bottom-{monitor}",
            monitor=monitor,
            exclusivity="exclusive",
            layer="top",
            kb_mode="none",
            css_classes=["screen-border-bottom-window"],
            anchor=["left", "bottom", "right"],
            child=widgets.Box(
                css_classes=["screen-border-bottom"],
                child=[
                    widgets.CenterBox(
                        hexpand=True,
                        start_widget=widgets.Label(label="b"),
                        center_widget=widgets.Label(label="b"),
                        end_widget=widgets.Label(label="b"),
                    ),
                ],
            ),
        )


class Corners(widgets.Window):
    def __init__(self, monitor):
        super().__init__(
            namespace=f"corners-windows",
            monitor=monitor,
            layer="overlay",
            anchor=["left"],
            visible=True,
            exclusivity="exclusive",
            kb_mode="none",
            css_classes=["corners"],
            child=CornersContainer(),
        )
