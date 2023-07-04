#!/usr/bin/env ruby
# store user input
usr_input = ARGV[0]
# store regex pattern
pattern = /hbt{1,4}n/
# use scan to find pattern in user input
matching = usr_input.scan(pattern)
#ouput joined match
puts matching.join
