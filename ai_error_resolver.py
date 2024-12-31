import sys
import logging
import subprocess

logging.basicConfig(level=logging.INFO)

def resolve_git_issues():
    logging.info("Attempting to resolve Git issues...")
    commands = [
        "git reset --hard",
        "git clean -fd",
        "git pull origin main"
    ]
    for command in commands:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            logging.error(f"Command failed: {command}")
            return False
    return True

def main(error_line):
    if "git pull origin main" in error_line:
        if not resolve_git_issues():
            logging.error("Failed to resolve Git issues.")
            sys.exit(1)
    else:
        logging.error(f"Unhandled error at line: {error_line}")
        sys.exit(1)

if __name__ == "__main__":
    error_line = sys.argv[1]
    main(error_line)
