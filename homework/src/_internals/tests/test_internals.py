from ...wordcount import parse_args
import subprocess

def test_parse_args():

    try:
        #subprocess.run(["python", "-m", "homework", "--input", "data/input",  "--output", "data/output"], check=True)
        result = subprocess.run(["python", "-m", "homework", "data/input", "data/output"], text=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    #input_folder, output_folder = parse_args()
    assert "data/input" in result.stdout
    assert "data/output" in result.stdout

#test_parse_args()
#subprocess.run(["python3", "-m", "homework", "data/input", "data/output"], check=True)