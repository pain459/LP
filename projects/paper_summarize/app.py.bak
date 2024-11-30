import fitz
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles


app = Starlette()

# Specify the directory containing your static files
static_directory = "/path/for/directory/static"

# Mount the StaticFiles middleware to serve static files
app.mount("/static", StaticFiles(directory=static_directory), name="static")


def read_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def generate_summary(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join(str(sentence) for sentence in summary)

def main():
    # Path to the PDF file
    pdf_path = "/path/for/pdf/file.pdf"

    # Read the PDF
    pdf_text = read_pdf(pdf_path)

    # Generate Summary
    summary = generate_summary(pdf_text)

    # Print Summary
    print(summary)

if __name__ == "__main__":
    main()
