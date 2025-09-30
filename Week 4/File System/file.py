with open('workfile','w',encoding="utf-8") as f:
    f.write("hello world")

print(f.closed) 


with open('workfile','r',encoding="utf-8") as f:
    content = f.read()
    print(content)

with open('workfile', 'a', encoding="utf-8") as f:
    f.write("\nAppending a new line.")

with open('image.jpg', 'rb') as f:
    data = f.read()

