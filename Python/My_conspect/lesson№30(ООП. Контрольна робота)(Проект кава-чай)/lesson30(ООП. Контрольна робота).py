from customer import Customer
from beverage import Coffee, Tea

def main():
    print('Welcome to Coffee Shop!')
    name = input('Enter your name: ')
    customer = Customer(name)

    while True:
        print('Menu: ')
        print('1. Coffee')
        print('2. Tea')
        print('3. Show order')
        print('4. Checkout and exit')

        choice = input('Choice an option: ')

        match choice:
            case '1':
                size = input('Choose size (small, medium, large): ').lower()

                coffee = Coffee(size)
                customer.add_to_order(coffee)
            case '2':
                flavor = input('Choose flavor: ').lower()

                tea = Tea(flavor)
                customer.add_to_order(tea)
            case '3':
                customer.checkout()
            case '4':
                customer.checkout()
                print('Thank you for visit!')
                exit()
            case _:
                print('Unknown option!')


if __name__ == '__main__':
    main()
