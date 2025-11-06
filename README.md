# Pythagoras Friend Number Finder

### 📚 Overview

**Pythagoras Friend Number Finder** is a Python package to find and check Pythagoras friend numbers — numbers that are amicable pairs, e.g., `(220, 284)`.

- Proper divisors are all the positive divisors of a number, excluding the number itself.
- The proper divisors of `220` are `1,2,4,5,10,11,20,22,44,55` and `110`, which add up to `284`.
- The proper divisors of `284` are `1,2,4,71` and `142`, which add up to `220`. 

---


### 🚀 Features
- Check if a given pair are friend numbers.
- Find all friend numbers up to a given limit.
- Find the friend number of a given number.
- View library metadata: version, author, GitHub link.

---


### 💻 Installation
```bash
git clone https://github.com/iamx-ariful-islam/friend-number.git
cd friend-number
pip install .
# or
python setup.py install
```


## 📂 Folder / File Structure

```bash
friend_number/
│
├── friend_number.py
├── README.md
├── setup.py
└── test.py
```


## 🚀 Usage

```python
from pythagoras_friend_number import FriendNumber

fnumber = FriendNumber()

print(fnumber.sum_of_divisors(220))  # 284
print(fnumber.check_friend([220, 284]))  # True
print(fnumber.find_friends(1000))  # [(220, 284)]
print(fnumber.find_friend(220))  # 284
```


## 💡 Notes & Limitations

- Pure Python implementation — no external dependencies.
- Compatible with Python 3.6+.


## Contributing

Contributions, suggestions, and feedback are always welcome! ❤️
To contribute:

1. Fork the repository
1. Create a new branch (`feature/new-feature`)
1. Commit your changes
1. Push and submit a Pull Request

💬 You can also open an issue if you’d like to discuss a feature or report a bug.


## For more or connect with me

<p align='center'>
  <a href="https://github.com/iamx-ariful-islam"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://x.com/mx_ariful_islam"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://bd.linkedin.com/in/iamx-ariful-islam"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.facebook.com/jonakisoft.net/"><img src="https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
</p>


## License

The [MIT](https://choosealicense.com/licenses/mit/) License (MIT)