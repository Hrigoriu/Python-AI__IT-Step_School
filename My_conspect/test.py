import time

time.sleep(10)
print("Hello world!") # This text will be displayed after 10 seconds.

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)


        return cls._instance



singleton_1 = Singleton()
singleton_2 = Singleton()
print(id(singleton_1))
print(id(singleton_2))