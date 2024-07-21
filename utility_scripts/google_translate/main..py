from google.cloud import translate_v2 as translate

def translate_text(text, target='te'):
    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(f'Translation: {result["translatedText"]}')

if __name__ == "__main__":
    text = """
    version: '3.8'

    services:
      postgres:
        build:
          context: ./pg
    """

    translate_text(text)
