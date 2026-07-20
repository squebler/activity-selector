import argparse
import random

def main(activity_file='activities.txt', lines_per_batch=5):
    with open(activity_file, 'r', encoding='utf-8') as file:
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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'activity_file',
        nargs='?',
        default='activities.txt',
        help='Activity file to read (default: activities.txt)',
    )

    parser.add_argument(
        "-n",
        "--lines-per-batch",
        type=int,
        default=5,
        help="Number of activities shown per batch (default: 5)",
    )

    args = parser.parse_args()

    if args.lines_per_batch < 1:
        parser.error('--lines-per-batch must be at least 1')

    main(args.activity_file, args.lines_per_batch)

