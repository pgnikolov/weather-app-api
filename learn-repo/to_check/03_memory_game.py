# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin.
# Until the player receives "end" from the console, you will receive strings with two integers separated by a space,
# representing the indexes of elements in the sequence.

elements = input().split(" ")
moves = 0

while True:
    command = input()
    if command == "end":
        break

    moves += 1
    indexes = command.split(" ")

    if (0 > int(indexes[0]) or int(indexes[0]) >= len(elements)) or (
            0 > int(indexes[1]) or int(indexes[1]) >= len(elements)):
        new_element = f"-{moves}a"
        index_new_el = int(len(elements) / 2)
        elements = elements[:index_new_el] + [new_element] * 2 + elements[index_new_el:]
        print("Invalid input! Adding additional elements to the board")

    elif elements[int(indexes[0])] == elements[int(indexes[1])]:
        print(f"Congrats! You have found matching elements - {elements[int(indexes[0])]}!")
        elements.pop(max(int(indexes[0]), (int(indexes[1]))))
        elements.pop(min(int(indexes[0]), (int(indexes[1]))))

    elif elements[int(indexes[0])] != elements[int(indexes[1])]:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break

if command == "end":
    final = " ".join(elements)
    print(f"Sorry you lose :(\n{final}")
