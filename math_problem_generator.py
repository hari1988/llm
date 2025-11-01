import ollama

def generate_problems(topics: list[str], num_counts = 5):
    prompt = f"""
    You are a helpful math tutor. Generate {num_counts} unique, separate math problems suitable for a 3rd grader.
    The problems should cover topics in {topics} list.
    Make sure the problems vary in difficulty.
    DO NOT provide the answers or solutions. Also, do not include the topic alongside each problem.

    Strictly present only the problems as a numbered list, one problem per line. DO NOT include any introductory or concluding remarks, just the list.
    """
    
    print("Generating math problems...")
    response = ollama.chat(
        model = "phi4",
        messages=[
            {'role': 'system', 'content': 'You are a helpful math tutor for 3rd graders.'},
            {'role': 'user', 'content': prompt}
        ],
        options={'temperature': 0.8}
    )

    problem_text = response['message']['content'].strip()
    problems = [
        line.strip()
        for line in problem_text.split('\n')
        if line.strip()
    ]

    print(f"Generated {len(problems)} problems.")
    print("\nProblems:")
    for problem in problems:
        print(problem)
    return problems