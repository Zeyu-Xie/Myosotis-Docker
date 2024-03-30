FROM pluswave/ctex:latest

WORKDIR /app

COPY . /app

CMD ["sh", "-c", "xelatex -output-directory=./src ./src/main.tex && bibtex ./src/main.aux && xelatex -output-directory=./src ./src/main.tex && xelatex -output-directory=./src ./src/main.tex"]

# I originally used pdflatex, but it does not support Chinese characters.

# FROM pandoc/latex:edge

# WORKDIR /app

# COPY . /app

# CMD ["pdflatex", "-halt-on-error", "-output-directory=./src", "./src/main.tex"]
