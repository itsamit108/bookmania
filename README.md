# Bookmania

## Introduction

Welcome to Bookmania! This web application, built with Django, allows users to review and discuss their favorite books. It provides a platform for sharing insights, opinions, and recommendations about various books.

## Features

- **User Registration and Authentication:** Users can sign up, log in, and securely manage their accounts.
- **Book Listings:** Browse a collection of books with detailed information.
- **Book Reviews:** Write and read reviews for books.
- **User Profiles:** Users can create and update their profiles.
- **Image Upload:** Users can add cover images when adding books.

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python 3.x
- Django 3.x
- Virtual Environment (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/itsamit108/bookmania.git
   cd bookmania
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

- Register or log in to your account.
- Explore the available books and add your reviews.
- Customize your profile settings.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m 'Add some feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a pull request on the original repository.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
