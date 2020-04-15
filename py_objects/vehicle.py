class Vehicle():

    default_spec = "two"

    def __init__(self,make,spec):
        self.make = make
        self.spec = spec
    
    @classmethod
    def bicycle(cls,spec=None):
        if not spec:
            spec = cls.default_spec
        return cls(None,spec)

    @staticmethod
    def description():
        print("This is static method")