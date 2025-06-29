from ignis import widgets
from ignis import utils
from ignis.gobject import IgnisGObject
from gi.repository import GLib, Gdk

class Popout(widgets.Window):
    """
    Re-usable widget to use EventBox as a revealer, allows you to customize the children inside the EventBox.
    """
    __gtype_name__ = "Popout"

    def __init__(
        self,
        namespace: str, # applied on Window and RevealerWindow
        child: IgnisGObject, # applied on Revealer but that is wrapped in an EventBox
        css_classes: list[str] = [],
        anchor: list[str] = ["left", "top", "right"], # applied on Window and RevealerWindow
        layer: str = "top", # applied on Window and RevealerWindow
        exclusivity: str = "exclusive", # applied on Window and RevealerWindow
        hide_delay: int = 300, # decides how long it should take after hover_lost to hide widget
        visible: bool = False, # decides if widget should be visible after created, False will hide until the area is hovered, and True will show it and then when hovered first and then unhovered it will dissappear and hide
        transition_type: str = "slide_down", # decides the transition_type for the Revealer
        transition_duration: int = 300, # decides the transition_duration for the Revealer (e.g. how long the animation will take)
        reveal_child: bool = False, # same as visible parameter but i'm not sure myself how this one works
        margin_bottom: int = 0,
        margin_left: int = 0,
        margin_right: int = 0,
        margin_top: int = 0,
        **kwargs, # pass the rest of the arguments to the Window
    ):
        self._css_classes = css_classes

        if not self._css_classes:
            self._css_classes = [f"{namespace}"]

        self._hide_delay_ms = hide_delay
        self._hide_timeout_id = None
        self._is_hovering = False
        self._trigger_zone_width = 0

        super().__init__(
            anchor=anchor,
            layer=layer,
            exclusivity=exclusivity,
            namespace=namespace,
            visible=True,
            css_classes=[f"{namespace}-window"],
            width_request=self._trigger_zone_width,
            child=widgets.EventBox(
                css_classes=[f"unset"],
                hexpand=True,
                vexpand=True,
                width_request=self._trigger_zone_width,
                child=[
                    # FIX: Make function to decide how long the widget inside the CenterBox should be depending on a
                    # parameter set in __init__ so basically calculate text length, one letter could be N px.

                    # NOTE: This could be the default placeholder but it's not very much good on catching gestures/hovers and not that flexible
                    # widgets.Label(label="q", style="color: transparent;")

                    # NOTE: This is the current placeholder, this is more flexible than the above one
                    widgets.CenterBox(
                        hexpand=True,
                        vexpand=True,
                        center_widget=widgets.Label(label="c", style="color: transparent;"),
                    ),
                ],
                visible=True,
                on_hover=self.on_hover,
                on_hover_lost=self.on_hover_lost,
            ),
            **kwargs,
        )

        self.revealer = widgets.Revealer(
            width_request=self._trigger_zone_width,
            css_classes=[f"{namespace}-revealer"],
            transition_type=transition_type,
            transition_duration=transition_duration,
            child=child,
            reveal_child=reveal_child,
        )

        self.revealer_window = widgets.RevealerWindow(
            anchor=anchor,
            layer=layer,
            exclusivity=exclusivity,
            popup=True,
            visible=visible,
            namespace=f"{namespace}-revealer-window",
            css_classes=[f"{namespace}-revealer-window"],
            margin_bottom=margin_bottom,
            margin_left=margin_left,
            margin_right=margin_right,
            margin_top=margin_top,
            width_request=self._trigger_zone_width,
            child=widgets.EventBox(
                width_request=self._trigger_zone_width,
                css_classes=self._css_classes,
                child=[self.revealer],
                on_hover=self.on_hover,
                on_hover_lost=self.on_hover_lost,
            ),
            revealer=self.revealer,
        ),


    def on_hover(self, *_):
        self._is_hovering = True

        if self._hide_timeout_id:
            GLib.source_remove(self._hide_timeout_id)
            self._hide_timeout_id = None

        self.revealer_window[0].set_visible(True)

    def on_hover_lost(self, *_):
        self._is_hovering = False

        def hide_if_not_hovering():
            if not self._is_hovering:
                self.revealer_window[0].set_visible(False)

        self._hide_timeout_id = GLib.timeout_add(self._hide_delay_ms, hide_if_not_hovering)

# FIX: Does not work properly and is still being worked on!
class PopoutDarken(widgets.Window):
    """
    Re-usable widget to use EventBox as a revealer, allows you to customize the children inside the EventBox.
    """
    __gtype_name__ = "PopoutDarken"

    def __init__(
        self,
        namespace: str, # applied on Window and RevealerWindow
        child: IgnisGObject, # applied on Revealer but that is wrapped in an EventBox
        css_classes: list[str] = [],
        anchor: list[str] = ["left", "top", "right"], # applied on Window and RevealerWindow
        layer: str = "top", # applied on Window and RevealerWindow
        exclusivity: str = "exclusive", # applied on Window and RevealerWindow
        hide_delay: int = 300, # decides how long it should take after hover_lost to hide widget
        visible: bool = False, # decides if widget should be visible after created, False will hide until the area is hovered, and True will show it and then when hovered first and then unhovered it will dissappear and hide
        transition_type: str = "slide_down", # decides the transition_type for the Revealer
        transition_duration: int = 300, # decides the transition_duration for the Revealer (e.g. how long the animation will take)
        reveal_child: bool = False, # same as visible parameter but i'm not sure myself how this one works
        margin_bottom: int = 0,
        margin_left: int = 0,
        margin_right: int = 0,
        margin_top: int = 0,
        **kwargs, # pass the rest of the arguments to the Window
    ):
        self._css_classes = css_classes

        if not self._css_classes:
            self._css_classes = [f"{namespace}"]

        self._hide_delay_ms = hide_delay
        self._hide_timeout_id = None
        self._is_hovering = False
        self._trigger_zone_width = 0

        super().__init__(
            anchor=anchor,
            layer=layer,
            exclusivity=exclusivity,
            namespace=namespace,
            visible=True,
            css_classes=[f"{namespace}-window"],
            # width_request=self._trigger_zone_width,
            child=widgets.EventBox(
                css_classes=[f"unset"],
                hexpand=True,
                vexpand=True,
                # width_request=self._trigger_zone_width,
                child=[
                    # FIX: Make function to decide how long the widget inside the CenterBox should be depending on a
                    # parameter set in __init__ so basically calculate text length, one letter could be N px.

                    # NOTE: This could be the default placeholder but it's not very much good on catching gestures/hovers and not that flexible
                    # widgets.Label(label="q", style="color: transparent;")

                    # NOTE: This is the current placeholder, this is more flexible than the above one
                    widgets.CenterBox(
                        hexpand=True,
                        vexpand=True,
                        center_widget=widgets.Label(label="c", style="color: transparent;"),
                    ),
                ],
                visible=True,
                on_hover=self.on_hover,
                on_hover_lost=self.on_hover_lost,
            ),
            **kwargs,
        )

        self.revealer = widgets.Revealer(
            width_request=self._trigger_zone_width,
            css_classes=[f"{namespace}-revealer"],
            transition_type=transition_type,
            transition_duration=transition_duration,
            child=child,
            reveal_child=reveal_child,
        )

        # TODO: Find a way to blur everything but the widget
        self.darken_overlay = widgets.Window(
            namespace=f"{namespace}-overlay",
            # anchor=["top", "bottom", "left", "right"],
            anchor=["top", "bottom", "right"],
            exclusivity="ignore",
            layer="overlay",
            kb_mode="none",
            input_width=1,
            input_height=1,
            visible=False,
            style="background-color: rgba(0, 0, 0, 0.25);",
        )

        self.darken_overlay.set_decorated(False)
        self.darken_overlay.set_can_focus(False)
        self.darken_overlay.set_focusable(False)

        self.bounds_box = widgets.Box(
            child=[self.revealer],
        )

        self.revealer_window = widgets.RevealerWindow(
            anchor=anchor,
            layer=layer,
            exclusivity=exclusivity,
            popup=True,
            visible=visible,
            namespace=f"{namespace}-revealer-window",
            css_classes=[f"{namespace}-revealer-window"],
            margin_bottom=margin_bottom,
            margin_left=margin_left,
            margin_right=margin_right,
            margin_top=margin_top,
            width_request=self._trigger_zone_width,
            child=widgets.EventBox(
                # width_request=self._trigger_zone_width,
                css_classes=self._css_classes,
                child=[self.bounds_box],
                on_hover=self.on_hover,
                on_hover_lost=self.on_hover_lost,
            ),
            revealer=self.revealer,
        )

        # print(self.revealer_window.get_default_size())
        # print(self.darken_overlay.get_default_size())

    def on_hover(self, *_):
        self._is_hovering = True

        if self._hide_timeout_id:
            # GLib.source_remove(self._hide_timeout_id)
            self._hide_timeout_id = None

        # bounds = self.revealer_window.compute_bounds(self.revealer_window.child.get_root())
        # bounds = self.revealer_window.compute_bounds(self.revealer_window.child.get_root())
        bounds = self.bounds_box.compute_bounds(self.revealer_window.child.get_root())
        print(bounds.out_bounds.get_width())
        # print("x:", bounds.out_bounds.get_x())
        # print("y:", bounds.out_bounds.get_y())
        # print("width:", self.revealer_window.get_width())
        # print("height:", self.revealer_window.get_height())
        #
        # print(dir(bounds.out_bounds))
        # print(bounds.out_bounds.get_area())

        monitor = utils.get_monitor(0)
        geometry = monitor.get_geometry()
        screen_width = geometry.width
        screen_height = geometry.height

        print(f"Monitor res: {screen_width}x{screen_height}")

        # widget_width = self.revealer.child.get_width()
        # widget_height = self.revealer.child.get_height()

        widget_width = bounds.out_bounds.get_width()

        # print("Widget width:", widget_width)
        # print("Widget height:", widget_height)

        darken_width = screen_width - widget_width
        darken_height = screen_height

        print(f"Darken overlay desired size: {darken_width}x{darken_height}")
        self.darken_overlay.set_default_size(darken_width, darken_height)
        # self.darken_overlay.set_default_size(1840, 1080)

        # self.revealer_window[0].set_visible(True)
        self.revealer_window.set_visible(True)
        self.darken_overlay.set_visible(True)

    def on_hover_lost(self, *_):
        self._is_hovering = False

        def hide_if_not_hovering():
            if not self._is_hovering:
                # self.revealer_window[0].set_visible(False)
                self.revealer_window.set_visible(False)
                self.darken_overlay.set_visible(False)


        self._hide_timeout_id = GLib.timeout_add(self._hide_delay_ms, hide_if_not_hovering)

