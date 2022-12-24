import random
import string


def create_string_number(n):
    """生成一串指定位数的字符+数组混合的字符串"""
    m = random.randint(1, n)
    a = "".join([str(random.randint(0, 9)) for _ in range(m)])
    b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
    return ''.join(random.sample(list(a + b), n))


with open('VIN.txt', 'w') as f:
    for i in range(30):
        vin = 'LGW'
        vin = vin + create_string_number(14).upper() + '\n'
        f.write(vin)
