import type { Metadata } from "next";
import { Geist } from "next/font/google";
import { ThemeProvider } from 'next-themes';
import "./globals.css";
import { Header } from '@/components/layout/header'; 

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: 'Fast Auth',
  description: 'Authentication Made Simple',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${geistSans.variable} font-sans antialiased`}>
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          enableSystem
          disableTransitionOnChange={false}
        >
          <Header />
          {/* Your AuthPage will be rendered inside this main tag */}
          <main className="bg-background">
            {children}
          </main>
        </ThemeProvider>
      </body>
    </html>
  );
}