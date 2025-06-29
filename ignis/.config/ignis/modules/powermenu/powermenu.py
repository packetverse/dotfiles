import asyncio

from ignis import widgets
from ignis import utils
from typing import Callable
from ..shared_widgets import Popout

def create_exec_task(cmd: str) -> None:
    asyncio.create_task(utils.exec_sh_async(cmd))

class PowerMenuButton(widgets.Button):
    def __init__(
        self,
        image: str,
        pixel_size: int,
        on_click: Callable,
        css_classes: list[str],
    ) -> None:
        super().__init__(
            child=widgets.Icon(image=image, pixel_size=pixel_size),
            on_click=on_click,
            css_classes=css_classes,
        ),

class ShutdownButton(PowerMenuButton):
    def __init__(self):
        super().__init__(
            image="system-shutdown-symbolic",
            pixel_size=48,
            on_click=lambda *_: print("shutdown"),
            css_classes=["power-menu-shutdown-button"],
        )

class RebootButton(PowerMenuButton):
    def __init__(self):
        super().__init__(
            image="system-reboot-symbolic",
            pixel_size=48,
            on_click=lambda *_: print("reboot"),
            css_classes=["power-menu-reboot-button"],
        )

class PowerMenu(Popout):
    def __init__(self):
        super().__init__(
            namespace="power-menu",
            anchor=["right"],
            exclusivity="ignore",
            layer="top",
            css_classes=["power-menu-window"],
            hide_delay=300,
            visible=False,
            reveal_child=True,
            transition_type="slide_left",
            transition_duration=300,
            height_request=256,
            child=widgets.Box(
                vertical=True,
                hexpand=True,
                vexpand=True,
                css_classes=["power-menu-box"],
                spacing=12,
                child=[
                    ShutdownButton(),
                    RebootButton(),
                ],
            ),
        ),
