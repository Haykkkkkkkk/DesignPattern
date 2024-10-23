class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key)


config1 = Configuration()

config2 = Configuration()

config1.set("theme", "dark")

print(config2.get("theme"))  

print(config1 is config2) 
