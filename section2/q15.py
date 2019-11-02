import argparse

def output_text_tail(text_lines, n):
    for line in text_lines[len(text_lines)-n:]:
        print(line,end='')
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('text_path', type=str)
    parser.add_argument('num', type=int)
    args = parser.parse_args()
    with open(args.text_path) as f:
        lines=f.readlines()
    output_text_tail(lines, args.num)