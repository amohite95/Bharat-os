require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const axios = require('axios');

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function runSovereignPulse() {
    console.log("🇮🇳 BHARAT-OS v6.0: THE FINAL REDIRECT...");
    
    // THE MASTER KEYS (Corrected ID: -6807984967)
    const botUrl = "https://api.telegram.org";
    const chatId = "-6807984967";

    const { data: clients, error } = await supabase.from('msme_clients').select('*');
    if (error) return console.log("❌ DB ERROR: " + error.message);

    for (let client of clients) {
        const msg = "भारत-ओएस अलर्ट: प्रिय " + client.business_name + ", तुमच्यासाठी नवीन टेंडर सापडले आहे. किंमत: ₹५,००,०००.";
        
        try {
            await axios.post(botUrl, { chat_id: chatId, text: msg });
            console.log("✅ SUCCESS: Marathi Alert delivered to Group!");
        } catch (e) {
            console.log("❌ ERROR: " + (e.response ? e.response.data.description : e.message));
        }
    }
}
runSovereignPulse();
