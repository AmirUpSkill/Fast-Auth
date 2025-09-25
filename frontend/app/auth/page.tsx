'use client';

import Link from 'next/link';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { GoogleAuthButton } from '@/components/auth/google-auth-button';

export default function AuthPage() {
  return (
    <div className="relative min-h-screen overflow-hidden bg-background transition-smooth">
      {/* Background gradient for dark/silver aesthetic */}
      <div className="absolute inset-0 bg-gradient-to-br from-background/90 via-muted/20 to-primary/5 -z-10" />
      
      {/* Centered container */}
      <div className="container relative z-10 flex min-h-screen items-center justify-center p-4 md:p-0">
        <Card className="w-full max-w-md animate-fade-in-up border-border/30 bg-card/90 backdrop-blur-md shadow-2xl shadow-primary/10 transition-smooth hover:shadow-primary/20">
          <CardHeader className="text-center space-y-4">
            {/* Removed Zap icon — no icon above title */}
            <CardTitle className="text-2xl font-bold tracking-tight text-foreground">
              Welcome to Fast Auth
            </CardTitle>
            <CardDescription className="text-muted-foreground">
              Sign in with your Google account to continue
            </CardDescription>
          </CardHeader>

          <CardContent className="space-y-6 px-8 pb-8">
            {/* Center the Google button */}
            <div className="flex justify-center">
              <GoogleAuthButton />
            </div>

            <p className="text-center text-xs text-muted-foreground">
              By continuing, we'll create an account for you and you agree to our{' '}
              <Link href="/terms" className="underline transition-colors hover:text-primary focus:outline-none focus:ring-2 focus:ring-primary">
                Terms of Service
              </Link>{' '}
              &{' '}
              <Link href="/privacy" className="underline transition-colors hover:text-primary focus:outline-none focus:ring-2 focus:ring-primary">
                Privacy Policy
              </Link>
              .
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}