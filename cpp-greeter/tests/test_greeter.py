import subprocess

def test_greeter():
    result = subprocess.run(
        ["./build/greeter_app", "Pixi"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "Hello, Pixi!"
