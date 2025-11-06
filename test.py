from friend_number import FriendNumber


fnumber = FriendNumber()

# tester
assert fnumber.sum_of_divisors(220) == 284
assert fnumber.sum_of_divisors(284) == 220
assert fnumber.check_friend([220, 284]) is True
assert fnumber.find_friend(220) == 284
assert (220, 284) in fnumber.find_friends(300)
print("All tests passed!")


# output
print(fnumber.sum_of_divisors(220))
print(fnumber.sum_of_divisors(284))
print(fnumber.check_friend([220, 284]))
print(fnumber.find_friends(1000))
print(fnumber.find_friend(220))