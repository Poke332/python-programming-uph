def valid_score_range(score_list):
    for_lang = score_list[0]
    math = score_list[1]
    prof_course_1 = score_list[2]
    prof_course_2 = score_list[2]
    
    if 0 <= for_lang <= 100 and 0 <= math <= 100 and 0 <= prof_course_1 <= 150 and 0 <= prof_course_2 <= 150:
        return True
    else:
        return False

def get_scores_input(n):
    student_grades = list()
    for _ in range(n):
        score_list = list(map(int, input().split()))
        if len(score_list) != 4:
            raise ValueError("Requires 4 inputs split between spaces")
        
        if valid_score_range(score_list):
            student_grades.append(score_list)
        else:
            raise ValueError("Inputted score is not within valid range")
    
    return student_grades

def check_examination_eligibility(student_grades):
    pass_count = 0
    for grades in student_grades:
        total_passes = sum(grades) >= 310
        foreign_and_math_passes = grades[0] >= 55 and grades[1] >= 55
        proffesional_passes = grades[2] >= 90 and grades[3] >= 90
        if total_passes and foreign_and_math_passes and proffesional_passes:
            print("YES")
            pass_count += 1
        else:
            print("NO")
    print(f"Pass: {pass_count}")
    
if __name__ == "__main__":
    num = input()
    try:
        num = int(num)
    except:
        print("Enter valid integer number")
        quit()
    
    check_examination_eligibility(get_scores_input(num))   