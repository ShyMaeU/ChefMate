import random 

print("Welcome to ChefMate!")
print("Let's make a desert together!\n")
themes = {
    "cookies" : { 
        "base": ["flour", "oats", "almond flour"],
        "sweetener": ["sugar", "honey", "brown sugar"],
        "fat": ["butter", "coconut oil", "margarine"],
        "mixins": ["chocolate chips", "nuts", "dried fruit"],
        "flavor": ["vanilla", "chocolate", "peanut butter"],
        "toppings": ["sprinkles", "icing", "sea salt"]

    },

    "cupcakes" : {
        "base": ["flour", "cake mix", "almond flour"],
        "sweetener": ["sugar", "honey", "maple syrup"],
        "flavor": ["vanilla", "chocolate", "red velvet", "lemon"],
        "fat": ["butter", "vegetable oil", "yogurt"],
        "toppings": ["frosting", "sprinkles", "whipped cream"],
        "mixins": ["fruit", "nuts", "chocolate chips"]
    
    },

    "brownies" : {
        "base": ["flour", "cocoa powder", "almond flour"],
        "sweetener": ["sugar", "honey", "maple syrup"],
        "fat": ["butter", "coconut oil", "vegetable oil"],
        "mixins": ["nuts", "chocolate chips", "caramel bits"],
        "flavor": ["dark chocolate", "milk chocolate", "white chocolate"],
        "toppings": ["powdered sugar", "whipped cream", "ice cream"]
    }
}
print("Choose a dessert theme:")
for theme in themes:
    print("-", theme)
chosen_theme = input("Enter your choice: ").strip().lower()
if chosen_theme not in themes:
    print("Sorry, that theme is not available. Please choose from the listed themes.")
    exit()
selected_theme = themes[chosen_theme]

print(f"\nGreat choice! Let's customize your {chosen_theme} recipe!\n")
# BASE
base_options = selected_theme["base"]
print("Choose your base:")
print("Options:", ", ".join(base_options))
base = input("Enter your choice: ").strip().lower()
if base not in base_options:
    base = random.choice(base_options)  
    print(f"Invalid choice. We'll use: {base}")

# SWEETENER
sweetener_options = selected_theme["sweetener"]
print("\nChoose your sweetener:")
print("Options:", ", ".join(sweetener_options))
sweetener = input("Enter your choice: ").strip().lower()
if sweetener not in sweetener_options:
    sweetener = random.choice(sweetener_options)
    print(f"Invalid choice. We'll use: {sweetener}")

    # FAT
fat_options = selected_theme["fat"]
print("\nChoose your fat ingredient:")
print("Options:", ", ".join(fat_options))
fat = input("Enter your choice: ").strip().lower()
if fat not in fat_options:
    fat = random.choice(fat_options)
    print(f"Invalid choice. We'll use: {fat}")

# FLAVOR
if "flavor" in selected_theme:
    flavor_options = selected_theme["flavor"]
    print("\nChoose your flavor:")
    print("Options:", ", ".join(flavor_options))
    flavor = input("Enter your choice: ").strip().lower()
    if flavor not in flavor_options:
        flavor = random.choice(flavor_options)
        print(f"Invalid choice. We'll use: {flavor}")



# TOPPINGS OR MIXINS
topping_options = selected_theme.get("toppings") or selected_theme.get("mixins")
print("\nChoose your topping:")
print("Options:", ", ".join(topping_options))
topping = input("Enter your choice: ").strip().lower()
if topping not in topping_options:
    topping = random.choice(topping_options)
    print(f"Invalid choice. We'll use: {topping}")


# Random cooking style
cooking_styles = ["baked", "whipped", "no-bake", "chilled"]
cooking_style = random.choice(cooking_styles)

#Generate recipe name
adjectives = ["Delightful", "Scrumptious", "Heavenly", "Dreamy"]
recipe_name = f"{random.choice(adjectives)} {flavor.capitalize() if flavor else 'Desert' } Surprise"

#Display the recipe
print("\nHere's your custom dessert recipe!")
print(f"Recipe Name: {recipe_name}")
print(f"Ingredients: {base}, {sweetener}, {flavor}, topped with {topping}, prepared in a {cooking_style} style.")

print(f"\nInstructions:")
print(f"1. Combine the {base} with {sweetener} and {flavor}.")
print(f"2. Add a hint of {flavor} and {topping} on top.")
print(f"3. {cooking_style.title()} for 20 minutes.")
print(f"4. Serve and enjoy your {recipe_name}!")

#Reactions = 
reactions = [
    "Yum! This was delicious!",
    "Oops it stuck to the pan, but still tasty!",
    "This is going to be my new favorite dessert!",
    "It's a bit too sweet for my taste, but still good!",
    "Wow, I didn't expect it to turn out this good!"
]

print("\nHow do you feel about your dessert?")
for i, reaction in enumerate(reactions, 1):
    print(f"{i}. {reaction}")
