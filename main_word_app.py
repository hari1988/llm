import pdf_generator
from math_problem_generator import generate_problems
from mem0_accessor import get_from_memory

def main():
    print("This is the main word application.")

    try:
        performance_context = get_from_memory()

        memory_instruction = f"""
            **IMPORTANT**: I will provide a summary of the student's recent performance.
            You MUST use this information to **customize** the new problems. 
            Focus on the topics where the student struggled, and reduce problems on topics
            they performed well.

            {performance_context}
        """
    
        problems = generate_problems(
            topics=["addition", "subtraction", "multiplication", "division", "fractions", "basic geometry"], 
            memory_instruction=memory_instruction,
            num_counts=10,
        )

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