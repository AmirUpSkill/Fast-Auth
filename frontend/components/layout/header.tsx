'use client';  

import { ThemeToggle } from '@/components/ui/theme-toggle'; 
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { APP_NAME } from '@/lib/constants';

export function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 transition-all">
      <div className="container flex h-14 items-center">
        <div className="mr-4 hidden md:flex">
          <Link href="/" className="mr-6 flex items-center space-x-2">
            <span className="font-bold text-xl transition-colors">⚡ {APP_NAME}</span>  {/* Lightning icon + name */}
          </Link>
        </div>
        <div className="flex flex-1 items-center justify-end space-x-2">
          <ThemeToggle />  {/* Dark/light toggle */}
          <Link href="/auth">
            <Button variant="ghost" size="sm">Sign In</Button>
          </Link>
          <Link href="/auth">
            <Button size="sm" className="btn-primary">Get Started</Button>
          </Link>
        </div>
      </div>
    </header>
  );
}