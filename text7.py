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
