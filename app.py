import json
import subprocess
from jinja2 import Environment, FileSystemLoader
import os

# Setting up the paths
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "output"
DATA_PATH = "data/sample_data.json"
OUTPUT_TEX = os.path.join(OUTPUT_DIR, "resume.tex")
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "resume.pdf")

# Loading the data
with open(DATA_PATH, "r", encoding = "utf-8") as f:
    data = json.load(f)

# Jinja2 env initiation
env = Environment(loader = FileSystemLoader(TEMPLATE_DIR))
template = env.get_template("resume_template.tex")

# Renderomg LaTeX with data
rendered_tex = template.render(**data)

# Making an output directory
os.makedirs(OUTPUT_DIR, exist_ok = True)

# Writing .tex file
with open(OUTPUT_TEX, "w", encoding = "utf-8") as f:
    f.write(rendered_tex)

# Compiling LaTeX to PDF using pdflatex
subprocess.run(["pdflatex", "-output-directory", OUTPUT_DIR, OUTPUT_TEX])

print(f"Resume generated at {OUTPUT_PDF}")