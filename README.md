### 1. Create a Task
* **URL:** `/tasks`
* **Method:** `POST`
* **Status Code:** `201 Created`
* **Request Body (`TaskIn`):**
  ```json
  {
    "title": "Complete Project Readme",
    "description": "Write a clean and scannable guide for GitHub.",
    "priority": 3,
    "internal_note": "Hidden note"
  }
  ```

### 2. Get a Task by ID
* **URL:** `/tasks/{task_id}`
* **Method:** `GET`
* **Status Code:** `200 OK`
* **Response Body (`TaskOut`):**
  ```json
  {
    "id": 1,
    "title": "Complete Project Readme",
    "description": "Write a clean and scannable guide for GitHub.",
    "priority": 3,
    "is_completed": false
  }
  ```
* **Errors:** Returns `404 Not Found` if the ID does not exist.

### 3. Mark Task as Completed
* **URL:** `/tasks/{task_id}/complete`
* **Method:** `PATCH`
* **Status Code:** `200 OK`
* **Response Body (`TaskOut`):** `is_completed` fields flips to `true`.
* **Errors:** Returns `404 Not Found` if the ID is missing, or `400 Bad Request` if the task is already completed.
