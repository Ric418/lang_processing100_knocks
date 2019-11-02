import argparse

def output_text_head(text_lines, n):
    for num in range(0,n):
        print(text_lines[num], end='')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('text_path', type=str)
    parser.add_argument('num', type=int)
    args = parser.parse_args()
    with open(args.text_path) as f:
        lines=f.readlines()
    output_text_head(lines, args.num)

