-- NOTE: Replaced with oil file explorer for now

return {
    {
        "nvim-neo-tree/neo-tree.nvim",
        enabled = false,
        branch = "v3.x",
        dependencies = {
            "nvim-lua/plenary.nvim",
            "nvim-tree/nvim-web-devicons",
            "MunifTanjim/nui.nvim",
            "3rd/image.nvim",
        },
        lazy = false,
        ---@module "neo-tree",
        ---@type neotree.Config?
        config = function()
            vim.keymap.set("n", "<leader>op", "<cmd>Neotree toggle<CR>", { desc = "Toggles Neotree" })
        end,
    }
}
