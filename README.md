# TerminalTranslator

Simple script to translate words or sentences between languages from the terminal. Uses the `deep-translator` library.

## How to use

1. Install requirements:
   ```bash
   pip install deep-translator
   ```

2. Run the script:
   ```bash
   python translate.py
   ```
   *By default, it translates from English to Russian.*

3. **Choose different languages:**
   ```bash
   python translate.py --src en --tgt fr
   ```

4. **List all supported languages:**
   ```bash
   python translate.py --list
   ```

5. Type any word or sentence and hit enter. Type `exit` to quit.

## Why?
Just needed a fast way to get translations without opening a browser every time.
