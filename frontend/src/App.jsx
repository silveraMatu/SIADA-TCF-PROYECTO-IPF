import React from 'react';
import Navbar from './components/Navbar/Navbar';
import LoginForm from './components/LoginForm/LoginForm';
import Footer from './components/Footer/Footer';
import './App.css';

function App() {
  return (
    <div className="app-layout">
      <Navbar />
      <main className="main-content">
        <LoginForm />
      </main>
      <Footer />
    </div>
  );
}

export default App;
