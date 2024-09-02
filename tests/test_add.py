def test_add():
    from subprocess import run, PIPE

    process = run(["python", "./code/add.py"], text=True, capture_output=True, input="10\n20\n")
    output_text = process.stdout.strip()

    assert output_text.find("30") >=0
