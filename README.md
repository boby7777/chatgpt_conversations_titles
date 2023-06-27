# ChatGPT Conversation Title Counter

The exported data of ChatGPT is `conversations.json`. With this tool, you can parse the JSON and retrieve the title for each date.

## Prerequisites

- Python 3.x
- `dotenv` library (install using `pip install python-dotenv`)

## Setup

1. Clone the repository and navigate to the project directory.
2. Create a file named `.env` in the project directory or rename the `.env_sample` to `.env`.
3. Open the `.env` file and add the following line, replacing `<json_filename>` with the name of your JSON file:
   ```
   JSON_FILENAME=<json_filename>
   ```

## Usage

1. Place your JSON file in the project directory.
2. Run the script by executing the command `python json_title_counter.py`.
3. The script will read the JSON file, calculate the number of titles per day, and print the results to the console.

## Example JSON Format

The JSON file should have the following format:

```json
[
  {
    "title": "Title 1",
    "create_time": 1687772562.265141,
    "message": "Message 1"
  },
  {
    "title": "Title 2",
    "create_time": 1687772662.265141,
    "message": "Message 2"
  },
  ...
]
```

## Output

The script will print the following information:

- The date and the count of titles for each day.
- The titles for each day, numbered sequentially.
- The total count of titles.

## License

This project is licensed under the [MIT License](LICENSE).