# DESIGN PATTERNS #

## Creational Patterns (Oluşturma Desenleri) ## 
* Abstract Factory
    >Abstract(soyut) Factory tasarım deseni, birbirine bağımlı nesnelerin ailesini oluşturmak için kullanılır ve bu nesnelerin nasıl oluşturulacağını gizler. Bir Abstract Factory, ilgili nesnelerin bir ailesini oluşturan ve bu nesnelerin nasıl oluşturulacağını tanımlayan bir arayüz sağlar. Ardından, somut fabrika sınıfları, bu arayüzü uygular ve belirli bir nesne ailesini oluşturur.

* Builder
    >Builder tasarım deseni, karmaşık nesnelerin adım adım oluşturulmasını sağlar ve farklı oluşturma adımlarını sarmalar. Bu tasarım deseni, nesne oluşturma sürecini basitleştirmek ve daha okunabilir, esnek kod oluşturmak için kullanılır.

* Factory Method
    >Factory Method tasarım deseni, bir üst sınıftaki bir methodu alt sınıflara devrederek nesnelerin oluşturulmasını sağlar. Bu desen, alt sınıfların nesnelerin türlerini belirleyebileceği ve bu nesneleri oluşturabileceği bir yapı sağlar.

* Prototype
    >Prototype tasarım deseni, bir nesnenin kopyasını oluşturarak yeni nesnelerin oluşturulmasını kolaylaştırır. Bu desen, bir nesnenin oluşturulması için maliyetli işlemleri azaltır ve karmaşık nesnelerin daha verimli bir şekilde oluşturulmasını sağlar.

* Singleton
    >Singleton tasarım deseni, bir sınıfın tek bir örneğinin (instance) oluşturulmasını ve tüm istemcilerin bu tek örneği paylaşmasını sağlar. Bu desen, bir nesnenin yalnızca bir kez oluşturulmasını ve global bir erişim noktası sağlamasını amaçlar.

## Structural Patterns (Yapısal Desenler) ## 
* Adapter
    >Adapter tasarım deseni, bir arayüzün beklenen bir şekilde davranmadığı durumlarda, mevcut bir sınıfın arayüzünü değiştirmek veya uyumlu hale getirmek için kullanılır. Bu desen, iki uyumsuz arayüzü bir araya getirerek birlikte çalışmalarını sağlar.

* Bridge
    >Bridge tasarım deseni, soyutlanmış bir arayüz ve uygulama arasındaki ilişkiyi koparır ve bu şekilde her ikisinin de bağımsız olarak değiştirilmesine olanak tanır. Bu desen, çok sayıda değişiklik yapıldığında kodun daha esnek ve bakımı daha kolay olmasını sağlar.

* Composite
    >Composite tasarım deseni, hiyerarşik bir nesne yapısını temsil eder ve bu nesnelerin tek bir nesne gibi davranmasını sağlar. Bu desen, parça-bütün ilişkisini temsil etmek için kullanılır ve ağaç yapısındaki nesnelerin işlenmesini kolaylaştırır.

* Decorator
    >Decorator tasarım deseni, bir nesneye dinamik olarak ek işlevsellik eklemeyi sağlar. Bu desen, bir nesneyi sarmalayarak (wrapper) ve bu nesneye ek işlevsellik ekleyerek çalışır.

* Facade
    >Facade tasarım deseni, bir alt sistemin karmaşıklığını gizlemek ve daha basit bir arabirim sağlamak için kullanılır. Bu desen, istemcilerin karmaşık alt sistemlerle doğrudan etkileşim kurmak yerine, bu alt sistemlerle iletişim kurmalarını sağlayan bir arayüz sağlar.

* Flyweight
    >Flyweight tasarım deseni, çok sayıda benzer nesnenin bellek kullanımını azaltmak için kullanılır. Bu desen, bir nesnenin paylaşılabilir durumdaki (intrinsic) kısmını ayırarak aynı veriyi paylaşan nesneler arasında bellek kullanımını minimize eder.

* Proxy
    >Proxy tasarım deseni, gerçek nesneye erişimi kontrol etmek, yükleme işlemlerini geciktirmek, önbelleklemek veya yetkilendirme eklemek gibi senaryolarda yaygın olarak kullanılır. Bu desen, uygulamanın performansını artırmak ve kaynakları etkin bir şekilde kullanmak için kullanılır.

## Behavioral Patterns (Davranış Desenleri) ## 
* Chain of Responsibility
    >Chain of Responsibility tasarım deseni, taleplerin işlenme sırasını dinamik olarak belirlemek ve her bir işleyiciyi gerektiğinde değiştirmek için kullanılır. Bu desen, istemcinin hangi işleyicinin talebi işleyeceğini bilmemesini ve isteği işleyecek işleyicinin otomatik olarak seçilmesini sağlar.

* Iterator
    >Iterator tasarım deseni, bir koleksiyon üzerinde gezinmek için bir arayüz sağlar ve koleksiyonun nasıl gezileceğini koleksiyonun kendisinden soyutlar. Bu desen, bir koleksiyonun iç yapısını değiştirmeden koleksiyon üzerinde farklı iterasyon stratejileri uygulamak için kullanılır.

* Memento
    >Memento tasarım deseni, bir nesnenin durumunu kaydetmek ve geri yüklemek için bir mekanizma sağlar. Bu desen, bir nesnenin iç durumunu saklamak ve sonradan geri yüklemek için kullanılır. Özellikle geri alma işlevselliği sağlamak için kullanılır.

* State
    >State tasarım deseni, bir nesnenin davranışını durumuna göre değiştirmek için kullanılır. Bu desen, bir nesnenin farklı durumlar arasında geçiş yapmasını sağlar ve durumlar arasındaki geçiş mantığını nesneden soyutlar. Bu, bir nesnenin durumunu dinamik olarak değiştirmek ve duruma bağlı davranışları yönetmek için kullanışlı bir yöntemdir.

* Template Method
    >Template Method tasarım deseni, bir sürecin yapısını belirleyen ancak bazı adımların alt sınıflar tarafından uygulanmasına izin veren bir yapı sağlar. Bu desen, bir algoritmanın genel yapısını tanımlamak ve alt sınıflar aracılığıyla belirli adımları özelleştirmek için kullanılır.

* Command
    >Command tasarım deseni, bir isteği nesne olarak temsil eder ve bu isteği bir aksiyona dönüştüren bir arayüz sağlar. Bu desen, komutların soyutlanmasını sağlar, böylece çağırıcı ve alıcı arasındaki bağımlılığı azaltır ve işlemleri parametrelerle ve önceden belirlenmiş komutlarla temsil eder.

* Mediator
    >Mediator tasarım deseni, bir grup nesnenin birbiriyle doğrudan iletişim kurmak yerine bir arabulucu aracılığıyla iletişim kurmasını sağlar. Bu, nesneler arasındaki bağımlılığı azaltır ve iletişimi merkezi hale getirerek sistemdeki karmaşıklığı azaltır.

* Observer
    >Observer tasarım deseni, bir nesnenin durumu değiştiğinde diğer nesneleri otomatik olarak güncellemek için kullanılır. Bu desen, nesneler arasındaki bağımlılığı azaltır ve sistemdeki değişiklikleri izlemeyi ve yönetmeyi kolaylaştırır.

* Strategy
    >Strategy tasarım deseni, algoritmayı sınıflara kapsülleyerek, algoritmanın kullanıldığı bağlamın değiştirilmesini sağlar. Bu, kodun daha modüler, esnek ve bakımı daha kolay hale gelmesini sağlar. Örneğin, bir hesap makinesi uygulamasında farklı matematiksel işlemler için aynı arayüzü sağlayarak, istenen işlemi dinamik olarak değiştirebiliriz.

* Visitor
    >Visitor tasarım deseni, bir nesne yapısını dolaşmak için bir ziyaretçi nesnesi kullanır. Bu desen, yeni işlevsellik eklemeyi kolaylaştırır çünkü yeni işlevselliği eklemek için yeni bir ziyaretçi sınıfı oluşturabiliriz. Ayrıca, eleman sınıflarını değiştirmeden farklı işlevselliği uygulamamıza olanak tanır.