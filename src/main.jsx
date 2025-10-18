import React, { useState } from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import MemoravelEAtraente from './components/MemoravelEAtraente'
import SplashScreen from './components/SplashScreen'
const App = () => { const [loading,setLoading]=useState(true); return <> {loading && <SplashScreen onFinish={()=>setLoading(false)} />} {!loading && <MemoravelEAtraente />} </> }
ReactDOM.createRoot(document.getElementById('root')).render(<React.StrictMode><App/></React.StrictMode>)