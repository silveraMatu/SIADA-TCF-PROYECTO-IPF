import LoginForm from '../components/LoginForm/LoginForm';

export default function LoginPage({ onLoginSuccess }) {
  return (
    <div className="page-container login-page">
      <LoginForm onLoginSuccess={onLoginSuccess} />
    </div>
  );
}
