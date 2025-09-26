'use client';

import { ThemeToggle } from '@/components/ui/theme-toggle';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Zap } from 'lucide-react';
import { useAuth } from '@/providers/auth-provider';
import { UserNav } from './user-nav'; 

const APP_NAME = 'Fast Auth';

export function Header() {
  const { user, isLoading } = useAuth();

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-14 items-center justify-between">
        <Link href="/" className="flex items-center space-x-2">
          <div className="p-2 bg-primary/10 rounded-lg">
            <Zap className="h-5 w-5 text-primary" />
          </div>
          <span className="font-bold text-lg tracking-tight">{APP_NAME}</span>
        </Link>

        <div className="flex items-center space-x-2">
          <ThemeToggle />

          {isLoading ? (
            // Skeleton loader while checking auth state
            <div className="h-9 w-24 rounded-md bg-muted animate-pulse" />
          ) : user ? (
            // Show UserNav if authenticated
            <UserNav />
          ) : (
            // Show Sign In buttons if not authenticated
            <div className="hidden md:flex items-center space-x-2">
              <Link href="/auth">
                <Button variant="ghost" size="sm">Sign In</Button>
              </Link>
              <Link href="/auth">
                <Button size="sm">Get Started</Button>
              </Link>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}