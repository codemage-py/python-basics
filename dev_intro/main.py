def about_me():
    name = "codemage-py"
    role = "Software Engineering Student"
    interests = ["Python", "Backend", "Automation", "Banks & Tech"]

    print(f"👋 Hi, I'm {name}")
    print(f"💻 Role: {role}")
    print("🚀 Interests:")
    for i in interests:
        print(f" - {i}")

if __name__ == "__main__":
    about_me()