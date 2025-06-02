# Dotfiles

## Description

Dotfiles for personal use, currently on Arch Linux.

| Type | Currently in use |
| --- | --- |
| Window Manager | i3 (X11) |
| Notifications | not working |
| Shell | bash |
| Prompt | starship |
| Edtior | neovim |
| Terminal Emulator | Ghostty |
| Terminal Multiplexer | tmux |

## Usage

1. Clone the repository and move and rename it to whatever you want
2. Ensure GNU Stow is installed: `sudo pacman -S --needed stow`
3. `cd` into the directory and run `stow .`

## TODO

- [ ] Setup screenshotting utility and keybind
- [ ] Setup notifications
- [ ] Setup scratchpad for i3
- [ ] Setp zsh together with starship as prompt
- [ ] Setup login manager like SDDM or something nice for i3
- [ ] Make most things catppuccin
- [ ] Make different branches on git repo for colorschemes e.g., `i3/catppuccin`, `i3/gruvbox`, `hyprland/catppuccin`
