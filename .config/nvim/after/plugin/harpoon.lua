local mark = require("harpoon.mark")
local ui = require("harpoon.ui")

vim.keymap.set("n", "<leader>a", mark.add_file)
vim.keymap.set("n", "<leader>h", ui.toggle_quick_menu)

vim.keymap.set("n", "<C-a>", function() ui.nav_file(1) end)
vim.keymap.set("n", "<C-b>", function() ui.nav_file(2) end)
vim.keymap.set("n", "<C-c>", function() ui.nav_file(3) end)
vim.keymap.set("n", "<C-d>", function() ui.nav_file(4) end)
vim.keymap.set("n", "<C-e>", function() ui.nav_file(5) end)
vim.keymap.set("n", "<C-f>", function() ui.nav_file(6) end)

