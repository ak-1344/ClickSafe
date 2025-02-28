// Import necessary libraries
import express from 'express';   // Framework for handling API routes
import cors from 'cors';         // Allows frontend to talk to backend
import axios from 'axios';       // For making API requests
import dotenv from 'dotenv';     // Loads environment variables

dotenv.config();

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 5000;

// Middleware setup
app.use(cors());                      // Enable cross-origin requests
app.use(express.json());              // Parse JSON body data

// Default route for testing
app.get('/', (req, res) => {
    res.send('ClickSafe Backend is running!');
});

// API route to check URL security
app.post('/check-url', async (req, res) => {
    const { url } = req.body;  // Extract URL from request

    if (!url) {
        return res.status(400).json({ error: 'No URL provided' });
    }

    try {
        const encodedUrl = Buffer.from(url).toString('base64');
        const apiResponse = await axios.get(`https://www.virustotal.com/api/v3/urls/${encodedUrl}`, {
            headers: { 'x-apikey': process.env.VIRUSTOTAL_API_KEY }
        });

        // Extract relevant data from the API response
        const threatLevel = apiResponse.data.data.attributes.last_analysis_stats.malicious;
        let riskCategory = '';

        if (threatLevel === 0) {
            riskCategory = 'Low Risk';
        } else if (threatLevel < 5) {
            riskCategory = 'Medium Risk';
        } else {
            riskCategory = 'High Risk';
        }

        // Send response back to frontend
        res.json({
            url: url,
            risk: riskCategory,
            threatScore: threatLevel.toFixed(2),
            // externalAnalysis: apiResponse.data  // Uncomment if using an external API
        });

    } catch (error) {
        console.error('Error analyzing URL:', error);
        res.status(500).json({ error: 'Server error during analysis' });
    }
});

// Start the server
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
