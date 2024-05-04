import subprocess

def generate_sequence_diagram(mermaid_code, output_file):
    try:
        # Write Mermaid code to a temporary file
        with open("temp.mmd", "w") as f:
            f.write(mermaid_code)
        
        # Call Mermaid CLI to generate the diagram
        subprocess.run(["mmdc", "-i", "temp.mmd", "-o", output_file], check=True)
        
        print("Sequence diagram generated successfully!")
    except subprocess.CalledProcessError as e:
        print("Error generating sequence diagram:", e)
    finally:
        # Clean up temporary file
        subprocess.run(["rm", "temp.mmd"])

# Example Mermaid code
mermaid_code = """
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>+Bob: Hello Bob, how are you?
    Bob-->>-Alice: I'm good, thanks! How about you?
"""

output_file = "sequence_diagram.png"
generate_sequence_diagram(mermaid_code, output_file)
