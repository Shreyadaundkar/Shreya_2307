
jobs = [('J1',2,100), ('J2',1,19), ('J3',2,27),
        ('J4',1,25),  ('J5',3,15)]


jobs.sort(key=lambda x: -x[2])


max_d = max(j[1] for j in jobs)
slots = [None] * (max_d + 1)    

result = []


for job, deadline, profit in jobs:
    for t in range(deadline, 0, -1):  
        if slots[t] is None:           
            slots[t] = job
            result.append((t, job, profit))
            break


result.sort()
print("Scheduled Jobs:")
for slot, job, profit in result:
    print(f"  Slot {slot}: {job}  profit={profit}")
print("Total Profit:", sum(p for _,_,p in result))
