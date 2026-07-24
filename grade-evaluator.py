import csv
import sys
import os

def load_csv_data():

    ## Prompts the user for a filename
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):

    # here data will be a list of dictionaries containing the assignment records.
    print("\nProcessing Grades")

    if not data:
        print("No assignment records found. Nothing to evaluate.")
        return
    
    # lets check if all scores are percentage based (0-100)
    invalid_scores = []
    for a in data:
        if a['score'] < 0 or a['score'] > 100:
            invalid_scores.append(a)

    if invalid_scores:
        print("Error: The following assignments have scores outside the valid 0-100 range:")
        for a in invalid_scores:
            print(f"  - {a['assignment']}: {a['score']}")
        return

    # Validate total weights (Total=100, Summative=40, Formative=60)
    total_weight = 0
    summative_weight = 0
    formative_weight = 0
    for a in data:
        total_weight += a['weight']
        if a['group'] == 'Summative':
            summative_weight += a['weight']
        elif a['group'] == 'Formative':
            formative_weight += a['weight']

    total_weight = round(total_weight, 2)
    summative_weight = round(summative_weight, 2)
    formative_weight = round(formative_weight, 2)

    if total_weight != 100 or summative_weight != 40 or formative_weight != 60:
        print("Error: Weight validation faled:")
        if total_weight != 100:
            print(f"Total weight is {total_weight}, but it must equal 100.")
        if summative_weight != 40:
            print(f"Summative weight is {summative_weight}, but it must equal 40.")
        if formative_weight != 60:
            print(f"Formative weight is {formative_weight}, but it must equal 60.")
        return

    # Calculate the final grade and gpa
    total_points = 0
    summative_points = 0
    formative_points = 0
    for a in data:
        total_points += a['score'] * a['weight']
        if a['group'] == 'Summative':
            summative_points += a['score'] * a['weight']
        elif a['group'] == 'Formative':
            formative_points += a['score'] * a['weight']

    total_grade = total_points / total_weight
    gpa = (total_grade / 100) * 5.0
    summative_pct = summative_points / summative_weight
    formative_pct = formative_points / formative_weight

    print(f"Total Grade: {total_grade:.2f}%")
    print(f"GPA: {gpa:.2f}")
    print(f"Summative Score: {summative_pct:.2f}%")
    print(f"Formative Score: {formative_pct:.2f}%")

    # Determine if its pas or fail status (>= 50% in all categories)
    if summative_pct >= 50 and formative_pct >= 50:
        status = "PASSED"
    else:
        status = "FAILED"
    print(f"\nFinal Status: {status}")

    # Check for failed formative assignments basically < 50% and find the highest ones for resubmission.
    failed_formatives = []
    for a in data:
        if a['group'] == 'Formative' and a['score'] < 50:
            failed_formatives.append(a)

    # Print the final decision and resubmission options
    if failed_formatives:
        max_weight = failed_formatives[0]['weight']
        for a in failed_formatives:
            if a['weight'] > max_weight:
                max_weight = a['weight']

        print("Resubmission required for the following highest-weight failed formative assignment(s):")
        for a in failed_formatives:
            if a['weight'] == max_weight:
                print(f"  - {a['assignment']} (Score: {a['score']}, Weight: {a['weight']})")
    else:
        print("No formative assignments require resubmission.")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2. Process the features
    evaluate_grades(course_data)
