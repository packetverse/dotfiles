#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

. "$HOME/.local/bin/env"

# XDG dirs
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_STATE_HOME="$HOME/.local/state"
export XDG_CACHE_HOME="$HOME/.cache"

# bash history
export HISTFILE="${XDG_STATE_HOME}"/bash/history

# cuda
export CUDA_CACHE_PATH="$XDG_CACHE_HOME"/nv

# go
export GOPATH="$XDG_DATA_HOME"/go

# WARNING: Moving this file can potentially lead to not being able to start your X11 session or some programs (eg. Wine) not working as intended.**
# export XINITRC="$XDG_CONFIG_HOME"/X11/xinitrc

# wget alias for history file in xdg dirs
alias wget="wget --hsts-file=$XDG_DATA_HOME/wget-hsts"

# uv and uvx auto completion
eval "$(uv generate-shell-completion bash)"
eval "$(uvx --generate-shell-completion bash)"

# starship prompt
eval "$(starship init bash)"

