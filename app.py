from flask import Flask, render_template, request
import random

app = Flask(__name__)

themes = {
    "cookies": {
        "base": ["flour", "oats", "almond flour"],
        "sweetener": ["sugar", "honey", "brown sugar"],
        "fat": ["butter", "coconut oil", "margarine"],
        "mix-ins": ["chocolate chips", "nuts", "dried fruit"]
    },

    "cupcakes": {
        "base": ["flour", "cake mix", "almond flour"],
        "sweetener": ["sugar", "honey", "maple syrup"],
        "flavor": ["vanilla", "chocolate", "red velvet", "lemon"],
        "fat": ["butter", "vegetable oil", "yogurt"],
        "toppings": ["frosting", "sprinkles", "whipped cream"]
    },

    "brownies": {
        "base": ["flour", "cocoa powder", "almond flour"],
        "sweetener": ["sugar", "honey", "maple syrup"],
        "fat": ["butter", "coconut oil", "vegetable oil"],
        "mixins": ["nuts", "chocolate chips", "caramel bits"],
        "chocolate": ["dark chocolate", "milk chocolate", "white chocolate"],
        "toppings": ["powdered sugar", "whipped cream", "ice cream"]
    }
}


@app.route("/")
def index():
    return render_template("index.html", themes=themes)


@app.route("/generate", methods=["POST"])
def generate():
    chosen_theme = request.form["theme"]
    selections = themes[chosen_theme]

    user_choices = {}
    for category, options in selections.items():
        user_choices[category] = request.form.get(category) or random.choice(options)


    return render_template("result.html",
                           theme=chosen_theme,
                           choices=user_choices)


if __name__ == "__main__":
    app.run(debug=True)
