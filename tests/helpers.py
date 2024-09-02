from subprocess import run

def run_python_script(script_path : str, input_text : str) -> str:
    process = run(["python", script_path], text=True, capture_output=True, input=input_text)
    output_text = process.stdout.strip()
    return output_text


