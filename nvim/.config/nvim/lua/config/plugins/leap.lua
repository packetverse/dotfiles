return {
    {
        "ggandor/leap.nvim",
        enabled = false,
        config = function()
            -- require("leap").setup()
            
            vim.keymap.set({"n", "x", "o"}, "ls", "<Plug>(leap)")
            vim.keymap.set("n", "lS", "<Plug>(leap-from-window)")
        end,
    }
}
