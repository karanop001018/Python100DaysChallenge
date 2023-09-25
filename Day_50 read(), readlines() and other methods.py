# f = open('file1.txt', 'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break
#     print(line)


# f = open('kp.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# ---------------------------------------------------------

# f = open('kp1.txt', 'r')
#
# while True:
#     i=0
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of student{i} in Maths is:{m1}")
#     print(f"Marks of student{i} in English is:{m2}")
#     print(f"Marks of student{i} in SST is:{m3}")
#     print(line)
#
# f = open('kp1.txt', 'r')
# while True:
#     i=0
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student{i} in Maths is:{m1 * 2}")
#     print(f"Marks of student{i} in English is:{m2 * 2}")
#     print(f"Marks of student{i} in SST is:{m3 * 2}")
#     print(line)
# --------------------------------------------------
# f = open('kp2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n', ]
# f.writelines(lines)
# f.close()