class MyClass:
    @staticmethod
    def static_hello(name):
        print(f"سلام {name} (این یک static method است)")

    @classmethod
    def class_hello(cls, name):
        print(f"سلام {name} (این یک class method است از کلاس {cls.__name__})")

if __name__=="__main__":
    c=MyClass.static_hello('ali')
    b=MyClass.class_hello('ali')