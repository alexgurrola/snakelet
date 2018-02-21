class Proxy:
    pass


def main():
    pass


if __name__ == '__main__':
    import plac

    try:
        plac.call(main)
    except KeyboardInterrupt:
        print('\nGoodbye!')
