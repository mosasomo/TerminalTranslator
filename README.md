# TerminalTranslator

Simple translate between languages from the terminal. Uses the `deep-translator` library.

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/mosasomo/TerminalTranslator.git
   cd TerminalTranslator
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Setup Shortcut (Optional)

To use the `trans` command from anywhere:

### Windows
1. Copy the path to `translate.py`.
2. Create a file named `trans.bat` in a folder that is in your PATH (like `C:\Windows`).
3. Add this to the file:
   ```batch
   @echo off
   python "C:\path\to\your\TerminalTranslator\translate.py" %*
   ```

### Linux/macOS
1. Add this to your `.bashrc` or `.zshrc`:
   ```bash
   alias trans='python3 /path/to/TerminalTranslator/translate.py'
   ```

## How to use

Run the script (or use the `trans` command if set up):
```bash
trans
```
*By default, it translates from English to Russian.*

### Options:
*   **Choose languages:** `trans --src en --tgt fr`
*   **List codes:** `trans --list`

Type any word or sentence and hit enter. Type `exit` to quit.
