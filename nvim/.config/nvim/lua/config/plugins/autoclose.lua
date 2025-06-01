-- auto-pairs could be used instead but this is way simpler and if i need those other wide range of features that
-- auto-pairs has I might consider switching but for now this works

-- ISSUE: Doesn't know where closing brackets or parentheses are, etc.
-- ISSUE: Always just for no reason appends two of "'", and other characters
-- ISSUE: Not really usable if meant to be used for programming efficiently more like a roadblock tbh

return {
    {
        "m4xshen/autoclose.nvim",
        enabled = false,
        config = function()
            require("autoclose").setup()
        end
    }
}
