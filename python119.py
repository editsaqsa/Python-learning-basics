# Command line Utilities
import argparse
import time
def main():
    parser = argparse.Argumentparser(
        description = "simple command line utilities for practice"
    )


    parser.add_argument(
        "--name", type=str,default="Aqsa", help="Name to greet in output"
    )


    parser.add_argument(
        "--repeat", type=int,default=2, help="How mny time to show message"
    )


    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay in second between messaga,"
    )

    args = parser.parse_args()
    for i in range(1, args.repeat + 1):
        print(f"[{i}/{args.repeat}] keep going, {args.name}")
        time.sleep(args.delay)

if __name__ == "__main__":
    main()
