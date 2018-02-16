set scrolloff=5
set tabstop=4
set shiftwidth=4
set expandtab
set number
set mouse=a
syntax on
filetype plugin on
colorscheme koehler
map <silent> ,l :w<CR>:!pdflatex --shell-escape %<CR>
