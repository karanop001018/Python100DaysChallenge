# READING A FILE
f = open('myfile.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()

# WRITING A FILE
f = open('myfile2.txt', 'w') # can use rt: for text and rb: for image and other
print(f)
text = f.write("Hello World!?")
print(text)
f.close()

f = open('myfile2.txt', 'a') # can use rt: for text and rb: for image and other
print(f)
text = f.write("Hello World!")
print(text)
f.close()