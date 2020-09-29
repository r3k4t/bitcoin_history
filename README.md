<h2>Bitcoin_History</h2>

<h4>Author : RKT</h4>

### Descripton ###


![1*7pzdEcTD0mmzUCLFpvO_1g](https://user-images.githubusercontent.com/69615463/94502612-3407c480-0222-11eb-8ccc-0775d24ae630.gif)


### Bitcoin Transactional History ###

To install the Pi Bitcoin tools library,open the command-line program and execute the following command:

<ul>
<li>sudo pip install bitcoin</li>
<li>or</li>
<li>sudo apt install python-bitcoin</li>
</ul>

You can also look preexisting bitcoin addresses transactional history.We will first get a valid address from <a href = "https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html">https://bitinfocharts.com</a>.The following screenshot shows the copied address of bitcoin block :

![Screenshot at 2020-09-29 06-32-44](https://user-images.githubusercontent.com/69615463/94502247-5d742080-0221-11eb-882b-228fa057a605.png)

Pass the copied address to the history function.as shown in the following code,along with the output to get the history of bitcoin address,including the transactional information :

#!/usr/bin/python
...
Title - Bitcoin Transaction HIstory

This program demonstrates listing history of a bitcoin address.
...

#import bitcoin
from bitcoin import *

#view address transaction history

a_vaild_bitcoin_address = '35hK24tcLEWcgNA4JxpvbkNkoAcDGqQPsP'
<br>
print(history(a_vaild_bitcoin_addres))

![Screenshot at 2020-09-29 06-30-10](https://user-images.githubusercontent.com/69615463/94502335-85638400-0221-11eb-8242-17db4c98ee22.png)

![Screenshot at 2020-09-29 06-27-18](https://user-images.githubusercontent.com/69615463/94502381-a035f880-0221-11eb-8a84-d225a41e48df.png)


