from IPython import embed
from time import sleep

def main():

    x = ['hello', 'world']

    for i in xrange(1000000000):
        try:
            sleep(1)
        except KeyboardInterrupt:
            embed()

if __name__ == '__main__':
    main()
