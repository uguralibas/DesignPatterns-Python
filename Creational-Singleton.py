"""
Singleton tasarım deseni, bir sınıfın tek bir örneğinin (instance) oluşturulmasını ve 
tüm istemcilerin bu tek örneği paylaşmasını sağlar. Bu desen, 
bir nesnenin yalnızca bir kez oluşturulmasını ve 
global bir erişim noktası sağlamasını amaçlar.
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Kullanım
def main():
    # Singleton sınıfından iki örnek oluşturulur
    obj1 = Singleton()
    obj2 = Singleton()

    # İki örnek aynı mı?
    print(obj1 is obj2)  # True

if __name__ == "__main__":
    main()