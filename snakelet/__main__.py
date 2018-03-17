def main():
    import argparse
    import snakelet

    parser = argparse.ArgumentParser(description='Schema-less Micro-ORM')
    parser.add_argument('-v', '--version', dest='version', action='version', version=snakelet.__version__)
    parser.parse_args()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
