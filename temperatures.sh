#!/bin/bash

@n = gets.to_i # the number of temperatures to analyse
@temps = gets.chomp # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using puts
# To debug: STDERR.puts "Debug messages..."
# STDERR.puts @temps
if @temps == ""
    puts 0
end

aTemps = @temps.split(' ').map{|i| i.to_i}
absTemps = aTemps.map {|j| j.abs}
if aTemps.include? (absTemps.min)
    puts aTemps[aTemps.index(absTemps.min)]
elsif aTemps.include? (absTemps.min*(-1))
    puts aTemps[aTemps.index(absTemps.min*(-1))]
end
