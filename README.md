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

### General

- [x] Setup screenshotting utility and keybind
- [x] Setup notifications
- [ ] Setp zsh together with starship as prompt
- [x] Setup login manager like SDDM or something nice for i3
- [ ] Make most things catppuccin

### tmux

- [ ] make session index start at 1 instead of 0

### niri

- [x] block gmail from screencapture

### mako (or any other notif daemon)

- [ ] make notifs dissappear (timeout) after inactivity

### neovim
- [ ] make keybind (<leader>ln) to toggle relative line numbers
