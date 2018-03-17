import subprocess


def main():
    # generate requirements
    process = subprocess.Popen(
        ['pipreqs', './', '--force'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, err = process.communicate()
    if process.returncode != 0:
        print(str(err, 'utf-8'))
        return

    # settings
    requirements_file = 'requirements.txt'

    # read
    with open(requirements_file, 'r') as requirements:
        content = requirements.read().splitlines()

    # sort content
    content = list(set(content))
    content.sort(key=lambda y: y.lower())
    content = '\n'.join(content)

    # save
    with open(requirements_file, 'w') as requirements:
        requirements.write(f'{content}\n')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
