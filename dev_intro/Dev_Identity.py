def dev_identity():
    name = "codemmage.py"
    age = 26
    stack = ["Python", "Git", "Linux", "Software Engineering"]

    print("👋 Hello, world!")
    print(f"My name is {name}")
    print(f"I'm {age} years old")
    print("My current stack:")

    for tech in stack:
        print(f" - {tech}")

if __name__ == "__main__":
    dev_identity()
