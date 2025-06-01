vim.cmd("let g:netrw_banner = 0")

local opt = vim.opt
-- opt.guicursor = "" -- makes cursor a block instead of line

-- line numbers with relative line number on --
opt.number = true
opt.relativenumber = true

-- indentation --
opt.tabstop = 4
opt.softtabstop = 4
opt.shiftwidth = 4
opt.expandtab = true
opt.autoindent = true
opt.smartindent = true

-- line wrapping disabled --
opt.wrap = false

-- swap file --
opt.swapfile = false
opt.backup = false
opt.undofile = true

-- search settings --
-- opt.incsearch = true -- incremental search
-- opt.inccommand = "split"
opt.ignorecase = true
opt.smartcase = true

-- colors and ui --
opt.termguicolors = true
opt.background = "dark"
opt.scrolloff = 8
opt.signcolumn = "yes"

opt.backspace = {"start", "eol", "indent"}

opt.splitright = true
opt.splitbelow = true

-- make lsp faster (not sure) --
opt.updatetime = 50

-- system clipboard access --
opt.clipboard:append("unnamedplus")

-- highlight text search --
opt.hlsearch = true

-- mouse support in all modes --
opt.mouse = "a"

-- not sure --
vim.g.editorconfig = true
