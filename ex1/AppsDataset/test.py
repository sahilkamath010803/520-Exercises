import json

file_path = 'C:\\Users\\Hp\\Desktop\\College\\MS\\520\\ex\\HumanEval.jsonl\\apps.json' 

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    inputs =json.loads(data[2]['input_output'])['inputs']
    outputs =json.loads(data[2]['input_output'])['outputs']
    print(data[2]['question'])
    cleaned_inputs = [s.strip() for s in inputs]
    cleaned_outputs = [s.strip() for s in outputs]
    test_cases = []
    
    for inp, outp in zip(cleaned_inputs, cleaned_outputs):
        test_cases.append({"input": inp, "output": outp})

    file_name = 'test_cases.json'

    with open(file_name, 'w') as f:
        json.dump(test_cases, f, indent=2)

    print(f"✅ Successfully saved {len(test_cases)} test cases to {file_name}")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    print(f"Error: Could not decode the JSON from '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")