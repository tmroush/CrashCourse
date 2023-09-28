def print_models(unprinted_designs, completed_models):
    """
    Simulated printing each design, until none are left.
    Move each design to completed_models after printing
    :param unprinted_designs: a list of the designs that need printing
    :param completed_models: a list of the designs that got pritned
    :return: nothing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


