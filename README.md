# JSONPlaceholder API Interaction Tool

This Python application demonstrates an Object-Oriented approach to interact with JSONPlaceholder, a fake online REST API for testing and prototyping. It fetches data from two different endpoints: `/posts` and `/users`.

## Features

- Fetch and display posts and users from JSONPlaceholder.
- Use of Python 3.10+ with type hints for improved code quality.
- Mypy for static type checking.
- Pytest with `requests-mock` for testing API interactions.
- GitHub Actions for automating tests.

## Installation

Ensure you have Python 3.10 or higher installed on your machine. Clone this repository and navigate into the project directory:

```bash
git clone https://github.com/InterviewAssignmentsDK/IAssignment.git
cd IAssignment
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Execute the main application script with:

```bash
python api_manager.py
```

This will print the fetched posts and users in the console.

## Testing

To run tests, ensure you are in the project directory and execute:

```bash
pytest
```

To view a coverage report, run:

```bash
pytest --cov-report term --cov=api_manager test_api.py
```

## Type Checking with Mypy

To check for type safety in the codebase, run Mypy with the following command:

```bash
mypy api_manager.py
```

Ensure there are no type errors to maintain code quality.

## GitHub Actions

This repository is configured with GitHub Actions to run tests manually. Navigate to the "Actions" tab in the GitHub repository, select the workflow, and use the "Run workflow" button to trigger the tests.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
