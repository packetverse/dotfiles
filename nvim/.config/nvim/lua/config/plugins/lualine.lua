return {
    {
        "nvim-lualine/lualine.nvim",
        dependencies = { "nvim-tree/nvim-web-devicons" },
        config = function()
            local lualine = require("lualine")
            local lazy_status = require("lazy.status")

            local mode = {
                "mode",
                fmt = function(str)
                    return " " .. str
                    -- return " " .. str
                end,
            }

            local diff = {
                "diff",
                colored = true,
                symbols = {
                    added = " ",
                    modified = " ",
                    removed = " ",
                }
            }

            local filename = {
                "filename",
                file_status = true,
                path = 0,
            }

            local branch = {
                "branch",
                icon = {
                    " ",
                }
            }

            lualine.setup({
                options = {
                    icons_enabled = true,
                    theme = "auto",
                    -- component_separators = { left = "", right = "" },
                    -- section_separators = { left = "", right = "" },
                    component_separators = "",
                    section_separators = "", 
                    disabled_filetypes = {
                        statusline = {},
                        winbar = {},
                    },
                    ignore_focus = {},
                    always_divide_middle = true,
                    always_show_tabline = true,
                    globalstatus = false,
                    refresh = {
                        statusline = 100,
                        tabline = 100,
                        winbar = 100,
                    },
                },
                sections = {
                    lualine_a = { mode },
                    -- lualine_b = { branch },
                    lualine_b = { "branch" },
                    lualine_c = { diff, filename },
                    lualine_x = { "filetype" } 
                    -- lualine_y = {"progress"},
                    -- lualine_z = {"location"}
                },
                inactive_sections = {
                    lualine_a = {},
                    lualine_b = {},
                    lualine_c = {},
                    lualine_x = {},
                    lualine_y = {},
                    lualine_z = {},
                },
                tabline = {},
                winbar = {},
                inactive_winbar = {},
                extensions = {},
            })
        end,
    }
}
