import { User } from '@/types/user';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import { User as UserIcon, Mail, Fingerprint } from 'lucide-react';

interface UserInfoCardProps {
  user: User;
}

export function UserInfoCard({ user }: UserInfoCardProps) {
  const getInitials = (name: string) => {
    return name.split(' ').map(n => n[0]).join('').toUpperCase();
  };

  return (
    <Card className="w-full max-w-lg animate-fade-in-up border-border/30 bg-card/90 backdrop-blur-md shadow-xl shadow-primary/10">
      <CardHeader className="flex flex-row items-center space-x-4 pb-4">
        <Avatar className="h-16 w-16 border-2 border-primary/50">
          <AvatarImage src={user.avatar_url || ''} alt={user.name} />
          <AvatarFallback className="text-xl font-bold bg-muted">
            {getInitials(user.name)}
          </AvatarFallback>
        </Avatar>
        <div>
          <CardTitle className="text-2xl font-bold tracking-tight">{user.name}</CardTitle>
          <CardDescription className="text-muted-foreground">
            User profile details from Google
          </CardDescription>
        </div>
      </CardHeader>
      <CardContent className="space-y-4 pt-4 border-t border-border/30">
        <div className="flex items-center space-x-3 text-sm">
          <Mail className="h-5 w-5 text-muted-foreground" />
          <span className="text-foreground flex-1 truncate">{user.email}</span>
        </div>
        <div className="flex items-center space-x-3 text-sm">
          <Fingerprint className="h-5 w-5 text-muted-foreground" />
          <span className="text-foreground font-mono text-xs flex-1 truncate">{user.id}</span>
        </div>
      </CardContent>
    </Card>
  );
}