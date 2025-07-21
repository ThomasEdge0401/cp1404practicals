import datetime
from project import Project


def main():
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"welcome to pythonic project management\nloaded {len(projects)} projects from {filename}")
    choice = ""
    while choice != "q":
        print("(l)oad projects\n(s)ave projects\n(d)isplay projects\n(f)ilter projects by date\n"
              "(a)dd new project\n(u)pdate project\n(q)uit")
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save = input(f"would you like to save to {filename}? ").lower()
            if save in ['y', 'yes']:
                save_projects(filename, projects)
            print("thank you for using custom-built project management software.")
        else:
            print("invalid choice")


def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as out_file:
        print("name\tstart date\tpriority\tcost estimate\tcompletion percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                  f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                  file=out_file)


def display_projects(projects):
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("completed projects:")
    for project in complete:
        print(f"  {project}")


def get_start_date(project):
    return project.start_date


def filter_projects_by_date(projects):
    date_string = input("show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = sorted([p for p in projects if p.start_date > date], key=get_start_date)
    for project in filtered:
        print(project)


def add_project(projects):
    print("let's add a new project")
    name = input("name: ")
    date_string = input("start date (dd/mm/yyyy): ")
    priority = int(input("priority: "))
    cost = float(input("cost estimate: $"))
    completion = int(input("percent complete: "))
    projects.append(Project(name, date_string, priority, cost, completion))


def update_project(projects):
    index = 0
    while index < len(projects):
        project = projects[index]
        print(f"{index} {project}")
        index += 1
    choice = int(input("project choice: "))
    project = projects[choice]
    print(project)
    completion = input("new percentage: ")
    if completion:
        project.completion_percentage = int(completion)
    priority = input("new priority: ")
    if priority:
        project.priority = int(priority)


main()
