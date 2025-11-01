import pdf_generator
from math_problem_generator import generate_problems

def main():
    print("This is the main word application.")

    try:
        print("Generating math problems...")
        problems = generate_problems(topics=["addition", "subtraction", "multiplication", "division", "fractions", "basic geometry"], num_counts=10)

        if not problems:
            print("No problems were generated.")
            raise ValueError("No problems generated.")

        print(f"Generated {len(problems)} problems.")

    except Exception as e:
        print(f"An error occurred during problem generation: {e}")
        return
    
    try:
        print("Creating PDF...")
        pdf_filename = pdf_generator.create_pdf(problems, "")
        print(f"PDF created successfully: {pdf_filename}")
    except Exception as e:
        print(f"An error occurred during PDF creation: {e}")
        return
    
if __name__ == "__main__":
    main()