def main(version: ("display version", 'flag', 'a')):
    import snakelet
    if version:
        print(snakelet.__version__)


if __name__ == '__main__':
    import plac

    try:
        plac.call(main)
    except KeyboardInterrupt:
        print('\nGoodbye!')
