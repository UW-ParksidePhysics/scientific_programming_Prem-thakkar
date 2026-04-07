code_snippets = {
    "Dictionary": "numbers = {}\nnumbers[0] = -5\nnumbers[1] = 10.5",
    "List": "other_numbers = []\nother_numbers[0] = -5\nother_numbers[1] = 10.5"
}

explanations = {
    "Dictionary": "Dictionary works because it allows new keys directly.",
    "List": "List does not work because index does not exist."
}

fixed_code = "other_numbers = []\nother_numbers.append(-5)\nother_numbers.append(10.5)"


for key in code_snippets:
    print("-----", key, "-----")
    print(code_snippets[key])
    print("Explanation:", explanations[key])
    
    if key == "List":
        print("Fixed Code:")
        print(fixed_code)
    
    print()


if __name__ == '__main__':
    pass