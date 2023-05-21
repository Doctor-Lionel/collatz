from PIL import Image

print('''
send this app and the image you want to one folder for it to work. When typing the name of the image, do not forget to add the image extension.
''')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
input = input()
camera = Image.open(input)
camera_x, camera_y = camera.size

my_tuple = ()
name = input()
for x in range(camera_x):
    for y in range(camera_y):
        my_tuple = list(camera.getpixel((x, y)))
        my_tuple[0] = 255 - my_tuple[0]
        my_tuple[1] = 255 - my_tuple[1]
        my_tuple[2] = 255 - my_tuple[2]
        camera.putpixel((x, y), tuple(my_tuple))


camera.save(name + '.jpg')
print('Done')