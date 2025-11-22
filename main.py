import random

# 1. 
print("1-masala (zar):", random.randint(1, 6))

# 2. 
four_digit = random.randint(1000, 9999)
print("2-masala (4 xonali son):", four_digit)

# 3. 
lst = ["olma", "banan", "anor", "gilos", "shaftoli"]
two_items = random.sample(lst, 2)
print("3-masala (2 ta element):", two_items)

# 4. 
num = random.randint(0, 100)
holat = "juft" if num % 2 == 0 else "toq"
print(f"4-masala: {num} → {holat}")

# 5.
letters = "abcdefghijklmnopqrstuvwxyz"
rand_string = "".join(random.choice(letters) for _ in range(10))
print("5-masala (10 harfli satr):", rand_string)

# 6. 
num2 = random.randint(1, 100)
holat2 = "katta" if num2 > 50 else "kichik yoki teng 50"
print(f"6-masala: {num2} → {holat2}")

# 7.
coin = random.choice(["heads", "tails"])
print("7-masala (tanga):", coin)
