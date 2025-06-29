from ignis import widgets
from ignis import utils
from ignis.services.niri import NiriService

niri = NiriService.get_default()

class WorkspaceButton(widgets.Button):
    def __init__(self, id, is_focused):
        super().__init__(
            setup=self._setup,
            css_classes=["workspace", "focused-workspace" if is_focused else ""],
            child=widgets.Label(
                label=str(id)
            ),
            tooltip_text=f"Switch to Workspace {id}",
            on_click=lambda *_: niri.switch_to_workspace(id)
        )

    def _setup(self, *_):
        pass

class PerOutputWorkspaces(widgets.Box):
    def __init__(self, output):
        super().__init__(
            vertical=True,
            css_classes=["workspaces"],
            spacing=4,
            child=niri.bind(
                "workspaces",
                transform=lambda value: [
                    WorkspaceButton(
                        workspace.get_idx(),
                        workspace.get_is_focused()
                    ) if workspace.get_output() == output else None for workspace in value or []
                ]
            )
        )

class Workspaces(widgets.Box):
    def __init__(self):
        super().__init__(
            vertical=True,
            spacing=16,
            child=[
                PerOutputWorkspaces(utils.get_monitor(id).get_connector()) for id in range(utils.get_n_monitors())
            ]
        )
