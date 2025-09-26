import { LOGOUT_URL } from './constants';
import { LogoutResponse } from '@/types/api';

export async function logoutUser(): Promise<LogoutResponse> {
  const response = await fetch(LOGOUT_URL, {
    method: 'POST',
    credentials: 'include', // Important to send the session cookie
  });

  if (!response.ok) {
    throw new Error('Logout failed');
  }

  return response.json();
}