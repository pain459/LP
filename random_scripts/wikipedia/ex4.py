# url, category and links
import wikipedia

categories = wikipedia.page('Python (programming language)').categories
links = wikipedia.page('"Hello, world!" program').links
set_lang = wikipedia.set_lang('hi')
lang_summary = wikipedia.page('Python (programming language)').summary


print(categories)
print(links)
print(lang_summary)