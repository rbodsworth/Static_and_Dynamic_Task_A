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

# missing colon after else, equals operator should be == 
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   

  # typo in def, no comma between cards, card 1 missing 1, 
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

#total not defined, should be 0, 
def cards_total(self, cards):
  total # should be = 0 
  for card in cards:
    total += card.value
    return "You have a total of" + total # should be an f string and indented 
  
```
