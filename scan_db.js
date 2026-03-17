require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function scan() {
    console.log("🔍 [SCAN] Checking Database Connection...");
    console.log("URL:", process.env.SUPABASE_URL);
    
    // Check if the table even exists to the Brain
    const { data, error } = await supabase.from('msme_clients').select('*');
    
    if (error) {
        console.log("❌ ERROR:", error.message);
    } else {
        console.log("📊 ROWS FOUND:", data.length);
        console.log("DATA:", JSON.stringify(data, null, 2));
    }
}
scan();
