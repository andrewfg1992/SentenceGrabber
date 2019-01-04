from quoteGrabber import grabQuotes
import random

quotes = grabQuotes()
num_quotes = len(quotes)
user_input = '' #String that holds user input

print("Type the following prompts correctly:")

while True:
  i = random.randint(0,num_quotes-1)
  quote = quotes[i][1:-1]
  if len(quote) > 200:
    continue
  print(quote)
  user_input = input()
  if(user_input == quote):
    print("Correct! Good job.")
  else:
    print("Incorrect :( Try again on the next prompt")
