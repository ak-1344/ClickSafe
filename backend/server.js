// Import necessary libraries
const express = require('express');   // Framework for handling API routes
const cors = require('cors');         // Allows frontend to talk to backend
const axios = require('axios');       // For making API requests
require('dotenv').config();           // Loads environment variables

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
        // Mock threat level (we'll replace this with real API checks)
        let threatLevel = Math.random();
        let riskCategory = '';

        if (threatLevel < 0.6) {
            riskCategory = 'Low Risk';
        } else if (threatLevel < 0.9) {
            riskCategory = 'Medium Risk';
        } else {
            riskCategory = 'High Risk';
        }

        // OPTIONAL: External API integration (VirusTotal, Google Safe Browsing, etc.)
        // Example: Calling VirusTotal API (Replace with actual API key)
        /*
        const apiResponse = await axios.get(`https://www.virustotal.com/api/v3/urls/${url}`, {
            headers: { 'x-apikey': process.env.VIRUSTOTAL_API_KEY }
        });
        */

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
