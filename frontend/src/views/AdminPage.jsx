import AdminDashboard from '../components/AdminDashboard/AdminDashboard';

export default function AdminPage({ user, onLogout }) {
  return (
    <div className="page-container admin-page">
      <AdminDashboard user={user} onLogout={onLogout} />
    </div>
  );
}
