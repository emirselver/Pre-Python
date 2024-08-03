#fonksiyondan bahsederken **args ve **kwargs kavramlarını anlatmayı unutma
#oop ye değineceğiz ama haftaya giriş yapacağız
#modüllere belki ufak ufak başlayabiliriz

#Problem21 : Amicable numbers

def amicable_numbers():

    for i in range(1,10000):
        num1_divisor_total = 0
        num2_divisor_total = 0
        for j in range(1, i):
            if i % j == 0:
                num1_divisor_total += j

        for k in range(1, num1_divisor_total):
            if num1_divisor_total % k == 0:
                num2_divisor_total += k

        if i == num2_divisor_total:
            print("kardeş sayılar...")

amicable_numbers()

