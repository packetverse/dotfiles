# ZDOTDIR is set to `$HOME/.config/zsh` in `/etc/zshenv` or `/etc/zsh/zshenv`

. "$HOME/.local/bin/env"

eval "$(uv generate-shell-completion zsh)"
eval "$(uvx --generate-shell-completion zsh)"
