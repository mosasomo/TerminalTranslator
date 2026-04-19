from deep_translator import GoogleTranslator
import sys
import argparse

def list_languages():
    langs = GoogleTranslator().get_supported_languages(as_dict=True)
    print("\nSupported languages (Code: Name):")
    for name, code in langs.items():
        print(f"{code}: {name}")

def main():
    parser = argparse.ArgumentParser(description="Simple Translator")
    parser.add_argument("--src", default="en", help="Source language code (default: en)")
    parser.add_argument("--tgt", default="ru", help="Target language code (default: ru)")
    parser.add_argument("--list", action="store_true", help="List all supported language codes")
    
    args = parser.parse_args()

    if args.list:
        list_languages()
        return

    src_name = GoogleTranslator().get_supported_languages(as_dict=True).get(args.src, args.src)
    tgt_name = GoogleTranslator().get_supported_languages(as_dict=True).get(args.tgt, args.tgt)

    print(f"--- {src_name.title()} to {tgt_name.title()} Translator ---")
    print("Type your word or sentence below (or type 'exit' to quit):")
    
    try:
        translator = GoogleTranslator(source=args.src, target=args.tgt)
    except Exception as e:
        print(f"Error initializing translator: {e}")
        return

    while True:
        try:
            text = input(f"\n{args.src.upper()}: ").strip()
            
            if not text:
                continue
                
            if text.lower() in ['exit', 'quit', 'e', 'q']:
                print("Goodbye!")
                break

            translation = translator.translate(text)
            print(f"{args.tgt.upper()}: {translation}")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
