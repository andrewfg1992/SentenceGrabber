def grabQuotes():
  with open('book.txt', 'r') as myfile:
    book=myfile.read().replace('\n', ' ')

  size = len(book)
  quote_loc = [] #list that will contain locations of quotes
  quotes = [] #list of the quotes
  #print(size)

  result = book.find('“')
  if result == -1:
    print('Text does not use standard quote characters.')
    quit() #exit program early

  #try to grab quotes as sentences, since this is easy
  start = 0 #start of search location
  keep = True #whether to keep or throw out the quote

  while start != -1:

    keep = True

    #find beginning/end of quote
    start = book.find('“', start, size-1)
    if start == -1:
      continue
    end = book.find('”', start, size-1)
    if end == -1:
      print("Error: end of quote not detected!")
      #TODO probably should do something here
    quote = book[start:end+1]

    #ignore improperly parsed quotes with extra quote marks in them
    if quote[1:].find('“') != -1:
      keep = False
    punc = quote[len(quote)-2:len(quote)-1]

    #make sure quotes end with '.' '!' or '?', ignore otherwise
    if punc!='.' and punc!='!' and punc!='?':
      keep = False

    #if quote is deemed good, store it
    if keep == True:
      quote_loc.append((start, end))
      quotes.append(quote)
    start = end + 1

  #end while

  return quotes

#end def

#print('Testing quotes:')
#for q in quotes:
#  print(q)

#TODO solve nested quotes, typos: mispaired quotes
#TODO implement finding non-quoted sentences in another file

