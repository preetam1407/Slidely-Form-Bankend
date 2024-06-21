import express, { Request, Response } from 'express';
import bodyParser from 'body-parser';
import fs from 'fs';
import path from 'path';

const app = express();
const PORT = 3000;
const DB_PATH = path.join(__dirname, 'db.json');

app.use(bodyParser.json());
app.use(express.static('public'));

// Helper to read and write the database
const readDB = () => JSON.parse(fs.readFileSync(DB_PATH, 'utf-8'));
const writeDB = (data: any) => fs.writeFileSync(DB_PATH, JSON.stringify(data, null, 2));

// Initialize database
if (!fs.existsSync(DB_PATH)) {
    writeDB([]);
}

app.get('/', (req, res) => {
    res.send('Welcome to the API!');
});
// Ping endpoint
app.get('/ping', (req: Request, res: Response) => {
    res.send(true);
});

// Submit endpoint
app.post('/submit', (req: Request, res: Response) => {
    const { name, email, phone, githubLink, stopwatchTime } = req.body;
    const submissions = readDB();
    submissions.push({ name, email, phone, githubLink, stopwatchTime });
    writeDB(submissions);
    res.status(201).json({ message: 'Submission saved' });
});

// Read endpoint
// Endpoint to fetch all submissions
app.get('/read/all', (req, res) => {
    const submissions = readDB();  
    if (submissions.length > 0) {
        res.json(submissions); 
    } else {
        res.status(404).json({ message: 'No submissions found' });
    }
});


// Delete a submission by index
app.delete('/delete', (req: Request, res: Response) => {
    const { index } = req.query;
    let submissions = readDB();
    if (index && parseInt(index as string) < submissions.length) {
        submissions.splice(parseInt(index as string), 1);
        writeDB(submissions);
        res.json({ message: 'Submission deleted successfully' });
    } else {
        res.status(404).json({ message: 'Submission not found' });
    }
});

// Update a submission by index
app.put('/update/:index', (req, res) => {
    console.log('Received data:', req.body);
    const index = parseInt(req.params.index);
    let submissions = readDB();
    if (index >= 0 && index < submissions.length) {
        const { name, email, phone, githubLink, stopwatchTime } = req.body;
        submissions[index] = { name, email, phone, githubLink, stopwatchTime };
        writeDB(submissions);
        res.json({ message: 'Submission updated successfully' });
    } else {
        console.error('Submission not found for index:', index);
        res.status(404).json({ message: 'Submission not found' });
    }
});




app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
