if __name__ == '__main__':

    # parsing inputs
    num_books = int(input())
    # sort prices in reverse order
    prices = sorted([int(input()) for _ in range(num_books)], reverse=True)
    # add up everything but skip every 3rd item
    # for example, 6 4 5 5 5 5 becomes
    #              6 5 5 5 5 4
    #                  ^     ^ are skipped
    # if there are 1-2 books not in a group of 3, this ensures they're counted at full price
    print(sum(prices[i] for i in range(len(prices)) if i%3!=2))
