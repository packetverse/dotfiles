#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

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

# use nvim as pager for man 
export MANPAGER="nvim +Man!"

# some important env vars
export EDITOR="nvim"
export PAGER="less"
export VISUAL="${EDITOR}"

# WARNING: Moving this file can potentially lead to not being able to start your X11 session or some programs (eg. Wine) not working as intended.**
# export XINITRC="$XDG_CONFIG_HOME"/X11/xinitrc

# wget alias for history file in xdg dirs
alias wget="wget --hsts-file=$XDG_DATA_HOME/wget-hsts"

# git aliases
alias gs="git status --short"
alias gd="git diff --output-indicator-new=' ' --output-indicator-old=' '"
alias gds="gd --staged"
alias ga="git add"
alias gap="git add --patch"
alias gc="git commit"
alias gca="gc --amend --no-edit"
alias gce="gc --amend"
alias gp="git push"
alias gu="git pull"
alias gl='git log --graph --all --pretty=format:"%C(magenta)%h %C(white) %an  %ar%C(blue)  %D%n%s%%C(magenta)%h %C(white) %an  %ar%C(blue)  %D%n%s%nn"'
alias gb="git branch"
alias gn="git branch --all"
alias gba="gb --all"
alias gco="git checkout"
alias gi="git init"
alias gcl="git clone --recursive"
alias gm="git merge"
alias gr="git reset"

# Seems to only work on zsh
# gcm() { git commit --message "$*" }

# uv and uvx auto completion
eval "$(uv generate-shell-completion bash)"
eval "$(uvx --generate-shell-completion bash)"

# starship prompt
eval "$(starship init bash)"
