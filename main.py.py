# Smart Data Organizer Project

def read_dictionary(filename):
    data = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                if ": " not in line:
                    print(f"Skipping invalid line: {line}")
                    continue

                key, value = line.split(": ")
                values = value.split(", ")

                data[key] = values

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Unexpected error:", e)

    return data


def invert_dictionary(data):
    inverted = {}

    for key, values in data.items():
        for value in values:
            if value not in inverted:
                inverted[value] = []
            inverted[value].append(key)

    return inverted


def write_dictionary(filename, data):
    try:
        with open(filename, "w") as file:
            file.write("--- Inverted Dictionary ---\n")

            for key in data:
                values = ", ".join(data[key])
                file.write(f"{key}: {values}\n")

    except Exception as e:
        print("Error writing file:", e)


def log_activity(message):
    with open("log.txt", "a") as log:
        log.write(message + "\n")


# Main Program
input_file = "C:/Users/Admin/Documents/Tasks/dictionary.txt"
output_file = "C:/Users/Admin/Documents/Tasks/inverted.txt"

original = read_dictionary(input_file)
print("\nOriginal Data:", original)

inverted = invert_dictionary(original)
print("\nInverted Data:", inverted)

write_dictionary(output_file, inverted)
log_activity("File processed successfully.")

print("\nProcess completed successfully.")