'use client';  

import { ThemeToggle } from '@/components/ui/theme-toggle'; 
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Zap } from 'lucide-react'; 
const APP_NAME = 'FastAuth'; 

export function Header() {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 transition-all duration-300">
      <div className="container flex h-14 items-center justify-between">
        <Link href="/" className="flex items-center space-x-3 transition-all hover:scale-105">
          <div className="p-2 bg-primary/10 rounded-lg transition-colors hover:bg-primary/20">
            <Zap className="h-5 w-5 text-primary" />  
          </div>
          <span className="font-bold text-xl tracking-tight bg-gradient-to-r from-foreground to-primary/80 bg-clip-text text-transparent">
            {APP_NAME}
          </span>
        </Link>
        
        <div className="flex items-center space-x-2">
          <ThemeToggle />  
          
          <div className="hidden md:flex items-center space-x-2">
            <Link href="/auth">
              <Button variant="ghost" size="sm" className="transition-all hover:scale-105">
                Sign In
              </Button>
            </Link>
            <Link href="/auth">
              <Button size="sm" className="btn-primary transition-all hover:scale-105 shadow-md">
                Get Started
              </Button>
            </Link>
          </div>
          <div className="md:hidden">
            <Button variant="ghost" size="sm" className="p-2">
              ☰
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
}