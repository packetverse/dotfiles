return {
    {
        "nvim-telescope/telescope.nvim",
        tag = "0.1.8",
        -- branch = "0.1.x",
        dependencies = {
            "nvim-lua/plenary.nvim",
            { "nvim-telescope/telescope-fzf-native.nvim", build = "make" },
            "nvim-tree/nvim-web-devicons",
            "andrew-george/telescope-themes",
        },
        config = function()
            local telescope = require("telescope")
            local actions = require("telescope.actions")
            local builtin = require("telescope.builtin")
            
            telescope.load_extension("fzf")
            telescope.load_extension("themes")

            telescope.setup({
                defaults = {
                    path_display = { "smart" },
                    mappings = {
                        i = {
                            ["<C-k>"] = actions.move_selection_previous,
                            ["<C-j>"] = actions.move_selection_next,
                        },
                    },
                    extensions = {
                        themes = {
                            enable_previewer = true,
                            enable_live_preview = true,
                            persist = {
                                enabled = true,
                                path = vim.fn.stdpath("config") .. "/lua/colorscheme.lua",
                            },
                        },
                    },
                },
            })
             
            local keymap = vim.keymap
            
            keymap.set("n", "<leader>pf", builtin.find_files, { desc = "Telescope find files" })
            keymap.set("n", "<leader>pr", builtin.oldfiles, { desc = "Telescope find files" })
            keymap.set("n", "<leader>pk", builtin.keymaps, { desc = "Telescope find files" })
            keymap.set("n", "<leader>pg", builtin.live_grep, { desc = "Telescope live grep" })
            keymap.set("n", "<leader>pb", builtin.buffers, { desc = "Telescope buffers" })
            keymap.set("n", "<leader>ph", builtin.help_tags, { desc = "Telescope help tags" })
            keymap.set("n", "<leader>ths", "<cmd>Telescope themes<CR>", { noremap = true, silent = true, desc = "Theme switcher" })
        end,
    }
}
