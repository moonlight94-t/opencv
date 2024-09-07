import shutil

diskLabel = 'c:/'
total, used, free = shutil.disk_usage(diskLabel)

print(total)
print(used)
print(free)