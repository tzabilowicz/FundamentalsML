import argparse

# Job imports
from scripts.DatabaseBuilder import DatabaseBuilder
#from scripts.ModelBuilder import ModelBuilder
#from scripts.Backtester import Backtester
# NOTE: What about portfolio and order execution job(s)

def main():
    parser = argparse.ArgumentParser(
        prog="run.py",
        description="FundamentalsML job processor."
    )

    # NOTE: If no args are specified, all jobs run
    # Add optional arguments (requires 1 or more if specified)
    parser.add_argument('-j', '--job', nargs='+', help='Job Name(s)')
    parser.add_argument('-a', '--all', action='store_true', help='All Jobs')

    args = parser.parse_args()

    # Determine if all jobs
    if args.all:
        print('Running all jobs...')
        return

    # No jobs specified
    if not args.job:
        parser.print_help()
        return

    # NOTE: Runs in order if multiple jobs specified
    if 'DatabaseBuilder' in args.job:
        print('Running database builder job...')

    if 'ModelBuilder' in args.job:
        print('Running model builder job...')

    if 'Backtester' in args.job:
        print('Running backtester job...')


if __name__ == '__main__':
    main()