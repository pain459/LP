## Installation

To set up the environment and install the necessary packages, run the following command from the root of this project:

```bash
python setup.py develop
```

### Usage
```bash
convert_script input_file output_file.pdf
```


### Explanation

1. **`find_packages()`**: This function automatically finds all packages in your project, assuming they are contained in directories with an `__init__.py` file.
   
2. **`install_requires`**: Lists all packages necessary for your project to run. These will be installed when the setup script is run.
   
3. **`entry_points`**: This makes your Python script accessible as a command-line tool after installation. Adjust `'convert_script=src.your_script:main'` to point to your script’s main function appropriately.

4. **`python_requires`**: Specifies which Python versions are compatible with your project.

### Final Steps

Run the setup script with:
```bash
python setup.py develop

