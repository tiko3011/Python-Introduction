# File names to compare
file1 = 'txt/file1.txt'
file2 = 'txt/file2.txt'

try:
    # Open both files
    with open(file1) as f1, open(file2) as f2:
        line_num = 1
        while True:
            # Read one line from each file
            line1 = f1.readline()
            line2 = f2.readline()

            # Stop if both files end
            if line1 == '' and line2 == '':
                break

            # Compare lines (strip newline characters for accurate comparison)
            if line1 != line2:
                print(f"Difference at line {line_num}:")
                print(f"{file1}: {line1.strip() if line1 else '<END OF FILE>'}")
                print(f"{file2}: {line2.strip() if line2 else '<END OF FILE>'}")
                print()  # Empty line for spacing

            line_num += 1

except FileNotFoundError as e:
    print(f"Error: File '{e.filename}' not found. Please check the file exists.")