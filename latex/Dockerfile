FROM texlive/texlive:pretest-doc-src

WORKDIR /app

COPY . /app

CMD ["pdflatex", "-halt-on-error", "-output-directory=./src", "./src/main.tex"]