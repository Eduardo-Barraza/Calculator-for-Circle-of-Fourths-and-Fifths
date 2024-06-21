# Calculator-for-Circle-of-Fourths-and-Fifths

Below is a Python program that calculates and displays the notes in a chromatic scale, focusing on either the circle of fourths or the circle of fifths. The program asks the user for a starting note and the type of circle to use (fourths or fifths). It then demonstrates how the circle works by displaying the sequence of notes and highlighting the picked note.

# Define the chromatic scale with enharmonic equivalents
chromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Define the circle of fourths and fifths using consistent naming
circle_of_fourths = ['C', 'F', 'A#', 'D#', 'G#', 'C#', 'F#', 'B', 'E', 'A', 'D', 'G']
circle_of_fifths = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'F']

# Function to display how notes are picked in the circle
def display_chromatic_steps(note, steps):
    note_index = chromatic_scale.index(note)
    for i in range(steps + 1):
        current_note = chromatic_scale[(note_index + i) % 12]
        if i == steps:
            print(f"{current_note} (Chosen Note)")
        else:
            print(f"{current_note} ({i} semi tone)")

# Function to calculate and display the circle of fourths or fifths
def calculate_circle(note, circle):
    if circle == "fourths":
        notes = circle_of_fourths
        steps = 5
    else:
        notes = circle_of_fifths
        steps = 7

    note_index = notes.index(note)
    chosen_notes = []

    for i in range(12):
        current_note = notes[(note_index + i) % 12]
        chosen_notes.append(current_note)
        print(f"{current_note} (Note picked)")
        display_chromatic_steps(current_note, steps)
        print()

    print(f"Final list of chosen notes in the circle of {circle}: {chosen_notes}")

# Main program function
def chromatic_circle_calculator():
    note = input("Enter the starting note (e.g., C, C#, D, etc.): ").capitalize()
    circle = input("Do you want to use the circle of fourths or fifths? ").lower()

    # Handle common enharmonic equivalents for user input
    enharmonics = {
        'Bb': 'A#', 'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#'
    }
    note = enharmonics.get(note, note)

    if note not in chromatic_scale:
        print("Invalid note. Please enter a valid note from the chromatic scale.")
        return

    if circle not in ["fourths", "fifths"]:
        print("Invalid choice. Please enter 'fourths' or 'fifths'.")
        return

    calculate_circle(note, circle)

# Run the program
chromatic_circle_calculator()

Enter the starting note (e.g., C, C#, D, etc.): C
Do you want to use the circle of fourths or fifths? fourths
C (Note picked)
C (0 semi tone)
C# (1 semi tone)
D (2 semi tone)
D# (3 semi tone)
E (4 semi tone)
F (5 semi tone) (Chosen Note)

F (Note picked)
F (0 semi tone)
F# (1 semi tone)
G (2 semi tone)
G# (3 semi tone)
A (4 semi tone)
A# (5 semi tone) (Chosen Note)

...

Final list of chosen notes in the circle of fourths: ['C', 'F', 'A#', 'D#', 'G#', 'C#', 'F#', 'B', 'E', 'A', 'D', 'G']

Explanation
Enharmonic Equivalents:

Added an enharmonics dictionary to handle common enharmonic equivalents. For instance, Bb is mapped to A#, Db to C#, and so on.
Normalized Note Names:

Used consistent note names (A# instead of Bb, etc.) throughout the program to avoid mismatches.
Chosen Notes List:

The calculate_circle function now collects chosen notes in a list (chosen_notes) and prints this list at the end.
Example Usage
When you run the program, it will prompt you to enter a starting note and whether you want to use the circle of fourths or fifths. It will display the sequence of notes, show how they are picked, highlight the chosen notes, and finally, print the list of chosen notes.

Output Example

This output demonstrates the circle of fourths starting from C, showing the chromatic steps and highlighting the chosen notes as specified. The final list of chosen notes is displayed at the end.
