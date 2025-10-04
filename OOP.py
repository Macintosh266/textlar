"Meto programming"-bu programmislar ishlatishi uchun yozilgan ko'dlar
masalan django


# OOP (Object-Oriented Programming – obyektga yo‘naltirilgan dasturlash) – bu dasturlash paradigmasi bo‘lib, unda dastur obyektlar va ularning o‘zaro aloqalari orqali quriladi. OOP dasturlashni yanada modulli, tushunarli va kengaytiriladigan qiladi.


# ---

# 🔑 OOP ning asosiy tushunchalari:

# 1. Class (klass)

# Bu – obyektlarning “andazasi” yoki “shabloni”.

# Klassda xususiyatlar (atributlar) va metodlar (funksiyalar) aniqlanadi.


class Car:
    def init(self, model, color):
        self.model = model
        self.color = color

    def drive(self):
        print(f"{self.color} {self.model} haydamoqda...")

# 2. Object (obyekt)

# Klassdan yaratilgan an’anaviy nusxa.


car1 = Car("BMW", "Qora")
car2 = Car("Tesla", "Oq")

car1.drive()  # Qora BMW haydamoqda...
car2.drive()  # Oq Tesla haydamoqda...


# ---

# 🔑 OOP ning asosiy prinsiplari:

# 1. Encapsulation (inkapsulyatsiya)

# Ma’lumotlarni yashirish va faqat kerakli metodlar orqali ularga murojaat qilish.

# Masalan: private, protected, public tushunchalari.


class BankAccount:
    def init(self, balans):
        self.__balans = balans   # private atribut

    def deposit(self, amount):
        self.__balans += amount

    def get_balance(self):
        return self.__balans

#==== Inkapsulyatsiya darajalari (Python’da) ====

# public → hamma joyda ochiq (self.name)

# _protected → faqat ichki va voris sinflar uchun (self._name)

# __private → tashqaridan kira olmaydi (self.__name)


# 2. Inheritance (merosxo‘rlik)

# Merosxo‘rlik orqali bir sinf (child, subclass) boshqa sinfning (parent, superclass) xususiyatlari va metodlarini o‘ziga oladi.
# Ya’ni, yangi sinfni yozishda hamma narsani boshqatdan yozish shart emas — ota-sinfdagi kodni qayta ishlatish mumkin.

# 🟢 Merosxo‘rlikning asosiy turlari:
# 1, Single Inheritance (Yagona meros)

# Bitta bola sinf faqat bitta ota-sinfdan meros oladi.

class Animal:
    def sound(self):
        print("Hayvon tovushi")

class Dog(Animal):   # faqat Animal’dan meros oldi
    def sound(self):
        print("Vov-vov")

dog = Dog()
dog.sound()  # Vov-vov

# 2, Multilevel Inheritance (Ko‘p darajali meros)

# Bir sinf boshqa sinfdan, u yana boshqasidan meros oladi → zanjir hosil bo‘ladi.

class LivingThing:
    pass

class Animal(LivingThing):  # LivingThing dan meros oladi
    pass

class Dog(Animal):  # Animal dan meros oladi
    pass


# 👉 Bu yerda Dog → Animal → LivingThing zanjiri bor.

# 3, Hierarchical Inheritance (Ierarxik meros)

# Bitta ota-sinfdan bir nechta bola-sinflar meros oladi.

class Animal:
    def sound(self):
        print("Hayvon tovushi")

class Dog(Animal):
    def sound(self):
        print("Vov-vov")

class Cat(Animal):
    def sound(self):
        print("Miyov-miyov")


# 👉 Dog va Cat ikkalasi ham Animaldan meros olgan.

# 4, Multiple Inheritance (Ko‘p ota-sinfli meros)

# Bir bola-sinf bir nechta ota-sinfdan meros oladi.

class Father:
    def skill(self):
        print("Otadan: Avtomobil haydash")

class Mother:
    def skill(self):
        print("Onadan: Ovqat pishirish")

class Child(Father, Mother):  # ikkala sinfdan meros
    pass

c = Child()
c.skill()   # MRO (Method Resolution Order) bo‘yicha birinchi Father’dan oladi

# 5, Hybrid Inheritance (Aralash meros)

# Yuqoridagi turlarni aralashtirib ishlatish.
# Masalan, multiple va multilevelni qo‘shib yuborish.

# 👉 Bunda MRO (Method Resolution Order) muhim: ya’ni metodlarni qaysi tartibda qidirishi belgilanadi.

# 🟣 Xulosa

# OOP’da merosxo‘rlikning turlari:

# Single (yagona)

# Multilevel (zanjirli)

# Hierarchical (ierarxik)

# Multiple (ko‘p ota-sinfli)

# Hybrid (aralash)

# 3. Polymorphism (polimorfizm)

# Bir xil metod nomi turli klasslarda turlicha ishlaydi.

# 🧠 1️⃣ Polimorfizm nima?

# Polimorfizm — so‘zma-so‘z tarjimada “ko‘p shakllilik” degan ma’noni anglatadi.
# Ya’ni bitta amal yoki metod turli sinflarda turlicha ishlaydi.

# Oddiy qilib aytganda: “Bir xil nomdagi metod — har xil obyektlarda har xil natija beradi.”

# 🎯 2️⃣ Maqsadi

# Polimorfizmning asosiy maqsadi —
# 👉 Kodni moslashuvchan va kengaytiriladigan qilish.
# 👉 Har xil obyektlar bilan bir xil interfeys orqali ishlash imkonini beradi.

# 🐍 3️⃣ Python misolida
# 🧩 Misol 1: Metod nomi bir xil, lekin har xil xulq
class Dog:
    def sound(self):
        return "Vov-vov"

class Cat:
    def sound(self):
        return "Miyov-miyov"

# Polimorfizm ishlatilmoqda:
for animal in [Dog(), Cat()]:
    print(animal.sound())


# 📤 Natija:

# Vov-vov
# Miyov-miyov


# Bu yerda sound() metodi bir xil nomda, lekin har bir sinfda turlicha ishlaydi.

# 🧩 Misol 2: Meros orqali (Overriding)
class Animal:
    def speak(self):
        print("Hayvon tovushi")

class Dog(Animal):
    def speak(self):
        print("Vov-vov")

class Cat(Animal):
    def speak(self):
        print("Miyov-miyov")

animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()


# 📤 Natija:

# Vov-vov
# Miyov-miyov
# Hayvon tovushi


# 👉 Bu method overriding deb ataladi — ota-sinfdagi metodni bola-sinf qayta aniqlaydi.
# Bu runtime polymorphism deyiladi (ya’ni ish vaqtida aniqlanadi).

# 🧩 Misol 3: Funksiya darajasida (Duck Typing)

# Python’da statik tur aniqlanmaganligi sababli, “polimorfizm” tabiiy tarzda ishlaydi.

class Bird:
    def fly(self):
        print("Qush uchmoqda")

class Airplane:
    def fly(self):
        print("Samolyot uchmoqda")

class Rocket:
    def fly(self):
        print("Raketa uchmoqda")

# Bir xil funksiyadan foydalanamiz
def lift_off(obj):
    obj.fly()

for obj in [Bird(), Airplane(), Rocket()]:
    lift_off(obj)


# 📤 Natija:

# Qush uchmoqda
# Samolyot uchmoqda
# Raketa uchmoqda


# 👉 Bu duck typing deyiladi:

# “Agar u o‘rdak kabi yurib, o‘rdak kabi qichqirsa — demak, u o‘rdak.”
# Ya’ni obyekt turi emas, balki unda kerakli metod borligi muhim.

# ⚙️ 4️⃣ Polimorfizm turlari
# Turi	Tushuntirish	Misol
# Compile-time (Static)	Dastur bajarilishidan oldin aniqlanadi	Method overloading (Java, C++)
# Run-time (Dynamic)	Dastur ish paytida aniqlanadi	Method overriding (Python, Java)

# Python’da asosan dynamic polymorphism ishlatiladi.

# 🧩 5️⃣ Method Overloading (Python’da “cheklangan”)

# Python’da rasmiy method overloading yo‘q, lekin uni *args orqali taqlid qilish mumkin:

class Math:
    def add(self, *args):
        return sum(args)

m = Math()
print(m.add(2, 3))
print(m.add(2, 3, 4))


# 📤 Natija:

# 5
# 9

# 💡 6️⃣ Real hayotdagi analogiya

# Biror so‘z har xil kontekstda turlicha ma’no beradi:

# “Run” – odam yuguradi

# “Run a program” – dastur ishga tushadi

# “Run a company” – kompaniya boshqariladi

# 👉 Bu ham polimorfizm: bitta so‘z (metod) – turli xatti-harakatlar (implementatsiya).

# 🔚 Xulosa:

# Polimorfizm — bu bir xil metod yoki funksiya turli obyektlarda turlicha ishlashidir.

# Afzalliklari:

# Kodni qayta ishlatish oson

# Tizimni kengaytirish oson

# Katta loyihalarda moslashuvchanlikni oshiradi


# 4. Abstraction (abstraksiya)

# Faqat kerakli funksionallikni ko‘rsatish, keraksiz tafsilotlarni yashirish.

# Python’da abc (Abstract Base Class) yordamida qilinadi.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def init(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

circle = Circle(5)
print(circle.area())  # 78.5


# ---

# ✅ OOP ning afzalliklari:

# Kodni modulli qiladi (bo‘laklarga bo‘lib ishlash mumkin).

# Qayta foydalanish oson (merosxo‘rlik orqali).

# Oson kengaytiriladi (yangi obyektlar qo‘shish).

# Real hayotdagi obyektlarni modellashtirish qulay.

# ======================================================
# ======================================================

# 🧠 Getter va Setter nima?

# Getter va Setter – bu obyekt (klass) ichidagi xususiy (private) qiymatlarni nazorat bilan olish va o‘zgartirish uchun ishlatiladigan metodlar (funksiyalar)dir.

# 📌 Asosiy maqsadlari:

# Encapsulation (inkapsulyatsiya) tamoyilini qo‘llash – ya'ni ma'lumotlarni bevosita emas, balki maxsus metodlar orqali boshqarish.

# Ma'lumotga kirish va o‘zgartirishda nazorat o‘rnatish.

# Xavfsizlik va barqarorlikni ta'minlash (nojo‘ya qiymatlardan himoya qilish).

# 🔒 Misol: Python dasturlash tilida
class Student:
    def __init__(self, name, age):
        self.__name = name     # private o'zgaruvchi
        self.__age = age       # private o'zgaruvchi

    # Getter - qiymatni olish
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter - qiymatni o'zgartirish
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Yosh manfiy bo'lishi mumkin emas!")

# 📋 Foydalanish:
student = Student("Ali", 20)

print(student.get_name())   # Ali
student.set_age(-5)         # Xato: Yosh manfiy bo'lishi mumkin emas!
student.set_age(21)
print(student.get_age())    # 21

# ⚙️ Getter va Setter-larni zamonaviy usulda – @property bilan ham yozish mumkin (Python):
class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):   # getter
        return self.__name

    @name.setter
    def name(self, value):   # setter
        self.__name = value

# 💡 Qayerda ishlatiladi?

# OOP (Object Oriented Programming) dasturlashda.

# Har qanday til: Python, Java, C#, JavaScript va hokazo.

# Ma'lumotlarga to'g'ridan-to'g'ri emas, chegaralangan va nazoratli kirishni ta'minlash uchun.
