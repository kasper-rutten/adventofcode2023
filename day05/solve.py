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
                print(f"Map hit, for {input=}, in map {self.header}, number is in range {[source_range_start,source_range_start+range_length]} at offset {offset}. Outputting {destination_range_start + offset}")
                return destination_range_start + offset
        print(f"Map miss.")
        return input
                
with open('input') as f:
    lines = f.read()
maps = []
for map_str in lines.split('\n\n')[1:]:
    maps.append(Map(map_str))

mapped_seeds = []
for seed in lines.split('\n\n')[0].split(':')[1].strip().split(' '):
    mapped_seed = int(seed)
    for map in maps:
        mapped_seed = map.do_map(mapped_seed)
    mapped_seeds.append(mapped_seed)

print(f"{len(mapped_seeds)=}")
print(f"{[len(x.mappings) for x in maps]=}")
print(min(mapped_seeds))