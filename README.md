# CommitCleaner

CommitCleaner is a tool designed to neatly reset the commit history of your Git repository while keeping the current state of the code intact. This utility allows you to maintain a clean repository, starting afresh without the clutter of unnecessary history.

## Features

- Removes Git commit history
- Retains the current state of the code
- Creates a new initial commit

## Installation

CommitCleaner is written in Python and can be easily installed via pip:

```bash
pip install commitcleaner
```

## Usage
Once installed, you can execute the `commitcleaner` command in your command line within the directory of your Git repository to reset its commit history:

```bash
cd {your project}
commitcleaner
```

This command performs the following actions:

1. Creates an orphan branch named `latest_branch`.
2. Adds all files to the staging area.
3. Creates a new commit with the message "Initial commit".
4. Deletes the existing `main` branch.
5. Renames the current branch to `main`.
6. Force pushes the changes to the remote repository.

## Caution
- It is advisable to backup important data before using this tool, as the process of removing commit history is irreversible.
- Force pushing (`git push -f`) to a remote repository can cause synchronization issues with other collaborators. Discuss with your team before using.

## Acknowledgments
This tool was inspired by a Stack Overflow answer, which provides a method for removing Git commit history while keeping the code in its current state. You can find the original solution [here](https://stackoverflow.com/a/26000395/10386667).

## Credits
This project was generated with the assistance of ChatGPT-4, an advanced language model developed by OpenAI. The tool's concept, code snippets, and documentation were crafted through interactive sessions with the AI, showcasing the potential of AI-assisted software development.

## Contributing
If you would like to contribute to the `commitcleaner` project, please feel free to submit an issue or a pull request on GitHub. All contributions are welcome!

## License
This project is distributed under the [MIT License](/LICENSE).
