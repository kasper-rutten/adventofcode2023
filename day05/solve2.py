class Map:
    def __init__(self, map_str: str) -> None:
        self.header, body = map_str.split(':')
        self.mappings = []
        for map in body.strip().split('\n'):
            strings = map.split(' ')
            mapping = [int(x) for x in strings]
            self.mappings.append(mapping)
            #print(f"parsed out new map {map} in {self.header}")

    def do_map(self, input: int):
        for mapping in self.mappings:
            destination_range_start = mapping[0]
            source_range_start = mapping[1]
            range_length = mapping[2]
            if source_range_start <= input < source_range_start + range_length:
                offset = input - source_range_start
                #print(f"Map hit, for {input=}, in map {self.header}, number is in range {[source_range_start,source_range_start+range_length]} at offset {offset}. Outputting {destination_range_start + offset}")
                return destination_range_start + offset
        #print(f"Map miss.")
        return input
                
with open('input') as f:
    lines = f.read()
maps = []
for map_str in lines.split('\n\n')[1:]:
    maps.append(Map(map_str))

seed_numbers = []
for seed in lines.split('\n\n')[0].split(':')[1].strip().split(' '):
    seed_number = int(seed)
    seed_numbers.append(seed_number)

seed_ranges = []
sum_of_ranges = 0
for i in range(0, len(seed_numbers), 2):
    seed_range_start = seed_numbers[i]
    seed_range_length = seed_numbers[i + 1]
    seed_range = range(seed_range_start, seed_range_start + seed_range_length)
    seed_ranges.append(seed_range)
    sum_of_ranges += len(seed_range)
    print(f"found a seed range of len {len(seed_range)}")

print(f"{sum_of_ranges=}")

# due to size of problem (1.8B), we implement gradient descent, rather than naive for loop

# first compute answers array for a couple thousand sample values, somewhat evenly spaced over all input ranges
# then start binary searching for local minima? 



#mapped_seeds = []
#count_mapped_seeds = 0
#for i in range(0, len(seed_numbers), 2):
#    seed_range_start = seed_numbers[i]
#    seed_range_length = seed_numbers[i + 1]
#    for seed in range(seed_range_start, seed_range_start + seed_range_length):
#        mapped_seed = seed
#        for map in maps:
#            mapped_seed = map.do_map(mapped_seed)
#        mapped_seeds.append(mapped_seed)
#        count_mapped_seeds += 1
#        print(count_mapped_seeds)
        

#print(f"{len(mapped_seeds)=}")
#print(f"{[len(x.mappings) for x in maps]=}")
#print(min(mapped_seeds))