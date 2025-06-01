-- NOTE: This is default config of `Noice` see below for Seth Phaeno's config which is currently in use
-- return {
--     "folke/noice.nvim",
--     event = "VeryLazy",
--     opts = {
--         -- add any options here
--     },
--     dependencies = {
--         -- if you lazy-load any plugin below, make sure to add proper `module="..."` entries
--         "MunifTanjim/nui.nvim",
--         -- OPTIONAL:
--         --   `nvim-notify` is only needed, if you want to use the notification view.
--         --   If not available, we use `mini` as the fallback
--         "rcarriga/nvim-notify",
--     },
--     config = function()
--         require("noice").setup({
--         lsp = {
--             -- override markdown rendering so that **cmp** and other plugins use **Treesitter**
--             override = {
--                 ["vim.lsp.util.convert_input_to_markdown_lines"] = true,
--                 ["vim.lsp.util.stylize_markdown"] = true,
--                 ["cmp.entry.get_documentation"] = true, -- requires hrsh7th/nvim-cmp
--             },
--             },
--                 -- you can enable a preset for easier configuration
--                 presets = {
--                 bottom_search = true, -- use a classic bottom cmdline for search
--                 command_palette = true, -- position the cmdline and popupmenu together
--                 long_message_to_split = true, -- long messages will be sent to a split
--                 inc_rename = false, -- enables an input dialog for inc-rename.nvim
--                 lsp_doc_border = false, -- add a border to hover docs and signature help
--             },
--         })
--     end,
-- }

return {
    {
		"folke/noice.nvim",
        event = "VeryLazy",
        enabled = true,
		dependencies = {
			-- if you lazy-load any plugin below, make sure to add proper `module="..."` entries
			"MunifTanjim/nui.nvim",
		},
        config = function ()
           local noice = require("noice")

            noice.setup({
				cmdline = {
                    -- NOTE: Looks like the auto-completion does work and popup correctly by the UI at end of line where used instead
                    -- of showing up in bottom left where original commandline is.
                    -- HACK: Set the below value to `true` if you want to see commandline UI in middle of screen
					enabled = false, 
					view = "cmdline_popup",
					format = {
						cmdline = { pattern = "", icon = "󱐌 :", lang = "vim" },
                        help = { pattern = "^:%s*he?l?p?%s+", icon = " 󰮦 :" },
                        search_down = { kind = "search", pattern = "^/", icon = "/", lang = "regex" },
                        search_up = { kind = "search", pattern = "^%?", icon = "/", lang = "regex" },
						filter = { pattern = "^:%s*!", icon = " $ :", lang = "bash" },
						lua = {
							pattern = { "^:%s*lua%s+", "^:%s*lua%s*=%s*", "^:%s*=%s*" },
							icon = "  :",
							lang = "lua",
						},
						input = { view = "cmdline_input", icon = " 󰥻 :" }, -- Used by input()
					},
				},
                views = {
                    popupmenu = {
                        relative = "editor",
                        position = {
                            row = 8,
                            col = "50%",
                        },
                        win_options = {
                            winhighlight = { Normal = "Normal", FloatBorder = "DiagnosticInfo" },
                        },
                    },
                    mini = {
                        size = {
                            width = "auto",
                            height = "auto",
                            max_height = 15,
                        },
                        position = {
                            row = -2,
                            col = "100%",
                        },
                    }
                },
				lsp = {
					progress = {
						enabled = true,
					},
					-- override markdown rendering so that **cmp** and other plugins use **Treesitter**
					override = {
						["vim.lsp.util.convert_input_to_markdown_lines"] = true,
						["vim.lsp.util.stylize_markdown"] = true,
						["cmp.entry.get_documentation"] = true, -- requires hrsh7th/nvim-cmp
					},
                    signature = {
                        auto_open = { enabled = false }, -- disable auto signature help on insert mode
                    },
				},
                routes = {
                    {
                        filter = {
                            event = 'msg_show',
                            any = {
                                { find = '%d+L, %d+B' },
                                { find = '; after #%d+' },
                                { find = '; before #%d+' },
                                { find = '%d fewer lines' },
                                { find = '%d more lines' },
                            },
                        },
                        opts = { skip = true },
                    }
                },
				messages = {
					enabled = false,
				},
                health = {
                    checker = true,
                },
				popupmenu = {
					enabled = true,
				},
				signature = {
					enabled = true,
				},
            })
        end
    }
}
