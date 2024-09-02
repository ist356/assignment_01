
def test_hello():
    from subprocess import Popen, PIPE

    process = Popen(["python", "./code/hello.py"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    output_text = output.decode("utf-8").strip()

    assert output_text == 'Hello, World!'
