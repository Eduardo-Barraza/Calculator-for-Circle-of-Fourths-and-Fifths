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
