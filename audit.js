require('dotenv').config();
const { createClient } = require('@supabase/supabase-js');
const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);

async function runAudit() {
    console.log("🧐 [AUDIT] Fetching Latest System States...");
    const { data: tasks, error } = await supabase
        .from('bharat_tasks')
        .select('*')
        .order('created_at', { ascending: false })
        .limit(5);

    if (error) {
        console.error("❌ [AUDIT FAILED]:", error.message);
    } else {
        console.table(tasks.map(t => ({
            ID: t.id.slice(0,8), 
            TYPE: t.task_type, 
            STATUS: t.status, 
            TIME: t.created_at
        })));
    }
}
runAudit();
