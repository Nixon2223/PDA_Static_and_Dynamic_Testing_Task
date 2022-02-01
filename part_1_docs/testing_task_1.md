### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
#missing def __init__(self)

  def check_for_ace(self, card):
    # single = used instead of ==
    if card.value = 1:
      return True
    # missing colon after else
    else
      return False
   
# dif typo (def), missing comma after card1
  dif highest_card(self, card1 card2):
  #indentation required 
  if card1.value > card2.value:
    #'card' instead of card1 
    return card
  else:
    return card2
  

#missing indentation
def cards_total(self, cards):
  #total not defined (total = 0)
  total
  for card in cards:
    total += card.value
    #return inside of for loop (loop will only run once)
    #can only concatenate str (not "int") to str
    return "You have a total of" + total
  
```
