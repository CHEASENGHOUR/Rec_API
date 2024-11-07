# from faker import Faker
# import random
# import json

# fake = Faker()
# data = []

# for _ in range(50):
#     laptop = {
#         "id": _ + 1,
#         "title": fake.company() + " Laptop",
#         "description": fake.sentence(nb_words=6),
#         "rating": round(random.uniform(3.5, 5.0), 1),  # Rating between 3.5 and 5.0
#         "processor": fake.word(ext_word_list=["Intel i5", "Intel i7", "AMD Ryzen 5", "AMD Ryzen 7"]),
#         "ram_size": f"{random.choice([8, 16, 32])}GB",
#         "storage": f"{random.choice([256, 512, 1024])}GB SSD"
#     }
#     data.append(laptop)

# # Save data to a JSON file
# with open("laptop_data.json", "w") as f:
#     json.dump(data, f, indent=4)

# print("Generated data saved to laptop_data.json")
from faker import Faker
import random
import json

fake = Faker()
data = []

for _ in range(100):
    laptop = {
        "id": _ + 1,
        "title": fake.company() + " Laptop",
        "description": fake.sentence(nb_words=6),
        "rating": round(random.uniform(3.5, 5.0), 1),  # Rating between 3.5 and 5.0
        "processor": fake.word(ext_word_list=["Intel i5", "Intel i7", "AMD Ryzen 5", "AMD Ryzen 7"]),
        "ram_size": f"{random.choice([8, 16, 32])}GB",
        "storage": f"{random.choice([256, 512, 1024])}GB SSD",
        "price": round(random.uniform(300, 2000), 2),  # Price between $300 and $2000
        "stock": random.randint(1, 100),  # Stock between 1 and 100 units
        "image_url": f"https://via.placeholder.com/150?text=Laptop+{_+1}"  # Random image URL
    }
    data.append(laptop)

# Save data to a JSON file
with open("laptop_data_with_images.json", "w") as f:
    json.dump(data, f, indent=4)

print("Generated data with image URLs saved to laptop_data_with_images.json")
