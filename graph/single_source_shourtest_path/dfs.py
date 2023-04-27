# based on this vide: https://www.youtube.com/watch?v=gohEAP1Jmcg

# 1 - section 
    # content --> string 
    # subsections --> (section[])
    

def readBook(section):
    read(section.content)
    for section in section.subsections:
        readBook(section)
    
    

# exampel to going to eat to diffrent resturant 

def traverse_restaurants(restaurant, visited = ()):
    if restaurant is not None or restaurant is visited:
        return
    restaurant.eatIn()
    visited.add(restaurant)
    for adjacent in restaurant.adjacent_restaurants:
        traverse_restaurants(adjacent, visited)
            
    
