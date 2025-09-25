def calculate_and_display_final_grade():
    """Runs the main function to calculate and display the final grade
    """
    user = get_scores_from_user()
    average = calculate_average_scores(user["scores"])
    grade = convert_average_to_letter_grade(average)
    print_final_report(user["name"], average, grade)

def get_scores_from_user():
    """Gets user input for name and scores

    Returns:
        Object: an object with name and scores 
    """
    name = input("Enter Name: ").strip()
    score = input("Enter Grade (seperated by space): ").split()
    return {
        "name" : name,
        "scores" : score
    }
    
def convert_average_to_letter_grade(average):
    """COnverts the average grade into letter grade from A-D

    Args:
        average (float): the average score calculated 

    Returns:
        string: the letter grade from A to D
    """
    if 90 <= average <= 100:
        return "A"
    elif 80 <= average <= 89:
        return "B"
    elif 60 <= average <= 79:
        return "C"
    else:
        return "D"

def calculate_average_scores(scores: list):
    """Calculates the average of the sum of scores

    Args:
        scores (list): list of scores

    Returns:
        float: the average score 
    """
    total = sum(float(score) for score in scores)
    return total / len(scores)

def print_final_report(name, average, grade):
    print(f"Student Name: {name}\nScore Average: {average:.2f}, Grade: {grade}")
    
if __name__ == "__main__":
    calculate_and_display_final_grade()