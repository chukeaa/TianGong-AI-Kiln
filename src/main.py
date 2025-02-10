import kiln_ai
import kiln_ai.datamodel
from kiln_ai.datamodel import Project

project = Project.load_from_file("projects/project.kiln")
print("Project: ", project.name, " - ", project.description)

# List all tasks in the project, and their dataset sizes
tasks = project.tasks()
for task in tasks:
    print("Task: ", task.name, " - ", task.description)
    print("Total dataset size:", len(task.runs()))


# Created a project and task via the UI and put its path here
task_path = (
    "/Users/youruser/Kiln Projects/test project/tasks/632780983478 - Joke Generator/task.kiln"
)
task = kiln_ai.datamodel.Task.load_from_file(task_path)

# Add data to the task - loop over you dataset and run this for each item
item = kiln_ai.datamodel.TaskRun(
    parent=task,
    input='{"topic": "AI"}',
    output=kiln_ai.datamodel.TaskOutput(
        output='{"setup": "What is AI?", "punchline": "content_here"}',
    ),
)
item.save_to_file()
print("Saved item to file: ", item.path)
