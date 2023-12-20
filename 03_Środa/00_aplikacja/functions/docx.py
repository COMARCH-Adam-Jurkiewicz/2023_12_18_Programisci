import subprocess

def docxcreate(filename: str):
    markd = f"{filename}.md"
    output = f"{filename}.docx"
    command = ["pandoc", "-o", output, markd]
    ret_code = subprocess.run(command, capture_output=True)
    print(f"Subprocess returned {ret_code}")

if __name__ == "__main__":
    docxcreate("wykres")