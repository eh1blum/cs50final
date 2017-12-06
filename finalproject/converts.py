with open('conservative_array.js', 'w') as outfile:
  with open('convservative_text.txt', 'r') as infile:
    outfile.write('let bias_words = [\n')
    for line in infile:
      outfile.write(','.join('"{0}"'.format(line)))
      outfile.write('];')
