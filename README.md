# Pony-Challenge

<p align="center"><img src="/data/pony_saved.gif" height="300"/></p>

**Pythonic approach to solve the [Pony-Challenge](https://ponychallenge.trustpilot.com/index.html) from Trustpilot. 
Recursively solves the maze and leads pony to the exit.**

***TODO:** add feature for avoiding Domokun. Since in lower difficulty levels Domokun walks pretty randomly,
 it should be sometimes possible to avoid him even if he blocks the way to exit.*

### Setup:
```
git clone https://github.com/km1414/Pony-Challenge.git
cd Pony-Challenge
pip3 install -r requirements.txt
```

### Run:
```
# default settings
python3 main.py

# changed settings
python3 main.py --width 20 --height 18 --difficulty 8 --name Fluttershy
```
