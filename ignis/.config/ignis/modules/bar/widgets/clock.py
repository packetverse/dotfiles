from ignis import widgets
from ignis import utils
from datetime import datetime

class Clock(widgets.Box):
    def __init__(self):
        super().__init__(
            vertical=True,
            halign="center",
        )

        self.hours = widgets.Label()
        self.minutes = widgets.Label()

        utils.Poll(
            timeout=1000,
            callback=lambda *_: self.set_time()
        )

        self.set_time()

        self.append(self.hours)
        self.append(self.minutes)

    def set_time(self):
        self.hours.label = datetime.now().strftime("%H")
        self.minutes.label = datetime.now().strftime("%M")
        self.tooltip_text = datetime.now().strftime("%A %d %B %Y")
