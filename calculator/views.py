from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe(request, name_of_dish):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    ingredients = get_recipe_ingredients(name_of_dish, servings)
    context = {
        'recipe': ingredients,
    }
    return render(request, template_name, context)


def get_recipe_ingredients(name_of_dish, person_number):
    dish = DATA.get(name_of_dish, {})
    ingredients = {}
    for k, v in dish.items():
        ingredients[k] = round(v * person_number, 2)
    return ingredients
