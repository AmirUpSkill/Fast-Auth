'use client';

import { ProtectedRoute } from '@/components/auth/protected-route';
import { useAuth } from '@/providers/auth-provider';
import { AuthStatusBadge } from '@/components/dashboard/auth-status-badge';
import { UserInfoCard } from '@/components/dashboard/user-info-card';

export default function DashboardPage() {
  const { user } = useAuth();

  return (
    <ProtectedRoute>
      <main className="container py-12 px-4">
        <div className="flex flex-col items-center justify-center space-y-8">
          <div className="text-center space-y-4 animate-fade-in">
            <h1 className="text-4xl md:text-5xl font-bold tracking-tight bg-gradient-to-r from-foreground to-primary/80 bg-clip-text text-transparent">
              Hello Fast API Developer
            </h1>
            <p className="text-lg text-muted-foreground max-w-2xl">
              Welcome to your secure dashboard. Your session is active and your data is protected.
            </p>
            <AuthStatusBadge />
          </div>

          {user && <UserInfoCard user={user} />}
        </div>
      </main>
    </ProtectedRoute>
  );
}