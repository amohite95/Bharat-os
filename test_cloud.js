require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const s = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);
s.from('msme_clients').select('*').then(({data, error}) => {
    if (error) console.log('❌ ERROR:', error.message);
    else console.log('✅ BHARAT-OS CONNECTED! Found clients:', data.length);
});
