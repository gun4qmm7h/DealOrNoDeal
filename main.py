"""
Jawad Taj
2021-11-14
Tell you if you should take a deal or not in the game show "Deal or No Deal"
"""


class DealOrNoDeal:
    """
        :param numbers: List of number picked from the game
    """
    def __init__(self, numbers):
        self.briefcases = {1: 100, 2: 500, 3: 1000, 4: 5000, 5: 10000,
                           6: 25000, 7: 50000, 8: 100000, 9: 500000, 10: 1000000}
        self.numbers = numbers

    """
        :take_offer: Removes the picked briefcases
        
        :return: Average of briefcases value
    """
    def take_offer(self):
        # Remove the numbers taken
        for x in self.numbers:
            self.briefcases.pop(x)

        return sum(self.briefcases.values()) / len(self.briefcases)


if __name__ == '__main__':
    numbers = []
    user_number = ""
    offer = ""
    # Keeps use in loop till number is 0
    while user_number != 0:
        user_number = ""
        # Checks if user enter a number
        while not user_number.isdigit():
            user_number = input("Enter The Number That Are Picked From 1-10: ")

        user_number = int(user_number)
        # Check If Number In Is Range
        if 0 < user_number < 11:
            numbers.append(user_number)

    # Checks if user enter a number
    while not offer.isdigit():
        offer = input("Enter The Banks Offer: ")

    offer = int(offer)
    dd = DealOrNoDeal(numbers)
    money = dd.take_offer()
    if money < offer:
        print("You Should Take The Deal, %s Is On The Line" % "{:,.2f}".format(money))
    else:
        print(F"You Should Not Take The Deal.")
