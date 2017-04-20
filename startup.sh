#!/bin/bash

# Turn on syntax coloring in vi

echo -n "1. "
if [ -f $HOME/.vimrc ]
then
    echo ".vimrc file already exists."
else
    echo "syntax on" >> $HOME/.vimrc
    echo "set expandtab shiftwidth=4 softtabstop=0 autoindent tabstop=4" >> $HOME/.vimrc
    echo ".vimrc file created."
fi

# Edit local git config for syncing with Github
echo -n "2. "
git config --global user.name "lcy2"
git config --global user.email "lichangyi888@hotmail.com"
echo "git config set."

# turn on sound for Kali
echo -n "3. "
systemctl --user enable pulseaudio && systemctl --user start pulseaudio
echo "sound turned on"

# download Heroku
echo -n "3. "
wget https://cli-assets.heroku.com/branches/stable/heroku-linux-amd64.tar.gz -O heroku.tar.gz
tar -xvzf heroku.tar.gz -C /usr/local/lib
/usr/local/lib/heroku/install
echo "installed Heroku command line utility."
