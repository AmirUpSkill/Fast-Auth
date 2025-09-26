// providers/auth-provider.tsx
'use client';

import { createContext, useContext } from 'react';
import { useUser } from '@/hooks/useUser';

type AuthContextType = ReturnType<typeof useUser>;

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const auth = useUser();
  return <AuthContext.Provider value={auth}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
}