import { Badge } from '@/components/ui/badge';
import { ShieldCheck } from 'lucide-react';

export function AuthStatusBadge() {
  return (
    <Badge 
      variant="outline" 
      className="border-green-500/50 bg-green-500/10 text-green-400 text-sm font-medium animate-fade-in"
    >
      <ShieldCheck className="h-4 w-4 mr-2 text-green-500" />
      Authenticated
    </Badge>
  );
}