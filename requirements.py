def main():
    # settings
    requirements_file = 'requirements.txt'

    # read
    with open(requirements_file, 'r') as requirements:
        content = requirements.read().splitlines()

    # sort content
    content = list(set(content))
    content.sort(key=lambda y: y.lower())
    content = '\n'.join(content)
    print(content)


if __name__ == '__main__':
    import plac

    try:
        plac.call(main)
    except KeyboardInterrupt:
        print('\nGoodbye!')
