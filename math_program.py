#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is math_program


def main():

    loop_counter = 1
    answer = 1
    # input
    integer = input("Enter any positive number: ")
    print("")

    # process & output
    try:
        number = int(integer)
        if number < 0:
            print("Please follow the instructions! Enter any POSITIVE number")
        else:
            while loop_counter <= number:
                answer = answer * loop_counter
                loop_counter = loop_counter + 1
            print("{0}! = {1}".format(number, answer))

    except Exception:
        print("Please follow the instructions! Use numbers")
    finally:
        print("")
        print("Done")


if __name__ == "__main__":
    main()
