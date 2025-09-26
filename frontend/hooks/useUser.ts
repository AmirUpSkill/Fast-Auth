import { useEffect, useState, useCallback } from 'react';
import { User } from '@/types/user';
import { USERS_ME_URL } from '@/lib/constants';
import { logoutUser } from '@/lib/api';

export function useUser() {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchUser = useCallback(async () => {
    try {
      const res = await fetch(USERS_ME_URL, { credentials: 'include' });
      if (res.ok) {
        const userData = await res.json();
        setUser(userData);
      } else if (res.status === 401) {
        setUser(null);
      } else {
        setError('Failed to fetch user');
      }
    } catch (err) {
      setError('Network error');
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchUser();
  }, [fetchUser]);

  const logout = useCallback(async () => {
    try {
      await logoutUser();
      setUser(null);
      window.location.href = '/';
    } catch (error) {
      console.error("Logout failed:", error);
    }
  }, []);

  return { user, isLoading, error, logout };
}