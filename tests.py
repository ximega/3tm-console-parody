class Foo:
    class Bar:
        def __init__(self):
            self.bar = "112233"
            
    def __init__(self):
        self.foo = 'abc'
        self.sbar = self.Bar()
        
obj = Foo()

print(obj.Bar)