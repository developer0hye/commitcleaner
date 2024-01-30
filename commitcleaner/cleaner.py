import subprocess
import sys

def clean_current_branch():
    current_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()

    commands = [
        f'git checkout --orphan temp_{current_branch}',
        'git add -A',
        f'git commit -am "Initial commit"',
        f'git branch -D {current_branch}',
        f'git branch -m {current_branch}',
        f'git push --set-upstream origin {current_branch} -f'
    ]

    for cmd in commands:
        process = subprocess.run(cmd, shell=True, check=True)
        if process.returncode != 0:
            print(f'Command failed: {cmd}', file=sys.stderr)
            return False
    return True

def main():
    print("Cleaning the current checked out branch...")
    if clean_current_branch():
        print("Current branch cleaned successfully.")
    else:
        print("Failed to clean the current branch.")

if __name__ == '__main__':
    main()
