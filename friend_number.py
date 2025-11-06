# root class
class FriendNumber:
    __version = '1.0.0'
    __author  = 'Md. Ariful Islam'
    __github  = 'https://github.com/iamx-ariful-islam'


    # show the all method list
    def __help__(self):
        return self.method_list(self)


    # show the program version
    def __version__(self):
        return self.__version

    
    # show the author name
    def __auth__(self):
        return self.__author

    
    # show the author github info
    def __github__(self):
        return self.__github

    
    # divisors sum of number
    def sum_of_divisors(self, n):
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sum(divisors)

    
    # just check friend number (Exp. pair=[220, 284])
    def check_friend(self, pair):
        a, b = pair[:2] if len(pair) >= 2 else (pair[0], 0)
        return self.sum_of_divisors(a) == b and self.sum_of_divisors(b) == a or False

    
    # list of all friends number from a limit (Exp. limit=1000)
    def find_friends(self, limit):
        friend_numbers = []
        for a in range(2, limit):
            b = self.sum_of_divisors(a)
            if self.sum_of_divisors(b) == a and a != b:
                pair = (min(a, b), max(a, b))
                if pair not in friend_numbers:
                    friend_numbers.append(pair)
        return friend_numbers

    
    # find friend number (Exp. x=220)
    def find_friend(self, x):
        a = self.sum_of_divisors(x)
        return a if x == self.sum_of_divisors(a) else False


    # show all method list for help
    @staticmethod
    def method_list(class_instance):
        all_methods = []
        for method in dir(class_instance):
            if callable(getattr(class_instance, method)) and not method.startswith('__'):
                all_methods.append(method)
        return all_methods


# root
if __name__ == '__main__':
    my_instance = FriendNumber()
    print(my_instance.method_list(my_instance))
    print(my_instance.__help__())
    print(my_instance.__version__())
    print(my_instance.__auth__())
    print(my_instance.__github__())

    print(my_instance.sum_of_divisors(220))
    print(my_instance.sum_of_divisors(284))
    print(my_instance.check_friend([220, 284]))
    print(my_instance.find_friends(1000))
    print(my_instance.find_friend(220))
    
    
    
    '''output:
    
    ['check_friend', 'find_friend', 'find_friends', 'method_list', 'sum_of_divisors']
    ['check_friend', 'find_friend', 'find_friends', 'method_list', 'sum_of_divisors']
    1.0.0
    Md. Ariful Islam
    https://github.com/iamx-ariful-islam
    284
    220
    True
    [(220, 284)]
    284
    '''