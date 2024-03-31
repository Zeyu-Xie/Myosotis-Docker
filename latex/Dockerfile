FROM acanxie/xelatex:1.0.0

WORKDIR /app

COPY . /app

RUN chmod +x /app/compile.sh

CMD ["./compile.sh"]

# I originally used pdflatex, but it does not support Chinese characters.

# FROM pandoc/latex:edge

# WORKDIR /app

# COPY . /app

# CMD ["pdflatex", "-halt-on-error", "-output-directory=./src", "./src/main.tex"]
