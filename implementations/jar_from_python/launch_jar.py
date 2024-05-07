import subprocess


def run_jar(jar_file):
    '''Launch jar from python'''
    try:
        # launch the script
        subprocess.run(['java', '-jar', jar_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Java application failed {e}')
    except Exception as e:
        print(f'An error occurred {e}')

def main():
    run_jar('helloWorld.jar')

if __name__ == "__main__":
    main()