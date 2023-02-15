class duck:
    def quack(self):
        print('quaack')

    def walk(self):
        print('walks like a duck')

def main():
    donald = duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__':
    main()