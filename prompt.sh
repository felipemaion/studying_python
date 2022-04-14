
function timerNow {
    /usr/local/opt/coreutils/libexec/gnubin/date +%s%N
    # date +%s
    # https://stackoverflow.com/questions/1862510/how-can-the-last-commands-wall-time-be-put-in-the-bash-prompt/1862762#1862762
}

function timerStart {
    timerStart=${timerStart:-$(timerNow)}
}

function timerStop {
    local deltaUs=$((($(timerNow) - $timerStart) / 1000))
    local us=$((deltaUs % 1000))
    local ms=$(((deltaUs / 1000) % 1000))
    local s=$(((deltaUs / 1000000) % 60))
    local m=$(((deltaUs / 60000000) % 60))
    local h=$((deltaUs / 3600000000))
    # Goal: always show around 3 digits of accuracy
    if ((h > 0)); then timerShow=${h}h${m}m
    elif ((m > 0)); then timerShow=${m}m${s}s
    elif ((s >= 10)); then timerShow=${s}.$((ms / 100))s
    elif ((s > 0)); then timerShow=${s}.$(printf %03d $ms)s
    elif ((ms >= 100)); then timerShow=${ms}ms
    elif ((ms > 0)); then timerShow=${ms}.$((us / 100))ms
    else timerShow=${us}us
    fi
    unset timerStart
    timerStop=${s}
}

EMOJIS=( 🤔 😱 🙄 😖 😏 🤦‍♂ 🙏 🤮 💩 😳 🥵 🤬 🤓 🧐 💬 💭 🗯 📀 💡 ⏳ 🔮 🦠 🧨 💣 🧲 🧫 🎹 🦜 🎯 🎲)

# function that selects and return a random element from the EMOJIS set
RANDOM_EMOJI() {
  SELECTED_EMOJI=${EMOJIS[$RANDOM % ${#EMOJIS[@]}]};
  echo $SELECTED_EMOJI;
}

set_prompt () {
    LastCommand=$? # Must come first!
    Blue='\[\e[01;34m\]'
    White='\[\e[01;37m\]'
    Red='\[\e[01;31m\]'
    Green='\[\e[01;32m\]'
    Reset='\[\e[00m\]'
    FancyX='\[\342\234\]\227'
    Checkmark='\[\342\234\]\223'

# $([ $timer_show -gt 3 ] && echo -e "\a[${timer_show}s]")
    # Add a bright white exit status for the last command
    # PS1="\n$White$([ $LastCommand -ne 0 ] && echo -e 'Error Status: $?\n ')"
    # If it was successful, print a green check mark. Otherwise, print
    # a red X.
    PS1="\\n"
    if [[ $LastCommand == 0 ]]; then
        PS1+="$Green$Checkmark "
    else
        PS1+="$Red$FancyX \\a Error Status: $LastCommand "
    fi

    # Add the ellapsed time and current date
    local S=$(timerStop)
    timerStop
    PS1+="($timerShow) "
    # $([ $timer_show -gt 3 ] && echo -e "\a[${timer_show}s]
    # If root, just print the host in red. Otherwise, print the current user
    # and host in green.
    if [[ $EUID == 0 ]]; then
        PS1+="$Red\\u$Green@\\h \n"
    else
        PS1+="$Green\\u@\\h \n"
    fi
    # Print the working directory and prompt marker in blue, and reset
    # the text color to the default.
    PS1+="@: $Blue\\w \\n$(RANDOM_EMOJI) =>"
    PS1+="$Reset"
}

trap 'timerStart' DEBUG
PROMPT_COMMAND='set_prompt'