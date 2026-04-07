code_snippets = {
    "dict": "numbers = {}\nnumbers[0] = -5\nnumbers[1] = 10.5",
    "list": "other_numbers = []\nother_numbers[0] = -5\nother_numbers[1] = 10.5"
}

fixed_code = "other_numbers = []\nother_numbers.append(-5)\nother_numbers.append(10.5)"

for key in code_snippets:
    print(code_snippets[key])
    if key == "list":
        print(fixed_code)
    print()

if __name__ == "__main__":
    pass