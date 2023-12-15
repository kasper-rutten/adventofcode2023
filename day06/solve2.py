class BoatRace:
    def __init__(self, time: int, best_distance: int) -> None:
        self.time = time
        self.best_distance = best_distance
        self.check_all()

    def check_strategy(self, accelerate_time: int, total_time: int) -> int:
        return accelerate_time * (total_time - accelerate_time)

    def check_all(self) -> None:
        self.distances = {}
        for i in range(self.time):
            print(i)
            self.distances[i] = self.check_strategy(i, self.time)
    
    def count_viable_strategies(self) -> int:
        count = 0
        for time, distance in self.distances.items():
            if distance > self.best_distance:
                count += 1
        return count



races = []
races.append(BoatRace(59707878, 430121812131276))
result = 1
for race in races:
    result *= race.count_viable_strategies()
print(result)

# for map_str in lines.split('\n\n')[1:]:
#     maps.append(Map(map_str))

# mapped_seeds = []
# for seed in lines.split('\n\n')[0].split(':')[1].strip().split(' '):
#     mapped_seed = int(seed)
#     for map in maps:
#         mapped_seed = map.do_map(mapped_seed)
#     mapped_seeds.append(mapped_seed)

# print(f"{len(mapped_seeds)=}")
# print(f"{[len(x.mappings) for x in maps]=}")
# print(min(mapped_seeds))