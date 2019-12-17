import subprocess

# has to use ", windows terminal does not support '
subprocess.call(["prettier", "--write", "./**/*.md"])