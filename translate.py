from deep_translator import GoogleTranslator
import sys

def main():
    print("--- English to Russian Translator ---")
    print("Type your word or sentence below (or type 'exit' to quit):")
    
    # Initialize the translator
    translator = GoogleTranslator(source='en', target='ru')

    while True:
        try:
            # Get user input
            text = input("\nEnglish: ").strip()
            
            if not text:
                continue
                
            if text.lower() in ['exit', 'quit', 'e', 'q']:
                print("Goodbye!")
                break

            # Translate the text
            translation = translator.translate(text)
            
            # Print the result
            print(f"Russian: {translation}")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
