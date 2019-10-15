from collections import deque

def FIFO_cache_miss(demands, frames):
	cache = deque()
	demand_list = demands.strip().split()
	misses = 0

	for demand in demand_list:
		if demand not in  cache:
			misses += 1
			print("Misses: {}, Old cache: {} New Cache: ".format(misses, cache), end="")
			if len(cache) == frames:
				cache.popleft()
			cache.append(demand)
			print(cache)

if __name__ == "__main__":
	demands = "0 1 2 3 0 1 4 0 1 2 3 4"
	FIFO_cache_miss(demands, 3)
	FIFO_cache_miss(demands, 4)
