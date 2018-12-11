import sys
import re
import random


def convert_input_to_list():
    """Takes the (hardcoded) source information selected from the source code
    of thuisbezorgd and separates the lines in elements of a list.

    Returns
    -------
    list
        List containing as elements the lines of the source code.

    """

    f = open('pizza_source.txt', 'r')
    file_to_list = f.read().split('\n')

    return file_to_list


def parse_pizza_info(l):
    """Creatively finds order among chaos and returns the ingredients for each
    pizza in a dictionary.

    Parameters
    ----------
    l : list
        List which contains the lines of the source code in its elements.

    Returns
    -------
    dictionary
        Dictionary with the pizzas and their ingredients.

    """

    pizza_dict = {}

    for i, element in enumerate(l):
        if element.strip() == '<span class="meal-name" itemprop="name">':

            # Names of pizza
            pizza_name = l[i+1].split('<')[0].strip()
            pizza_dict[pizza_name] = []

        elif '<div class="meal-description-additional-info" itemprop="description">' in element:

            pizza_dict[pizza_name] = re.split(',|and',re.split('<|>|\(', element.strip())[2])
            pizza_dict[pizza_name] = [x.strip() for x in pizza_dict[pizza_name]]
            pizza_dict[pizza_name] = [x.strip('-') for x in pizza_dict[pizza_name]]

    return pizza_dict


def choose_pizza(pizzas):
    """Selects a random suitable pizza.

    Parameters
    ----------
    pizzas : dictionary
        Dictionary with the pizzas and their ingredients.

    Returns
    -------
    string
        Winner of the pizza competition.

    """
    possible_pizzas = []
    for i in pizzas.keys():
        suitable = True
        for element in pizzas[i]:
            if "tuna" in element:
                suitable =  False
            elif "garlic sauce" in element:
                suitable =  False
            elif "anchovy" in element:
                suitable =  False
            elif "mussels" in element:
                suitable =  False
            elif "shrimp" in element:
                suitable =  False
        if suitable:
            possible_pizzas.append(i)

    pizza_choice = random.choice(possible_pizzas)

    return pizza_choice


def print_winner(chosen_pizza):
    """Prints the choice of pizza for tonight.

    Parameters
    ----------
    chosen_pizza : string
        Winner of the pizza competition.

    """
    print("Tonight's pizza is {0}".format(chosen_pizza))


def main():
    """Finds a pizza that does not contain seafood nor garlic sauce.
    """
    splitted_file = convert_input_to_list()
    encyclopedia_of_pizza = parse_pizza_info(splitted_file)
    pizza_winner = choose_pizza(encyclopedia_of_pizza)
    print_winner(pizza_winner)


if __name__ == '__main__':
    main()
