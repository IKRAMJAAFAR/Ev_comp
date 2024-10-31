target = "14h!S@A$Qse35DAzx"

import string

character = string.ascii_letters + string.punctuation  # Possible character set

k = len(target)
total_gen = len(character)**k
print("\nAssume the target password has the length of \"k\"")
print("whereas 12 <= k < +inf")

print("Total characters:\t", len(character))
print(f"Total generations: \t{len(character)}^{k}")
print(f"or \t\t\t{total_gen}\n")