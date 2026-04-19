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

3. **Auto-Setup Shortcut:**
   *   **Windows:** Double-click `install.bat`.
   *   **Linux/macOS:** Run `bash install.sh`.

## How to use

Once installed, just type:
```bash
trans
```
*By default, it translates from English to Russian.*

### Options:
*   **Choose languages:** `trans -from en -to fr`
*   **List codes:** `trans --list` (includes alphabetical sorting and interactive search)

Type any word or sentence and hit enter. Type `exit` to quit.
