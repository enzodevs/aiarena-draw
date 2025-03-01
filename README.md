# aiarena-draw

## Overview

This project uses the DeepSeek API to generate a winner from a list of usernames stored in a CSV file.

## Features

*   Reads usernames from `followers/`.
*   Utilizes the DeepSeek API to select a winner.
*   Outputs the selected winner.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <https://github.com/enzodevs/aiarena-draw.git>
    ```
2.  **Install dependencies:**

    ```bash
    pip install openai python-dotenv pandas
    ```
3.  **Set up your environment variables:**

    *   Create a `.env` file in the project root.
    *   Create a `followers/` folder in the project root and add your data csv files.
    *   Add your DeepSeek API key:

        ```
        DEEPSEEK_API_KEY=YOUR_API_KEY
        ```

## Usage

1.  **Ensure `followers/data.csv` exists and contains a `username` column.**
2.  **Run the `main.py` script:**

    ```bash
    python main.py
    ```

## Author

Enzo Cambraia