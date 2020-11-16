def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        if i == 2:
            verses.append("2 bottles of beer on the wall, 2 bottles of beer.")
            verses.append("Take one down and pass it around, 1 bottle of beer on the wall.")
        elif i == 1:
            verses.append("1 bottle of beer on the wall, 1 bottle of beer.")
            verses.append("Take it down and pass it around, no more bottles of beer on the wall.")
        elif i == 0:
            verses.append("No more bottles of beer on the wall, no more bottles of beer.")
            verses.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        else:
            verses.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            verses.append(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
        if i != start - take + 1:
            verses.append("")
    return verses


# Prints the lines of recite start=5 take=6
lines = recite(5, 6)
for line in range(17):
    print(lines[line])
