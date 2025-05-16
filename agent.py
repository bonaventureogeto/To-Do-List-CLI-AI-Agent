from modules.perception import parse
from modules.brain import decide
from modules.action import add_task, list_tasks, remove_task


def run():
    print("To-Do Agent live. Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower in ("exit", "quit"):
            print("See you next time")
            break

        # perception
        command = parse(user_input)

        # Reasoning
        decision = decide(command)
        tool, args = decision.get("tool"), decision.get("args", {})

        # action
        match tool:
            case "add_task": print(add_task(**args))
            case "list_tasks": print(list_tasks())
            case "remove_task": print(remove_task(**args))
            case _:
                print(f"? Unrecognized tool: {tool}")


if __name__ == "__main__":
    run()
