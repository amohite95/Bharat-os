const axios = require('axios');
require('dotenv').config();

async function sendMarathiAlert(businessName, tenderInfo) {
    const message = `🇮🇳 *Bharat-OS अलर्ट* \n\nप्रिय ${businessName}, \nतुमच्या उद्योगासाठी नवीन सरकारी टेंडर (GeM) सापडले आहे: \n\n📌 *माहिती:* ${tenderInfo} \n💰 *किंमत:* ₹५,००,००० \n\n_तुमचा ३० दिवसांचा मोफत ट्रायल सुरू आहे._`;
    
    const token = process.env.TELEGRAM_TOKEN;
    const chat_id = process.env.TELEGRAM_CHAT_ID;
    
    if (!token || !chat_id) {
        console.log("[HAND] Token/ChatID missing. Logging to Cloud only.");
        return;
    }

    const url = `https://api.telegram.org{token}/sendMessage`;
    try {
        await axios.post(url, { chat_id: chat_id, text: message, parse_mode: 'Markdown' });
        console.log(`✅ [HAND] Marathi Alert sent to ${businessName}.`);
    } catch (err) {
        console.log("[HAND ERROR] Message delivery failed.");
    }
}
module.exports = { sendMarathiAlert };
