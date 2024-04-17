def cost_of_tile():
    width = int(input("How wide is the floor in ft: "))
    length = int(input("How long is the floor in ft: "))
    tile_area = 2
    tile_cost = int(input("How much do tiles cost at your local Rona: "))
    floor = width * length
    total_tiles = floor / tile_area
    answer = total_tiles * tile_cost
    print("It will cost you:", answer, "to lay down tiles")

cost_of_tile()