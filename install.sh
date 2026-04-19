#!/bin/bash

# Get the absolute path of the directory where the script is located
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SHELL_RC="$HOME/.bashrc"

# Check if it's zsh
if [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
fi

# Check if the alias already exists
if grep -q "alias trans=" "$SHELL_RC"; then
    echo "Alias 'trans' already exists in $SHELL_RC"
else
    echo "alias trans='python3 $PROJECT_DIR/translate.py'" >> "$SHELL_RC"
    echo "Alias 'trans' added to $SHELL_RC"
    echo "Please restart your terminal or run: source $SHELL_RC"
fi
