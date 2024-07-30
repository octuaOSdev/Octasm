# Define the Octasm instruction table
octasm_instruction_table = {
    "add": "0001",
    "sub": "0010",
    "mult": "0011",
    "div": "0100",
    "and": "0101",
    "or": "0110",
    "nor": "0111",
    "nand": "1000",
    "push to bus": "1001"
}

def compile_octasm_to_binary(octasm_filename, output_filename):
    try:
        with open(octasm_filename, "r") as octasm_file:
            octasm_instructions = octasm_file.read().splitlines()

        binary_code = ""
        for instruction in octasm_instructions:
            binary_instruction = octasm_instruction_table.get(instruction, "")
            if binary_instruction:
                binary_code += binary_instruction + "\n"
            else:
                print(f"Unknown instruction: {instruction}")

        with open(output_filename, "w") as output_file:
            output_file.write(binary_code)

        print(f"Binary code written to {output_filename}")
    except FileNotFoundError:
        print(f"File '{octasm_filename}' not found.")
input = input("input file: ")
# Usage example
compile_octasm_to_binary(input, "Compiled_app.txt")
