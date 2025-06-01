return {
    "stevearc/oil.nvim",
    dependencies = {
        "nvim-tree/nvim-web-devicons"
    },
    config = function()
        -- NOTE: Use defaults to get used to oil first before
        -- reconfiguring and messing with different values
        require("oil").setup({
            default_file_explorer = true,
            columns = { },
            keymaps = {
                ["<C-h>"] = false,
                ["<C-c>"] = false,
                ["<M-h>"] = "actions.select_split",
                ["q"] = "actions.close",
            },
            delete_to_trash = true,
            view_options = {
                show_hidden = true,
            },
            skip_confirm_for_simple_edits = true,
        })

        -- keymaps for oil
        vim.keymap.set("n", "-", "<cmd>Oil<CR>", { desc = "Open parent directory" })
        vim.keymap.set("n", "<leader>-", require("oil").toggle_float, { desc = "Toggle float oil" })
        -- vim.keymap.set("n", "<leader>r", "<cmd>edit!<CR>", { desc = "Refreshes oil explorer" })

        vim.api.nvim_create_autocmd("DirChanged", {
            pattern = "*",
            callback = function()
                if vim.bo.filetype == "oil" then
                    vim.cmd("edit!")
                end
            end
        })

        vim.api.nvim_create_autocmd("FileType", {
            pattern = "oil",
            callback = function()
                vim.opt_local.cursorline = true
            end,
        })
    end,
}
