require("ayush.remap")
require("ayush.packer")
--line numbers with good ui
vim.o.number = true
vim.o.numberwidth =4 
vim.o.relativenumber = true
vim.o.signcolumn = "no"
vim.o.cursorline = true
-- Makes neovim and host OS clipboard play nicely with each other
vim.o.clipboard = "unnamedplus"
-- Case insensitive searching UNLESS /C or capital in search
vim.o.ignorecase = true
vim.o.smartcase = true
-- Better editing experience
vim.o.expandtab = true
vim.o.smarttab = true
vim.o.cindent = true
vim.o.autoindent = true
vim.o.wrap = true
vim.o.textwidth = 300
vim.o.tabstop = 4
vim.o.shiftwidth = 4
vim.o.softtabstop = -1 -- If negative, shiftwidth value is used
vim.o.list = true
vim.o.listchars = "trail:·,nbsp:◇,tab:→ ,extends:▸,precedes:◂"
-- o.listchars = 'eol:¬,space:·,lead: ,trail:·,nbsp:◇,tab:→-,extends:▸,precedes:◂,multispace:···⬝,leadmultispace:│   ,'
-- o.formatoptions = 'qrn1'
-- Undo and backup options
vim.o.backup = false
vim.o.writebackup = false
vim.o.undofile = true
vim.o.swapfile = false
vim.o.backupdir = '/tmp/'
vim.o.directory = '/tmp/'
vim.o.undodir = '/tmp/'

vim.opt.mouse = "a"
