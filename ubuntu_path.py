path = input("Enter path: ")

new_path = path.replace('\\', '/').replace('D:', 'cd /mnt/d').replace('C:', 'cd /mnt/c')

print(new_path)


