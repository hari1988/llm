from mem0 import MemoryClient

client = MemoryClient(api_key="m0-OJZiMWACjG9mRtRJalUfSmihzqQFR1oaxuBDgP54")

def add_to_memory():
    messages = [
        { 
            "role": "user", 
            "content": "On November 2, 2025 Aaradhya struggled with word problems that involved more than 1 step. She also made mistakes with multiplication in 8 tables",
        },
    ]

    client.add(messages=messages, user_id = "aaradhya")

def get_from_memory():
    summary = client.get_summary()
    print(f"summary={summary}")
    return summary

if __name__ == "__main__":
    add_to_memory()