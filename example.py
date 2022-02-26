import function

if __name__ == '__main__':
    while (1):
        print("\r\n1: Search historical data")
        print("2: Convert price")
        print("3: Exit")
        command = input("Enter command: ")

        if (command == '1'):
            print("\r\n-Search historical data-")
            source = input("Base Currency: ")
            target = input("Target Currency: ")
            starting = input("Starting at: ")
            ending = input("Ending at: ")

            if ',' in target:
                target = target.replace(" ", "")
                target_list = target.split(',')
                for x in range(len(target_list)):
                    function.print_historical_data(source.upper(), target_list[x].upper(), starting, ending)
            else:
                function.print_historical_data(source.upper(), target.upper(), starting, ending)

        elif (command == '2'):
            print("\r\n-Convert price-")
            source = input("From: ")
            target = input("To: ")
            when = input("At: ")

            function.print_converted_price(source.upper(), target.upper(), when.upper())

        elif (command == '3'):
            print("\r\n-Exit-")
            break

        else:
            print("\r\n-Invalid command-")