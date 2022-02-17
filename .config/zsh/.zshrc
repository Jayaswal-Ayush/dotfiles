#
#███████╗███████╗██╗  ██╗
#╚══███╔╝██╔════╝██║  ██║
#  ███╔╝ ███████╗███████║
# ███╔╝  ╚════██║██╔══██║
#███████╗███████║██║  ██║
#╚══════╝╚══════╝╚═╝  ╚═╝
# Basic stff
source ~/.config/zsh/.zprofile #.zshenv stuff
export TERM="xterm-256color"
export HISTFILE=~/.config/zsh/.zsh_history
export EDITOR='nvim'
export TERMINAL='st'
export BROWSER='firefox'
HISTSIZE=100000
SAVEHIST=100000
HISTFILE=~/.config/zsh/.zsh_history

# Basic zsh settings
PATH=$PATH:$HOME/.scripts #making my scripts run without typing the whole path
autoload -Uz compinit && compinit #need the next two lines for case insensitive tab completion
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}'
# Prompt Settings
declare -a PROMPTS
PROMPTS=(	" "
	" "
	"# "
	" ")

RANDOM=$$$(date +%s)
ignition=${PROMPTS[$RANDOM % ${#RANDOM[*]}+1]}
PROMPT='%F{green}%1~%f %F{red}$ignition%f '
## Git Settings
autoload -Uz vcs_info
precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )
setopt prompt_subst
RPROMPT=\$vcs_info_msg_0_
zstyle ':vcs_info:git:*' formats '%F{yellow}(%b)%r%f'
zstyle ':vcs_info:*' enable git
# Aliases
## App launchers
alias bt='bat -p'
alias weather='curl wttr.in'
alias kill='killall -q'
alias wal='feh --bg-fill --randomize ~/.config/wall/*'
alias ls='exa -a'
alias zshrc="vim ~/.config/zsh/.zshrc"      
alias config="ranger ~/.config/"
alias sound="pulsemixer"
# Snippets
alias ddate='date +"%R - %a, %B %d, %Y" | xclip -select clipboard && date +"%R - %a, %B %d, %Y"' 
alias dday='date +"%Y.%m.%d - " | xclip -select clipboard ; date +"%Y.%m.%d"'

source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
ZSH_AUTOSUGGEST_STRATEGY=(history completion)
