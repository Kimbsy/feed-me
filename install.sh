BASHCONFIG=$1

RUNPATH="$(pwd)/src/feed-me.py"

if grep -q "feed-me" $BASHCONFIG; then
    echo "feed-me command seems to already be installed."
else
    echo "Installing feed-me command..."
    sudo echo "# Python dinner choosing application." >> $BASHCONFIG
    sudo echo "alias feed-me='sudo python3 $RUNPATH'" >> $BASHCONFIG
    echo "Done."
fi
