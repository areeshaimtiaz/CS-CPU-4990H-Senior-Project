
from flask import Flask, request, render_template_string
import tempfile, subprocess, os, pathlib

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>AI-CFG Optimizer (Prototype)</title>
<h2>Upload a C++ file (.cpp)</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
{% if output %}
<h3>Result</h3>
<pre>{{output}}</pre>
{% endif %}
"""

@app.route("/", methods=["GET","POST"])
def index():
    output = ""
    if request.method == "POST" and "file" in request.files:
        f = request.files["file"]
        with tempfile.TemporaryDirectory() as td:
            src = os.path.join(td, "input.cpp")
            f.save(src)
            ll = os.path.join(td, "out.ll")
            try:
                subprocess.check_output(["clang", "-emit-llvm", "-S", "-o", ll, src], stderr=subprocess.STDOUT)
                output = pathlib.Path(ll).read_text()[:2000]
            except Exception as e:
                output = f"Error running clang: {e}"
    return render_template_string(TEMPLATE, output=output)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
