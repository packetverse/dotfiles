local opts = { noremap = true, silent = true }

-- set leader to spacebar --
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- moves selected lines down and up (very useful) --
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv", { desc = "moves lines up in visual selection" })
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv", { desc = "moves lines down in visual selection" })

-- default keybind not needed actually --
vim.keymap.set("n", "J", "mzJ`z")

-- move down page with cursor centered --
vim.keymap.set("n", "<C-d>", "<C-d>zz", { desc = "move down in buffer with cursor centered" })
vim.keymap.set("n", "<C-u>", "<C-u>zz", { desc = "move up in buffer with cursor centered" })

-- properly move between highlighted search results
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- indent with greater than or lesser than signs in visual mode
vim.keymap.set("v", "<", "<gv", opts)
vim.keymap.set("v", ">", ">gv", opts)

-- exit insert mode with ctrl+c --
vim.keymap.set("i", "<C-C>", "<Esc>")

-- clear search highlight ctrl+c --
vim.keymap.set("n", "<C-c>", ":nohl<CR>", { desc = "Clear search highlight", silent = true })

-- remove keybind for replaying last macro --
-- vim.keymap.set("n", "Q", "<nop>")

-- globally search and then replace string in buffer --
vim.keymap.set("n", "<leader>s", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]], { desc = "Replace word cursor is on globally" })

-- Highlight yank --
vim.api.nvim_create_autocmd("TextYankPost", {
    desc = "Highlight when yanking (copying) text",
    group = vim.api.nvim_create_augroup("kickstart-highlight-yank", { clear = true }),
    callback = function()
        vim.highlight.on_yank()
    end,
})

-- tab stuff --
vim.keymap.set("n", "<leader>to", "<cmd>tabnew<CR>") -- open new tab
vim.keymap.set("n", "<leader>tx", "<cmd>tabclose<CR>") -- close current tab
vim.keymap.set("n", "<leader>tn", "<cmd>tabn<CR>") -- go to next tab
vim.keymap.set("n", "<leader>tp", "<cmd>tabp<CR>") -- go to previous tab
vim.keymap.set("n", "<leader>tf", "<cmd>tabnew %<CR>") -- open current tab in new tab

-- split stuff --
vim.keymap.set("n", "<leader>sv", "<C-w>v", { desc = "Split window vertically" })
vim.keymap.set("n", "<leader>sh", "<C-w>s", { desc = "Split window horizontally" })
vim.keymap.set("n", "<leader>se", "<C-w>=", { desc = "Make splits equal size" })
vim.keymap.set("n", "<leader>sx", "<cmd>close<CR>", { desc = "Close current split" })

-- copy filepath to the clipboard --
vim.keymap.set("n", "<leader>fp", function()
    local filePath = vim.fn.expand("%:~")
    vim.fn.setreg("+", filePath)
    print("File path copied to clipboard: " .. filePath)
end, { desc = "Copy file to path to clipboard" })


