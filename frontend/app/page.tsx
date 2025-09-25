import { Button } from '@/components/ui/button';
import Link from 'next/link';
import { Shield } from 'lucide-react'; 

export default function HomePage() {
  return (
    <div className="relative min-h-screen overflow-hidden">

      <div className="absolute inset-0 bg-gradient-to-br from-background via-background/80 to-primary/5" />
      
      <div className="container relative z-10 flex flex-col items-center justify-center min-h-screen text-center py-12 px-4">
        <div className="flex flex-col items-center space-y-8 max-w-3xl mx-auto">
 
          <div className="animate-fade-in-up">
            <h1 className="text-6xl md:text-8xl font-bold tracking-tight bg-gradient-to-r from-foreground to-primary/80 bg-clip-text text-transparent">
              Fast Auth
            </h1>
          </div>
          
     
          <div className="animate-fade-in-up animation-delay-300 max-w-lg">
            <p className="text-lg md:text-xl text-muted-foreground leading-relaxed opacity-90">
              Secure, fast, and developer-friendly authentication solution. 
            </p>
          </div>
          
   
          <div className="animate-fade-in-up animation-delay-500">
            <Link href="/auth" passHref>
              <Button size="lg" className="btn-primary group relative overflow-hidden">
                Start For Free
                <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
              </Button>
            </Link>
          </div>
          

          <div className="flex items-center space-x-6 opacity-70 animate-fade-in-up animation-delay-700">
            <div className="flex items-center space-x-1 text-sm text-muted-foreground">
              <Shield className="h-4 w-4" />
              <span>Secure OAuth</span>
            </div>
            <span className="text-muted-foreground">•</span>
            <div className="flex items-center space-x-1 text-sm text-muted-foreground">
              <span>FastAPI Ready</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}