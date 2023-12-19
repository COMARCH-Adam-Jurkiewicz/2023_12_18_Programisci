class First:
    def run(self):
        print("running from first")

class Second:
    def run(self):
        print("running from second")

class Third(First):
    def third_run(self):
        print("running from third")

first = First()
second = Second()
third = Third()

first.run()
second.run()

third.third_run()
third.run()