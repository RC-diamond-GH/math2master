import os

if __name__ == '__main__':
    output = open('./默写大王.md', 'w', encoding='utf-8')
    for x in range(1, len(os.listdir('./origin')) + 1):
        with open(f'./origin/{x}.md', 'r', encoding='utf-8') as f:
            output.write(f.read())
            output.write('\n\n')
    output.close()