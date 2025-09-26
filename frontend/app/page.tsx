'use client';

import Link from 'next/link';
import { motion } from 'framer-motion';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { ArrowRight, ShieldCheck, Zap, Server } from 'lucide-react';


const FADE_UP_ANIMATION_VARIANTS = {
  hidden: { opacity: 0, y: 10 },
  show: { opacity: 1, y: 0, transition: { type: 'spring', stiffness: 100 } },
} as const; 

export default function HomePage() {
  return (
    <main className="relative flex flex-col items-center justify-center min-h-screen overflow-hidden bg-background p-4">
      <div className="absolute inset-0 z-0 bg-gradient-to-br from-background via-background/80 to-primary/5" />
      <div
        className="absolute -top-1/2 left-1/2 -z-10 h-[150vh] w-[150vh] -translate-x-1/2 rounded-full 
        bg-[radial-gradient(circle_500px_at_50%_300px,_rgba(var(--primary-rgb),0.15),_transparent)]"
      />

      <motion.div
        initial="hidden"
        animate="show"
        viewport={{ once: true }}
        variants={{
          show: {
            transition: {
              staggerChildren: 0.15,
            },
          },
        }}
        className="relative z-10 flex flex-col items-center text-center max-w-3xl space-y-8"
      >
        <motion.div variants={FADE_UP_ANIMATION_VARIANTS}>
          <Badge variant="outline" className="border-primary/50 bg-primary/10 text-primary py-1 px-3">
            Lightning Fast Authentication
          </Badge>
        </motion.div>

        <motion.h1
          variants={FADE_UP_ANIMATION_VARIANTS}
          className="text-5xl md:text-7xl font-bold tracking-tighter bg-gradient-to-b from-foreground to-foreground/80 bg-clip-text text-transparent"
        >
          Fast Auth 
        </motion.h1>

        <motion.p
          variants={FADE_UP_ANIMATION_VARIANTS}
          className="text-lg md:text-xl text-muted-foreground max-w-xl"
        >
          A secure, fast, and developer-first authentication template for your next project. Get started in minutes, not days.
        </motion.p>

        <motion.div variants={FADE_UP_ANIMATION_VARIANTS}>
          <Link href="/auth" passHref>
            <Button size="lg" className="group shadow-lg shadow-primary/20 hover:shadow-primary/30 transition-shadow">
              Start For Free
              <ArrowRight className="ml-2 h-5 w-5 transition-transform duration-300 group-hover:translate-x-1" />
            </Button>
          </Link>
        </motion.div>

        <motion.div
          variants={FADE_UP_ANIMATION_VARIANTS}
          className="flex items-center justify-center space-x-4 rounded-full bg-card/60 p-2 px-4 backdrop-blur-sm border border-border/30"
        >
          
        </motion.div>
      </motion.div>
    </main>
  );
}