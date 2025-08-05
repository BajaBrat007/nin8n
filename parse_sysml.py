import json
import re

def parse_sysml(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    model = {
        "components": [],
        "connections": [],
        "parameters": {}
    }

    # Regex to find blocks (components) and their properties
    block_pattern = re.compile(r'block (\w+)\s*{([^}]*)}', re.DOTALL)
    property_pattern = re.compile(r'property\s+\'param:([a-zA-Z0-9_]+)\':\s+(\w+)\s*=\s*(.+?);')
    state_pattern = re.compile(r'property\s+\'state:([a-zA-Z0-9_]+)\':\s+(\w+)\s*=\s*(.+?);')

    # Find all blocks and their properties
    for match in block_pattern.finditer(content):
        block_name = match.group(1)
        block_content = match.group(2)
        model["components"].append(block_name)

        for prop_match in property_pattern.finditer(block_content):
            param_name = prop_match.group(1)
            data_type = prop_match.group(2)
            value = prop_match.group(3).strip()
            model["parameters"][f"{block_name}.{param_name}"] = {"type": data_type, "value": value}

        for state_match in state_pattern.finditer(block_content):
            state_name = state_match.group(1)
            data_type = state_match.group(2)
            value = state_match.group(3).strip()
            model["parameters"][f"{block_name}.{state_name}"] = {"type": data_type, "value": value}


    # Regex to find connections
    connection_pattern = re.compile(r'connect\s+(\w+)\s+to\s+(\w+);')
    for match in connection_pattern.finditer(content):
        source = match.group(1)
        target = match.group(2)
        model["connections"].append({"source": source, "target": target})

    return model

if __name__ == "__main__":
    parsed_model = parse_sysml("coffee_machine.sysml")
    print(json.dumps(parsed_model, indent=2))