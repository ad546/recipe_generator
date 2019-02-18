#recipe program
import random

#list
# recipe_names = ['Breakfast Tacos', 'Shrimp Scampi', 'Enchiladas', 'Stir Fry', 'Shredded BBQ Pork',
                # 'Spaghetti and Meatballs', 'Buffalo Chicken Wings', 'Crockpot Chicken Casserole', 
                # 'Chicken Skillet Fajitas', 'Cast Iron Skillet Brussel Sprouts', 'Jambalaya', 'Chicken ' 
                # 'and Broccoli Alfredo Pasta', 'Spicy Pineapple Chicken', 'Stuffed Bell Peppers', 
                # 'Greek Chicken', 'Sausage Egg Casserole', 'Baked Chicken', 'Baked Pork Chop', 'Burgers',
                # 'Smothered Pork Chops', 'Red Beans and Rice', 'Mashed Cauliflower', 'Asparagus']

#dictionary
recipe_names = { 1 : ['Breakfast Tacos', 'Egg, Tortilla, Salsa', 295, 12, 5, 18], 2 : ['Shrimp Scampi','Shrimp, pasta, sauce',\
                330, 16, 2, 18], 3 : ['Enchiladas','Tortilla, Chicken, Enchilada Sauce, Beans', 400, 13, 13, 13]}



def main():
    rand_int = random.randrange(1, len(recipe_names) + 1) 
    print(rand_int)
    print(recipe_names[rand_int][0])

def create_recipe():
    print('placeholder')

if __name__ == '__main__':
    main()