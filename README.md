# Dictionary App

This is a Django-based dictionary application that allows users to add, edit, delete, and listen to words in English, Russian, and Uzbek. The application also supports categorizing words and adding terms for better organization.

## Features

- Add, edit, and delete words in multiple languages.
- Categorize words and terms.
- Text-to-speech functionality for English and Russian words.
- Easy navigation and management of dictionary entries.

## Installation

### Prerequisites

- Python 3.6+
- Pipenv

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/diyorbekqodirboyev863/dictionary-app.git
    cd dictionary-app
    ```

2. **Install dependencies**:
    ```bash
    pipenv install --dev
    ```

3. **Activate the virtual environment**:
    ```bash
    pipenv shell
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Home Page**: View all dictionary entries.
- **Add Dictionary**: Add new words with their translations and descriptions.
- **Change Dictionary**: Edit or delete existing words.
- **Categories**: Manage word categories.
- **Terms**: Manage word terms.

## Text-to-Speech

The app uses the `pyttsx3` library for text-to-speech functionality. You can listen to the pronunciation of words in both English and Russian.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## Author

[Diyorbek Qodirboyev](https://github.com/diyorbekqodirboyev863)