from setuptools import setup, find_packages

setup(
    name="tp_pdf_converter",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'fpdf2',         # For PDF generation
        'ebooklib',      # For EPUB file handling
        'beautifulsoup4',# For parsing HTML
        'Pillow'         # For image processing in PDFs
    ],
    entry_points={
        'console_scripts': [
            'convert_script=src.your_script:main',  # Adjust accordingly if your function is named differently
        ]
    },
    python_requires='>=3.6',  # Specify your Python version requirements
)
