def make_car(make, model, **features):
    features['make'] = make
    features['model'] = model
    return features


car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car1)
car2 = make_car('mazda', 'miata', color='red', top='soft')
print(car2)
car3 = make_car('acura', 'mdx', color='gray', sport_package=True)
print(car3)