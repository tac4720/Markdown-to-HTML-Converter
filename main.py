import sys
import markdown

def main():
    argc = len(sys.argv)
    if argc != 5:
        print("Usage: python main.py markdown inputfile.md outputfile.html")
        return 1

    inputfile = sys.argv[2]
    outputfile = sys.argv[3]

    with open(inputfile, 'r') as f:
        markdown_text = f.read()

    html = markdown.markdown(markdown_text)

    with open(outputfile, 'w') as f:
        f.write(html)

    return 0

if __name__ == "__main__":
    sys.exit(main())
