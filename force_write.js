require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');

if (!process.env.SUPABASE_URL || !process.env.SUPABASE_KEY) {
    console.log("❌ ERROR: Keys are missing from .env!");
    process.exit(1);
}

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function forceWrite() {
    console.log("⚡ [BHARAT-OS] Force-Writing to Cloud Memory...");
    const { data, error } = await supabase
        .from('bharat_tasks')
        .insert([{ task_type: 'FORCE_LINK_2026', status: 'SUCCESS' }])
        .select();

    if (error) {
        console.log("❌ DB ERROR:", error.message);
    } else {
        console.log("✅ SUCCESS! Data is now in Supabase.");
    }
}
forceWrite();
