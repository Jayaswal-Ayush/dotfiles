""""             _                    
""""      __   _(_)_ __ ___  _ __ ___ 
""""      \ \ / / | '_ ` _ \| '__/ __|
""""       \ V /| | | | | | | | | (__ 
""""      (_)_/ |_|_| |_| |_|_|  \___|
""""
set number relativenumber
set noswapfile
set incsearch
set smartcase
set tabstop =4 softtabstop=4

call plug#begin('~/.config/nvim/plugged')
      Plug 'morhetz/gruvbox'
      Plug 'itchyny/lightline.vim'
      Plug 'mhinz/vim-startify'
      Plug 'chriskempson/tomorrow-theme'
      Plug 'ap/vim-css-color'
      Plug 'jiangmino/auto-pairs'
      Plug 'preservim/nerdtree'
      Plug 'tpope/vim-surround'
      plug 'alvan/vim-closetag'
call plug#end()

"  Color Settings
colorscheme gruvbox 
set background=dark
set termguicolors
let g:limelight_conceal_ctermfg = 240
let g:limelight_conceal_guifg = '#777777'
hi! Normal ctermbg=NONE guibg=NONE 
hi! NonText ctermbg=NONE guibg=NONE guifg=NONE ctermfg=NONE

noremap <leader>n :NERDTreeFocus<CR>
noremap <C-n> :NERDTree<CR>
noremap <C-t> :NERDTreeToggle<CR>
noremap <C-f> :NERDTreeFind<CR>

" make Vim behave in a more useful way
set nocompatible

" Statusline
set laststatus=2
set noshowmode
let g:lightline = {
      \ 'colorscheme': 'gruvbox',
      \ }
