with open('liberal_array.js', 'w') as outfile:
  with open('liberal_text.txt', 'r') as infile:
    outfile.write('let liberal_array = [\n')
    data = infile.read().splitlines()
    for line in data:
      outfile.write('"{0}"'.format(line))
      outfile.write(',')
    outfile.write('];')