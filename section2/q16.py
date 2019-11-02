import argparse
ANS16_PATH='./section2/ans16/script/split'

def split_file(text_lines,num):
    order=0
    for count, n in enumerate(range(0,len(text_lines)+1,num)):
        tmp_text=''
        for line in text_lines[order:order+num]:
            tmp_text+=line
        with open(ANS16_PATH+str(num)+'_'+str(count+1)+'.txt', mode='w') as f:
            f.write(tmp_text)
        order+=num

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('text_path', type=str)
    parser.add_argument('num', type=int)
    args = parser.parse_args()
    with open(args.text_path) as f:
        lines=f.readlines()
    split_file(lines, args.num)