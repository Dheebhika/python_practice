def count_rabbit_chicken():
    no_of_heads = int(input())
    no_of_legs = int(input())
    legs = no_of_heads * 2
    rabbit = (no_of_legs - legs) / 2
    chicken = no_of_heads - rabbit
    print("rabbit=", int(rabbit))
    print("chicken=", int(chicken))


count_rabbit_chicken()
