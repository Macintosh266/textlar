# Python'da dekoratorlar (decorators) — bu funksiyalarga yoki klasslarga qo‘shimcha 
# imkoniyatlar berish uchun ishlatiladigan funksiya yoki klasslardir.
# Ular, mavjud funksiyani o‘zgartirmasdan, uning funksionalligini kengaytirishga imkon beradi.

import time
from itertools import count

# Dekorator — bu boshqa funksiyani qabul qilib, uni o‘zgartirgan yoki qo‘shimcha ish qilgan holda yangi funksiyani qaytaruvchi funksiya.

# Dekorator — bu funksiyani argument sifatida qabul qiluvchi va yangilangan funksiyani qaytaruvchi funksiya.


def decorater_func(func):
    def wrapper():
        print(f"Funksiya chaqirildi: {func.__name__}")
        start=time.time()
        sec=func()
        end=time.time()
        # print(f"{end-start} sekund")
        print("Abdulaziz")

    return wrapper

@decorater_func
def nums():
    count = 0
    for i in range(1, 100_000_000):
        count+=1

nums()

# Dekoratorlar qayerda foydali?
# 
# Log yozish (logging)
# Ruxsatni tekshirish (authentication)
# Vaqtni o‘lchash (timing)
# Cache (keshlash)
# Retry mexanizmlari

