
# Backend Server for Submission Management

This is a backend server for managing submissions. It uses Express.js and stores data in a `db.json` file, simulating a simple database.

## Prerequisites

Before you begin, ensure you have [Node.js](https://nodejs.org/) installed on your system.

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://your-repository-url.git](https://github.com/preetam1407/Slidely-Form-Bankend.git)
   cd move to Slidely-Form-Backend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

## Running the Server

1. **Start the server:**
   ```bash
   npx ts-node src/server.ts
   ```

   This will start the server on `localhost:3000`. 

## API Endpoints

- **GET /ping** - Test endpoint to check if the server is running.
- **POST /submit** - Submit a new entry. Requires a JSON body with `name`, `email`, `phone`, `githubLink`, and `stopwatchTime`.
- **GET /read** - Retrieves all submissions.
- **PUT /update/:index** - Updates a submission at a specific index. Requires the same fields as submit.
- **DELETE /delete/:index** - Deletes a submission at a specific index.

## Storing Data

Data is stored in a `db.json` file in the root directory of the project. Make sure not to delete or corrupt this file as it acts as database.
