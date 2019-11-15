import time
import palingrams2
import palingrams

start_time1 = time.time()
palingrams2.find_palingrams()
end_time1 = time.time()

start_time2 = time.time()
palingrams.find_palingrams()
end_time2 = time.time()

print('With sets', end_time1-start_time1)
print('With sets', end_time2-start_time2)

