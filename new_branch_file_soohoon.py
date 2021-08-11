import os

class GitCourse:

    course_name = "Git & GitHub 201"
    instructor_name = "Kalob Taulien"
    dir_name = os.getcwd()
    course_description = "Intermediate Git and Modern Developer Workflow"

course = GitCourse()
check_dir = "/git-essentials"

if check_dir in course.dir_name:
    name = course.instructor_name.split(' ')
    print(f"Hi {name[0]}!")
