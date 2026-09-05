def make_car(first, last, **kwargs):
    kwargs['first_car'] = first
    kwargs['last_car'] = last
    return kwargs

user_cars = make_car('subaru', 'outback', color='blue', tow_package=True)
print(user_cars)

user_cars = make_car('dodge', 'GT RWD', color='red', tow_package=True)
print(user_cars)

user_cars = make_car('BMW', 'xDrive 18d M Sport SE', color='blue', tow_package=True)
print(user_cars)