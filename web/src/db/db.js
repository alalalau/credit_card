import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
const supabaseKey = import.meta.env.VITE_SUPABASE_KEY

export const supabase = createClient(supabaseUrl, supabaseKey)

// get transactions given month and year, get all days in the month
export async function getTransactions(month, year) {
  const { data, error } = await supabase
    .from('transactions')
    .select('*')
    .eq('month', month)
    .eq('year', year)
    .order('date', { ascending: true })

  if (error) {
    console.error(error)
    return []
  }
  return data
}

console.log('here',supabaseUrl, supabaseKey)
