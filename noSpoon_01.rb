STDOUT.sync = true # DO NOT REMOVE
# Don't let the machines win. You are humanity's last hope...

@width = gets.to_i # the number of cells on the X axis
@height = gets.to_i # the number of cells on the Y axis
map = []
corX=0
corY=0
@height.times do
    line = gets.chomp # width characters, each either 0 or .
    map << line
end
STDERR.puts map.inspect
def getNode(map, corX, corY)
    if map[corY][corX] == '0'
        return "#{corX} #{corY} "
    end
    return "-1 -1 "
end

def rightNeigh(map, corX, corY)
    i=1
    while corX+i < map[corY].length do
        if map[corY][corX+i] == '0'
            return "#{corX+i} #{corY} "
        end
        i+=1
    end
    return "-1 -1 "
end

def botNeigh(map, corX, corY)
    i=1
    while corY+i < map.length do
        if map[corY+i][corX] == '0'
            return "#{corX} #{corY+i}"
        end
        i+=1
    end
    return "-1 -1"
end

def loopMap(map, corX, corY)
    while corY < map.length do
        while corX < map[corY].length do
            if getNode(map, corX, corY) != "-1 -1 "
                puts getNode(map, corX, corY) + rightNeigh(map, corX, corY) + botNeigh(map, corX, corY)
            end
            corX+=1
        end
        corX = 0
        corY+= 1
    end
end

#
loopMap(map, corX, corY)

# Write an action using puts
# To debug: STDERR.puts "Debug messages..."






# Three coordinates: a node, its right neighbor, its bottom neighbor
