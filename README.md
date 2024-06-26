# Research Data Lifecycle Visualization

This project is a web application that visualizes the Research Data Lifecycle using Express and SQLite for the backend, and React with TypeScript for the frontend.

## Project Structure

```
/your-project-root
├── server/
│   ├── prisma/
│   ├── src/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── config/
│   │   └── server.js
│   ├── package.json
│   └── .env
├── client/
│   ├── src/
│   │   ├── components/
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── public/
│   ├── package.json
│   └── tsconfig.json
└── README.md
```

## Prerequisites

- Node.js (v14 or later)
- npm (v6 or later)

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Set up the server:
   ```
   cd server
   npm install
   ```

3. Set up the client:
   ```
   cd ../client
   npm install
   ```

4. Set up the database:
   In the `server` directory, create a `.env` file with the following content:
   ```
   DATABASE_URL="file:./dev.db"
   ```

5. Generate Prisma client and push the database schema:
   ```
   cd ../server
   npx prisma generate
   npx prisma db push
   ```

## Running the Application

1. Start the server:
   ```
   cd server
   npm start
   ```

2. In a new terminal, start the client:
   ```
   cd client
   npm start
   ```

The server will run on `http://localhost:4000`, and the client will run on `http://localhost:3000`.

## Features

- Interactive visualization of the Research Data Lifecycle
- RESTful API for data management
- React-based frontend with TypeScript
- SQLite database for data persistence

## Technologies Used

- Backend: 
  - Express.js
  - Prisma ORM
  - SQLite
- Frontend: 
  - React
  - TypeScript
  - D3.js for visualizations

## API Endpoints

- `GET /api/stages`: Retrieve all stages with their substages
- (Add other endpoints as they are implemented)

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.