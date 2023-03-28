vim.cmd [[packadd packer.nvim]]
return require('packer').startup(function(use)
  -- Packer can manage itself
  use 'wbthomason/packer.nvim'
  use {
	  'nvim-telescope/telescope.nvim', tag = '0.1.1',
	  -- or                            , branch = '0.1.x',
	  requires = { {'nvim-lua/plenary.nvim'} }
  }
  use { "ellisonleao/gruvbox.nvim" }
  use {
	  'nvim-lualine/lualine.nvim',
	  requires = { 'kyazdani42/nvim-web-devicons', opt = true }
  }
  use("nvim-tree/nvim-web-devicons")
  use("theprimeagen/harpoon")
  use("preservim/nerdtree")
  use("ryanoasis/vim-devicons")
  use("folke/which-key.nvim")
  use("junegunn/goyo.vim")
  use("junegunn/vim-emoji")
  use("tpope/vim-commentary")
  use("tpope/vim-surround")
  use({"nvim-treesitter/nvim-treesitter"})
end)
