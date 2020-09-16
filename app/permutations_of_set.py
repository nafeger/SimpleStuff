
# again this is stealing from Daily coding problem
import copy

def go(data, prefix = []):
	if len(data) == 1:
		prefix_cp = copy.deepcopy(prefix)
		prefix_cp.extend(data)
		print(f"all: {prefix_cp}")
		return data
		
	for i in range(0,len(data)):
		cp = copy.deepcopy(data)
		val = data[i]
		cp.remove(val)

		prefix_cp = copy.deepcopy(prefix)
		prefix_cp.extend([val])
		go(cp, prefix_cp)

			
size = 3
capture = []
go(['a','b','c'] )
go(['a','b','c','d'] )
