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

# 2. Inheritance (merosxo‘rlik)

# Bir klass boshqa klassdan xususiyatlarni meros qilib oladi.

# Kodni qayta yozmasdan foydalanish imkonini beradi.


class Animal:
    def sound(self):
        print("Hayvon tovush chiqarmoqda")

class Dog(Animal):
    def sound(self):
        print("Vov-vov!")

dog = Dog()
dog.sound()  # Vov-vov!

# 3. Polymorphism (polimorfizm)

# Bir xil metod nomi turli klasslarda turlicha ishlaydi.


class Cat:
    def sound(self):
        print("Miyov!")

class Dog:
    def sound(self):
        print("Vov-vov!")

for animal in [Cat(), Dog()]:
    animal.sound()
# Miyov!
# Vov-vov!

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