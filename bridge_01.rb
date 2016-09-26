STDOUT.sync = true # DO NOT REMOVE
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

@road = gets.to_i # the length of the road before the gap.
@gap = gets.to_i # the length of the gap.
@platform = gets.to_i # the length of the landing platform.
land = @road+@gap
# game loop
loop do
    speed = gets.to_i # the motorbike's speed.
    coord_x = gets.to_i # the position on the road of the motorbike.
    
    # Write an action using puts
    # To debug: STDERR.puts "Debug messages..."
    ans = "WAIT"
    rLeft = @road-coord_x
    
    # UGLY DEBUGGING INCOMING
    STDERR.puts "gap in #{rLeft}"
    STDERR.puts "gap is #{@gap}"
    STDERR.puts "and platform is #{@platform}"
    STDERR.puts "we at #{coord_x}"
    STDERR.puts "going at #{speed}"
    
    # UGLY CONDITIONALS INCOMING
    if (rLeft < speed && speed > @gap && rLeft >= 0)
        ans = "JUMP"
    elsif (speed > @gap+1 || coord_x >= land)
        ans = "SLOW"
    elsif (speed <= @gap)
        ans = "SPEED"
    end
    
    rLeft= rLeft-speed
    coord_x+= speed
    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    puts ans
end
