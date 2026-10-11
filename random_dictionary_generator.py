import json
import random
import string

count = 1000000
min_len, max_len = 5, 15
chars = string.ascii_lowercase + string.digits + string.punctuation

words = {
    "".join(random.choices(chars, k=random.randint(min_len, max_len)))
    for _ in range(count)
}

with open("words.json", "w") as f:
    json.dump(list(words), f, indent=2)