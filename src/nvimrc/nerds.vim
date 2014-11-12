
" #### NERDTree
"
let NERDTreeWinSize=51
let NERDTreeQuitOnOpen=1
let NERDTreeHijackNetrw=1
let NERDTreeDirArrows=1
let NERDTreeStatusline=1
nmap <c-d> <ESC>:NERDTreeToggle<CR>
" nmap <c-d> <ESC>:e .<CR>

" #### NERDCommenter 
"
let b:leader = exists('g:mapleader') ? g:mapleader : '\'
" I like to use CTRL-C to toggle comments 
exec 'noremap <C-C> :call NERDComment("n", "AlignLeft")<cr>'
exec 'noremap <C-N> :call NERDComment("n", "Uncomment")<cr>'

" I like space around comments
let g:NERDSpaceDelims = 1

" Custom comment delimiters for NERDCommenter 
if exists("loaded_nerd_comments")
    let g:NERDCustomDelimiters = {
        \ 'python': { 'left': '#' },
        \ 'ecl': { 'left': '//', 'leftAlt': '/*', 'rightAlt': '*/' },
    \ }
endif
