" Enable syntax highlighting
syntax enable 

" color schemes I have liked.
" * colo elflord " a low color dark theme. Great for the real console.
" * colo evening " dark theme, low color console friendly
" * colo xoria256 " a nice dark theme for 256 color terms
" * colo wombat256 " the classic wombat theme for 256 color terms
" * colo pyte " A white theme
" * colo mySlate 
" * colo peaksea " A light theme
" * colo molokai " A dark pastelly theme, a little bisexual but very pleasing.
" * colo neutron " A very nice creamy light theme.
" * colo vylight  " A light theme
" * colo jellybeans " A dark color full theme
"
" Add the tomorrow themes to the runtime path
" set runtimepath+=~/.vim/bundle/tomorrow-theme/vim

" Explicitly say we want 256 colors when we find 256
" in the TERM environmental variable.
" When this is set it can mess up using vim on a real console.
"  Definitely in Fedora >= 11. So we try to be smart about
" it and only set it if we think it's wanted.  
"
" We default to a theme that works everywere.
" Then we see if we can upgrade to a better theme
" based on the environment.
colo evening " evening is a nice dark theme, usually available with a default install.

function! <SID>Havescheme(name)
    let l:pat = 'colors/'.a:name.'.vim'
    if 1 == empty(globpath(&rtp, l:pat))
        return 0
    else
        return 1
    endif
endfunction

function! <SID>UseSolarized()
        " let g:solarized_style = 'dark'
        let g:solarized_termcolors = 16
        " let g:solarized_visibility = "low"
        " let g:solarized_contrast = "low"
        " let g:solarized_degrade=1
        " let g:solarized_termtrans=1
        " Disabling italics is necessary for konsole
        " let g:solarized_italic = 0
        " let g:solarized_bold = 0
        " let g:solarized_underline = 0
        colorscheme solarized

        " Set the lightline theme too
		let g:lightline.colorscheme = 'solarized'
endfunction

" We like italics in the terminal, so add some sauce to make sure we get it.
set t_ZH=[3m
set t_ZR=[23m
highlight Comment cterm=italic

function! <SID>SolarizedToggle()
    if (w:solarized_style == "dark")
        let g:solarized_style = "light"
        colorscheme solarized
    else
        let g:solarized_style = "dark"
        colorscheme solarized
    endif
endfunction
command! SolarizedToggle call <SID>SolarizedToggle()

if $TERM =~ '256' || $COLORTERM =~ 'gnome-terminal' || $TERM =~ 'screen'  || $TERM =~ 'xterm'
	" Use a console friendly theme and force Vim to
	" use 256 colors if we think the console can handle it.
	" set t_Co=256
	hi clear CursorLine 

    set background=dark
    let g:lucius_style = "dark"

    if $TERM_META =~ 'white'
        set background=light

        if 1 == <SID>Havescheme('solarized')
            let g:solarized_style = 'light'
            call <SID>UseSolarized()
        elseif 1 == <SID>Havescheme('lucius')
            let g:lucius_style = "light"
            colorscheme lucius
        elseif 1 == <SID>Havescheme('Tomorrow')
            colorscheme Tomorrow
        elseif 1 == <SID>Havescheme('summerfruit256')
            colorscheme summerfruit256
        endif

        set nocursorline
    else
        if 1 == <SID>Havescheme('solarized')
            let g:solarized_style = 'dark'
            call <SID>UseSolarized()
        endif
    endif

	set cursorline
	set cursorcolumn
endif

" set linenumbers on by default
set number 
set relativenumber 

" A cleaner vertical split
 set fillchars=vert:\:


 " Change the cursor shape depending on mode.
 " Use a block in normal mode
 " Use a bar in insert mode
 if $KONSOLE_PROFILE_NAME
     let &t_SI = "\<Esc>]50;CursorShape=1\x7"
     let &t_EI = "\<Esc>]50;CursorShape=0\x7"
 endif

 " Only use cursorline/cursorcolun in normal mode
 autocmd InsertLeave * :set cursorline
 autocmd InsertLeave * :set cursorcolumn

 autocmd InsertEnter * :set nocursorline
 autocmd InsertEnter * :set nocursorcolumn

" autocmd VimLeave * :let &t_EI =  "\<Esc>]50;CursorShape=0\x7"

" Automatically adjust the quickfix size
" Set to a ratio/percentag of the window
" the cursor is in when this is called.
" Also honor a minimum height so the QFW
" won't get to small. And if the calculated
" size is larger then there are lines to put 
" in it, only size QF to the number of items 
" available.
au FileType qf call AdjustQFWindowHeight()
function! AdjustQFWindowHeight()
    " get the current window, qf, number and height
    let thiswindow = winnr()
    let thiswindow_h = winheight(0)
    let qnr = winnr('$')

    " go the last open window and get it's size
    " and add it to the qf window size and account for the
    " extra line seperating the two
    exe "wincmd w"
    let wh = winheight(0) + thiswindow_h + 1
    exe "wincmd w"

    " Open the quick to approx 1/3 the size of it's
    " closest relative.
    let qf_height = max([3, wh/3])

    " If the QF list isn't big enough to fill the 
    " new window size, shrink the window to the list.
    let qf_height = min([qf_height, len(getqflist())])
    

    " echo "window H: " . wh . ", qf_height " . qf_height
    exe "normal ". qnr . "\<C-W>w" 
    exe qf_height . "wincmd _"


    " Move the quickfix window to the bottom right
    " so it's always full length.
    exe "normal \<C-W>\<S-J>" 
endfunction

