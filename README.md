# Flask Application for Avatar Generation

This repository contains a Flask-based web application that processes uploaded images to generate avatars. The image processing includes detecting a face, centralizing it, and cropping the region to create an avatar. The project uses OpenCV for face recognition and is containerized using Docker Compose for easy setup and deployment.

---

## Features

- Accepts image files via a simple HTTP POST API.
- Automatically detects faces in the uploaded image.
- Crops and centers the image around the detected face.
- Built using the OpenCV library for robust face detection.
- Fully containerized with Docker Compose for streamlined deployment.

---

## How it Works

1. A `POST` request is made to the API with an image file uploaded as multipart form data.
2. The uploaded image is processed using OpenCV to detect faces in the image.
3. If a face is detected:
    - The image is cropped and centered around the detected face.
    - An avatar is generated from the cropped portion.
4. If no face is detected, the API provides an appropriate response or error.
5. The response includes the processed avatar image or error details based on the result.

---

## Prerequisites

Ensure you have the following installed before starting:

1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker Compose](https://docs.docker.com/compose/)

---

## How to Run the Application

Follow these steps to run the application:

### Step 1: Clone the Repository

Clone this repository to your local machine:

```shell
git clone https://github.com/hmayer/avatar-normalization.git
cd avatar-normalization
```

### Step 2: Build the Docker Images

Use the following command to build the Docker images specified in the `docker-compose.yml` file:

```shell
docker compose build --no-cache
```

### Step 3: Start the Application

Start the application using Docker Compose:

```shell
docker compose up -d
```

- The `-d` flag runs the containers in detached mode (background).

By default, the application will be accessible at [http://localhost:5000](http://localhost:5000).

### Step 4: Stop the Application

When you're done, stop and remove the running containers with:

```shell
docker compose stop
```

---

## API Usage

Once the application is running, you can interact with the API using tools like `curl`, Postman, or any HTTP client library.

### Endpoint

#### POST `/`

This endpoint expects a `multipart/form-data` request with an image file attached.

**Request Details:**

- **URL**: `http://localhost:5000/`
- **Method**: POST
- **Content-Type**: `multipart/form-data`
- **Required Field**:
    - `avatar`: The image file to be uploaded.

**Example `curl` Command:**

To upload an image (e.g., `avatar.jpg`):

```shell
curl --request POST \
  --url http://localhost:5000/ \
  --header 'Content-Type: multipart/form-data' \
  --form avatar=@./avatar.jpg
```

Replace `avatar.jpg` with the path to your image file.

**Response:**

- **Success**:
    - Returns the processed avatar image.
- **Failure**:
    - If no face is detected or if the file format is unsupported, a "No face detected" error message is returned.

---

## How OpenCV is Used

This application uses OpenCV for the following tasks:

- Detecting faces in the uploaded image using pre-trained face recognition models.
- Cropping the image to focus on the detected face(s).
- Centralizing and resizing the cropped face region to generate a consistent avatar format.

OpenCV's robust algorithms ensure accurate and efficient face detection, making this application ideal for generating avatars from any image.

---

## File Structure

A brief overview of the project structure:
```
. ├── app/ # Application source code
  ├── Dockerfile # Docker image instructions
  ├── docker-compose.yml # Docker Compose configuration
  ├── requirements.txt # Python dependencies
  └── README.md # You're here!
```

---

## Troubleshooting

1. **Docker Issues**:
    - Ensure Docker and Docker Compose are running (`docker --version`, `docker compose --version`).
    - If ports are in use, adjust the `docker-compose.yml` file to bind to an available port.

2. **API Errors**:
    - Make sure you're uploading an image in the supported format (e.g., JPEG, PNG).
    - Check application logs for issues:
      ```shell
      docker logs <container-name>
      ```

3. **Face Not Detected**:
    - Ensure the uploaded image is clear and contains a recognizable face.
    - If the face is partially obscured or at an extreme angle, face detection might fail.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

Feel free to contribute, report issues, or open pull requests!

---

Generate avatars automatically and portably with this Flask-based containerized API! 🚀