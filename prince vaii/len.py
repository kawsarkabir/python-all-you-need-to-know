rochona ="lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis fugiat voluptas cumque ea blanditiis accusamus veniam, consequuntur quae amet."

#একটা ব্যাককে কয়টা লেটার আছে সেটা জানা যাবে।
print(len(rochona))


#লাস্টে কি শব্দ দিয়ে শেষ হইছে সেটা জানা যাবে ।
print(rochona.endswith("."))


# যেকোনো শব্দ একটা ব্যাককে কত বার আছে সেটা জানতে পারা যাবে।
print(rochona.count("k2"))

#প্রথম লেটারকে বর করা
print(rochona.capitalize())

#যেকোনো শব্দ কোন পসিসনে আছে সেটা জানেতে পারা জাইইই

print(rochona.find("lorem"))
