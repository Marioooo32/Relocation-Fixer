import binascii

def find_relocations(first_dump_path, second_dump_path):
    # Read the content of the first dump
    with open(first_dump_path, 'rb') as f1:
        first_dump = f1.read()

    # Read the content of the second dump
    with open(second_dump_path, 'rb') as f2:
        second_dump = f2.read()

    # Compare the dumps byte by byte
    differences = [i for i, (b1, b2) in enumerate(zip(first_dump, second_dump)) if b1 != b2]

    # Extract potential relocation addresses
    relocation_addresses = [hex(address) for address in differences]

    return relocation_addresses

def save_relocations_to_file(relocations):
    # Save the potential relocation addresses to 'relocation.txt'
    with open('relocation.txt', 'w') as file:
        file.write(", ".join(relocations))

def main():
    # Prompt the user to input paths to the two dump files
    first_dump_path = input("Enter the path to the first dump file: ")
    second_dump_path = input("Enter the path to the second dump file: ")

    relocations = find_relocations(first_dump_path, second_dump_path)

    # Print the potential relocation addresses with a space between them
    print("\nPotential relocation addresses:")
    print(", ".join(relocations))

    # Save the potential relocation addresses to 'relocation.txt'
    save_relocations_to_file(relocations)
    print("Relocation addresses saved to 'relocation.txt'.")

if __name__ == "__main__":
    main()