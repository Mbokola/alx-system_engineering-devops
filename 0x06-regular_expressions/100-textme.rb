#!/usr/bin/env ruby
# store user input
usr_input = ARGV[0]
# store regex pattern
pattern = /(?<=from:|to:|flags:)(.+?)(?=\])/
# use scan to find pattern in user input
matching = usr_input.scan(pattern)
#ouput joined match
puts matching.join(",")
