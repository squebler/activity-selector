import random

def main(lines_per_batch=5):
    with open('activities.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    random.shuffle(lines)

    line_num = 0
    for batch_ind in range(0, len(lines), lines_per_batch):
        batch = lines[batch_ind : batch_ind + lines_per_batch]

        for i, line in enumerate(batch):
            line_num += 1
            print(f"{line_num}. {line}", end='')

        is_last_batch = batch_ind + lines_per_batch >= len(lines)
        if not is_last_batch:
            print("\nPress [Enter] for more.")
            print("Press CTRL+C to quit.")
            input()

if __name__ == '__main__':
    main()

