print("Jay Surya \n1AY24AI048 \nAIML 'M' ")
import re
def mad_libs(python):
    with open(python, 'r') as file:
        text = file.read()
    placeholders = re.findall(r'\b(ADJECTIVE|NOUN|VERB|ADVERB)\b', text)
    user_inputs = []

    for word in placeholders:
        article = 'an' if word[0] in 'AEIOU' else 'a'
        user_input = input(f"Enter {article.lower()} {word.lower()}: ")
        user_inputs.append(user_input)
        
    def replace_match(match):
        return user_inputs.pop(0)
    result_text = re.sub(r'\b(ADJECTIVE|NOUN|VERB|ADVERB)\b', replace_match, text)
    print("\n--- Final Mad Libs Story ---")
    print(result_text)
    output_filename = 'python.txt'
    with open(output_filename, 'w') as output_file:
        output_file.write(result_text)

    print(f"\nThe completed story has been saved to '{output_filename}'.")
mad_libs('python.txt')
