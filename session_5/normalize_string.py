a = input("Enter a string: ")

# take an input string
# "normalize" - lowercased, no leading or trailing white spaces, "?" -> ".", "!" -> "."
stage1 = a.lower()
stage2 = stage1.strip()
stage3 = stage2.replace("?", ".")
stage4 = stage3.replace("!", ".")
print(stage4)

# Alternate concise way of doing the same task
print(a.lower().strip().replace("?", ".").replace("!", "."))
