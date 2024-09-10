# Custom-GPT

This project creates a custom GPT application using the OpenAI API.

## Building and Running with Docker

1. Make sure you have Docker and Docker Compose installed on your system.
2. Clone this repository.
3. Navigate to the project directory.
4. Build and run the Docker container:
   ```
   docker-compose up --build
   ```
5. The application will be available at `http://localhost:5001`.

Note: Ensure that you have set the `OPENAI_API_KEY` environment variable before running the container.

## OpenAI Model

This project currently uses the `gpt-3.5-turbo-instruct` model from OpenAI. This model provides a good balance between performance and cost for most applications.

## Future Vision

Our future plans for this project include:

1. Creating a custom user interface for easier interaction with the GPT model.
2. Implementing more advanced features and customizations.
3. Exploring the use of newer OpenAI models as they become available.

Stay tuned for updates!
