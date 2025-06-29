# TODO: Add support for rotating active window title 90 degrees, otherwise this module
# is useless if your bar is vertical

from ignis import widgets
from ignis import utils
from ignis.services.niri import NiriService, NiriWindow

niri = NiriService.get_default()

class ActiveWindow(widgets.Label):
    def __init__(self):
        super().__init__(
            css_classes=["active-window-label"],
            # justify="center",
            halign="center",
            valign="center",
            # hexpand=True,
            vexpand=True,
            # height_request=100,
            # width_request=20,
            # wrap=True,
            # wrap_mode="word_char",
            # use_markup=False,
            ellipsize="end",
            # max_width_chars=52,
            label=niri.bind(
                "active_window",
                transform=lambda v: self.handle_title(v),
            )
        )

    def handle_title(self, niri_window: NiriWindow):
        if len(niri_window.title) >= 20:
            return "\n".join(niri_window.title[:20]) + "\n.\n.\n."
        elif len(niri_window.title) <= 20:
            return "\n".join(niri_window.title)
        elif niri_window.title == "":
            return "Desktop"

        return "Desktop"
