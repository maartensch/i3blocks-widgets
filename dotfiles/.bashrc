function nnode() {
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm
    echo "[✓] Loaded Node and npm"
}

# Colors in terminal
alias ls='ls --color'
alias grep='grep -n --color'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# Custom aliases
alias ll='ls -ahl'
alias snmr='sudo service network-manager restart'
alias venv3='virtualenv -p python3 .env'
alias a="atom && exit"

# Custom programs
export PATH=$PATH:/home/sword/git/mounty
export PATH=$PATH:/home/sword/git/finalyze
export PATH=$PATH:/home/sword/git/netflower
export PATH=$PATH:/home/sword/git/restbot
export PATH=$PATH:/home/sword/git/sqlitegrep
export PATH=$PATH:/home/sword/git/sysbash
export PATH=$PATH:/home/sword/git/slg
export ANDROID_HOME=$HOME/android-sdk
export PATH="$PATH:$ANDROID_HOME/tools"
export PATH="$PATH:$HOME/soundcloud-dl"
export PATH=$PATH:/home/sword/git/webstatus
