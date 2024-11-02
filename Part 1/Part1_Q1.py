target = "G7$pQz!9sW@tL4"
import string

character = string.ascii_letters + string.punctuation + string.digits  # Possible character set

k = len(target)
total_gen = len(character)**k

print("Total characters:\t", len(character))
print(f"Total generations: \t{len(character)}^{k}")
print(f"or \t\t\t{total_gen}\n")