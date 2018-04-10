from datetime import date

class Product:
    '''
    module to get the price per articles
    '''

    def __init__(self, article, discount):
        self._article = article
        self._price = price

    def article_price(self, item):
        pricing_article = {'washing_powder': 8.00, 'chocolate': 2.00, "chines_vegetables": 3.00, 'yoghurt': 1.50, 'butter': 4.00}
        price = pricing_article.get[item]
        return price

class Discount:
    '''
    Calcutate the Discount per articles
    '''
    def __init__(self, article, amount, discount):
        self._article = article
        self._price = price
        self._amount = amount
        self._discount = discount

    def calc_discount(self, item, amount):
        '''
        Claculate the discount depending on article and amaount
        '''
        if  itme == 'washing_powder' and amount == 2:
            self._discount = Product.article_price(item) * amount * 0.3           #two articles give 30% discount
        elif item == 'yughurt' and date.today().weekday() == 2:         #2 is Wednesday
            self._discount = 0.50 *self._amount                                   #amount of articles * 0,50 euro
        elif item == 'butter' and amount == 4:                   # if 4 articles -> one is free
            self._discount = Product.article_price(item)
        else:
            self._discount = 0.00
        return self._discount

class Register:
    '''
    Use shoppinglist customer to calculate total _price
    '''
    def __init__(self, shoppinglist, article, amount, discount):
        self._shoppinglist = shoppinglist
        self._article = article
        self._price = price
        self._amount = amount
        self._discount = discount

    def total_price(self, shoppinglist):
        '''
        Get item of shippinglist and calculate price and discount per item and return total _price
        '''
        total = 0
        for item in shoppinglist:                                                #get item form shoppinglist customer
            self._amount = shoppinglist.value[item]
            total = total + Product.article_price(item) * self._amount           #calculate total price articles
            self._discount = Discount.calc_discount(item, self._amount)          #get the discount per article
            total = total - self._discount
        print('total price of shoppinglist = ' + str(total))                    #print total pricing_article


class Customer:
    '''
    Customer starts shoppinglist
    '''
    def __init__(self, shoppinglist):
        self._shoppinglist = shoppinglist

    def customer_list(self, shoppinglist):
        print("hello")
        Register.total_price(shoppinglist)


if __name__ == '__main__':
    #shoppinglist customer
    shoppinglist = {'washing_powder': 2, 'chocolate': 1, "chines_vegetables": 2, 'yoghurt': 1, 'butter': 4}
    customer = Customer(shoppinglist)
